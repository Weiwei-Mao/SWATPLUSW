#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_swat_notes.py — 扫描本地 SWAT+ 源码，生成 Obsidian 笔记框架。

设计要点（见 00-总览与索引/00-SWATPLUS总览.md）：
- 按类型分子目录：01-源码程序 / 02-模块与变量 / 03-输入文件 / 04-输出文件
- 文件名 = 源文件名 + .md（去掉执行序号前缀）
- frontmatter 丰富结构化：type/tags/file/subroutine/module/calls/reads/writes
- 调用图反向查询交给 dataview 实时计算（不在 frontmatter 里存 called_by）

重跑安全：已存在的笔记会保留正文（frontmatter 之后的内容），只更新结构化部分，
已迁移的手写注解不会丢。重跑前如想全量刷新，删除对应 .md 即可。
"""
import os
import re
import glob
from collections import defaultdict

# ----------------------------------------------------------------------------
# 路径配置（含中文，硬编码避免 shell 转义问题）
# ----------------------------------------------------------------------------
SRC = r"D:\Acode\SWATPLUS\SWATPLUS\swatplus\src"
DEST = r"D:\NoteBook\Obsdian\Obsidian-Vault\10-19 科研\00-课题\14 - SWAT\SWATPLUS"

SRC_DIR = os.path.join(DEST, "01-源码程序")   # program + subroutine
MOD_DIR = os.path.join(DEST, "02-模块与变量")  # *_module.f90
IN_DIR  = os.path.join(DEST, "03-输入文件")    # file.cio / *.bsn / *.hru ...
OUT_DIR = os.path.join(DEST, "04-输出文件")    # *.out / *.txt
IDX_DIR = os.path.join(DEST, "00-总览与索引")

# dataview FROM / dv.pages 用：库根相对路径（含空格/中文，dataview 需用引号包裹）
BASE = "10-19 科研/00-课题/14 - SWAT/SWATPLUS"

# 迁移自旧笔记的手写注解种子（仅首次生成时填入「我的笔记」区，之后由用户维护）
# key = 源文件名（r['fname']，含 .f90）
SEED_SOURCE = {
    'main.f90': (
        '- Line 30: 打开文件 `simulation.out`（unit 9003）\n'
        '- Line 38: 打开文件 `erosion.txt`（unit 888, recl 1500）\n'
        '- 调用入口 [[proc_bsn.f90]]'
    ),
    'proc_bsn.f90': (
        '- use: `time_module`, `output_path_module`\n'
        '- Line 12: call [[readcio_read.f90]]\n'
        '- Line 15: call `open_output_file(9000, "files_out.out")`\n'
        '- Line 18: call `open_output_file(9001, "diagnostics.out", 8000)` —— unit 9001, recl 8000\n'
        '- Line 21: call `open_output_file(9004, "area_calc.out", 80000)` —— unit 9004, recl 80000\n'
        '- Line 23: call [[basin_read_cc.f90]]'
    ),
    'basin_read_cc.f90': (
        '- use: `input_file_module`, [[basin_module.f90]]\n'
        '- Line 13–28: 从 `codes.bsn` 读取 `bsn_cc`（basin control codes）\n'
        '- Line 30–40: 若 `bsn_cc%pet == 3`（输入潜在蒸散发），则检查输入文件 `pet.cli` 是否存在'
    ),
    'readcio_read.f90': (
        '- use: `input_file_module`, `output_path_module`\n'
        '- Line 17–109: 读取 [[file.cio]]\n'
        '- Line 112: file.cio 第 32 行为输出路径；若有效则初始化输出路径（校验并按需创建目录）'
    ),
}

# ----------------------------------------------------------------------------
# 正则
# ----------------------------------------------------------------------------
RE_PROGRAM  = re.compile(r'^\s*program\s+([a-z0-9_]+)', re.I)
RE_MODULE   = re.compile(r'^\s*module\s+([a-z0-9_]+)\s*$', re.I)   # 模块定义（排除 module procedure）
RE_SUBROUT  = re.compile(r'^\s*(?:recursive\s+|pure\s+|elemental\s+)*subroutine\s+([a-z0-9_]+)', re.I)
RE_USE      = re.compile(r'^\s*use\s+([a-z0-9_]+)', re.I)
RE_CALL     = re.compile(r'\bcall\s+([a-z0-9_]+)', re.I)
RE_OPEN     = re.compile(r'\bopen\s*\(([^)]*)\)', re.I)
RE_FILEARG  = re.compile(r'\bfile\s*=\s*([^,)]+)', re.I)
RE_UNITARG  = re.compile(r'(?:^|,)\s*(?:unit\s*=\s*)?(\d+)\b')
RE_TYPEDEF  = re.compile(r'^\s*type\s+(?!.*\()\s*([a-z0-9_]+)', re.I)          # type foo  （定义）
RE_TYPEVAR  = re.compile(r'^\s*type\s*\(\s*([a-z0-9_]+)\s*\)\s*::\s*([a-z0-9_,\s]+)', re.I)  # type(t) :: 实例
RE_SCALAR   = re.compile(r'^\s*(?:real|integer|logical|character[^:!]*)::\s*([a-z0-9_,\s]+)', re.I)
RE_WRITE_U  = re.compile(r'\bwrite\s*\(\s*(\d+)\s*,', re.I)
RE_READ_U   = re.compile(r'\bread\s*\(\s*(\d+)\s*,', re.I)


def strip_comment(line):
    """去掉 Fortran 行内注释（! 之后）。字符串里的 ! 极少，可接受。"""
    idx = line.find('!')
    return line[:idx] if idx >= 0 else line


def clean_target(raw):
    """清理 open 的 file= 参数：去引号、去首尾空格。"""
    t = raw.strip().strip().strip("'\"").strip()
    return t


def is_literal_file(target):
    """判断 target 是字面文件名还是变量/表达式。"""
    t = target.strip()
    if t.startswith("'") or t.startswith('"'):
        return True
    # 含 % 或 // 或 纯标识符（无点）视为变量/表达式
    if '%' in t or '//' in t:
        return False
    if '.' in t:
        return True
    return False  # 无点的标识符 -> 变量


def parse_source(path):
    """解析单个 .f90，返回结构化字典。"""
    with open(path, encoding='utf-8', errors='replace') as f:
        text = f.read()
    raw_lines = text.splitlines()
    lines = [strip_comment(ln) for ln in raw_lines]

    fname = os.path.basename(path)
    stem = fname[:-4]

    # 1) 判定类型 + 主名
    kind = 'subroutine'
    name = stem
    module_end_contains = None
    for ln in lines:
        m = RE_PROGRAM.match(ln)
        if m:
            kind, name = 'program', m.group(1)
            break
        m = RE_MODULE.match(ln)
        if m and 'procedure' not in ln.lower():
            kind, name = 'module', m.group(1)
            break
        m = RE_SUBROUT.match(ln)
        if m:
            kind, name = 'subroutine', m.group(1)
            break

    # 2) 收集 use / call / open / type
    uses, calls, opens = [], [], []
    types, typevars, scalars = [], [], []
    in_module_scope = (kind == 'module')

    for ln in lines:
        stripped = ln.strip()
        if not stripped:
            continue

        m = RE_USE.match(ln)
        if m:
            mod = m.group(1)
            if mod not in uses:
                uses.append(mod)

        for cm in RE_CALL.finditer(ln):
            c = cm.group(1).lower()
            if c not in calls:
                calls.append(c)

        om = RE_OPEN.search(ln)
        if om:
            inner = om.group(1)
            fm = RE_FILEARG.search(inner)
            um = RE_UNITARG.search(inner)
            if fm:
                target = clean_target(fm.group(1))
                unit = um.group(1) if um else ''
                opens.append((unit, target))

        # 模块级类型/变量（仅在 module 作用域、contains 之前）
        if in_module_scope:
            if re.match(r'^\s*contains\b', ln, re.I):
                in_module_scope = False
            else:
                tm = RE_TYPEDEF.match(ln)
                if tm and tm.group(1).lower() not in [t.lower() for t in types]:
                    types.append(tm.group(1))
                tvm = RE_TYPEVAR.match(ln)
                if tvm:
                    for v in re.split(r'[,\s]+', tvm.group(2).strip()):
                        v = v.strip()
                        if v and v.lower() not in [x.lower() for x in typevars]:
                            typevars.append(v)
                sm = RE_SCALAR.match(ln)
                if sm:
                    for v in re.split(r'[,\s]+', sm.group(1).strip()):
                        v = v.strip().split('=')[0].strip()
                        if v and v.lower() not in [x.lower() for x in scalars]:
                            scalars.append(v)

    # 3) read/write 分类（按 unit 是否出现在 write()/read()）
    write_units = set(RE_WRITE_U.findall(text))
    read_units = set(RE_READ_U.findall(text))
    writes, reads = [], []
    for unit, target in opens:
        u = unit.strip()
        literal = is_literal_file(target)
        if u in write_units and u not in read_units:
            writes.append(target)
        elif u in read_units and u not in write_units:
            reads.append(target)
        elif u in write_units:
            writes.append(target)
        else:
            # 未知 unit：按扩展名兜底
            if literal and re.search(r'\.(out|txt|csv|prt)$', target, re.I):
                writes.append(target)
            else:
                reads.append(target)

    # 4) 概要：取首个 !! 文档块（SWAT+ 用 !! 标注 PURPOSE，通常紧跟声明之后）
    leading_comments = _extract_desc(raw_lines)

    return {
        'path': path, 'fname': fname, 'stem': stem,
        'kind': kind, 'name': name,
        'uses': uses, 'calls': calls,
        'opens': opens, 'writes': writes, 'reads': reads,
        'types': types, 'typevars': typevars, 'scalars': scalars,
        'desc': leading_comments,
    }


def _extract_desc(raw_lines, max_lines=3, scan=120):
    """提取 `~ ~ ~ PURPOSE ~ ~ ~` 装饰行之后的 !! 文档作为概要。

    SWAT+ 约定：文档块以 `!! ~ ~ ~ PURPOSE ~ ~ ~` 开头，其后几行是真正的用途说明。
    找不到 PURPOSE 标记则返回 []（宁可留空，也不把变量文档当概要）。
    """
    desc, collecting = [], False
    for ln in raw_lines[:scan]:
        s = ln.strip()
        if s.startswith('!!'):
            c = s[2:].strip()
            if c.startswith('~') and c.endswith('~') and 'PURPOSE' in c.upper():
                collecting = True
                continue
            if collecting:
                if c.startswith('~') and c.endswith('~'):
                    break  # 遇到下一个段落装饰（VARIABLES 等），结束
                if c:
                    desc.append(c)
                    if len(desc) >= max_lines:
                        break
        elif collecting and s and not s.startswith('!'):
            break
    return desc[:max_lines]


# ----------------------------------------------------------------------------
# 渲染辅助
# ----------------------------------------------------------------------------
def yaml_list(items, indent='  '):
    """渲染 YAML 列表；空则 ' []'（前置空格，避免 key:[] 被解析成字符串）。"""
    items = [i for i in items if i]
    if not items:
        return ' []'
    return '\n' + '\n'.join(f'{indent}- {i}' for i in items)


def yaml_str(s):
    """安全地把字符串渲染为 YAML 双引号字符串。"""
    s = (s or '').replace('\\', '\\\\').replace('"', '\\"')
    s = ' '.join(s.split())   # 折叠空白/换行，避免 frontmatter 里出现裸换行
    return f'"{s}"'


def linkify_call(name, stems):
    """call 目标 -> wikilink 或 code。stems 是不含 .f90 的文件名集合。"""
    if name in stems:
        return f'[[{name}.f90]]'
    return f'`{name}`'


def linkify_module(mod, mod_stems):
    """use 模块 -> wikilink（指向 02-模块与变量 中的 _module.f90）。"""
    if mod in mod_stems:
        return f'[[{mod}.f90]]'
    return f'`{mod}`'


# 脚本自己写进「我的笔记」区的样板行；preserve 时剔除，保证重跑幂等
_BOILERPLATE = {
    '## 我的笔记',
    '（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）',
    '（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）',
}


def preserve_user_body(target_path):
    """提取已存在笔记中 USER-NOTES 标记之间的【用户手写】内容（重跑幂等）。

    剔除脚本自己写入的样板行（标题/占位符），只留真正的用户笔记；
    旧格式（无标记）返回空，避免结构化内容被重复追加。
    """
    if not os.path.exists(target_path):
        return ''
    with open(target_path, encoding='utf-8', errors='replace') as f:
        content = f.read()
    m = re.search(r'<!-- USER-NOTES-START -->(.*?)<!-- USER-NOTES-END -->', content, re.S)
    if not m:
        return ''
    lines = [ln for ln in m.group(1).splitlines() if ln.strip() not in _BOILERPLATE]
    return '\n'.join(lines).strip()


def write_note(path, frontmatter, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        if frontmatter.strip():
            f.write('---\n')
            f.write(frontmatter.strip('\n'))
            f.write('\n---\n\n')
        f.write(body.rstrip() + '\n')


# ----------------------------------------------------------------------------
# 主流程
# ----------------------------------------------------------------------------
def main():
    for d in (SRC_DIR, MOD_DIR, IN_DIR, OUT_DIR, IDX_DIR):
        os.makedirs(d, exist_ok=True)

    f90_files = sorted(glob.glob(os.path.join(SRC, '*.f90')))
    records = [parse_source(p) for p in f90_files]

    stems = {r['stem'] for r in records}                 # 全部源文件 stem
    mod_stems = {r['stem'] for r in records if r['kind'] == 'module'}

    # 全局：输出文件 -> 写它的源码；输入变量/字面 -> 读它的源码
    output_writers = defaultdict(set)   # filename -> set(source stem)
    input_readers = defaultdict(set)    # target -> set(source stem)

    n_src = n_mod = 0
    for r in records:
        # 汇总 IO 全局表
        for w in r['writes']:
            if is_literal_file(w):
                output_writers[w].add(r['stem'])
        for rr in r['reads']:
            input_readers[rr].add(r['stem'])

        if r['kind'] == 'module':
            _write_module_note(r, mod_stems, stems)
            n_mod += 1
        else:
            _write_source_note(r, mod_stems, stems)
            n_src += 1

    # 输出文件笔记
    n_out = 0
    for fname in sorted(output_writers.keys()):
        n_out += 1
        _write_output_note(fname, sorted(output_writers[fname]), stems)

    # 输入文件笔记（从 file.cio 解析 + 全局 input_readers 补 read_by）
    n_in = _write_input_notes_from_cio(stems, input_readers)

    # 索引页
    _write_indexes(records, stems, mod_stems, output_writers, input_readers)

    print(f'生成完成：源码 {n_src} / 模块 {n_mod} / 输出 {n_out} / 输入 {n_in}')


# ----------------------------------------------------------------------------
# 各类笔记渲染
# ----------------------------------------------------------------------------
def _write_source_note(r, mod_stems, stems):
    target = os.path.join(SRC_DIR, f"{r['stem']}.f90.md")
    subtype = 'program' if r['kind'] == 'program' else 'subroutine'

    fm = []
    fm.append('type: source')
    fm.append(f'subtype: {subtype}')
    fm.append('tags:')
    fm.append('  - swat/源码')
    fm.append('  - swat/待读')
    fm.append(f'file: {r["fname"]}')
    fm.append(f'subroutine: {r["name"]}')
    if r['uses']:
        fm.append('module:')
        for u in r['uses']:
            fm.append(f'  - {u}')
    else:
        fm.append('module: []')
    if r['calls']:
        fm.append('calls:')
        for c in r['calls']:
            fm.append(f'  - {c}')
    else:
        fm.append('calls: []')
    fm.append('reads:' + yaml_list(r['reads']))
    fm.append('writes:' + yaml_list(r['writes']))
    fm.append('purpose: ' + yaml_str('；'.join(r['desc'])))

    # 正文
    b = []
    b.append(f'# {r["name"]}')
    b.append('')
    desc = '；'.join(r['desc']) if r['desc'] else '待补充'
    b.append(f'> [!info] 概要')
    b.append(f'> {desc}')
    b.append('')
    b.append('## 基本信息')
    b.append(f'- **类型**：`{subtype}`')
    b.append(f'- **源文件**：`{r["fname"]}`')
    use_links = '、'.join(linkify_module(u, mod_stems) for u in r['uses']) or '—'
    b.append(f'- **使用模块**：{use_links}')
    b.append(f'- **调用子程序**：{len(r["calls"])} 个 ｜ **读取文件**：{len(r["reads"])} ｜ **写入文件**：{len(r["writes"])}')
    b.append('')
    b.append('## 调用关系')
    if r['calls']:
        b.append('**本程序调用：**')
        b.append('')
        for c in r['calls']:
            b.append(f'- {linkify_call(c, stems)}')
    else:
        b.append('（无 call 语句，叶子节点）')
    b.append('')
    b.append('**被以下程序调用**（dataview 实时反查）：')
    b.append('')
    b.append('```dataview')
    b.append('LIST file.link')
    b.append('WHERE type = "source" AND contains(calls, this.subroutine)')
    b.append('```')
    b.append('')
    if r['reads'] or r['writes']:
        b.append('## 文件读写')
        if r['writes']:
            b.append('- **写入**：' + '、'.join(f'`{w}`' for w in r['writes']))
        if r['reads']:
            rd = []
            for x in r['reads']:
                if is_literal_file(x):
                    rd.append(f'`{x}`')
                else:
                    rd.append(f'`{x}` _（变量，见 file.cio）_')
            b.append('- **读取**：' + '、'.join(rd))
        b.append('')
    b.append('<!-- USER-NOTES-START -->')
    b.append('## 我的笔记')
    b.append('（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）')
    user_body = preserve_user_body(target) or SEED_SOURCE.get(r['fname'], '')
    if user_body.strip():
        b.append('')
        b.append(user_body.strip())
    b.append('<!-- USER-NOTES-END -->')
    write_note(target, '\n'.join(fm), '\n'.join(b))


def _write_module_note(r, mod_stems, stems):
    target = os.path.join(MOD_DIR, f"{r['stem']}.f90.md")

    fm = []
    fm.append('type: module')
    fm.append('tags:')
    fm.append('  - swat/模块')
    fm.append('  - swat/待读')
    fm.append(f'file: {r["fname"]}')
    fm.append(f'module_name: {r["name"]}')
    fm.append('defines_types:' + yaml_list(r['types']))
    fm.append('defines_vars:' + yaml_list(r['typevars'] + r['scalars']))
    fm.append('purpose: ' + yaml_str('；'.join(r['desc'])))

    b = []
    b.append(f'# {r["name"]}')
    b.append('')
    b.append('> [!info] 模块')
    b.append('> 定义派生类型与模块级变量（关键变量的归宿）。')
    b.append('')
    b.append('## 定义的类型')
    if r['types']:
        b.append('| 类型 | 说明 |')
        b.append('|---|---|')
        for t in r['types']:
            b.append(f'| `{t}` |  |')
    else:
        b.append('（未检测到 type 定义）')
    b.append('')
    b.append('## 模块级变量（关键变量）')
    vars_all = r['typevars'] + r['scalars']
    if vars_all:
        b.append('| 变量 | 类型 | 含义 |')
        b.append('|---|---|---|')
        shown = vars_all[:40]
        for v in shown:
            b.append(f'| `{v}` |  |  |')
        if len(vars_all) > 40:
            b.append(f'\n*（仅显示前 40 个，共 {len(vars_all)} 个）*')
    else:
        b.append('（未检测到模块级变量）')
    b.append('')
    b.append('## 被以下源码使用（dataview 实时反查）')
    b.append('')
    b.append('```dataview')
    b.append('LIST file.link')
    b.append('WHERE type = "source" AND contains(module, this.module_name)')
    b.append('```')
    b.append('')
    b.append('<!-- USER-NOTES-START -->')
    b.append('## 我的笔记')
    b.append('（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）')
    user_body = preserve_user_body(target)
    if user_body.strip():
        b.append('')
        b.append(user_body.strip())
    b.append('<!-- USER-NOTES-END -->')
    write_note(target, '\n'.join(fm), '\n'.join(b))


def _write_output_note(fname, writers, stems):
    safe = re.sub(r'[\\/:*?"<>|]', '_', fname)
    target = os.path.join(OUT_DIR, f'{safe}.md')
    ext = fname.rsplit('.', 1)[-1] if '.' in fname else ''
    unit_hint = ''
    fm = []
    fm.append('type: output')
    fm.append('tags:')
    fm.append('  - swat/输出')
    fm.append(f'file: {fname}')
    fm.append(f'ext: {ext}')
    fm.append('written_by:' + yaml_list([f'{w}.f90' for w in writers]))
    fm.append('purpose: ""')

    b = []
    b.append(f'# {fname}')
    b.append('')
    b.append('> [!info] 输出文件')
    b.append(f'> 由程序写入。扩展名 `.{ext}`。')
    b.append('')
    b.append('## 写入它的程序')
    b.append('')
    for w in writers:
        b.append(f'- [[{w}.f90]]')
    b.append('')
    b.append('## 文件格式')
    b.append('（读代码 / 看实际输出时补充：字段含义、列说明）')

    write_note(target, '\n'.join(fm), '\n'.join(b))


def _write_input_notes_from_cio(stems, input_readers):
    """从 file.cio.md 的正文解析输入文件清单，生成轻量输入笔记。"""
    cio_path = os.path.join(IN_DIR, 'file.cio.md')
    if not os.path.exists(cio_path):
        return 0
    with open(cio_path, encoding='utf-8', errors='replace') as f:
        cio = f.read()
    # 匹配 **field**: filename.ext 形式
    pairs = re.findall(r'\*\*([a-z0-9_]+)\*\*\s*:\s*([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+)', cio)
    seen = {}
    for field, filename in pairs:
        filename = filename.strip()
        if filename not in seen:
            seen[filename] = field

    n = 0
    for filename, field in sorted(seen.items()):
        safe = re.sub(r'[\\/:*?"<>|]', '_', filename)
        if safe == 'file.cio':
            continue
        target = os.path.join(IN_DIR, f'{safe}.md')
        ext = filename.rsplit('.', 1)[-1]
        # 反查读取它的程序：字面匹配 + 字段变量匹配
        readers = set()
        for stem in input_readers.get(filename, set()):
            readers.add(stem)
        # 变量形式：input_readers 的 key 可能是 in_xxx%field 或 field
        for key, sts in input_readers.items():
            if key.endswith('%' + field) or key == field:
                readers |= sts
        fm = []
        fm.append('type: input')
        fm.append('tags:')
        fm.append('  - swat/输入')
        fm.append(f'file: {filename}')
        fm.append(f'ext: {ext}')
        fm.append(f'cio_field: {field}')
        fm.append('read_by:' + yaml_list([f'{s}.f90' for s in sorted(readers)]))
        fm.append('purpose: ""')

        b = []
        b.append(f'# {filename}')
        b.append('')
        b.append('> [!info] 输入文件')
        b.append(f'> 在 `file.cio` 中以字段 `{field}` 声明。格式详见 [[file.cio]]。')
        b.append('')
        b.append('## 读取它的程序')
        if readers:
            for s in sorted(readers):
                b.append(f'- [[{s}.f90]]')
        else:
            b.append('（暂未自动定位，读代码时补充）')
        b.append('')
        b.append('## 文件格式')
        b.append('（补充：各字段含义、单位、取值）')
        write_note(target, '\n'.join(fm), '\n'.join(b))
        n += 1
    return n


# ----------------------------------------------------------------------------
# 索引页
# ----------------------------------------------------------------------------
def _write_indexes(records, stems, mod_stems, output_writers, input_readers):
    # 00-SWATPLUS总览
    total = len(records)
    n_src = sum(1 for r in records if r['kind'] != 'module')
    n_mod = sum(1 for r in records if r['kind'] == 'module')
    overview = f'''# SWAT+ 代码学习系统

> 本子系统用于理清 SWAT+ 源码：**程序相互调用**、**关键变量**、**输入输出文件**。
> 笔记由 `_tools/gen_swat_notes.py` 自动生成骨架，手写内容在重跑时会被保留。

## 统计

- 源码文件（program + subroutine）：**{n_src}**
- 模块文件（`*_module.f90`，关键变量归宿）：**{n_mod}**
- 输出文件：见 [[输入输出文件索引]]
- 输入文件：以 [[file.cio]] 为总纲

## 目录结构

| 文件夹 | 内容 | 笔记类型 |
|---|---|---|
| `01-源码程序/` | `program` + `subroutine`，每个 `.f90` 一篇 | `type: source` |
| `02-模块与变量/` | `*_module.f90`，定义派生类型与全局变量 | `type: module` |
| `03-输入文件/` | `file.cio` 为总纲，其余输入文件逐个成篇 | `type: input` |
| `04-输出文件/` | `.out` / `.txt` 等输出文件 | `type: output` |

## 索引页

- [[调用关系图]] — 主调用树 + 调用热度排行
- [[模块与变量索引]] — 全部模块及其类型/变量
- [[输入输出文件索引]] — 输入输出文件清单与读写关系

## 怎么用

1. **读某个子程序**：打开 `01-源码程序/xxx.f90.md`，看「调用关系」「文件读写」，在「逐行注解」里记笔记。
2. **查谁调用了 X**：X 的笔记末尾 dataview 自动列出所有调用方；无需手工维护。
3. **查关键变量**：去 `02-模块与变量/` 找定义它的模块；模块笔记末尾列出所有使用它的源码。
4. **更新进度**：改 frontmatter 的 `tags`：`swat/待读` → `swat/进行中` → `swat/已读`；并补 `purpose`。
5. **功能域归类**：按需加 `swat/域-水文` `swat/域-泥沙` 等标签（见 [[模块与变量索引]] 的域说明）。

## 重跑生成

源码更新后，重跑 `_tools/gen_swat_notes.py` 即可刷新结构化字段；手写正文（frontmatter 之后）会被保留。

```bash
python "_tools/gen_swat_notes.py"
```
'''
    write_note(os.path.join(IDX_DIR, '00-SWATPLUS总览.md'), '', overview)

    # 调用关系图
    main_rec = next((r for r in records if r['kind'] == 'program'), None)
    mermaid = ['```mermaid', 'graph LR']
    if main_rec:
        mermaid.append(f'  main["main<br/>{main_rec["fname"]}"]')
        for c in main_rec['calls']:
            if f'{c}.f90' in stems:
                mermaid.append(f'  main --> {c}["{c}"]')
            else:
                mermaid.append(f'  main --> {c}["{c}"]')
    mermaid.append('```')
    mermaid_str = "\n".join(mermaid)
    call_graph = f'''# 调用关系图

## 主程序 main 的直接调用

{mermaid_str}

> 完整调用关系：每篇源码笔记的「调用关系」section 都有正向调用列表 + dataview 实时反查「被谁调用」。

## 调用热度排行（被调用最多的子程序 = 核心枢纽）

```dataviewjs
const pages = dv.pages('"{BASE}/01-源码程序"').where(p => p.calls);
const counter = {{}};
for (const p of pages) {{
  for (const c of p.calls) {{ counter[c] = (counter[c] || 0) + 1; }}
}}
const rows = Object.entries(counter)
  .sort((a,b) => b[1]-a[1])
  .slice(0, 30)
  .map(([name, n]) => [name + ".f90", n]);
dv.table(["被调用子程序", "调用方数量"], rows);
```

## 按子程序查调用方

在任一源码笔记里，下面的查询会列出调用它的所有程序（`this.subroutine` 自动取当前笔记）：

```
```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
``` ```
'''
    write_note(os.path.join(IDX_DIR, '调用关系图.md'), '', call_graph)

    # 模块与变量索引
    mod_index = f'''# 模块与变量索引

## 全部模块（关键变量的归宿）

```dataview
TABLE defines_types AS "定义的类型", defines_vars AS "模块级变量"
FROM "{BASE}/02-模块与变量"
SORT file ASC
```

## 功能域标签（建议）

阅读时给笔记打域标签，便于按学科浏览。可用值：

`swat/域-主控` `swat/域-水文` `swat/域-泥沙` `swat/域-营养盐` `swat/域-气候`
`swat/域-渠道` `swat/域-水库` `swat/域-地下水` `swat/域-植物` `swat/域-校准` `swat/域-工具`

## 按域浏览模块

```dataview
TABLE file, defines_types
FROM "{BASE}/02-模块与变量"
WHERE contains(tags, "#swat/域-水文")
```
（把 `域-水文` 换成其它域即可。）
'''
    write_note(os.path.join(IDX_DIR, '模块与变量索引.md'), '', mod_index)

    # 输入输出文件索引
    io_index = f'''# 输入输出文件索引

## 输入文件

> [`file.cio`](file://file.cio) 是输入总纲，逐段声明所有输入文件。其余输入文件见 `03-输入文件/`。

```dataview
TABLE ext AS "扩展名", read_by AS "读取程序", cio_field AS "file.cio 字段"
FROM "{BASE}/03-输入文件"
WHERE type = "input"
SORT file ASC
```

## 输出文件

```dataview
TABLE ext AS "扩展名", written_by AS "写入程序"
FROM "{BASE}/04-输出文件"
WHERE type = "output"
SORT file ASC
```

## 输入文件总纲

- [[file.cio]] — 控制文件，逐段列出全部输入文件
'''
    write_note(os.path.join(IDX_DIR, '输入输出文件索引.md'), '', io_index)


if __name__ == '__main__':
    main()

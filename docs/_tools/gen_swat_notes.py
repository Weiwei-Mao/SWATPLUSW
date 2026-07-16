#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the SWAT+ source-study note skeleton.

The generator scans the repository-local SWAT+ Fortran source and writes an
English Obsidian-style note tree under docs/SWATPLUS. Existing content between
USER-NOTES markers is preserved across reruns.
"""
from __future__ import annotations

import os
import re
from collections import defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DOCS_DIR = SCRIPT_DIR.parent
REPO_ROOT = DOCS_DIR.parent

SRC = Path(os.environ.get("SWATPLUS_SRC", REPO_ROOT / "SWATPLUS" / "swatplus" / "src"))
DEST = Path(os.environ.get("SWAT_NOTES_DEST", DOCS_DIR / "SWATPLUS"))

# Dataview paths are relative to the Obsidian vault root. Override this when the
# vault root is not the repository root.
BASE = os.environ.get("SWAT_NOTES_BASE", "docs/SWATPLUS")

SRC_DIR = DEST / "01-source-routines"
MOD_DIR = DEST / "02-modules-and-variables"
IN_DIR = DEST / "03-input-files"
OUT_DIR = DEST / "04-output-files"
IDX_DIR = DEST / "00-overview-and-index"


SEED_SOURCE = {
    "main.f90": (
        "- Line 30: Opens `simulation.out` (unit 9003)\n"
        "- Line 38: Opens `erosion.txt` (unit 888, recl 1500)\n"
        "- Entry call: [[proc_bsn.f90]]"
    ),
    "proc_bsn.f90": (
        "- use: `time_module`, `output_path_module`\n"
        "- Line 12: call [[readcio_read.f90]]\n"
        '- Line 15: call `open_output_file(9000, "files_out.out")`\n'
        '- Line 18: call `open_output_file(9001, "diagnostics.out", 8000)` - unit 9001, recl 8000\n'
        '- Line 21: call `open_output_file(9004, "area_calc.out", 80000)` - unit 9004, recl 80000\n'
        "- Line 23: call [[basin_read_cc.f90]]"
    ),
    "basin_read_cc.f90": (
        "- use: `input_file_module`, [[basin_module.f90]]\n"
        "- Lines 13-28: Reads `bsn_cc` from `codes.bsn` (basin control codes)\n"
        "- Lines 30-40: If `bsn_cc%pet == 3` (input potential evapotranspiration), checks whether `pet.cli` exists"
    ),
    "readcio_read.f90": (
        "- use: `input_file_module`, `output_path_module`\n"
        "- Lines 17-109: Reads [[file.cio]]\n"
        "- Line 112: line 32 of file.cio is the output path; if valid, initializes the output path by validating and creating directories as needed"
    ),
}


RE_PROGRAM = re.compile(r"^\s*program\s+([a-z0-9_]+)", re.I)
RE_MODULE = re.compile(r"^\s*module\s+([a-z0-9_]+)\s*$", re.I)
RE_SUBROUT = re.compile(r"^\s*(?:recursive\s+|pure\s+|elemental\s+)*subroutine\s+([a-z0-9_]+)", re.I)
RE_USE = re.compile(r"^\s*use\s+([a-z0-9_]+)", re.I)
RE_CALL = re.compile(r"\bcall\s+([a-z0-9_]+)", re.I)
RE_OPEN = re.compile(r"\bopen\s*\(([^)]*)\)", re.I)
RE_FILEARG = re.compile(r"\bfile\s*=\s*([^,)]+)", re.I)
RE_UNITARG = re.compile(r"(?:^|,)\s*(?:unit\s*=\s*)?(\d+)\b")
RE_TYPEDEF = re.compile(r"^\s*type\s+(?!.*\()\s*([a-z0-9_]+)", re.I)
RE_TYPEVAR = re.compile(r"^\s*type\s*\(\s*([a-z0-9_]+)\s*\)\s*::\s*([a-z0-9_,\s]+)", re.I)
RE_SCALAR = re.compile(r"^\s*(?:real|integer|logical|character[^:!]*)::\s*([a-z0-9_,\s]+)", re.I)
RE_WRITE_U = re.compile(r"\bwrite\s*\(\s*(\d+)\s*,", re.I)
RE_READ_U = re.compile(r"\bread\s*\(\s*(\d+)\s*,", re.I)


NEW_BOILERPLATE = {
    "## Notes",
    "Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.",
    "Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.",
}

BOILERPLATE = NEW_BOILERPLATE


def strip_comment(line: str) -> str:
    idx = line.find("!")
    return line[:idx] if idx >= 0 else line


def clean_target(raw: str) -> str:
    return raw.strip().strip("'\"").strip()


def is_literal_file(target: str) -> bool:
    t = target.strip()
    if t.startswith("'") or t.startswith('"'):
        return True
    if "%" in t or "//" in t:
        return False
    if "." in t:
        return True
    return False


def source_files() -> list[Path]:
    files = sorted(SRC.glob("*.f90"))
    main_template = SRC / "main.f90.in"
    if main_template.exists() and not (SRC / "main.f90").exists():
        files.append(main_template)
    return sorted(files, key=lambda p: p.name.lower())


def note_names(path: Path) -> tuple[str, str, str]:
    fname = path.name
    if fname.endswith(".f90.in"):
        note_file = fname[:-3]
        stem = note_file[:-4]
    else:
        note_file = fname
        stem = fname[:-4]
    return fname, note_file, stem


def parse_source(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw_lines = text.splitlines()
    lines = [strip_comment(ln) for ln in raw_lines]

    fname, note_file, stem = note_names(path)

    kind = "subroutine"
    name = stem
    for ln in lines:
        m = RE_PROGRAM.match(ln)
        if m:
            kind, name = "program", m.group(1)
            break
        m = RE_MODULE.match(ln)
        if m and "procedure" not in ln.lower():
            kind, name = "module", m.group(1)
            break
        m = RE_SUBROUT.match(ln)
        if m:
            kind, name = "subroutine", m.group(1)
            break

    uses, calls, opens = [], [], []
    types, typevars, scalars = [], [], []
    in_module_scope = kind == "module"

    for ln in lines:
        if not ln.strip():
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
                unit = um.group(1) if um else ""
                opens.append((unit, target))

        if in_module_scope:
            if re.match(r"^\s*contains\b", ln, re.I):
                in_module_scope = False
            else:
                tm = RE_TYPEDEF.match(ln)
                if tm and tm.group(1).lower() not in [t.lower() for t in types]:
                    types.append(tm.group(1))
                tvm = RE_TYPEVAR.match(ln)
                if tvm:
                    for v in re.split(r"[,\s]+", tvm.group(2).strip()):
                        v = v.strip()
                        if v and v.lower() not in [x.lower() for x in typevars]:
                            typevars.append(v)
                sm = RE_SCALAR.match(ln)
                if sm:
                    for v in re.split(r"[,\s]+", sm.group(1).strip()):
                        v = v.strip().split("=")[0].strip()
                        if v and v.lower() not in [x.lower() for x in scalars]:
                            scalars.append(v)

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
        elif literal and re.search(r"\.(out|txt|csv|prt|fin)$", target, re.I):
            writes.append(target)
        else:
            reads.append(target)

    return {
        "path": path,
        "fname": fname,
        "note_file": note_file,
        "stem": stem,
        "kind": kind,
        "name": name,
        "uses": uses,
        "calls": calls,
        "opens": opens,
        "writes": writes,
        "reads": reads,
        "types": types,
        "typevars": typevars,
        "scalars": scalars,
        "desc": extract_desc(raw_lines),
    }


def extract_desc(raw_lines: list[str], max_lines: int = 3, scan: int = 120) -> list[str]:
    desc, collecting = [], False
    for ln in raw_lines[:scan]:
        s = ln.strip()
        if s.startswith("!!"):
            c = s[2:].strip()
            if c.startswith("~") and c.endswith("~") and "PURPOSE" in c.upper():
                collecting = True
                continue
            if collecting:
                if c.startswith("~") and c.endswith("~"):
                    break
                if c:
                    desc.append(c)
                    if len(desc) >= max_lines:
                        break
        elif collecting and s and not s.startswith("!"):
            break
    return desc[:max_lines]


def yaml_list(items: list[str], indent: str = "  ") -> str:
    items = [i for i in items if i]
    if not items:
        return " []"
    return "\n" + "\n".join(f"{indent}- {i}" for i in items)


def yaml_str(s: str) -> str:
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"')
    s = " ".join(s.split())
    return f'"{s}"'


def linkify_call(name: str, stems: set[str]) -> str:
    if name in stems:
        return f"[[{name}.f90]]"
    return f"`{name}`"


def linkify_module(mod: str, mod_stems: set[str]) -> str:
    if mod in mod_stems:
        return f"[[{mod}.f90]]"
    return f"`{mod}`"


def translate_preserved_note(text: str) -> str:
    return text


def preserve_user_body(target_path: Path) -> str:
    if not target_path.exists():
        return ""
    content = target_path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<!-- USER-NOTES-START -->(.*?)<!-- USER-NOTES-END -->", content, re.S)
    if not m:
        return ""
    lines = [ln for ln in m.group(1).splitlines() if ln.strip() not in BOILERPLATE]
    return translate_preserved_note("\n".join(lines).strip())


def write_note(path: Path, frontmatter: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        if frontmatter.strip():
            f.write("---\n")
            f.write(frontmatter.strip("\n"))
            f.write("\n---\n\n")
        f.write(body.rstrip() + "\n")


def main() -> None:
    for d in (SRC_DIR, MOD_DIR, IN_DIR, OUT_DIR, IDX_DIR):
        d.mkdir(parents=True, exist_ok=True)

    records = [parse_source(p) for p in source_files()]

    stems = {r["stem"] for r in records}
    mod_stems = {r["stem"] for r in records if r["kind"] == "module"}

    output_writers = defaultdict(set)
    input_readers = defaultdict(set)

    n_src = n_mod = 0
    for r in records:
        for w in r["writes"]:
            if is_literal_file(w):
                output_writers[w].add(r["stem"])
        for rr in r["reads"]:
            input_readers[rr].add(r["stem"])

        if r["kind"] == "module":
            write_module_note(r, stems)
            n_mod += 1
        else:
            write_source_note(r, mod_stems, stems)
            n_src += 1

    n_out = 0
    for fname in sorted(output_writers.keys()):
        n_out += 1
        write_output_note(fname, sorted(output_writers[fname]))

    n_in = write_input_notes_from_cio(input_readers)
    write_indexes(records, output_writers)

    print(f"Generated: source {n_src} / modules {n_mod} / outputs {n_out} / inputs {n_in}")


def write_source_note(r: dict, mod_stems: set[str], stems: set[str]) -> None:
    target = SRC_DIR / f"{r['note_file']}.md"
    subtype = "program" if r["kind"] == "program" else "subroutine"

    fm = []
    fm.append("type: source")
    fm.append(f"subtype: {subtype}")
    fm.append("tags:")
    fm.append("  - swat/source")
    fm.append("  - swat/to-read")
    fm.append(f"file: {r['fname']}")
    fm.append(f"note_file: {r['note_file']}")
    fm.append(f"subroutine: {r['name']}")
    if r["uses"]:
        fm.append("module:")
        for u in r["uses"]:
            fm.append(f"  - {u}")
    else:
        fm.append("module: []")
    if r["calls"]:
        fm.append("calls:")
        for c in r["calls"]:
            fm.append(f"  - {c}")
    else:
        fm.append("calls: []")
    fm.append("reads:" + yaml_list(r["reads"]))
    fm.append("writes:" + yaml_list(r["writes"]))
    fm.append("purpose: " + yaml_str("; ".join(r["desc"])))

    desc = "; ".join(r["desc"]) if r["desc"] else "TBD"
    use_links = ", ".join(linkify_module(u, mod_stems) for u in r["uses"]) or "-"

    b = []
    b.append(f"# {r['name']}")
    b.append("")
    b.append("> [!info] Summary")
    b.append(f"> {desc}")
    b.append("")
    b.append("## Basic Information")
    b.append(f"- **Type**: `{subtype}`")
    b.append(f"- **Source file**: `{r['fname']}`")
    b.append(f"- **Modules used**: {use_links}")
    b.append(f"- **Subroutine calls**: {len(r['calls'])} | **Files read**: {len(r['reads'])} | **Files written**: {len(r['writes'])}")
    b.append("")
    b.append("## Call Relationships")
    if r["calls"]:
        b.append("**This routine calls:**")
        b.append("")
        for c in r["calls"]:
            b.append(f"- {linkify_call(c, stems)}")
    else:
        b.append("(No call statements; leaf node.)")
    b.append("")
    b.append("**Called by** (live Dataview back-query):")
    b.append("")
    b.append("```dataview")
    b.append('LIST file.link')
    b.append('WHERE type = "source" AND contains(calls, this.subroutine)')
    b.append("```")
    b.append("")
    if r["reads"] or r["writes"]:
        b.append("## File I/O")
        if r["writes"]:
            b.append("- **Writes**: " + ", ".join(f"`{w}`" for w in r["writes"]))
        if r["reads"]:
            rd = []
            for x in r["reads"]:
                if is_literal_file(x):
                    rd.append(f"`{x}`")
                else:
                    rd.append(f"`{x}` _(variable; see file.cio)_")
            b.append("- **Reads**: " + ", ".join(rd))
        b.append("")
    b.append("<!-- USER-NOTES-START -->")
    b.append("## Notes")
    b.append("Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.")
    user_body = preserve_user_body(target) or SEED_SOURCE.get(r["note_file"], "")
    if user_body.strip():
        b.append("")
        b.append(user_body.strip())
    b.append("<!-- USER-NOTES-END -->")
    write_note(target, "\n".join(fm), "\n".join(b))


def write_module_note(r: dict, stems: set[str]) -> None:
    target = MOD_DIR / f"{r['note_file']}.md"

    fm = []
    fm.append("type: module")
    fm.append("tags:")
    fm.append("  - swat/module")
    fm.append("  - swat/to-read")
    fm.append(f"file: {r['fname']}")
    fm.append(f"note_file: {r['note_file']}")
    fm.append(f"module_name: {r['name']}")
    fm.append("defines_types:" + yaml_list(r["types"]))
    fm.append("defines_vars:" + yaml_list(r["typevars"] + r["scalars"]))
    fm.append("purpose: " + yaml_str("; ".join(r["desc"])))

    b = []
    b.append(f"# {r['name']}")
    b.append("")
    b.append("> [!info] Module")
    b.append("> Defines derived types and module-level variables.")
    b.append("")
    b.append("## Defined Types")
    if r["types"]:
        b.append("| Type | Notes |")
        b.append("|---|---|")
        for t in r["types"]:
            b.append(f"| `{t}` |  |")
    else:
        b.append("(No type definitions detected.)")
    b.append("")
    b.append("## Module-Level Variables")
    vars_all = r["typevars"] + r["scalars"]
    if vars_all:
        b.append("| Variable | Type | Meaning |")
        b.append("|---|---|---|")
        shown = vars_all[:40]
        for v in shown:
            b.append(f"| `{v}` |  |  |")
        if len(vars_all) > 40:
            b.append("")
            b.append(f"*(Showing first 40 of {len(vars_all)} variables.)*")
    else:
        b.append("(No module-level variables detected.)")
    b.append("")
    b.append("## Used By Source Routines")
    b.append("")
    b.append("```dataview")
    b.append("LIST file.link")
    b.append('WHERE type = "source" AND contains(module, this.module_name)')
    b.append("```")
    b.append("")
    b.append("<!-- USER-NOTES-START -->")
    b.append("## Notes")
    b.append("Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.")
    user_body = preserve_user_body(target)
    if user_body.strip():
        b.append("")
        b.append(user_body.strip())
    b.append("<!-- USER-NOTES-END -->")
    write_note(target, "\n".join(fm), "\n".join(b))


def write_output_note(fname: str, writers: list[str]) -> None:
    safe = re.sub(r'[\\/:*?"<>|]', "_", fname)
    target = OUT_DIR / f"{safe}.md"
    ext = fname.rsplit(".", 1)[-1] if "." in fname else ""

    fm = []
    fm.append("type: output")
    fm.append("tags:")
    fm.append("  - swat/output")
    fm.append(f"file: {fname}")
    fm.append(f"ext: {ext}")
    fm.append("written_by:" + yaml_list([f"{w}.f90" for w in writers]))
    fm.append('purpose: ""')

    b = []
    b.append(f"# {fname}")
    b.append("")
    b.append("> [!info] Output File")
    b.append(f"> Written by SWAT+ routines. Extension: `.{ext}`.")
    b.append("")
    b.append("## Writer Routines")
    b.append("")
    for w in writers:
        b.append(f"- [[{w}.f90]]")
    b.append("")
    b.append("## File Format")
    b.append("(Add field meanings and column notes after tracing the writer code or inspecting actual output.)")

    write_note(target, "\n".join(fm), "\n".join(b))


def write_input_notes_from_cio(input_readers: dict[str, set[str]]) -> int:
    cio_path = IN_DIR / "file.cio.md"
    if not cio_path.exists():
        return 0

    cio = cio_path.read_text(encoding="utf-8", errors="replace")
    pairs = re.findall(r"\*\*([a-z0-9_.]+)\*\*\s*[:=]+\s*([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+)", cio)
    seen = {}
    for field, filename in pairs:
        filename = filename.strip()
        if filename not in seen:
            seen[filename] = field

    n = 0
    for filename, field in sorted(seen.items()):
        safe = re.sub(r'[\\/:*?"<>|]', "_", filename)
        if safe == "file.cio":
            continue
        target = IN_DIR / f"{safe}.md"
        ext = filename.rsplit(".", 1)[-1]

        readers = set(input_readers.get(filename, set()))
        for key, sts in input_readers.items():
            if key.endswith("%" + field) or key == field:
                readers |= sts

        fm = []
        fm.append("type: input")
        fm.append("tags:")
        fm.append("  - swat/input")
        fm.append(f"file: {filename}")
        fm.append(f"ext: {ext}")
        fm.append(f"cio_field: {field}")
        fm.append("read_by:" + yaml_list([f"{s}.f90" for s in sorted(readers)]))
        fm.append('purpose: ""')

        b = []
        b.append(f"# {filename}")
        b.append("")
        b.append("> [!info] Input File")
        b.append(f"> Declared in `file.cio` field `{field}`. See [[file.cio]] for the controlling file map.")
        b.append("")
        b.append("## Reader Routines")
        if readers:
            for s in sorted(readers):
                b.append(f"- [[{s}.f90]]")
        else:
            b.append("(Reader routine not located automatically; add evidence after tracing the code.)")
        b.append("")
        b.append("## File Format")
        b.append("(Add field meanings, units, and allowed values.)")
        write_note(target, "\n".join(fm), "\n".join(b))
        n += 1
    return n


def write_indexes(records: list[dict], output_writers: dict[str, set[str]]) -> None:
    n_src = sum(1 for r in records if r["kind"] != "module")
    n_mod = sum(1 for r in records if r["kind"] == "module")
    n_out = len(output_writers)

    overview = f"""# SWAT+ Code Learning System

> This subsystem maps the SWAT+ source code: routine call relationships, key variables, and input/output files.
> `_tools/gen_swat_notes.py` generates the note skeleton. User-written note sections are preserved across reruns.

## Statistics

- Source routines (program + subroutine): **{n_src}**
- Module files (`*_module.f90`): **{n_mod}**
- Output files: **{n_out}**; see [[input-output-file-index]]
- Input files: see [[file.cio]] as the controlling index

## Directory Structure

| Folder | Contents | Note type |
|---|---|---|
| `01-source-routines/` | `program` and `subroutine` notes, one per source file | `type: source` |
| `02-modules-and-variables/` | `*_module.f90` notes for derived types and global variables | `type: module` |
| `03-input-files/` | `file.cio` plus one note per input file | `type: input` |
| `04-output-files/` | `.out`, `.txt`, and other output file notes | `type: output` |

## Index Pages

- [[call-graph]] - main call tree and call frequency table
- [[module-variable-index]] - all modules and their type/variable definitions
- [[input-output-file-index]] - input/output file lists and reader/writer relationships

## How To Use

1. To read a routine, open `01-source-routines/xxx.f90.md` and review "Call Relationships" and "File I/O".
2. To see who calls a routine, use the live Dataview back-query at the end of each routine note.
3. To inspect key variables, open the defining module under `02-modules-and-variables/`.
4. To update reading progress, change frontmatter tags from `swat/to-read` to `swat/in-progress` or `swat/read`, and fill in `purpose`.
5. To classify a functional domain, add tags such as `swat/domain-hydrology`, `swat/domain-sediment`, or `swat/domain-reservoir`.

## Regenerate

After source updates, rerun the generator to refresh structured fields. Content between USER-NOTES markers is preserved.

```bash
python "docs/_tools/gen_swat_notes.py"
```
"""
    write_note(IDX_DIR / "00-SWATPLUS-overview.md", "", overview)

    main_rec = next((r for r in records if r["kind"] == "program"), None)
    mermaid = ["```mermaid", "graph LR"]
    if main_rec:
        mermaid.append(f'  main["main<br/>{main_rec["fname"]}"]')
        for c in main_rec["calls"]:
            mermaid.append(f'  main --> {c}["{c}"]')
    mermaid.append("```")
    mermaid_str = "\n".join(mermaid)

    call_graph = f"""# Call Graph

## Direct Calls From main

{mermaid_str}

> Full call relationships live in each source note under "Call Relationships".

## Call Frequency

```dataviewjs
const pages = dv.pages('"{BASE}/01-source-routines"').where(p => p.calls);
const counter = {{}};
for (const p of pages) {{
  for (const c of p.calls) {{ counter[c] = (counter[c] || 0) + 1; }}
}}
const rows = Object.entries(counter)
  .sort((a,b) => b[1]-a[1])
  .slice(0, 30)
  .map(([name, n]) => [name + ".f90", n]);
dv.table(["Called routine", "Caller count"], rows);
```

## Find Callers For A Routine

Use this query inside any source note to list all routines that call the current one:

````markdown
```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```
````
"""
    write_note(IDX_DIR / "call-graph.md", "", call_graph)

    mod_index = f"""# Module And Variable Index

## All Modules

```dataview
TABLE defines_types AS "Defined types", defines_vars AS "Module-level variables"
FROM "{BASE}/02-modules-and-variables"
SORT file ASC
```

## Functional Domain Tags

Add domain tags while reading so modules can be browsed by process area. Suggested values:

`swat/domain-control` `swat/domain-hydrology` `swat/domain-sediment` `swat/domain-nutrients` `swat/domain-climate`
`swat/domain-channel` `swat/domain-reservoir` `swat/domain-groundwater` `swat/domain-plant` `swat/domain-calibration` `swat/domain-utility`

## Browse Modules By Domain

```dataview
TABLE file, defines_types
FROM "{BASE}/02-modules-and-variables"
WHERE contains(tags, "#swat/domain-hydrology")
```
"""
    write_note(IDX_DIR / "module-variable-index.md", "", mod_index)

    io_index = f"""# Input/Output File Index

## Input Files

> [`file.cio`](file.cio.md) is the controlling input index. Other input-file notes live in `03-input-files/`.

```dataview
TABLE ext AS "Extension", read_by AS "Reader routines", cio_field AS "file.cio field"
FROM "{BASE}/03-input-files"
WHERE type = "input"
SORT file ASC
```

## Output Files

```dataview
TABLE ext AS "Extension", written_by AS "Writer routines"
FROM "{BASE}/04-output-files"
WHERE type = "output"
SORT file ASC
```

## Controlling Input File

- [[file.cio]] - control file that declares the input files and output path
"""
    write_note(IDX_DIR / "input-output-file-index.md", "", io_index)


if __name__ == "__main__":
    main()

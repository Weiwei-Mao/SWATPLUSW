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
        "- use: [[time_module.f90]], [[output_path_module.f90]]\n"
        "- Line 12: call [[readcio_read.f90]]\n"
        "- Line 15: call [[output_path_module.f90#open_output_file]]; opens [[files_out.out]] (unit 9000)\n"
        "- Line 18: call [[output_path_module.f90#open_output_file]]; opens [[diagnostics.out]] (unit 9001, recl 8000)\n"
        "- Line 21: call [[output_path_module.f90#open_output_file]]; opens [[area_calc.out]] (unit 9004, recl 80000)\n"
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
RE_FUNCTION = re.compile(r"^\s*(?!end\b)(?:recursive\s+|pure\s+|elemental\s+)*(?:[a-z0-9_(),=*:\s]+\s+)?function\s+([a-z0-9_]+)", re.I)
RE_USE = re.compile(r"^\s*use\s+([a-z0-9_]+)", re.I)
RE_CALL = re.compile(r"\bcall\s+([a-z0-9_]+)", re.I)
RE_OPEN_OUTPUT_FILE = re.compile(r'\bcall\s+open_output_file\s*\(\s*[^,]+,\s*["\']([^"\']+)["\']', re.I)
RE_OPEN = re.compile(r"\bopen\s*\(([^)]*)\)", re.I)
RE_FILEARG = re.compile(r"\bfile\s*=\s*([^,)]+)", re.I)
RE_UNITARG = re.compile(r"(?:^|,)\s*(?:unit\s*=\s*)?(\d+)\b")
RE_READ_FULL = re.compile(r"\bread\s*\(([^)]*)\)\s*(.*)$", re.I)
RE_TYPEDEF = re.compile(r"^\s*type\s+(?!.*\()\s*([a-z0-9_]+)", re.I)
RE_END_TYPE = re.compile(r"^\s*end\s+type\b", re.I)
RE_TYPEVAR = re.compile(r"^\s*type\s*\(\s*([a-z0-9_]+)\s*\)\s*::\s*([a-z0-9_,\s]+)", re.I)
RE_SCALAR = re.compile(r"^\s*(?:real|integer|logical|character[^:!]*)::\s*([a-z0-9_,\s]+)", re.I)
RE_DECL = re.compile(
    r"^\s*((?:real|integer|logical|complex|double\s+precision|character[^:!]*|type\s*\(\s*[a-z0-9_]+\s*\))[^:!]*)::\s*(.+)$",
    re.I,
)
RE_WRITE_U = re.compile(r"\bwrite\s*\(\s*(\d+)\s*,", re.I)
RE_READ_U = re.compile(r"\bread\s*\(\s*(\d+)\s*,", re.I)
RE_READ_STMT = re.compile(r"\bread\s*\([^)]*\)\s*(.+)$", re.I)


NEW_BOILERPLATE = {
    "## Notes",
    "Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.",
    "Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.",
}

BOILERPLATE = NEW_BOILERPLATE


def strip_comment(line: str) -> str:
    idx = line.find("!")
    return line[:idx] if idx >= 0 else line


def strip_strings(line: str) -> str:
    return re.sub(r"'[^']*'|\"[^\"]*\"", " ", line)


def fortran_logical_lines(raw_lines: list[str]) -> list[tuple[int, str]]:
    logical, buf, start = [], "", 1
    for line_no, raw in enumerate(raw_lines, start=1):
        code = strip_comment(raw).rstrip()
        stripped = code.strip()
        if not buf:
            start = line_no
        if stripped.startswith("&"):
            stripped = stripped[1:].lstrip()
        continued = stripped.endswith("&")
        if continued:
            stripped = stripped[:-1].rstrip()
        buf = (buf + " " + stripped).strip() if buf else stripped
        if not continued:
            if buf:
                logical.append((start, buf))
            buf = ""
    if buf:
        logical.append((start, buf))
    return logical


def source_comment(line: str) -> str:
    if "!!" in line:
        return line.split("!!", 1)[1].strip()
    if "!" in line:
        return line.split("!", 1)[1].strip()
    return ""


def split_top_level_commas(text: str) -> list[str]:
    parts, buf = [], []
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        parts.append(tail)
    return parts


def clean_decl_name(raw: str) -> str:
    raw = raw.split("=>", 1)[0].split("=", 1)[0].strip()
    m = re.match(r"([a-z][a-z0-9_]*)", raw, re.I)
    return m.group(1) if m else ""


def clean_type_spec(raw: str) -> str:
    spec = " ".join(raw.strip().split())
    tm = re.match(r"type\s*\(\s*([a-z0-9_]+)\s*\)", spec, re.I)
    if tm:
        return tm.group(1)
    return spec


def parse_declaration(raw_line: str) -> tuple[str, list[str], str] | None:
    line = strip_comment(raw_line)
    if "::" not in line:
        return None
    left, right = line.split("::", 1)
    left = left.strip()
    if not re.match(r"^(real|integer|logical|complex|double\s+precision|character\b|type\s*\()", left, re.I):
        return None
    type_spec = clean_type_spec(left)
    names = []
    for part in split_top_level_commas(right):
        name = clean_decl_name(part)
        if name and name.lower() not in [n.lower() for n in names]:
            names.append(name)
    if not names:
        return None
    return type_spec, names, source_comment(raw_line)


def clean_target(raw: str) -> str:
    return raw.strip().strip("'\"").strip()


# Filenames opened with a quoted literal but having no extension (e.g. 'salt_plants')
# are indistinguishable from variables after quote-stripping, so the parser records
# every quoted file= literal here; is_literal_file() then recognizes them.
LITERAL_FILES: set[str] = set()


def is_literal_file(target: str) -> bool:
    t = target.strip()
    if t in LITERAL_FILES:
        return True
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


def build_input_file_aliases() -> dict[str, str]:
    path = SRC / "input_file_module.f90"
    if not path.exists():
        return {}

    type_fields: dict[str, dict[str, str]] = {}
    aliases: dict[str, str] = {}
    current_type = ""

    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        ln = strip_comment(raw)
        tm = RE_TYPEDEF.match(ln)
        if tm:
            current_type = tm.group(1).lower()
            type_fields.setdefault(current_type, {})
            continue
        if re.match(r"^\s*end\s+type\b", ln, re.I):
            current_type = ""
            continue

        cm = re.match(
            r'^\s*character[^:!]*::\s*([a-z0-9_]+)\s*=\s*["\']([^"\']+)["\']',
            ln,
            re.I,
        )
        if cm:
            name = cm.group(1).lower()
            filename = cm.group(2).strip()
            if current_type:
                type_fields[current_type][name] = filename
            else:
                aliases[name] = filename
            continue

        vm = RE_TYPEVAR.match(ln)
        if vm:
            type_name = vm.group(1).lower()
            fields = type_fields.get(type_name, {})
            if not fields:
                continue
            for var in re.split(r"[,\s]+", vm.group(2).strip()):
                var = var.strip().lower()
                if not var:
                    continue
                for field, filename in fields.items():
                    aliases[f"{var}%{field}"] = filename

    return aliases


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

    uses, calls, opens, output_files = [], [], [], []
    types, typevars, scalars, subroutines, functions = [], [], [], [], []
    type_defs, module_vars, local_vars = [], [], []
    open_events, read_events = [], []
    in_module_scope = kind == "module"
    current_type = ""
    current_type_idx = -1

    for line_no, ln in enumerate(lines, start=1):
        raw_ln = raw_lines[line_no - 1]
        if not ln.strip():
            if in_module_scope and current_type_idx >= 0:
                cont = source_comment(raw_ln)
                if cont and type_defs[current_type_idx]["fields"]:
                    field = type_defs[current_type_idx]["fields"][-1]
                    field["comment"] = append_comment(field.get("comment", ""), cont)
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
                raw_file = fm.group(1)
                target = clean_target(raw_file)
                if raw_file.strip().startswith(("'", '"')):
                    LITERAL_FILES.add(target)
                unit = um.group(1) if um else ""
                opens.append((unit, target))

        for oom in RE_OPEN_OUTPUT_FILE.finditer(ln):
            target = clean_target(oom.group(1))
            if target not in output_files:
                output_files.append(target)

        if kind != "module":
            decl = parse_declaration(raw_ln)
            if decl:
                type_spec, names, comment = decl
                for v in names:
                    if v.lower() in [x["name"].lower() for x in local_vars]:
                        continue
                    local_vars.append(
                        {
                            "name": v,
                            "type": type_spec,
                            "line": line_no,
                            "comment": comment,
                        }
                    )

        if in_module_scope:
            if re.match(r"^\s*contains\b", ln, re.I) and not current_type:
                in_module_scope = False
            else:
                tm = RE_TYPEDEF.match(ln)
                if tm:
                    current_type = tm.group(1)
                    if current_type.lower() not in [t.lower() for t in types]:
                        types.append(current_type)
                    type_defs.append(
                        {
                            "name": current_type,
                            "line": line_no,
                            "comment": source_comment(raw_ln),
                            "fields": [],
                        }
                    )
                    current_type_idx = len(type_defs) - 1
                    continue
                if RE_END_TYPE.match(ln):
                    current_type = ""
                    current_type_idx = -1
                    continue

                decl = parse_declaration(raw_ln)
                if decl:
                    type_spec, names, comment = decl
                    if current_type and current_type_idx >= 0:
                        for v in names:
                            type_defs[current_type_idx]["fields"].append(
                                {
                                    "name": v,
                                    "type": type_spec,
                                    "line": line_no,
                                    "comment": comment,
                                }
                            )
                    else:
                        for v in names:
                            if v.lower() in [x["name"].lower() for x in module_vars]:
                                continue
                            item = {
                                "name": v,
                                "type": type_spec,
                                "line": line_no,
                                "comment": comment,
                            }
                            module_vars.append(item)
                            if type_spec.lower().startswith(("real", "integer", "logical", "character", "complex", "double precision")):
                                scalars.append(v)
                            else:
                                typevars.append(v)
        elif kind == "module":
            sm = RE_SUBROUT.match(ln)
            fm = RE_FUNCTION.match(ln)
            if sm:
                proc = sm.group(1).lower()
                if proc not in subroutines:
                    subroutines.append(proc)
            elif fm:
                proc = fm.group(1).lower()
                if proc not in functions:
                    functions.append(proc)

    for line_no, stmt in fortran_logical_lines(raw_lines):
        om = RE_OPEN.search(stmt)
        if om:
            inner = om.group(1)
            fm = RE_FILEARG.search(inner)
            um = RE_UNITARG.search(inner)
            if fm and um:
                open_events.append(
                    {
                        "line": line_no,
                        "unit": um.group(1),
                        "target": clean_target(fm.group(1)),
                    }
                )

        rm = RE_READ_FULL.search(stmt)
        if rm:
            um = RE_UNITARG.search(rm.group(1))
            if um:
                targets = [p.strip() for p in split_top_level_commas(rm.group(2)) if p.strip()]
                read_events.append(
                    {
                        "line": line_no,
                        "unit": um.group(1),
                        "targets": targets,
                    }
                )

    write_units = set(RE_WRITE_U.findall(text))
    read_units = set(RE_READ_U.findall(text))
    writes, reads = list(output_files), []
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
        "type_defs": type_defs,
        "module_vars": module_vars,
        "local_vars": local_vars,
        "open_events": open_events,
        "read_events": read_events,
        "subroutines": subroutines,
        "functions": functions,
        "procedures": subroutines + functions,
        "desc": extract_desc(raw_lines),
        "code_lines": lines,
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


def md_cell(s: str) -> str:
    return " ".join((s or "").replace("|", r"\|").split())


def append_comment(existing: str, extra: str) -> str:
    extra = " ".join((extra or "").split())
    if "::" in extra:
        return existing
    extra = extra.lstrip("|").strip()
    if not extra:
        return existing
    if not existing:
        return extra
    return f"{existing} {extra}"


def build_routine_note_map(records: list[dict]) -> dict[str, str]:
    routine_notes = {}
    for r in records:
        if r["kind"] != "module":
            routine_notes.setdefault(r["name"].lower(), r["note_file"])
    return routine_notes


def build_module_procedure_map(records: list[dict]) -> dict[str, tuple[str, str]]:
    proc_notes = {}
    for r in records:
        if r["kind"] != "module":
            continue
        for proc in r.get("subroutines", []) + r.get("functions", []):
            proc_notes.setdefault(proc, (r["note_file"], proc))
    return proc_notes


def build_called_by(records: list[dict]) -> dict[str, list[dict]]:
    callers = defaultdict(list)
    for r in records:
        for c in r["calls"]:
            callers[c].append(r)
    return callers


def build_module_variable_map(records: list[dict]) -> dict[str, dict[str, dict]]:
    module_vars: dict[str, dict[str, dict]] = {}
    for r in records:
        if r["kind"] != "module":
            continue
        module_key = r["name"].lower()
        module_vars[module_key] = {}
        for var in r.get("module_vars", []):
            module_vars[module_key][var["name"].lower()] = {
                "name": var["name"],
                "type": var.get("type", ""),
                "line": var.get("line", ""),
                "comment": var.get("comment", ""),
                "module": r["name"],
                "note_file": r["note_file"],
            }
    return module_vars


def build_type_map(records: list[dict]) -> dict[str, dict]:
    type_map: dict[str, dict] = {}
    for r in records:
        if r["kind"] != "module":
            continue
        for t in r.get("type_defs", []):
            type_map.setdefault(
                t["name"].lower(),
                {
                    "name": t["name"],
                    "module": r["name"],
                    "note_file": r["note_file"],
                    "line": t.get("line", ""),
                    "fields": {f["name"].lower(): f for f in t.get("fields", [])},
                },
            )
    return type_map


def extract_read_target_names(code_lines: list[str]) -> set[str]:
    names = set()
    for ln in code_lines:
        line = strip_strings(ln)
        m = RE_READ_STMT.search(line)
        if not m:
            continue
        for part in split_top_level_commas(m.group(1)):
            name = clean_decl_name(part)
            if name:
                names.add(name.lower())
    return names


def annotate_variable_refs(records: list[dict], module_vars: dict[str, dict[str, dict]]) -> None:
    for r in records:
        r["var_refs"] = []
        r["input_var_refs"] = []
        if r["kind"] == "module":
            continue

        candidates = {}
        for mod in r.get("uses", []):
            for name, info in module_vars.get(mod.lower(), {}).items():
                candidates.setdefault(name, info)
        if not candidates:
            continue

        code = "\n".join(strip_strings(ln) for ln in r.get("code_lines", []))
        tokens = set(t.lower() for t in re.findall(r"\b[a-z][a-z0-9_]*\b", code, re.I))
        read_targets = extract_read_target_names(r.get("code_lines", []))

        refs, input_refs = [], []
        for name, info in sorted(candidates.items(), key=lambda item: (item[1]["note_file"], item[1]["name"].lower())):
            if name not in tokens:
                continue
            refs.append(info)
            if name in read_targets:
                input_refs.append(info)
        r["var_refs"] = refs
        r["input_var_refs"] = input_refs


def target_path_parts(expr: str) -> list[str]:
    expr = re.sub(r"\([^()]*\)", "", expr.strip())
    expr = expr.strip("() ")
    parts = []
    for part in expr.split("%"):
        name = clean_decl_name(part)
        if name:
            parts.append(name)
    return parts


def split_units_meaning(comment: str) -> tuple[str, str]:
    comment = " ".join((comment or "").split())
    if "|" in comment:
        units, meaning = comment.split("|", 1)
        return units.strip(), meaning.strip()
    return "", comment


def variable_context_for_record(r: dict, module_vars: dict[str, dict[str, dict]]) -> dict[str, dict]:
    context: dict[str, dict] = {}
    for mod in r.get("uses", []):
        for name, info in module_vars.get(mod.lower(), {}).items():
            context.setdefault(name, info)
    for var in r.get("local_vars", []):
        context.setdefault(
            var["name"].lower(),
            {
                "name": var["name"],
                "type": var.get("type", ""),
                "line": var.get("line", ""),
                "comment": var.get("comment", ""),
                "module": "",
                "note_file": r["note_file"],
                "local": True,
            },
        )
    return context


def normalize_type_name(type_spec: str) -> str:
    return (type_spec or "").strip().lower()


def source_ref_for_variable(var_info: dict, field_type: str = "") -> str:
    if var_info.get("local"):
        line = var_info.get("line", "")
        return f"`{var_info['note_file']}:{line}`" if line else f"[[{var_info['note_file']}]]"
    return f"[[{var_info['note_file']}#{var_info['name']}]]"


def parameter_row(
    expr: str,
    type_spec: str,
    comment: str,
    source: str,
    reader: str,
    line: int,
) -> dict:
    units, meaning = split_units_meaning(comment)
    return {
        "expr": expr,
        "type": type_spec or "",
        "units": units,
        "meaning": meaning,
        "source": source,
        "reader": reader,
        "line": str(line),
    }


def flatten_type_parameters(
    type_name: str,
    type_map: dict[str, dict],
    prefix: str,
    source: str,
    reader: str,
    line: int,
    depth: int = 0,
    parent_comment: str = "",
) -> list[dict]:
    type_info = type_map.get(normalize_type_name(type_name))
    if not type_info or depth > 4:
        return []
    rows = []
    for field in type_info["fields"].values():
        expr = f"{prefix}%{field['name']}"
        field_type = field.get("type", "")
        comment = field.get("comment", "") or parent_comment
        nested = type_map.get(normalize_type_name(field_type))
        if nested:
            nested_comment = field.get("comment", "") or parent_comment
            rows.extend(
                flatten_type_parameters(
                    field_type,
                    type_map,
                    expr,
                    source,
                    reader,
                    line,
                    depth + 1,
                    nested_comment,
                )
            )
        else:
            rows.append(parameter_row(expr, field_type, comment, source, reader, line))
    return rows


def resolve_field_path(type_name: str, path: list[str], type_map: dict[str, dict]) -> tuple[str, str]:
    current_type = normalize_type_name(type_name)
    comments = []
    field_type = ""
    for part in path:
        type_info = type_map.get(current_type)
        if not type_info:
            return field_type, " / ".join(c for c in comments if c)
        field = type_info["fields"].get(part.lower())
        if not field:
            return field_type, " / ".join(c for c in comments if c)
        field_type = field.get("type", "")
        if field.get("comment"):
            comments.append(field["comment"])
        current_type = normalize_type_name(field_type)
    return field_type, " / ".join(c for c in comments if c)


def parameter_rows_for_target(
    target: str,
    r: dict,
    var_context: dict[str, dict],
    type_map: dict[str, dict],
    line: int,
) -> list[dict]:
    parts = target_path_parts(target)
    if not parts:
        return []
    base = parts[0].lower()
    if base in {"titldum", "header"}:
        return []
    var_info = var_context.get(base)
    if not var_info:
        return []

    source = source_ref_for_variable(var_info)
    base_expr = var_info["name"]
    type_spec = var_info.get("type", "")
    if len(parts) == 1:
        rows = flatten_type_parameters(type_spec, type_map, base_expr, source, r["note_file"], line)
        if rows:
            return rows
        return [parameter_row(base_expr, type_spec, var_info.get("comment", ""), source, r["note_file"], line)]

    path = parts[1:]
    expr = base_expr + "%" + "%".join(path)
    field_type, comment = resolve_field_path(type_spec, path, type_map)
    return [parameter_row(expr, field_type, comment, source, r["note_file"], line)]


def find_open_for_read(open_events: list[dict], read_event: dict) -> dict | None:
    candidates = [
        ev
        for ev in open_events
        if ev["unit"] == read_event["unit"] and ev["line"] <= read_event["line"]
    ]
    if not candidates:
        return None
    return sorted(candidates, key=lambda ev: ev["line"])[-1]


def build_input_details(
    records: list[dict],
    file_aliases: dict[str, str],
    module_vars: dict[str, dict[str, dict]],
    type_map: dict[str, dict],
) -> dict[str, dict]:
    details: dict[str, dict] = defaultdict(lambda: {"events": [], "parameters": []})
    seen_params: dict[str, set[tuple[str, str, str]]] = defaultdict(set)

    for r in records:
        if r["kind"] == "module":
            continue
        var_context = variable_context_for_record(r, module_vars)
        for read_event in r.get("read_events", []):
            open_event = find_open_for_read(r.get("open_events", []), read_event)
            if not open_event:
                continue
            filename = resolve_file_io_target(open_event["target"], file_aliases)
            if not filename:
                continue

            event_targets = [t.strip() for t in read_event.get("targets", []) if t.strip()]
            details[filename]["events"].append(
                {
                    "reader": r["note_file"],
                    "line": read_event["line"],
                    "targets": event_targets,
                }
            )
            for target in event_targets:
                for row in parameter_rows_for_target(target, r, var_context, type_map, read_event["line"]):
                    key = (row["expr"].lower(), row["source"], row["reader"])
                    if key in seen_params[filename]:
                        continue
                    seen_params[filename].add(key)
                    details[filename]["parameters"].append(row)

    return details


def linkify_record(r: dict) -> str:
    return f"[[{r['note_file']}]]"


def linkify_call(name: str, routine_notes: dict[str, str], module_procs: dict[str, tuple[str, str]]) -> str:
    if name in routine_notes:
        return f"[[{routine_notes[name]}]]"
    if name in module_procs:
        note_file, heading = module_procs[name]
        return f"[[{note_file}#{heading}]]"
    return f"`{name}`"


def linkify_module(mod: str, mod_stems: set[str]) -> str:
    if mod in mod_stems:
        return f"[[{mod}.f90]]"
    return f"`{mod}`"


def linkify_variable_ref(ref: dict) -> str:
    return f"[[{ref['note_file']}#{ref['name']}]]"


def safe_note_name(fname: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "_", fname)


def resolve_file_io_target(target: str, file_aliases: dict[str, str]) -> str:
    alias = file_aliases.get(target.lower())
    if alias:
        return alias
    if is_literal_file(target):
        return target
    return ""


def linkify_file_io(target: str, file_aliases: dict[str, str]) -> str:
    exact = resolve_file_io_target(target, file_aliases)
    if exact:
        return f"[[{safe_note_name(exact)}]]"
    return f"`{target}` _(variable; see [[file.cio]])_"


def linkify_file_io_list(items: list[str], file_aliases: dict[str, str]) -> str:
    return ", ".join(linkify_file_io_items(items, file_aliases))


def linkify_file_io_items(items: list[str], file_aliases: dict[str, str]) -> list[str]:
    rendered = []
    seen = set()
    for item in items:
        link = linkify_file_io(item, file_aliases)
        if link not in seen:
            rendered.append(link)
            seen.add(link)
    return rendered


def append_markdown_item_list(b: list[str], label: str, items: list[str]) -> None:
    b.append(f"- **{label}**:")
    if items:
        for item in items:
            b.append(f"  - {item}")
    else:
        b.append("  - -")


def translate_preserved_note(text: str) -> str:
    text = "\n".join(ln.rstrip() for ln in text.splitlines())
    text = text.replace("，", ",").replace("ï¼Œ", ",")
    text = text.replace(",checks", ", checks")
    text = re.sub(r"\[\[([^|\]\n]+#[^|\]\n]+)\|[^\]\n]+\]\]", r"[[\1]]", text)
    text = re.sub(r"\[\[([^\]\n]+)#\^\]\]([a-z][a-z0-9_]*)", r"[[\1#\2]]", text, flags=re.I)
    return re.sub(r"\[\[([^\]\n]+)#\^([a-z][a-z0-9_]*)\]\]", r"[[\1#\2]]", text, flags=re.I)


def preserve_user_body(target_path: Path) -> str:
    if not target_path.exists():
        return ""
    content = target_path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<!-- USER-NOTES-START -->(.*?)<!-- USER-NOTES-END -->", content, re.S)
    if not m:
        return ""
    lines = [ln for ln in m.group(1).splitlines() if ln.strip() not in BOILERPLATE]
    return translate_preserved_note("\n".join(lines).strip())


def load_existing_tags(path: Path) -> list[str]:
    """Read the `tags:` block from an existing note's frontmatter."""
    if not path.exists():
        return []
    txt = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^tags:\s*\n((?:\s+-\s+.+\n?)+)", txt, re.M)
    if not m:
        return []
    return [t.strip() for t in re.findall(r"-\s+(.+)", m.group(1))]


def preserved_tags(target: Path, default_type: str) -> list[str]:
    """Keep the user's reading-status (swat/read, swat/in-progress) and any domain
    tags across regeneration, instead of always resetting to swat/to-read."""
    existing = load_existing_tags(target)
    tags = [default_type]
    status = [t for t in existing if t in ("swat/read", "swat/in-progress")]
    tags.append(status[0] if status else "swat/to-read")
    reserved = {"swat/source", "swat/module", "swat/to-read", "swat/read", "swat/in-progress"}
    for t in existing:
        if t not in reserved and t not in tags:
            tags.append(t)
    return tags


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
    routine_notes = build_routine_note_map(records)
    module_procs = build_module_procedure_map(records)
    called_by = build_called_by(records)
    module_vars = build_module_variable_map(records)
    type_map = build_type_map(records)
    annotate_variable_refs(records, module_vars)
    file_aliases = build_input_file_aliases()
    input_details = build_input_details(records, file_aliases, module_vars, type_map)

    output_writers = defaultdict(set)
    input_readers = defaultdict(set)

    n_src = n_mod = 0
    for r in records:
        for w in r["writes"]:
            if is_literal_file(w):
                output_writers[w].add(r["stem"])
        for rr in r["reads"]:
            exact_read = resolve_file_io_target(rr, file_aliases)
            if exact_read:
                input_readers[exact_read].add(r["stem"])

        if r["kind"] == "module":
            write_module_note(r, stems)
            n_mod += 1
        else:
            write_source_note(r, mod_stems, routine_notes, module_procs, called_by, file_aliases)
            n_src += 1

    n_out = 0
    for fname in sorted(output_writers.keys()):
        n_out += 1
        write_output_note(fname, sorted(output_writers[fname]))

    n_in = write_input_notes_from_cio(input_readers, input_details)
    n_in += write_extra_input_notes(input_readers, input_details)
    write_indexes(records, output_writers)

    print(f"Generated: source {n_src} / modules {n_mod} / outputs {n_out} / inputs {n_in}")


def write_source_note(
    r: dict,
    mod_stems: set[str],
    routine_notes: dict[str, str],
    module_procs: dict[str, tuple[str, str]],
    called_by: dict[str, list[dict]],
    file_aliases: dict[str, str],
) -> None:
    target = SRC_DIR / f"{r['note_file']}.md"
    subtype = "program" if r["kind"] == "program" else "subroutine"

    fm = []
    fm.append("type: source")
    fm.append(f"subtype: {subtype}")
    fm.append("tags:")
    for _t in preserved_tags(target, "swat/source"):
        fm.append(f"  - {_t}")
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
    fm.append("uses_variables:" + yaml_list([f"{v['note_file']}#{v['name']}" for v in r.get("var_refs", [])]))
    fm.append("input_variables:" + yaml_list([f"{v['note_file']}#{v['name']}" for v in r.get("input_var_refs", [])]))
    fm.append("reads:" + yaml_list(r["reads"]))
    fm.append("writes:" + yaml_list(r["writes"]))
    fm.append("purpose: " + yaml_str("; ".join(r["desc"])))

    desc = "; ".join(r["desc"]) if r["desc"] else "TBD"

    b = []
    b.append(f"# {r['name']}")
    b.append("")
    b.append("> [!info] Summary")
    b.append(f"> {desc}")
    b.append("")
    b.append("## Basic Information")
    b.append(f"- **Type**: `{subtype}`")
    b.append(f"- **Source file**: `{r['fname']}`")
    append_markdown_item_list(b, "Modules used", [linkify_module(u, mod_stems) for u in r["uses"]])
    b.append(f"- **Subroutine calls**: {len(r['calls'])} | **Files read**: {len(r['reads'])} | **Files written**: {len(r['writes'])}")
    b.append("")
    b.append("## Call Relationships")
    if r["calls"]:
        b.append("**This routine calls:**")
        b.append("")
        for c in r["calls"]:
            b.append(f"- {linkify_call(c, routine_notes, module_procs)}")
    else:
        b.append("(No call statements; leaf node.)")
    b.append("")
    b.append("**Called by:**")
    callers = called_by.get(r["name"].lower(), [])
    if callers:
        b.append("")
        for caller in callers:
            b.append(f"- {linkify_record(caller)}")
    else:
        b.append("")
        b.append("(No static callers detected.)")
    b.append("")
    b.append("**Live Dataview back-query:**")
    b.append("")
    b.append("```dataview")
    b.append('LIST file.link')
    b.append('WHERE type = "source" AND contains(calls, this.subroutine)')
    b.append("```")
    b.append("")
    b.append("## Module Variables Referenced")
    if r.get("var_refs"):
        for ref in r["var_refs"]:
            type_note = f" - `{ref['type']}`" if ref.get("type") else ""
            b.append(f"- {linkify_variable_ref(ref)}{type_note}")
    else:
        b.append("(No module-level variable references detected.)")
    if r.get("input_var_refs"):
        b.append("")
        b.append("**Populated by file reads:**")
        b.append("")
        for ref in r["input_var_refs"]:
            b.append(f"- {linkify_variable_ref(ref)}")
    b.append("")
    if r["reads"] or r["writes"]:
        b.append("## File I/O")
        if r["writes"]:
            append_markdown_item_list(b, "Writes", linkify_file_io_items(r["writes"], file_aliases))
        if r["reads"]:
            append_markdown_item_list(b, "Reads", linkify_file_io_items(r["reads"], file_aliases))
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
    for _t in preserved_tags(target, "swat/module"):
        fm.append(f"  - {_t}")
    fm.append(f"file: {r['fname']}")
    fm.append(f"note_file: {r['note_file']}")
    fm.append(f"module_name: {r['name']}")
    fm.append("defines_types:" + yaml_list(r["types"]))
    fm.append("defines_vars:" + yaml_list([v["name"] for v in r.get("module_vars", [])]))
    fm.append("defines_subroutines:" + yaml_list(r.get("subroutines", [])))
    fm.append("defines_functions:" + yaml_list(r.get("functions", [])))
    fm.append("defines_procedures:" + yaml_list(r.get("procedures", [])))
    fm.append("purpose: " + yaml_str("; ".join(r["desc"])))

    b = []
    b.append(f"# {r['name']}")
    b.append("")
    b.append("> [!info] Module")
    b.append("> Defines derived types and module-level variables.")
    b.append("")
    b.append("## Defined Types")
    if r.get("type_defs"):
        for t in r["type_defs"]:
            b.append(f"### {t['name']}")
            b.append("")
            b.append(f"- **Defined in source**: `{r['fname']}:{t['line']}`")
            if t.get("comment"):
                b.append(f"- **Source note**: {t['comment']}")
            if t.get("fields"):
                b.append("")
                b.append("| Field | Type | Source line | Meaning |")
                b.append("|---|---|---:|---|")
                for field in t["fields"]:
                    b.append(
                        f"| `{field['name']}` | `{md_cell(field['type'])}` | {field['line']} | {md_cell(field.get('comment', ''))} |"
                    )
            b.append("")
    else:
        b.append("(No type definitions detected.)")
        b.append("")
    b.append("## Variables Defined")
    vars_all = r.get("module_vars", [])
    if vars_all:
        for v in vars_all:
            b.append(f"### {v['name']}")
            b.append("")
            b.append(f"- **Type**: `{v['type']}`")
            b.append(f"- **Defined in source**: `{r['fname']}:{v['line']}`")
            if v.get("comment"):
                b.append(f"- **Source note**: {v['comment']}")
            b.append("")
    else:
        b.append("(No variables detected.)")
        b.append("")
    b.append("## Subroutines Defined")
    if r.get("subroutines"):
        for proc in r["subroutines"]:
            b.append(f"### {proc}")
            b.append("")
    else:
        b.append("(No subroutines detected.)")
        b.append("")
    b.append("## Functions Defined")
    if r.get("functions"):
        for proc in r["functions"]:
            b.append(f"### {proc}")
            b.append("")
    else:
        b.append("(No functions detected.)")
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


def append_input_detail_sections(
    b: list[str],
    filename: str,
    field: str,
    readers: set[str],
    details: dict,
    auxiliary: bool = False,
) -> None:
    b.append("## Overview")
    if field:
        b.append(f"- **Declared in `file.cio` field**: `{field}`")
    elif auxiliary:
        b.append("- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.")
    else:
        b.append("- **Declared in `file.cio` field**: not identified.")
    b.append("- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.")
    b.append("- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.")
    b.append("")

    b.append("## Reader Routines")
    if readers:
        for s in sorted(readers):
            b.append(f"- [[{s}.f90]]")
    else:
        b.append("(Reader routine not located automatically; add evidence after tracing the code.)")
    b.append("")

    b.append("## File Structure")
    events = details.get("events", [])
    if events:
        for ev in events[:80]:
            targets = ", ".join(f"`{t}`" for t in ev.get("targets", [])) or "(no targets parsed)"
            b.append(f"- [[{ev['reader']}]] source line {ev['line']}: reads {targets}")
        if len(events) > 80:
            b.append(f"- ... {len(events) - 80} additional read statements omitted from this generated summary.")
    else:
        b.append("(No line-level read structure detected automatically.)")
    b.append("")

    b.append("## Parameters")
    params = details.get("parameters", [])
    if params:
        b.append("| Parameter | Type | Units | Meaning | Source | Reader line |")
        b.append("|---|---|---|---|---|---:|")
        for row in params:
            b.append(
                "| "
                f"`{md_cell(row['expr'])}` | "
                f"`{md_cell(row['type'])}` | "
                f"{md_cell(row['units'])} | "
                f"{md_cell(row['meaning'])} | "
                f"{row['source']} | "
                f"[[{row['reader']}]]:{row['line']} |"
            )
    else:
        b.append("(No parameter table detected automatically. Check the reader routines above for manual interpretation.)")


def input_files_declared_in_cio() -> dict[str, str]:
    cio_path = IN_DIR / "file.cio.md"
    if not cio_path.exists():
        return {}

    cio = cio_path.read_text(encoding="utf-8", errors="replace")
    pairs = re.findall(r"\*\*([a-z0-9_.]+)\*\*\s*[:=]+\s*([a-zA-Z0-9_./-]+\.[a-zA-Z0-9]+)", cio)
    seen = {}
    for field, filename in pairs:
        filename = filename.strip()
        if filename not in seen:
            seen[filename] = field
    return seen


def write_input_notes_from_cio(input_readers: dict[str, set[str]], input_details: dict[str, dict]) -> int:
    seen = input_files_declared_in_cio()
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
        append_input_detail_sections(b, filename, field, readers, input_details.get(filename, {}))
        write_note(target, "\n".join(fm), "\n".join(b))
        n += 1
    return n


def write_extra_input_notes(input_readers: dict[str, set[str]], input_details: dict[str, dict]) -> int:
    n = 0
    cio_files = set(input_files_declared_in_cio())
    for filename, readers in sorted(input_readers.items()):
        safe = safe_note_name(filename)
        if safe == "file.cio" or filename in cio_files:
            continue
        target = IN_DIR / f"{safe}.md"
        ext = filename.rsplit(".", 1)[-1] if "." in filename else ""

        fm = []
        fm.append("type: input")
        fm.append("tags:")
        fm.append("  - swat/input")
        fm.append("  - swat/auxiliary-input")
        fm.append(f"file: {filename}")
        fm.append(f"ext: {ext}")
        fm.append("cio_field: []")
        fm.append("read_by:" + yaml_list([f"{s}.f90" for s in sorted(readers)]))
        fm.append('purpose: ""')

        b = []
        b.append(f"# {filename}")
        b.append("")
        b.append("> [!info] Input File")
        b.append("> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.")
        b.append("")
        append_input_detail_sections(b, filename, "", readers, input_details.get(filename, {}), auxiliary=True)
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

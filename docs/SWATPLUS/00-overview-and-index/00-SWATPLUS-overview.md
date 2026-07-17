---
type: overview
tags:
  - swat/overview
  - swat/index
---

# SWAT+ Code Learning System

> This subsystem maps the SWAT+ source code: routine call relationships, key variables, and input/output files.
> `_tools/gen_swat_notes.py` generates the note skeleton. User-written note sections are preserved across reruns.

## Statistics

- Source routines (program + subroutine): **583**
- Module files (`*_module.f90`): **66**
- Output files: **669**; see [[input-output-file-index]]
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
- [[input-file-architecture]] - how readers locate input files (file.cio vs hardcoded) and file roles (database / scenario / operations)
- [[hardcoded-input-files]] - curated index of literal/default input filenames not controlled by file.cio
- [[osu-1hru-input-inventory]] - configured files, active objects, and record chains in the default debug scenario
- [[osu-1hru-baseline-and-debug]] - reproducible build, run, breakpoint, and output checks for the default scenario
- [[source-reading-checklist]] - required questions and status vocabulary for durable source-reading notes

## How To Use

1. Before changing model behavior, establish the current scenario result with [[osu-1hru-baseline-and-debug]].
2. To read a routine, open `01-source-routines/xxx.f90.md` and review "Call Relationships" and "File I/O".
3. To see who calls a routine, use the live Dataview back-query at the end of each routine note.
4. To inspect key variables, open the defining module under `02-modules-and-variables/`.
5. To update reading progress, follow [[source-reading-checklist]], change frontmatter tags from `swat/to-read` to `swat/in-progress` or `swat/read`, and fill in `purpose`.
6. To classify a functional domain, add tags such as `swat/domain-hydrology`, `swat/domain-sediment`, or `swat/domain-reservoir`.

## Regenerate

After source updates, rerun the generator to refresh structured fields. Content between USER-NOTES markers is preserved.

```bash
python "docs/_tools/gen_swat_notes.py"
```

To check for stale generated notes without writing files:

```bash
python "docs/_tools/gen_swat_notes.py" --check-orphans
```

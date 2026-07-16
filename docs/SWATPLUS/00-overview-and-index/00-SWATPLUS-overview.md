# SWAT+ Code Learning System

> This subsystem maps the SWAT+ source code: routine call relationships, key variables, and input/output files.
> `_tools/gen_swat_notes.py` generates the note skeleton. User-written note sections are preserved across reruns.

## Statistics

- Source routines (program + subroutine): **583**
- Module files (`*_module.f90`): **66**
- Output files: **51**; see [[input-output-file-index]]
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

---
tags:
  - project
  - project/open
  - research
type: project
area: research
project_order: 14
project_name: 'APEX/SWAT'
aliases:
  - 'APEX/SWAT'
project_folder: '14 - APEX/SWAT'
status: active
progress_pct: 0
progress_label: '0%'
progress_note: 'Project started'
source: ''
pi: ''
role: ''
funding: ''
proposal: ''
target: ''
notion_export: false
start_date: 2026-05-05
end_date: ''
---
# APEX/SWAT

This folder is the English entry point for the SWAT+ code-learning notes in this repository.

## SWAT+ Notes

- Overview: [00-SWATPLUS-overview](SWATPLUS/00-overview-and-index/00-SWATPLUS-overview.md)
- Call graph: [call-graph](SWATPLUS/00-overview-and-index/call-graph.md)
- Module and variable index: [module-variable-index](SWATPLUS/00-overview-and-index/module-variable-index.md)
- Input/output file index: [input-output-file-index](SWATPLUS/00-overview-and-index/input-output-file-index.md)

## Generated Note Tree

- `SWATPLUS/01-source-routines/`: 583 program and subroutine notes.
- `SWATPLUS/02-modules-and-variables/`: 66 module notes.
- `SWATPLUS/03-input-files/`: `file.cio` plus per-input-file notes.
- `SWATPLUS/04-output-files/`: per-output-file notes traced from writer routines.

## Regeneration

The generator is repo-local and reads `SWATPLUS/swatplus/src`. It also includes `main.f90.in` as the source for `main.f90.md`, because this workspace tracks the template and generates the Visual Studio `main.f90` copy.

```powershell
python docs\_tools\gen_swat_notes.py
```

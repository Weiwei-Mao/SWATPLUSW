---
type: input
tags:
  - swat/input
file: wnd.cli
ext: cli
cio_field: wnd_cli
read_by:
  - cli_wmeas.f90
purpose: ""
---

# wnd.cli

> [!info] Input File
> Declared in `file.cio` field `wnd_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `wnd_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_wmeas.f90]]

## File Structure
- [[cli_wmeas.f90]] source line 32: reads `titldum`
- [[cli_wmeas.f90]] source line 34: reads `header`
- [[cli_wmeas.f90]] source line 37: reads `titldum`
- [[cli_wmeas.f90]] source line 46: reads `titldum`
- [[cli_wmeas.f90]] source line 48: reads `header`
- [[cli_wmeas.f90]] source line 51: reads `wnd_n(i)`
- [[cli_wmeas.f90]] source line 56: reads `titldum`
- [[cli_wmeas.f90]] source line 58: reads `header`
- [[cli_wmeas.f90]] source line 62: reads `wnd(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `wnd_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#wnd_n]] | [[cli_wmeas.f90]]:51 |
| `wnd%filename` | `character (len=50)` |  |  | [[climate_module.f90#wnd]] | [[cli_wmeas.f90]]:62 |

---
type: input
tags:
  - swat/input
file: tmp.cli
ext: cli
cio_field: tmp_cli
read_by:
  - cli_tmeas.f90
purpose: ""
---

# tmp.cli

> [!info] Input File
> Declared in `file.cio` field `tmp_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `tmp_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_tmeas.f90]]

## File Structure
- [[cli_tmeas.f90]] source line 41: reads `titldum`
- [[cli_tmeas.f90]] source line 43: reads `header`
- [[cli_tmeas.f90]] source line 47: reads `titldum`
- [[cli_tmeas.f90]] source line 56: reads `titldum`
- [[cli_tmeas.f90]] source line 58: reads `header`
- [[cli_tmeas.f90]] source line 61: reads `tmp_n(i)`
- [[cli_tmeas.f90]] source line 66: reads `titldum`
- [[cli_tmeas.f90]] source line 68: reads `header`
- [[cli_tmeas.f90]] source line 72: reads `tmp(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `tmp_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#tmp_n]] | [[cli_tmeas.f90]]:61 |
| `tmp%filename` | `character (len=50)` |  |  | [[climate_module.f90#tmp]] | [[cli_tmeas.f90]]:72 |

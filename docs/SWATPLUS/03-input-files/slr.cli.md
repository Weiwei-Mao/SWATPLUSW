---
type: input
tags:
  - swat/input
file: slr.cli
ext: cli
cio_field: slr_cli
read_by:
  - cli_smeas.f90
purpose: ""
---

# slr.cli

> [!info] Input File
> Declared in `file.cio` field `slr_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `slr_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_smeas.f90]]

## File Structure
- [[cli_smeas.f90]] source line 33: reads `titldum`
- [[cli_smeas.f90]] source line 35: reads `header`
- [[cli_smeas.f90]] source line 38: reads `titldum`
- [[cli_smeas.f90]] source line 47: reads `titldum`
- [[cli_smeas.f90]] source line 49: reads `header`
- [[cli_smeas.f90]] source line 52: reads `slr_n(i)`
- [[cli_smeas.f90]] source line 57: reads `titldum`
- [[cli_smeas.f90]] source line 59: reads `header`
- [[cli_smeas.f90]] source line 63: reads `slr(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `slr_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#slr_n]] | [[cli_smeas.f90]]:52 |
| `slr%filename` | `character (len=50)` |  |  | [[climate_module.f90#slr]] | [[cli_smeas.f90]]:63 |

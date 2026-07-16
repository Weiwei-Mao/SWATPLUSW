---
type: input
tags:
  - swat/input
file: pet.cli
ext: cli
cio_field: pet_cli
read_by:
  - basin_read_cc.f90
  - cli_petmeas.f90
purpose: ""
---

# pet.cli

> [!info] Input File
> Declared in `file.cio` field `pet_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pet_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_read_cc.f90]]
- [[cli_petmeas.f90]]

## File Structure
- [[basin_read_cc.f90]] source line 33: reads `titldum`
- [[basin_read_cc.f90]] source line 35: reads `header`
- [[basin_read_cc.f90]] source line 37: reads `titldum`
- [[cli_petmeas.f90]] source line 33: reads `titldum`
- [[cli_petmeas.f90]] source line 35: reads `header`
- [[cli_petmeas.f90]] source line 38: reads `titldum`
- [[cli_petmeas.f90]] source line 47: reads `titldum`
- [[cli_petmeas.f90]] source line 49: reads `header`
- [[cli_petmeas.f90]] source line 52: reads `petm_n(i)`
- [[cli_petmeas.f90]] source line 57: reads `titldum`
- [[cli_petmeas.f90]] source line 59: reads `header`
- [[cli_petmeas.f90]] source line 63: reads `petm(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `petm_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#petm_n]] | [[cli_petmeas.f90]]:52 |
| `petm%filename` | `character (len=50)` |  |  | [[climate_module.f90#petm]] | [[cli_petmeas.f90]]:63 |

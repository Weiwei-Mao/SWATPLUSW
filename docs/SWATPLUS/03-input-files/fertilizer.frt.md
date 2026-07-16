---
type: input
tags:
  - swat/input
file: fertilizer.frt
ext: frt
cio_field: fert_frt
read_by:
  - fert_parm_read.f90
purpose: ""
---

# fertilizer.frt

> [!info] Input File
> Declared in `file.cio` field `fert_frt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `fert_frt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[fert_parm_read.f90]]

## File Structure
- [[fert_parm_read.f90]] source line 28: reads `titldum`
- [[fert_parm_read.f90]] source line 30: reads `header`
- [[fert_parm_read.f90]] source line 33: reads `titldum`
- [[fert_parm_read.f90]] source line 41: reads `titldum`
- [[fert_parm_read.f90]] source line 43: reads `header`
- [[fert_parm_read.f90]] source line 47: reads `fertdb(it)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `fertdb%fertnm` | `character(len=16)` |  |  | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |
| `fertdb%fminn` | `real` | kg minN/kg frt | fract of fert which is mineral nit (NO3+NH3) | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |
| `fertdb%fminp` | `real` | kg minN/kg frt | frac of fert which is mineral phos | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |
| `fertdb%forgn` | `real` | kg orgN/kg frt | frac of fert which is org n | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |
| `fertdb%forgp` | `real` | kg orgP/kg frt | frac of fert which is org p | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |
| `fertdb%fnh3n` | `real` | kg NH3-N/kg N | frac of mineral N content of fert which is NH3 | [[fertilizer_data_module.f90#fertdb]] | [[fert_parm_read.f90]]:47 |

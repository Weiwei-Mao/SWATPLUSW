---
type: input
tags:
  - swat/input
file: tillage.til
ext: til
cio_field: till_til
read_by:
  - till_parm_read.f90
purpose: ""
---

# tillage.til

> [!info] Input File
> Declared in `file.cio` field `till_til`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `till_til`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[till_parm_read.f90]]

## File Structure
- [[till_parm_read.f90]] source line 28: reads `titldum`
- [[till_parm_read.f90]] source line 30: reads `header`
- [[till_parm_read.f90]] source line 33: reads `titldum`
- [[till_parm_read.f90]] source line 41: reads `titldum`
- [[till_parm_read.f90]] source line 43: reads `header`
- [[till_parm_read.f90]] source line 47: reads `tilldb(itl)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `tilldb%tillnm` | `character(len=16)` |  |  | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |
| `tilldb%effmix` | `real` | none | mixing efficiency of tillage operation | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |
| `tilldb%deptil` | `real` | mm | depth of mixing caused by tillage | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |
| `tilldb%ranrns` | `real` | mm | random roughness | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |
| `tilldb%ridge_ht` | `real` | mm | ridge height | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |
| `tilldb%ridge_sp` | `real` | mm | ridge interval (or row spacing) | [[tillage_data_module.f90#tilldb]] | [[till_parm_read.f90]]:47 |

---
type: input
tags:
  - swat/input
file: urban.urb
ext: urb
cio_field: urban_urb
read_by:
  - urban_parm_read.f90
purpose: ""
---

# urban.urb

> [!info] Input File
> Declared in `file.cio` field `urban_urb`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `urban_urb`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[urban_parm_read.f90]]

## File Structure
- [[urban_parm_read.f90]] source line 22: reads `titldum`
- [[urban_parm_read.f90]] source line 24: reads `header`
- [[urban_parm_read.f90]] source line 28: reads `titldum`
- [[urban_parm_read.f90]] source line 36: reads `titldum`
- [[urban_parm_read.f90]] source line 38: reads `header`
- [[urban_parm_read.f90]] source line 42: reads `urbdb(iu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `urbdb%urbnm` | `character(len=16)` |  |  | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%fimp` | `real` | fraction | fraction of HRU area that is imp | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%fcimp` | `real` | fraction | fraction of HRU that is classified as directly connected imp | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%curbden` | `real` | km/ha | curb length density | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%urbcoef` | `real` | 1/mm | wash-off coefficient for removal of constituents from an imp surface | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%dirtmx` | `real` | kg/curb km | max amt of solids allowed to build up on imp surfaces | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%thalf` | `real` | days | time for the amt of solids on imp areas to build up to 1/2 max level | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%tnconc` | `real` | mg N/kg sed | conc of total nitrogen in suspended solid load from imp areas | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%tpconc` | `real` | mg P/kg sed | conc of total phosphorus in suspened solid load from imp areas | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%tno3conc` | `real` | mg NO3-N/kg sed | conc of NO3-N in suspended solid load from imp areas | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |
| `urbdb%urbcn2` | `real` | none | moisture condition II curve number for imp areas | [[urban_data_module.f90#urbdb]] | [[urban_parm_read.f90]]:42 |

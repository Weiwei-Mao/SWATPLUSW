---
type: input
tags:
  - swat/input
file: septic.sep
ext: sep
cio_field: septic_sep
read_by:
  - septic_parm_read.f90
purpose: ""
---

# septic.sep

> [!info] Input File
> Declared in `file.cio` field `septic_sep`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `septic_sep`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[septic_parm_read.f90]]

## File Structure
- [[septic_parm_read.f90]] source line 25: reads `titldum`
- [[septic_parm_read.f90]] source line 27: reads `header`
- [[septic_parm_read.f90]] source line 30: reads `titldum`
- [[septic_parm_read.f90]] source line 39: reads `titldum`
- [[septic_parm_read.f90]] source line 41: reads `header`
- [[septic_parm_read.f90]] source line 45: reads `titldum`
- [[septic_parm_read.f90]] source line 48: reads `sepdb(is)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sepdb%sepnm` | `character(len=20)` |  |  | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%qs` | `real` | m3/d | flow rate of the septic tank effluent per capita (sptq) | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%bodconcs` | `real` | mg/l | biological oxygen demand of the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%tssconcs` | `real` | mg/l | concentration of total suspended solid in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%nh4concs` | `real` | mg/l | concentration of total phosphorus in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%no3concs` | `real` | mg/l | concentration of nitrate in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%no2concs` | `real` | mg/l | concentration of nitrite in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%orgnconcs` | `real` | mg/l | concentration of organic nitrogen in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%minps` | `real` | mg/l | concentration of mineral phosphorus in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%orgps` | `real` | mg/l | concentration of organic phosphorus in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |
| `sepdb%fcolis` | `real` | mg/l | concentration of fecal coliform in the septic tank effluent | [[septic_data_module.f90#sepdb]] | [[septic_parm_read.f90]]:48 |

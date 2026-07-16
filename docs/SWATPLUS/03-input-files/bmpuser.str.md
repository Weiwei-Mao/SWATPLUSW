---
type: input
tags:
  - swat/input
file: bmpuser.str
ext: str
cio_field: bmpuser_str
read_by:
  - scen_read_bmpuser.f90
purpose: ""
---

# bmpuser.str

> [!info] Input File
> Declared in `file.cio` field `bmpuser_str`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `bmpuser_str`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[scen_read_bmpuser.f90]]

## File Structure
- [[scen_read_bmpuser.f90]] source line 25: reads `titldum`
- [[scen_read_bmpuser.f90]] source line 27: reads `header`
- [[scen_read_bmpuser.f90]] source line 30: reads `titldum`
- [[scen_read_bmpuser.f90]] source line 37: reads `titldum`
- [[scen_read_bmpuser.f90]] source line 39: reads `header`
- [[scen_read_bmpuser.f90]] source line 43: reads `bmpuser_db(ibmpop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `bmpuser_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_flag` | `integer` |  |  | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_sed` | `real` | % | Sediment removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_pp` | `real` | % | Particulate P removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_sp` | `real` | % | Soluble P removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_pn` | `real` | % | Particulate N removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_sn` | `real` | % | Soluble N removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |
| `bmpuser_db%bmp_bac` | `real` | % | Bacteria removal by BMP | [[mgt_operations_module.f90#bmpuser_db]] | [[scen_read_bmpuser.f90]]:43 |

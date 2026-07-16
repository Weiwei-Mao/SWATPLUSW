---
type: input
tags:
  - swat/input
file: ls_reg.def
ext: def
cio_field: def_reg
read_by:
  - reg_read_elements.f90
purpose: ""
---

# ls_reg.def

> [!info] Input File
> Declared in `file.cio` field `def_reg`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_reg`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[reg_read_elements.f90]]

## File Structure
- [[reg_read_elements.f90]] source line 43: reads `titldum`
- [[reg_read_elements.f90]] source line 45: reads `mreg`, `mlug`
- [[reg_read_elements.f90]] source line 75: reads `i`, `lum_grp%num`, `(lum_grp%name(ilum), ilum = 1, mlug)`
- [[reg_read_elements.f90]] source line 78: reads `header`
- [[reg_read_elements.f90]] source line 101: reads `k`, `lsu_reg(i)%name`, `lsu_reg(i)%area_ha`, `nspu`
- [[reg_read_elements.f90]] source line 106: reads `k`, `lsu_reg(i)%name`, `lsu_reg(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` |  |  | `reg_read_elements.f90:21` | [[reg_read_elements.f90]]:45 |
| `mlug` | `integer` |  |  | `reg_read_elements.f90:22` | [[reg_read_elements.f90]]:45 |
| `i` | `integer` | none | counter | `reg_read_elements.f90:24` | [[reg_read_elements.f90]]:75 |
| `lum_grp%num` | `integer` |  |  | [[landuse_data_module.f90#lum_grp]] | [[reg_read_elements.f90]]:75 |
| `lum_grp%name` | `character(len=40), dimension(:), allocatable` |  | land use groups | [[landuse_data_module.f90#lum_grp]] | [[reg_read_elements.f90]]:75 |
| `k` | `integer` |  |  | `reg_read_elements.f90:25` | [[reg_read_elements.f90]]:101 |
| `lsu_reg%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#lsu_reg]] | [[reg_read_elements.f90]]:101 |
| `lsu_reg%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#lsu_reg]] | [[reg_read_elements.f90]]:101 |
| `nspu` | `integer` |  |  | `reg_read_elements.f90:27` | [[reg_read_elements.f90]]:101 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[reg_read_elements.f90]]:106 |

---
type: input
tags:
  - swat/input
file: res_reg.def
ext: def
cio_field: def_res_reg
read_by:
  - res_read_elements.f90
purpose: ""
---

# res_reg.def

> [!info] Input File
> Declared in `file.cio` field `def_res_reg`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_res_reg`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_elements.f90]]

## File Structure
- [[res_read_elements.f90]] source line 83: reads `titldum`
- [[res_read_elements.f90]] source line 85: reads `mreg`
- [[res_read_elements.f90]] source line 87: reads `header`
- [[res_read_elements.f90]] source line 92: reads `k`, `rcu_cal(i)%name`, `rcu_cal(i)%area_ha`, `nspu`
- [[res_read_elements.f90]] source line 97: reads `k`, `rcu_cal(i)%name`, `rcu_cal(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` |  |  | `res_read_elements.f90:19` | [[res_read_elements.f90]]:85 |
| `k` | `integer` |  |  | `res_read_elements.f90:21` | [[res_read_elements.f90]]:92 |
| `rcu_cal%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_reg) | [[calibration_data_module.f90#rcu_cal]] | [[res_read_elements.f90]]:92 |
| `rcu_cal%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#rcu_cal]] | [[res_read_elements.f90]]:92 |
| `nspu` | `integer` |  |  | `res_read_elements.f90:22` | [[res_read_elements.f90]]:92 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[res_read_elements.f90]]:97 |

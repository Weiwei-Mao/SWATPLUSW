---
type: input
tags:
  - swat/input
file: res_catunit.def
ext: def
cio_field: def_res
read_by:
  - res_read_elements.f90
purpose: ""
---

# res_catunit.def

> [!info] Input File
> Declared in `file.cio` field `def_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_elements.f90]]

## File Structure
- [[res_read_elements.f90]] source line 36: reads `titldum`
- [[res_read_elements.f90]] source line 38: reads `mreg`
- [[res_read_elements.f90]] source line 40: reads `header`
- [[res_read_elements.f90]] source line 48: reads `k`, `rcu_out(i)%name`, `rcu_out(i)%area_ha`, `nspu`
- [[res_read_elements.f90]] source line 53: reads `k`, `rcu_out(i)%name`, `rcu_out(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` |  |  | `res_read_elements.f90:19` | [[res_read_elements.f90]]:38 |
| `k` | `integer` |  |  | `res_read_elements.f90:21` | [[res_read_elements.f90]]:48 |
| `rcu_out%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#rcu_out]] | [[res_read_elements.f90]]:48 |
| `rcu_out%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#rcu_out]] | [[res_read_elements.f90]]:48 |
| `nspu` | `integer` |  |  | `res_read_elements.f90:22` | [[res_read_elements.f90]]:48 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[res_read_elements.f90]]:53 |

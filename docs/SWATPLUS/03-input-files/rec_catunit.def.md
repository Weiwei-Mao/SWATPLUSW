---
type: input
tags:
  - swat/input
file: rec_catunit.def
ext: def
cio_field: def_psc
read_by:
  - rec_read_elements.f90
purpose: ""
---

# rec_catunit.def

> [!info] Input File
> Declared in `file.cio` field `def_psc`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_psc`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[rec_read_elements.f90]]

## File Structure
- [[rec_read_elements.f90]] source line 34: reads `titldum`
- [[rec_read_elements.f90]] source line 36: reads `mreg`
- [[rec_read_elements.f90]] source line 38: reads `header`
- [[rec_read_elements.f90]] source line 49: reads `k`, `pcu_out(i)%name`, `pcu_out(i)%area_ha`, `nspu`
- [[rec_read_elements.f90]] source line 54: reads `k`, `pcu_out(i)%name`, `pcu_out(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` | none | end of loop | `rec_read_elements.f90:18` | [[rec_read_elements.f90]]:36 |
| `k` | `integer` |  |  | `rec_read_elements.f90:20` | [[rec_read_elements.f90]]:49 |
| `pcu_out%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#pcu_out]] | [[rec_read_elements.f90]]:49 |
| `pcu_out%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#pcu_out]] | [[rec_read_elements.f90]]:49 |
| `nspu` | `integer` | none | end of loop | `rec_read_elements.f90:21` | [[rec_read_elements.f90]]:49 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[rec_read_elements.f90]]:54 |

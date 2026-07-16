---
type: input
tags:
  - swat/input
file: ls_unit.def
ext: def
cio_field: def_lsu
read_by:
  - lsu_read_elements.f90
purpose: ""
---

# ls_unit.def

> [!info] Input File
> Declared in `file.cio` field `def_lsu`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_lsu`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[lsu_read_elements.f90]]

## File Structure
- [[lsu_read_elements.f90]] source line 35: reads `titldum`
- [[lsu_read_elements.f90]] source line 37: reads `mlsu`
- [[lsu_read_elements.f90]] source line 39: reads `header`
- [[lsu_read_elements.f90]] source line 66: reads `k`, `lsu_out(i)%name`, `lsu_out(i)%area_ha`, `nspu`
- [[lsu_read_elements.f90]] source line 71: reads `k`, `lsu_out(i)%name`, `lsu_out(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mlsu` | `integer` | none | counter | `lsu_read_elements.f90:20` | [[lsu_read_elements.f90]]:37 |
| `k` | `integer` |  |  | `lsu_read_elements.f90:22` | [[lsu_read_elements.f90]]:66 |
| `lsu_out%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#lsu_out]] | [[lsu_read_elements.f90]]:66 |
| `lsu_out%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#lsu_out]] | [[lsu_read_elements.f90]]:66 |
| `nspu` | `integer` |  |  | `lsu_read_elements.f90:17` | [[lsu_read_elements.f90]]:66 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[lsu_read_elements.f90]]:71 |

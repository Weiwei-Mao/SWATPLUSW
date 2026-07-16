---
type: input
tags:
  - swat/input
file: aqu_catunit.def
ext: def
cio_field: def_aqu
read_by:
  - aqu_read_elements.f90
purpose: ""
---

# aqu_catunit.def

> [!info] Input File
> Declared in `file.cio` field `def_aqu`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_aqu`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu_read_elements.f90]]

## File Structure
- [[aqu_read_elements.f90]] source line 37: reads `titldum`
- [[aqu_read_elements.f90]] source line 39: reads `mreg`
- [[aqu_read_elements.f90]] source line 41: reads `header`
- [[aqu_read_elements.f90]] source line 55: reads `k`, `acu_out(i)%name`, `acu_out(i)%area_ha`, `nspu`
- [[aqu_read_elements.f90]] source line 60: reads `k`, `acu_out(i)%name`, `acu_out(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`
- [[aqu_read_elements.f90]] source line 90: reads `titldum`
- [[aqu_read_elements.f90]] source line 92: reads `mreg`
- [[aqu_read_elements.f90]] source line 94: reads `header`
- [[aqu_read_elements.f90]] source line 98: reads `k`, `acu_reg(i)%name`, `acu_reg(i)%area_ha`, `nspu`
- [[aqu_read_elements.f90]] source line 103: reads `k`, `acu_reg(i)%name`, `acu_reg(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` |  |  | `aqu_read_elements.f90:19` | [[aqu_read_elements.f90]]:39 |
| `k` | `integer` |  |  | `aqu_read_elements.f90:21` | [[aqu_read_elements.f90]]:55 |
| `acu_out%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#acu_out]] | [[aqu_read_elements.f90]]:55 |
| `acu_out%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#acu_out]] | [[aqu_read_elements.f90]]:55 |
| `nspu` | `integer` |  |  | `aqu_read_elements.f90:22` | [[aqu_read_elements.f90]]:55 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[aqu_read_elements.f90]]:60 |
| `acu_reg%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#acu_reg]] | [[aqu_read_elements.f90]]:98 |
| `acu_reg%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#acu_reg]] | [[aqu_read_elements.f90]]:98 |

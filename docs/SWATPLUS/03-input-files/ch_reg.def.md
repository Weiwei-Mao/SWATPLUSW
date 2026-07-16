---
type: input
tags:
  - swat/input
file: ch_reg.def
ext: def
cio_field: def_cha_reg
read_by:
  - ch_read_elements.f90
purpose: ""
---

# ch_reg.def

> [!info] Input File
> Declared in `file.cio` field `def_cha_reg`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `def_cha_reg`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_elements.f90]]

## File Structure
- [[ch_read_elements.f90]] source line 86: reads `titldum`
- [[ch_read_elements.f90]] source line 88: reads `mreg`
- [[ch_read_elements.f90]] source line 90: reads `header`
- [[ch_read_elements.f90]] source line 95: reads `k`, `ccu_reg(i)%name`, `ccu_reg(i)%area_ha`, `nspu`
- [[ch_read_elements.f90]] source line 100: reads `k`, `ccu_reg(i)%name`, `ccu_reg(i)%area_ha`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` | units | description | `ch_read_elements.f90:19` | [[ch_read_elements.f90]]:88 |
| `k` | `integer` | units | description | `ch_read_elements.f90:21` | [[ch_read_elements.f90]]:95 |
| `ccu_reg%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_out) | [[calibration_data_module.f90#ccu_reg]] | [[ch_read_elements.f90]]:95 |
| `ccu_reg%area_ha` | `real` |  | area of landscape cataloging unit -hectares | [[calibration_data_module.f90#ccu_reg]] | [[ch_read_elements.f90]]:95 |
| `nspu` | `integer` | units | description | `ch_read_elements.f90:22` | [[ch_read_elements.f90]]:95 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[ch_read_elements.f90]]:100 |

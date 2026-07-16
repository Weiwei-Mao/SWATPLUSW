---
type: input
tags:
  - swat/input
file: graze.ops
ext: ops
cio_field: graze_ops
read_by:
  - mgt_read_grazeops.f90
purpose: ""
---

# graze.ops

> [!info] Input File
> Declared in `file.cio` field `graze_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `graze_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_grazeops.f90]]

## File Structure
- [[mgt_read_grazeops.f90]] source line 30: reads `titldum`
- [[mgt_read_grazeops.f90]] source line 32: reads `header`
- [[mgt_read_grazeops.f90]] source line 35: reads `titldum`
- [[mgt_read_grazeops.f90]] source line 43: reads `titldum`
- [[mgt_read_grazeops.f90]] source line 45: reads `header`
- [[mgt_read_grazeops.f90]] source line 49: reads `grazeop_db(igrazop)%name`, `grazeop_db(igrazop)%fertnm`, `grazeop_db(igrazop)%eat`, `grazeop_db(igrazop)%tramp`, `grazeop_db(igrazop)%manure`, `grazeop_db(igrazop)%biomin`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `grazeop_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |
| `grazeop_db%fertnm` | `character (len=40)` |  |  | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |
| `grazeop_db%eat` | `real` | (kg/ha)/day | dry weight of biomass removed by grazing daily | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |
| `grazeop_db%tramp` | `real` | (kg/ha)/day | dry weight of biomass removed by trampling daily | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |
| `grazeop_db%manure` | `real` | (kg/ha)/day | dry weight of manure deposited | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |
| `grazeop_db%biomin` | `real` | kg/ha | minimum plant biomass for grazing | [[mgt_operations_module.f90#grazeop_db]] | [[mgt_read_grazeops.f90]]:49 |

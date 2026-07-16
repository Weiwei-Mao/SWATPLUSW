---
type: input
tags:
  - swat/input
file: harv.ops
ext: ops
cio_field: harv_ops
read_by:
  - mgt_read_harvops.f90
purpose: ""
---

# harv.ops

> [!info] Input File
> Declared in `file.cio` field `harv_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `harv_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_harvops.f90]]

## File Structure
- [[mgt_read_harvops.f90]] source line 26: reads `titldum`
- [[mgt_read_harvops.f90]] source line 28: reads `header`
- [[mgt_read_harvops.f90]] source line 31: reads `titldum`
- [[mgt_read_harvops.f90]] source line 38: reads `titldum`
- [[mgt_read_harvops.f90]] source line 40: reads `header`
- [[mgt_read_harvops.f90]] source line 44: reads `harvop_db(iharvop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `harvop_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#harvop_db]] | [[mgt_read_harvops.f90]]:44 |
| `harvop_db%typ` | `character (len=40)` | none | grain;biomass;residue;tree;tuber | [[mgt_operations_module.f90#harvop_db]] | [[mgt_read_harvops.f90]]:44 |
| `harvop_db%hi_ovr` | `real` | (kg/ha)/(kg/ha) | harvest index target specified at harvest | [[mgt_operations_module.f90#harvop_db]] | [[mgt_read_harvops.f90]]:44 |
| `harvop_db%eff` | `real` | none | harvest efficiency: fraction of harvested yield that is removed the remainder becomes residue on the soil surface | [[mgt_operations_module.f90#harvop_db]] | [[mgt_read_harvops.f90]]:44 |
| `harvop_db%bm_min` | `real` | kg/ha | minimum biomass to allow harvest | [[mgt_operations_module.f90#harvop_db]] | [[mgt_read_harvops.f90]]:44 |

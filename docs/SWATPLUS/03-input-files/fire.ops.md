---
type: input
tags:
  - swat/input
file: fire.ops
ext: ops
cio_field: fire_ops
read_by:
  - mgt_read_fireops.f90
purpose: ""
---

# fire.ops

> [!info] Input File
> Declared in `file.cio` field `fire_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `fire_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_fireops.f90]]

## File Structure
- [[mgt_read_fireops.f90]] source line 26: reads `titldum`
- [[mgt_read_fireops.f90]] source line 28: reads `header`
- [[mgt_read_fireops.f90]] source line 31: reads `titldum`
- [[mgt_read_fireops.f90]] source line 39: reads `titldum`
- [[mgt_read_fireops.f90]] source line 41: reads `header`
- [[mgt_read_fireops.f90]] source line 45: reads `fire_db(ifireop)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `fire_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#fire_db]] | [[mgt_read_fireops.f90]]:45 |
| `fire_db%cn2_upd` | `real` |  | change in SCS curve number II value | [[mgt_operations_module.f90#fire_db]] | [[mgt_read_fireops.f90]]:45 |
| `fire_db%fr_burn` | `real` |  | fraction burned | [[mgt_operations_module.f90#fire_db]] | [[mgt_read_fireops.f90]]:45 |

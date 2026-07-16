---
type: input
tags:
  - swat/input
file: irr.ops
ext: ops
cio_field: irr_ops
read_by:
  - mgt_read_irrops.f90
purpose: ""
---

# irr.ops

> [!info] Input File
> Declared in `file.cio` field `irr_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `irr_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_irrops.f90]]

## File Structure
- [[mgt_read_irrops.f90]] source line 29: reads `titldum`
- [[mgt_read_irrops.f90]] source line 31: reads `header`
- [[mgt_read_irrops.f90]] source line 34: reads `titldum`
- [[mgt_read_irrops.f90]] source line 42: reads `titldum`
- [[mgt_read_irrops.f90]] source line 44: reads `header`
- [[mgt_read_irrops.f90]] source line 48: reads `irrop_db(irr_op)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `irrop_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%amt_mm` | `real` | mm | irrigation application amount | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%eff` | `real` |  | irrigation in-field efficiency | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%surq` | `real` | frac | surface runoff ratio | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%dep_mm` | `real` | mm | depth of application for subsurface irrigation | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%salt` | `real` | mg/kg | concentration of total salt in irrigation | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%no3` | `real` | mg/kg | concentration of nitrate in irrigation | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |
| `irrop_db%po4` | `real` | mg/kg | concentration of phosphate in irrigation | [[mgt_operations_module.f90#irrop_db]] | [[mgt_read_irrops.f90]]:48 |

---
type: input
tags:
  - swat/input
file: chem_app.ops
ext: ops
cio_field: chem_ops
read_by:
  - mgt_read_chemapp.f90
purpose: ""
---

# chem_app.ops

> [!info] Input File
> Declared in `file.cio` field `chem_ops`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `chem_ops`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[mgt_read_chemapp.f90]]

## File Structure
- [[mgt_read_chemapp.f90]] source line 26: reads `titldum`
- [[mgt_read_chemapp.f90]] source line 28: reads `header`
- [[mgt_read_chemapp.f90]] source line 31: reads `titldum`
- [[mgt_read_chemapp.f90]] source line 39: reads `titldum`
- [[mgt_read_chemapp.f90]] source line 41: reads `header`
- [[mgt_read_chemapp.f90]] source line 45: reads `chemapp_db(ichemapp)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `chemapp_db%name` | `character (len=40)` |  |  | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%form` | `character (len=40)` |  | solid; liquid | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%op_typ` | `character (len=40)` |  | operation type-spread; spray; inject; direct | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%app_eff` | `real` |  | application efficiency | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%foliar_eff` | `real` |  | foliar efficiency | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%inject_dep` | `real` | mm | injection depth | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%surf_frac` | `real` |  | surface fraction-amount in upper 10 mm | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%drift_pot` | `real` |  | drift potential | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |
| `chemapp_db%aerial_unif` | `real` |  | aerial uniformity | [[mgt_operations_module.f90#chemapp_db]] | [[mgt_read_chemapp.f90]]:45 |

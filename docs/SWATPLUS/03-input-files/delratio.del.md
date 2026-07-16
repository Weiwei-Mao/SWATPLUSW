---
type: input
tags:
  - swat/input
file: delratio.del
ext: del
cio_field: del_ratio
read_by:
  - dr_db_read.f90
purpose: ""
---

# delratio.del

> [!info] Input File
> Declared in `file.cio` field `del_ratio`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `del_ratio`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_db_read.f90]]

## File Structure
- [[dr_db_read.f90]] source line 26: reads `titldum`
- [[dr_db_read.f90]] source line 28: reads `header`
- [[dr_db_read.f90]] source line 32: reads `titldum`
- [[dr_db_read.f90]] source line 41: reads `titldum`
- [[dr_db_read.f90]] source line 43: reads `header`
- [[dr_db_read.f90]] source line 47: reads `dr_db(ii)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_db%name` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |
| `dr_db%om_file` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |
| `dr_db%pest_file` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |
| `dr_db%path_file` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |
| `dr_db%hmet_file` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |
| `dr_db%salts_file` | `character(len=16)` |  |  | [[dr_module.f90#dr_db]] | [[dr_db_read.f90]]:47 |

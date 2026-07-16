---
type: input
tags:
  - swat/input
file: exco.exc
ext: exc
cio_field: exco
read_by:
  - exco_db_read.f90
purpose: ""
---

# exco.exc

> [!info] Input File
> Declared in `file.cio` field `exco`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `exco`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_db_read.f90]]

## File Structure
- [[exco_db_read.f90]] source line 28: reads `titldum`
- [[exco_db_read.f90]] source line 30: reads `header`
- [[exco_db_read.f90]] source line 32: reads `header`
- [[exco_db_read.f90]] source line 36: reads `titldum`
- [[exco_db_read.f90]] source line 45: reads `titldum`
- [[exco_db_read.f90]] source line 47: reads `header`
- [[exco_db_read.f90]] source line 49: reads `header`
- [[exco_db_read.f90]] source line 53: reads `i`
- [[exco_db_read.f90]] source line 56: reads `k`, `exco_db(i)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `exco_db_read.f90:17` | [[exco_db_read.f90]]:53 |
| `k` | `integer` |  |  | `exco_db_read.f90:19` | [[exco_db_read.f90]]:56 |
| `exco_db%name` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%om_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%pest_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%path_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%hmet_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%salts_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%constit_file` | `character(len=16)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |
| `exco_db%descrip` | `character(len=40)` |  |  | [[exco_module.f90#exco_db]] | [[exco_db_read.f90]]:56 |

---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: recall_db.rec
ext: rec
cio_field: []
read_by:
  - recall_read.f90
purpose: ""
---

# recall_db.rec

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[recall_read.f90]]

## File Structure
- [[recall_read.f90]] source line 25: reads `titldum`
- [[recall_read.f90]] source line 27: reads `header`
- [[recall_read.f90]] source line 31: reads `i`
- [[recall_read.f90]] source line 45: reads `titldum`
- [[recall_read.f90]] source line 47: reads `header`
- [[recall_read.f90]] source line 51: reads `i`
- [[recall_read.f90]] source line 54: reads `k`, `recall_db(i)%name`, `recall_db(i)%org_min`, `recall_db(i)%pest`, `recall_db(i)%path`, `recall_db(i)%hmet`, `recall_db(i)%salt`, `recall_db(i)%constit`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `recall_read.f90:14` | [[recall_read.f90]]:31 |
| `k` | `integer` |  |  | `recall_read.f90:16` | [[recall_read.f90]]:54 |
| `recall_db%name` | `character(len=13)` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%org_min` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%pest` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%path` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%hmet` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%salt` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |
| `recall_db%constit` | `constituent_file_data` |  |  | [[recall_module.f90#recall_db]] | [[recall_read.f90]]:54 |

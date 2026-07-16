---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: manure_db.frt
ext: frt
cio_field: []
read_by:
  - manure_db_read.f90
purpose: ""
---

# manure_db.frt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[manure_db_read.f90]]

## File Structure
- [[manure_db_read.f90]] source line 28: reads `titldum`
- [[manure_db_read.f90]] source line 30: reads `header`
- [[manure_db_read.f90]] source line 33: reads `titldum`
- [[manure_db_read.f90]] source line 41: reads `titldum`
- [[manure_db_read.f90]] source line 43: reads `header`
- [[manure_db_read.f90]] source line 47: reads `manure_db(it)%name`, `manure_db(it)%org_min`, `manure_db(it)%pests`, `manure_db(it)%paths`, `manure_db(it)%hmets`, `manure_db(it)%salts`, `manure_db(it)%constit`, `manure_db(it)%descrip`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `manure_db%name` | `character (len=25)` |  | name of manure type | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%org_min` | `character (len=25)` |  | sediment, carbon, and nutrients | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%pests` | `character (len=25)` |  | pesticides - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%paths` | `character (len=25)` |  | pathogens - cfu | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%hmets` | `character (len=25)` |  | heavy metals - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%salts` | `character (len=25)` |  | salt ions - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%constit` | `character (len=25)` |  | other constituents - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |
| `manure_db%descrip` | `character (len=80)` |  | description | [[fertilizer_data_module.f90#manure_db]] | [[manure_db_read.f90]]:47 |

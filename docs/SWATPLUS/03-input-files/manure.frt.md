---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: manure.frt
ext: frt
cio_field: []
read_by:
  - manure_parm_read.f90
purpose: ""
---

# manure.frt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[manure_parm_read.f90]]

## File Structure
- [[manure_parm_read.f90]] source line 28: reads `titldum`
- [[manure_parm_read.f90]] source line 30: reads `header`
- [[manure_parm_read.f90]] source line 33: reads `titldum`
- [[manure_parm_read.f90]] source line 41: reads `titldum`
- [[manure_parm_read.f90]] source line 43: reads `header`
- [[manure_parm_read.f90]] source line 47: reads `manure_db(it)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `manure_db%name` | `character (len=25)` |  | name of manure type | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%org_min` | `character (len=25)` |  | sediment, carbon, and nutrients | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%pests` | `character (len=25)` |  | pesticides - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%paths` | `character (len=25)` |  | pathogens - cfu | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%hmets` | `character (len=25)` |  | heavy metals - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%salts` | `character (len=25)` |  | salt ions - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%constit` | `character (len=25)` |  | other constituents - ppm | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%descrip` | `character (len=80)` |  | description | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%iorg_min` | `integer` |  | sediment, carbon, and nutrients - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%ipests` | `integer` |  | pesticides - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%ipaths` | `integer` |  | pathogens - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%imets` | `integer` |  | heavy metals - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%isalts` | `integer` |  | salt ions - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |
| `manure_db%iconstit` | `integer` |  | other constituents - pointer to | [[fertilizer_data_module.f90#manure_db]] | [[manure_parm_read.f90]]:47 |

---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: shade_factor.shf
ext: shf
cio_field: []
read_by:
  - shade_factor_read.f90
purpose: ""
---

# shade_factor.shf

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[shade_factor_read.f90]]

## File Structure
- [[shade_factor_read.f90]] source line 31: reads `titldum`
- [[shade_factor_read.f90]] source line 33: reads `header`
- [[shade_factor_read.f90]] source line 36: reads `titldum`
- [[shade_factor_read.f90]] source line 44: reads `titldum`
- [[shade_factor_read.f90]] source line 46: reads `header`
- [[shade_factor_read.f90]] source line 50: reads `shf_db(idlsu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `shf_db%jday` | `integer` | none | day of the year | [[hydrograph_module.f90#shf_db]] | [[shade_factor_read.f90]]:50 |
| `shf_db%lsu` | `integer` | none | landscape unit | [[hydrograph_module.f90#shf_db]] | [[shade_factor_read.f90]]:50 |
| `shf_db%value` | `real` | none | shade factor value | [[hydrograph_module.f90#shf_db]] | [[shade_factor_read.f90]]:50 |

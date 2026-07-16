---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: dr_pest.del
ext: del
cio_field: []
read_by:
  - dr_read_pest.f90
purpose: ""
---

# dr_pest.del

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_read_pest.f90]]

## File Structure
- [[dr_read_pest.f90]] source line 33: reads `titldum`
- [[dr_read_pest.f90]] source line 35: reads `header`
- [[dr_read_pest.f90]] source line 39: reads `titldum`
- [[dr_read_pest.f90]] source line 53: reads `titldum`
- [[dr_read_pest.f90]] source line 55: reads `header`
- [[dr_read_pest.f90]] source line 60: reads `titldum`
- [[dr_read_pest.f90]] source line 63: reads `dr_pest_name(ii)`, `(dr_pest(ii)%pest(ipest), ipest = 1, cs_db%num_pests)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_pest_name` | `character(len=16), dimension(:), allocatable` |  |  | [[dr_module.f90#dr_pest_name]] | [[dr_read_pest.f90]]:63 |
| `dr_pest%pest%num_pests` | `real, dimension (:), allocatable` |  | pesticide delivery | [[constituent_mass_module.f90#dr_pest]] | [[dr_read_pest.f90]]:63 |

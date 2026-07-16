---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: field.fld
ext: fld
cio_field: []
read_by:
  - field_read.f90
purpose: ""
---

# field.fld

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[field_read.f90]]

## File Structure
- [[field_read.f90]] source line 26: reads `titldum`
- [[field_read.f90]] source line 28: reads `header`
- [[field_read.f90]] source line 31: reads `titldum`
- [[field_read.f90]] source line 40: reads `titldum`
- [[field_read.f90]] source line 42: reads `header`
- [[field_read.f90]] source line 46: reads `titldum`
- [[field_read.f90]] source line 49: reads `field_db(ith)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `field_db%name` | `character(len=16)` |  |  | [[topography_data_module.f90#field_db]] | [[field_read.f90]]:49 |
| `field_db%length` | `real` |  | m \|field length for wind erosion | [[topography_data_module.f90#field_db]] | [[field_read.f90]]:49 |
| `field_db%wid` | `real` |  | m \|field width for wind erosion | [[topography_data_module.f90#field_db]] | [[field_read.f90]]:49 |
| `field_db%ang` | `real` |  | deg \|field angle for wind erosion | [[topography_data_module.f90#field_db]] | [[field_read.f90]]:49 |

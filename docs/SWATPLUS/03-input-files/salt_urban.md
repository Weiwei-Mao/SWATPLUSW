---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_urban
ext: 
cio_field: []
read_by:
  - salt_urban_read.f90
purpose: ""
---

# salt_urban

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_urban_read.f90]]

## File Structure
- [[salt_urban_read.f90]] source line 29: reads `header`
- [[salt_urban_read.f90]] source line 30: reads `header`
- [[salt_urban_read.f90]] source line 37: reads `titldum`
- [[salt_urban_read.f90]] source line 48: reads `header`
- [[salt_urban_read.f90]] source line 49: reads `header`
- [[salt_urban_read.f90]] source line 51: reads `urb_type`
- [[salt_urban_read.f90]] source line 56: reads `urb_type`, `(salt_urban_conc(iu,isalt),isalt=1,cs_db%num_salts)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `urb_type` | `character (len=16)` |  | urban land use type | `salt_urban_read.f90:12` | [[salt_urban_read.f90]]:51 |
| `salt_urban_conc%num_salts` | `` |  |  | [[salt_module.f90#salt_urban_conc]] | [[salt_urban_read.f90]]:56 |

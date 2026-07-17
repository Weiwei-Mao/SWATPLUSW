---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_urban
ext: 
cio_field: []
read_by:
  - cs_urban_read.f90
purpose: ""
---

# cs_urban

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_urban_read.f90]]

## File Structure
- [[cs_urban_read.f90]] source line 29: reads `header`
- [[cs_urban_read.f90]] source line 30: reads `header`
- [[cs_urban_read.f90]] source line 37: reads `titldum`
- [[cs_urban_read.f90]] source line 48: reads `header`
- [[cs_urban_read.f90]] source line 49: reads `header`
- [[cs_urban_read.f90]] source line 51: reads `urb_type`
- [[cs_urban_read.f90]] source line 56: reads `urb_type`, `(cs_urban_conc(iu,ics),ics=1,cs_db%num_cs)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `urb_type` | `character (len=16)` |  | urban land use type | `cs_urban_read.f90:12` | [[cs_urban_read.f90]]:51 |
| `cs_urban_conc%num_cs` | `` |  |  | [[cs_module.f90#cs_urban_conc]] | [[cs_urban_read.f90]]:56 |

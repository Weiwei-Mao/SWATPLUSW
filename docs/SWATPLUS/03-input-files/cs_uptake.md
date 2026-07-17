---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_uptake
ext: 
cio_field: []
read_by:
  - cs_uptake_read.f90
purpose: ""
---

# cs_uptake

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_uptake_read.f90]]

## File Structure
- [[cs_uptake_read.f90]] source line 37: reads `header`
- [[cs_uptake_read.f90]] source line 38: reads `header`
- [[cs_uptake_read.f90]] source line 39: reads `header`
- [[cs_uptake_read.f90]] source line 47: reads `name`, `(cs_uptake_kg(i,j),j=1,cs_db%num_cs)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `name` | `character (len=30)` |  | header of file | `cs_uptake_read.f90:17` | [[cs_uptake_read.f90]]:47 |
| `cs_uptake_kg%num_cs` | `` |  |  | [[cs_module.f90#cs_uptake_kg]] | [[cs_uptake_read.f90]]:47 |

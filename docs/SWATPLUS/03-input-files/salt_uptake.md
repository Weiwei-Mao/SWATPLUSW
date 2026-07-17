---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_uptake
ext: 
cio_field: []
read_by:
  - salt_uptake_read.f90
purpose: ""
---

# salt_uptake

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_uptake_read.f90]]

## File Structure
- [[salt_uptake_read.f90]] source line 38: reads `header`
- [[salt_uptake_read.f90]] source line 39: reads `header`
- [[salt_uptake_read.f90]] source line 40: reads `header`
- [[salt_uptake_read.f90]] source line 48: reads `name`, `(salt_uptake_kg(i,j),j=1,cs_db%num_salts)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `name` | `character (len=30)` |  | header of file | `salt_uptake_read.f90:17` | [[salt_uptake_read.f90]]:48 |
| `salt_uptake_kg%num_salts` | `` |  |  | [[salt_module.f90#salt_uptake_kg]] | [[salt_uptake_read.f90]]:48 |

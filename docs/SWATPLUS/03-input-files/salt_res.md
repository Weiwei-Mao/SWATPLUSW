---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_res
ext: 
cio_field: []
read_by:
  - res_read_saltdb.f90
purpose: ""
---

# salt_res

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_saltdb.f90]]

## File Structure
- [[res_read_saltdb.f90]] source line 32: reads `titldum`
- [[res_read_saltdb.f90]] source line 33: reads `titldum`
- [[res_read_saltdb.f90]] source line 35: reads (no targets parsed)
- [[res_read_saltdb.f90]] source line 39: reads `header`
- [[res_read_saltdb.f90]] source line 42: reads `titldum`
- [[res_read_saltdb.f90]] source line 54: reads `titldum`
- [[res_read_saltdb.f90]] source line 56: reads `titldum`
- [[res_read_saltdb.f90]] source line 58: reads (no targets parsed)
- [[res_read_saltdb.f90]] source line 60: reads `header`
- [[res_read_saltdb.f90]] source line 64: reads `titldum`
- [[res_read_saltdb.f90]] source line 67: reads `res_salt_data(ires)%name`, `res_salt_data(ires)%c_init`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_salt_data%name` | `character(len=25)` |  |  | [[res_salt_module.f90#res_salt_data]] | [[res_read_saltdb.f90]]:67 |
| `res_salt_data%c_init` | `real, dimension (:), allocatable` | g/m3 | initial concentration of each salt ion | [[res_salt_module.f90#res_salt_data]] | [[res_read_saltdb.f90]]:67 |

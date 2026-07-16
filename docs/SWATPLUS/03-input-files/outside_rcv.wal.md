---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: outside_rcv.wal
ext: wal
cio_field: []
read_by:
  - water_orcv_read.f90
purpose: ""
---

# outside_rcv.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_orcv_read.f90]]

## File Structure
- [[water_orcv_read.f90]] source line 35: reads `titldum`
- [[water_orcv_read.f90]] source line 37: reads `imax`
- [[water_orcv_read.f90]] source line 38: reads `header`
- [[water_orcv_read.f90]] source line 45: reads `i`, `orcv(ircv)%name`, `orcv(ircv)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_orcv_read.f90:17` | [[water_orcv_read.f90]]:37 |
| `i` | `integer` | none | counter | `water_orcv_read.f90:19` | [[water_orcv_read.f90]]:45 |
| `orcv%name` | `character (len=25)` |  | name of outside basin receiving object | [[water_allocation_module.f90#orcv]] | [[water_orcv_read.f90]]:45 |
| `orcv%filename` | `character (len=25)` |  | name of outside basin receiving object | [[water_allocation_module.f90#orcv]] | [[water_orcv_read.f90]]:45 |

---
type: input
tags:
  - swat/input
file: cntable.lum
ext: lum
cio_field: cntable_lum
read_by:
  - cntbl_read.f90
purpose: ""
---

# cntable.lum

> [!info] Input File
> Declared in `file.cio` field `cntable_lum`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `cntable_lum`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cntbl_read.f90]]

## File Structure
- [[cntbl_read.f90]] source line 26: reads `titldum`
- [[cntbl_read.f90]] source line 28: reads `header`
- [[cntbl_read.f90]] source line 31: reads `titldum`
- [[cntbl_read.f90]] source line 39: reads `titldum`
- [[cntbl_read.f90]] source line 41: reads `header`
- [[cntbl_read.f90]] source line 45: reads `cn(icno)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cn%name` | `character(len=40)` |  | name includes abbrev for lu/treatment/condition | [[landuse_data_module.f90#cn]] | [[cntbl_read.f90]]:45 |
| `cn%cn` | `real, dimension(4)` |  | curve number | [[landuse_data_module.f90#cn]] | [[cntbl_read.f90]]:45 |

---
type: input
tags:
  - swat/input
file: cons_practice.lum
ext: lum
cio_field: cons_prac_lum
read_by:
  - cons_prac_read.f90
purpose: ""
---

# cons_practice.lum

> [!info] Input File
> Declared in `file.cio` field `cons_prac_lum`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `cons_prac_lum`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cons_prac_read.f90]]

## File Structure
- [[cons_prac_read.f90]] source line 26: reads `titldum`
- [[cons_prac_read.f90]] source line 28: reads `header`
- [[cons_prac_read.f90]] source line 31: reads `titldum`
- [[cons_prac_read.f90]] source line 39: reads `titldum`
- [[cons_prac_read.f90]] source line 41: reads `header`
- [[cons_prac_read.f90]] source line 45: reads `cons_prac(icp)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cons_prac%name` | `character(len=40)` |  | name of conservation practice | [[landuse_data_module.f90#cons_prac]] | [[cons_prac_read.f90]]:45 |
| `cons_prac%pfac` | `real` |  | usle p factor | [[landuse_data_module.f90#cons_prac]] | [[cons_prac_read.f90]]:45 |
| `cons_prac%sl_len_mx` | `real` |  | m !maximum slope length | [[landuse_data_module.f90#cons_prac]] | [[cons_prac_read.f90]]:45 |

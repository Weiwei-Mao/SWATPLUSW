---
type: input
tags:
  - swat/input
file: rout_unit.def
ext: def
cio_field: ru_def
read_by:
  - ru_read_elements.f90
purpose: ""
---

# rout_unit.def

> [!info] Input File
> Declared in `file.cio` field `ru_def`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ru_def`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ru_read_elements.f90]]

## File Structure
- [[ru_read_elements.f90]] source line 96: reads `titldum`
- [[ru_read_elements.f90]] source line 98: reads `header`
- [[ru_read_elements.f90]] source line 102: reads `titldum`
- [[ru_read_elements.f90]] source line 108: reads `titldum`
- [[ru_read_elements.f90]] source line 110: reads `header`
- [[ru_read_elements.f90]] source line 118: reads `numb`, `namedum`, `nspu`
- [[ru_read_elements.f90]] source line 126: reads `numb`, `ru_def(iru)%name`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `numb` | `integer` |  |  | `ru_read_elements.f90:29` | [[ru_read_elements.f90]]:118 |
| `namedum` | `character (len=16)` |  |  | `ru_read_elements.f90:15` | [[ru_read_elements.f90]]:118 |
| `nspu` | `integer` |  |  | `ru_read_elements.f90:18` | [[ru_read_elements.f90]]:118 |
| `ru_def%name` | `character(len=16)` |  |  | [[hydrograph_module.f90#ru_def]] | [[ru_read_elements.f90]]:126 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[ru_read_elements.f90]]:126 |

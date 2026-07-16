---
type: input
tags:
  - swat/input
file: rout_unit.ele
ext: ele
cio_field: ru_ele
read_by:
  - ru_read_elements.f90
purpose: ""
---

# rout_unit.ele

> [!info] Input File
> Declared in `file.cio` field `ru_ele`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ru_ele`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ru_read_elements.f90]]

## File Structure
- [[ru_read_elements.f90]] source line 43: reads `titldum`
- [[ru_read_elements.f90]] source line 45: reads `header`
- [[ru_read_elements.f90]] source line 49: reads `i`
- [[ru_read_elements.f90]] source line 60: reads `titldum`
- [[ru_read_elements.f90]] source line 62: reads `header`
- [[ru_read_elements.f90]] source line 68: reads `i`
- [[ru_read_elements.f90]] source line 71: reads `k`, `ru_elem(i)%name`, `ru_elem(i)%obtyp`, `ru_elem(i)%obtypno`, `ru_elem(i)%frac`, `ru_elem(i)%dr_name`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `ru_read_elements.f90:20` | [[ru_read_elements.f90]]:49 |
| `k` | `integer` |  |  | `ru_read_elements.f90:23` | [[ru_read_elements.f90]]:71 |
| `ru_elem%name` | `character(len=16)` |  |  | [[hydrograph_module.f90#ru_elem]] | [[ru_read_elements.f90]]:71 |
| `ru_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[hydrograph_module.f90#ru_elem]] | [[ru_read_elements.f90]]:71 |
| `ru_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[hydrograph_module.f90#ru_elem]] | [[ru_read_elements.f90]]:71 |
| `ru_elem%frac` | `real` |  | fraction of element in ru (expansion factor) | [[hydrograph_module.f90#ru_elem]] | [[ru_read_elements.f90]]:71 |
| `ru_elem%dr_name` | `character(len=16)` |  | name of dr in delratio.del | [[hydrograph_module.f90#ru_elem]] | [[ru_read_elements.f90]]:71 |

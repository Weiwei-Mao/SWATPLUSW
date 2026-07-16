---
type: input
tags:
  - swat/input
file: ls_unit.ele
ext: ele
cio_field: ele_lsu
read_by:
  - lsu_read_elements.f90
purpose: ""
---

# ls_unit.ele

> [!info] Input File
> Declared in `file.cio` field `ele_lsu`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ele_lsu`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[lsu_read_elements.f90]]

## File Structure
- [[lsu_read_elements.f90]] source line 103: reads `titldum`
- [[lsu_read_elements.f90]] source line 105: reads `header`
- [[lsu_read_elements.f90]] source line 109: reads `i`
- [[lsu_read_elements.f90]] source line 117: reads `titldum`
- [[lsu_read_elements.f90]] source line 119: reads `header`
- [[lsu_read_elements.f90]] source line 125: reads `i`
- [[lsu_read_elements.f90]] source line 128: reads `k`, `lsu_elem(i)%name`, `lsu_elem(i)%obtyp`, `lsu_elem(i)%obtypno`, `lsu_elem(i)%bsn_frac`, `lsu_elem(i)%ru_frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `lsu_read_elements.f90:21` | [[lsu_read_elements.f90]]:109 |
| `k` | `integer` |  |  | `lsu_read_elements.f90:22` | [[lsu_read_elements.f90]]:128 |
| `lsu_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#lsu_elem]] | [[lsu_read_elements.f90]]:128 |
| `lsu_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[calibration_data_module.f90#lsu_elem]] | [[lsu_read_elements.f90]]:128 |
| `lsu_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#lsu_elem]] | [[lsu_read_elements.f90]]:128 |
| `lsu_elem%bsn_frac` | `real` |  | fraction of element in basin (expansion factor) | [[calibration_data_module.f90#lsu_elem]] | [[lsu_read_elements.f90]]:128 |
| `lsu_elem%ru_frac` | `real` |  | fraction of element in ru (expansion factor) | [[calibration_data_module.f90#lsu_elem]] | [[lsu_read_elements.f90]]:128 |

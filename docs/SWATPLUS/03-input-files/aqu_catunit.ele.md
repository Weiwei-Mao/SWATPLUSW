---
type: input
tags:
  - swat/input
file: aqu_catunit.ele
ext: ele
cio_field: ele_aqu
read_by:
  - aqu_read_elements.f90
purpose: ""
---

# aqu_catunit.ele

> [!info] Input File
> Declared in `file.cio` field `ele_aqu`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ele_aqu`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu_read_elements.f90]]

## File Structure
- [[aqu_read_elements.f90]] source line 150: reads `titldum`
- [[aqu_read_elements.f90]] source line 152: reads `header`
- [[aqu_read_elements.f90]] source line 156: reads `i`
- [[aqu_read_elements.f90]] source line 164: reads `titldum`
- [[aqu_read_elements.f90]] source line 166: reads `header`
- [[aqu_read_elements.f90]] source line 171: reads `i`
- [[aqu_read_elements.f90]] source line 174: reads `k`, `acu_elem(i)%name`, `acu_elem(i)%obtyp`, `acu_elem(i)%obtypno`, `acu_elem(i)%bsn_frac`, `acu_elem(i)%ru_frac`, `acu_elem(i)%reg_frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `aqu_read_elements.f90:20` | [[aqu_read_elements.f90]]:156 |
| `k` | `integer` |  |  | `aqu_read_elements.f90:21` | [[aqu_read_elements.f90]]:174 |
| `acu_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |
| `acu_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |
| `acu_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |
| `acu_elem%bsn_frac` | `real` |  | fraction of element in basin (expansion factor) | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |
| `acu_elem%ru_frac` | `real` |  | fraction of element in ru (expansion factor) | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |
| `acu_elem%reg_frac` | `real` |  | fraction of element in calibration region (expansion factor) | [[calibration_data_module.f90#acu_elem]] | [[aqu_read_elements.f90]]:174 |

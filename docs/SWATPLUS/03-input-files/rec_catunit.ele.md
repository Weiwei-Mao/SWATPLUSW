---
type: input
tags:
  - swat/input
file: rec_catunit.ele
ext: ele
cio_field: ele_psc
read_by:
  - rec_read_elements.f90
purpose: ""
---

# rec_catunit.ele

> [!info] Input File
> Declared in `file.cio` field `ele_psc`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ele_psc`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[rec_read_elements.f90]]

## File Structure
- [[rec_read_elements.f90]] source line 137: reads `titldum`
- [[rec_read_elements.f90]] source line 139: reads `header`
- [[rec_read_elements.f90]] source line 143: reads `i`
- [[rec_read_elements.f90]] source line 151: reads `titldum`
- [[rec_read_elements.f90]] source line 153: reads `header`
- [[rec_read_elements.f90]] source line 159: reads `i`
- [[rec_read_elements.f90]] source line 162: reads `k`, `pcu_elem(i)%name`, `pcu_elem(i)%obtyp`, `pcu_elem(i)%obtypno`, `pcu_elem(i)%bsn_frac`, `pcu_elem(i)%ru_frac`, `pcu_elem(i)%reg_frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `rec_read_elements.f90:19` | [[rec_read_elements.f90]]:143 |
| `k` | `integer` |  |  | `rec_read_elements.f90:20` | [[rec_read_elements.f90]]:162 |
| `pcu_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |
| `pcu_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |
| `pcu_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |
| `pcu_elem%bsn_frac` | `real` |  | fraction of element in basin (expansion factor) | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |
| `pcu_elem%ru_frac` | `real` |  | fraction of element in ru (expansion factor) | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |
| `pcu_elem%reg_frac` | `real` |  | fraction of element in calibration region (expansion factor) | [[calibration_data_module.f90#pcu_elem]] | [[rec_read_elements.f90]]:162 |

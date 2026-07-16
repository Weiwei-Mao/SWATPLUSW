---
type: input
tags:
  - swat/input
file: res_catunit.ele
ext: ele
cio_field: ele_res
read_by:
  - res_read_elements.f90
purpose: ""
---

# res_catunit.ele

> [!info] Input File
> Declared in `file.cio` field `ele_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ele_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_elements.f90]]

## File Structure
- [[res_read_elements.f90]] source line 142: reads `titldum`
- [[res_read_elements.f90]] source line 144: reads `header`
- [[res_read_elements.f90]] source line 148: reads `i`
- [[res_read_elements.f90]] source line 156: reads `titldum`
- [[res_read_elements.f90]] source line 158: reads `header`
- [[res_read_elements.f90]] source line 162: reads `i`
- [[res_read_elements.f90]] source line 165: reads `k`, `rcu_elem(i)%name`, `rcu_elem(i)%obtyp`, `rcu_elem(i)%obtypno`, `rcu_elem(i)%bsn_frac`, `rcu_elem(i)%ru_frac`, `rcu_elem(i)%reg_frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `res_read_elements.f90:20` | [[res_read_elements.f90]]:148 |
| `k` | `integer` |  |  | `res_read_elements.f90:21` | [[res_read_elements.f90]]:165 |
| `rcu_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |
| `rcu_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |
| `rcu_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |
| `rcu_elem%bsn_frac` | `real` |  | fraction of element in basin (expansion factor) | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |
| `rcu_elem%ru_frac` | `real` |  | fraction of element in ru (expansion factor) | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |
| `rcu_elem%reg_frac` | `real` |  | fraction of element in calibration region (expansion factor) | [[calibration_data_module.f90#rcu_elem]] | [[res_read_elements.f90]]:165 |

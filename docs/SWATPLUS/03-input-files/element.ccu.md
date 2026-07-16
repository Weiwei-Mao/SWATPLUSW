---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: element.ccu
ext: ccu
cio_field: []
read_by:
  - ch_read_elements.f90
purpose: ""
---

# element.ccu

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_elements.f90]]

## File Structure
- [[ch_read_elements.f90]] source line 146: reads `titldum`
- [[ch_read_elements.f90]] source line 148: reads `header`
- [[ch_read_elements.f90]] source line 152: reads `i`
- [[ch_read_elements.f90]] source line 160: reads `titldum`
- [[ch_read_elements.f90]] source line 162: reads `header`
- [[ch_read_elements.f90]] source line 166: reads `i`
- [[ch_read_elements.f90]] source line 169: reads `k`, `ccu_elem(i)%name`, `ccu_elem(i)%obtyp`, `ccu_elem(i)%obtypno`, `ccu_elem(i)%bsn_frac`, `ccu_elem(i)%ru_frac`, `ccu_elem(i)%reg_frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `ch_read_elements.f90:20` | [[ch_read_elements.f90]]:152 |
| `k` | `integer` | units | description | `ch_read_elements.f90:21` | [[ch_read_elements.f90]]:169 |
| `ccu_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |
| `ccu_elem%obtyp` | `character (len=3)` |  | object type- 1=hru, 2=hru_lte, 11=export coef, etc | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |
| `ccu_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |
| `ccu_elem%bsn_frac` | `real` |  | fraction of element in basin (expansion factor) | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |
| `ccu_elem%ru_frac` | `real` |  | fraction of element in ru (expansion factor) | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |
| `ccu_elem%reg_frac` | `real` |  | fraction of element in calibration region (expansion factor) | [[calibration_data_module.f90#ccu_elem]] | [[ch_read_elements.f90]]:169 |

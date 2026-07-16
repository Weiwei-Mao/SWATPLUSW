---
type: input
tags:
  - swat/input
file: ls_reg.ele
ext: ele
cio_field: ele_reg
read_by:
  - reg_read_elements.f90
purpose: ""
---

# ls_reg.ele

> [!info] Input File
> Declared in `file.cio` field `ele_reg`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ele_reg`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[reg_read_elements.f90]]

## File Structure
- [[reg_read_elements.f90]] source line 134: reads `titldum`
- [[reg_read_elements.f90]] source line 136: reads `header`
- [[reg_read_elements.f90]] source line 140: reads `i`
- [[reg_read_elements.f90]] source line 148: reads `titldum`
- [[reg_read_elements.f90]] source line 150: reads `header`
- [[reg_read_elements.f90]] source line 155: reads `i`
- [[reg_read_elements.f90]] source line 157: reads `k`, `reg_elem(i)%name`, `reg_elem(i)%ha`, `reg_elem(i)%obtyp`, `reg_elem(i)%obtypno`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `reg_read_elements.f90:24` | [[reg_read_elements.f90]]:140 |
| `k` | `integer` |  |  | `reg_read_elements.f90:25` | [[reg_read_elements.f90]]:157 |
| `reg_elem%name` | `character(len=16)` |  |  | [[calibration_data_module.f90#reg_elem]] | [[reg_read_elements.f90]]:157 |
| `reg_elem%ha` | `real` |  | area of region element -hectares | [[calibration_data_module.f90#reg_elem]] | [[reg_read_elements.f90]]:157 |
| `reg_elem%obtyp` | `character (len=3)` |  | object type- hru, hru_lte, lsu, etc | [[calibration_data_module.f90#reg_elem]] | [[reg_read_elements.f90]]:157 |
| `reg_elem%obtypno` | `integer` |  | 2-number of hru_lte"s or 1st hru_lte command | [[calibration_data_module.f90#reg_elem]] | [[reg_read_elements.f90]]:157 |

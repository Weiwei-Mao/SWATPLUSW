---
type: input
tags:
  - swat/input
file: calibration.cal
ext: cal
cio_field: cal_upd
read_by:
  - cal_parmchg_read.f90
purpose: ""
---

# calibration.cal

> [!info] Input File
> Declared in `file.cio` field `cal_upd`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `cal_upd`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cal_parmchg_read.f90]]

## File Structure
- [[cal_parmchg_read.f90]] source line 58: reads `titldum`
- [[cal_parmchg_read.f90]] source line 60: reads `mcal`
- [[cal_parmchg_read.f90]] source line 63: reads `header`
- [[cal_parmchg_read.f90]] source line 68: reads `cal_upd(i)%name`, `cal_upd(i)%chg_typ`, `cal_upd(i)%val`, `cal_upd(i)%conds`, `cal_upd(i)%lyr1`, `cal_upd(i)%lyr2`, `cal_upd(i)%year1`, `cal_upd(i)%year2`, `cal_upd(i)%day1`, `cal_upd(i)%day2`, `nspu`
- [[cal_parmchg_read.f90]] source line 75: reads `cal_upd(i)%name`, `cal_upd(i)%chg_typ`, `cal_upd(i)%val`, `cal_upd(i)%conds`, `cal_upd(i)%lyr1`, `cal_upd(i)%lyr2`, `cal_upd(i)%year1`, `cal_upd(i)%year2`, `cal_upd(i)%day1`, `cal_upd(i)%day2`, `cal_upd(i)%num_tot`, `(elem_cnt(isp), isp = 1, nspu)`
- [[cal_parmchg_read.f90]] source line 94: reads `range`
- [[cal_parmchg_read.f90]] source line 97: reads `range`, `cal_upd(i)%cond(icond)%var`, `cal_upd(i)%val1`, `cal_upd(i)%val2`
- [[cal_parmchg_read.f90]] source line 100: reads `cal_upd(i)%cond(icond)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mcal` | `integer` |  |  | `cal_parmchg_read.f90:40` | [[cal_parmchg_read.f90]]:60 |
| `cal_upd%name` | `character(len=25)` |  | cn2, terrace, land use, mgt, etc. | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%chg_typ` | `character(len=16)` |  | type of change (absval,abschg,pctchg) | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%val` | `real` |  | value of change | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%conds` | `integer` |  | number of conditions | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%lyr1` | `integer` |  | first layer in range for soil variables (0 assumes all layers are modified) | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%lyr2` | `integer` |  | last layer in range for soil variables (0 assumes through last layer) | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%year1` | `integer` |  | first year for precip and temp | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%year2` | `integer` |  | last year for precip and temp | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%day1` | `integer` |  | first day in range for precip and temp | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%day2` | `integer` |  | last day in range for precip and temp | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:68 |
| `nspu` | `integer` |  |  | `cal_parmchg_read.f90:36` | [[cal_parmchg_read.f90]]:68 |
| `cal_upd%num_tot` | `integer` |  | total number of integers read in | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:75 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[cal_parmchg_read.f90]]:75 |
| `range` | `character (len=10)` |  | real conditional variable range | `cal_parmchg_read.f90:33` | [[cal_parmchg_read.f90]]:94 |
| `cal_upd%cond%var` | `character(len=25)` |  |  | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:97 |
| `cal_upd%val1` | `real` |  | lower bound of numerical condition | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:97 |
| `cal_upd%val2` | `real` |  | upper bound of numerical condition | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:97 |
| `cal_upd%cond` | `calibration_conditions` |  |  | [[calibration_data_module.f90#cal_upd]] | [[cal_parmchg_read.f90]]:100 |

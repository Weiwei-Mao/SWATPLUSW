---
type: input
tags:
  - swat/input
file: cal_parms.cal
ext: cal
cio_field: cal_parms
read_by:
  - cal_parm_read.f90
purpose: ""
---

# cal_parms.cal

> [!info] Input File
> Declared in `file.cio` field `cal_parms`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `cal_parms`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cal_parm_read.f90]]

## File Structure
- [[cal_parm_read.f90]] source line 31: reads `titldum`
- [[cal_parm_read.f90]] source line 33: reads `mchg_par`
- [[cal_parm_read.f90]] source line 38: reads `header`
- [[cal_parm_read.f90]] source line 42: reads `cal_parms(i)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mchg_par` | `integer` |  |  | `cal_parm_read.f90:17` | [[cal_parm_read.f90]]:33 |
| `cal_parms%name` | `character(len=25)` |  | cn2, esco, awc, etc. | [[calibration_data_module.f90#cal_parms]] | [[cal_parm_read.f90]]:42 |
| `cal_parms%ob_typ` | `character(len=25)` |  | object type the parameter is associated with (hru, chan, res, basin, etc) | [[calibration_data_module.f90#cal_parms]] | [[cal_parm_read.f90]]:42 |
| `cal_parms%absmin` | `real` |  | minimum range for variable | [[calibration_data_module.f90#cal_parms]] | [[cal_parm_read.f90]]:42 |
| `cal_parms%absmax` | `real` |  | maximum change for variable | [[calibration_data_module.f90#cal_parms]] | [[cal_parm_read.f90]]:42 |
| `cal_parms%units` | `character(len=25)` |  | units used for each parameter | [[calibration_data_module.f90#cal_parms]] | [[cal_parm_read.f90]]:42 |

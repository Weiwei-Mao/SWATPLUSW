---
type: input
tags:
  - swat/input
file: wb_parms.sft
ext: sft
cio_field: wb_parms_sft
read_by:
  - ls_read_parms_cal.f90
purpose: ""
---

# wb_parms.sft

> [!info] Input File
> Declared in `file.cio` field `wb_parms_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `wb_parms_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ls_read_parms_cal.f90]]

## File Structure
- [[ls_read_parms_cal.f90]] source line 24: reads `titldum`
- [[ls_read_parms_cal.f90]] source line 26: reads `mlsp`
- [[ls_read_parms_cal.f90]] source line 28: reads `header`
- [[ls_read_parms_cal.f90]] source line 37: reads `ls_prms(i)%name`, `ls_prms(i)%chg_typ`, `ls_prms(i)%neg`, `ls_prms(i)%pos`, `ls_prms(i)%lo`, `ls_prms(i)%up`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mlsp` | `integer` | none | end of loop | `ls_read_parms_cal.f90:13` | [[ls_read_parms_cal.f90]]:26 |
| `ls_prms%name` | `character(len=16)` |  | cn2, terrace, land use, mgt, etc. | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |
| `ls_prms%chg_typ` | `character(len=16)` |  | type of change (absval,abschg,pctchg) | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |
| `ls_prms%neg` | `real` |  | negative limit of change | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |
| `ls_prms%pos` | `real` |  | positive limit of change | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |
| `ls_prms%lo` | `real` |  | lower limit of parameter | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |
| `ls_prms%up` | `real` |  | upper limit of parameter | [[calibration_data_module.f90#ls_prms]] | [[ls_read_parms_cal.f90]]:37 |

---
type: input
tags:
  - swat/input
file: water_balance.sft
ext: sft
cio_field: water_balance_sft
read_by:
  - lcu_read_softcal.f90
purpose: ""
---

# water_balance.sft

> [!info] Input File
> Declared in `file.cio` field `water_balance_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `water_balance_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[lcu_read_softcal.f90]]

## File Structure
- [[lcu_read_softcal.f90]] source line 36: reads `titldum`
- [[lcu_read_softcal.f90]] source line 38: reads `mreg`
- [[lcu_read_softcal.f90]] source line 40: reads `header`
- [[lcu_read_softcal.f90]] source line 67: reads `region(ireg)%name`, `region(ireg)%nlum`
- [[lcu_read_softcal.f90]] source line 85: reads `header`
- [[lcu_read_softcal.f90]] source line 89: reads `lscal(ireg)%lum(ilum)%meas`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` | none | end of loop | `lcu_read_softcal.f90:20` | [[lcu_read_softcal.f90]]:38 |
| `region%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_reg) | [[calibration_data_module.f90#region]] | [[lcu_read_softcal.f90]]:67 |
| `region%nlum` | `integer` |  | number of land use and mgt in the region | [[calibration_data_module.f90#region]] | [[lcu_read_softcal.f90]]:67 |
| `lscal%lum%meas` | `soft_calib_ls_processes` |  | dimension for land uses within a region / input soft calibration parms of each land use - ratio,t/ha,kg/ha | [[calibration_data_module.f90#lscal]] | [[lcu_read_softcal.f90]]:89 |

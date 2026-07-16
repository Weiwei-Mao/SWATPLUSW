---
type: input
tags:
  - swat/input
file: plant_gro.sft
ext: sft
cio_field: plant_gro_sft
read_by:
  - pl_read_regions_cal.f90
purpose: ""
---

# plant_gro.sft

> [!info] Input File
> Declared in `file.cio` field `plant_gro_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `plant_gro_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pl_read_regions_cal.f90]]

## File Structure
- [[pl_read_regions_cal.f90]] source line 39: reads `titldum`
- [[pl_read_regions_cal.f90]] source line 41: reads `mreg`
- [[pl_read_regions_cal.f90]] source line 43: reads `header`
- [[pl_read_regions_cal.f90]] source line 49: reads `plcal(i)%name`, `plcal(i)%lum_num`, `nspu`
- [[pl_read_regions_cal.f90]] source line 54: reads `plcal(i)%name`, `plcal(i)%lum_num`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`
- [[pl_read_regions_cal.f90]] source line 82: reads `header`
- [[pl_read_regions_cal.f90]] source line 86: reads `plcal(i)%lum(ilum)%meas`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` |  |  | `pl_read_regions_cal.f90:20` | [[pl_read_regions_cal.f90]]:41 |
| `plcal%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_reg) | [[calibration_data_module.f90#plcal]] | [[pl_read_regions_cal.f90]]:49 |
| `plcal%lum_num` | `integer` |  | number of land uses in each region | [[calibration_data_module.f90#plcal]] | [[pl_read_regions_cal.f90]]:49 |
| `nspu` | `integer` |  |  | `pl_read_regions_cal.f90:18` | [[pl_read_regions_cal.f90]]:49 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[pl_read_regions_cal.f90]]:54 |
| `plcal%lum%meas` | `soft_calib_pl_processes` |  | dimension for land uses within a region / input soft calibration parms of each land use - ratio,t/ha,kg/ha | [[calibration_data_module.f90#plcal]] | [[pl_read_regions_cal.f90]]:86 |

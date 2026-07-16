---
type: input
tags:
  - swat/input
file: plant_parms.sft
ext: sft
cio_field: plant_parms_sft
read_by:
  - pl_read_parms_cal.f90
purpose: ""
---

# plant_parms.sft

> [!info] Input File
> Declared in `file.cio` field `plant_parms_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `plant_parms_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pl_read_parms_cal.f90]]

## File Structure
- [[pl_read_parms_cal.f90]] source line 38: reads `titldum`
- [[pl_read_parms_cal.f90]] source line 40: reads `mreg`
- [[pl_read_parms_cal.f90]] source line 42: reads `header`
- [[pl_read_parms_cal.f90]] source line 48: reads `pl_prms(i)%name`, `pl_prms(i)%lum_num`, `pl_prms(i)%parms`, `nspu`
- [[pl_read_parms_cal.f90]] source line 53: reads `pl_prms(i)%name`, `pl_prms(i)%lum_num`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`
- [[pl_read_parms_cal.f90]] source line 79: reads `header`
- [[pl_read_parms_cal.f90]] source line 83: reads `pl_prms(i)%prm(ilum)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` | none | end of loop | `pl_read_parms_cal.f90:18` | [[pl_read_parms_cal.f90]]:40 |
| `pl_prms%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_reg) | [[calibration_data_module.f90#pl_prms]] | [[pl_read_parms_cal.f90]]:48 |
| `pl_prms%lum_num` | `integer` |  | number of land uses in each region | [[calibration_data_module.f90#pl_prms]] | [[pl_read_parms_cal.f90]]:48 |
| `pl_prms%parms` | `integer` |  | number of plant parameters used in calibration | [[calibration_data_module.f90#pl_prms]] | [[pl_read_parms_cal.f90]]:48 |
| `nspu` | `integer` |  |  | `pl_read_parms_cal.f90:26` | [[pl_read_parms_cal.f90]]:48 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[pl_read_parms_cal.f90]]:53 |
| `pl_prms%prm` | `pl_parms_cal` |  | dimension for land uses within a region | [[calibration_data_module.f90#pl_prms]] | [[pl_read_parms_cal.f90]]:83 |

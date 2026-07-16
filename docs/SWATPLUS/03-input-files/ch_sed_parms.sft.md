---
type: input
tags:
  - swat/input
file: ch_sed_parms.sft
ext: sft
cio_field: ch_sed_parms_sft
read_by:
  - ch_read_parms_cal.f90
purpose: ""
---

# ch_sed_parms.sft

> [!info] Input File
> Declared in `file.cio` field `ch_sed_parms_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ch_sed_parms_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_parms_cal.f90]]

## File Structure
- [[ch_read_parms_cal.f90]] source line 23: reads `titldum`
- [[ch_read_parms_cal.f90]] source line 25: reads `mchp`
- [[ch_read_parms_cal.f90]] source line 27: reads `header`
- [[ch_read_parms_cal.f90]] source line 34: reads `ch_prms(i)%name`, `ch_prms(i)%chg_typ`, `ch_prms(i)%neg`, `ch_prms(i)%pos`, `ch_prms(i)%lo`, `ch_prms(i)%up`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mchp` | `integer` |  | ending of loop | `ch_read_parms_cal.f90:12` | [[ch_read_parms_cal.f90]]:25 |
| `ch_prms%name` | `character(len=16)` |  | cn2, terrace, land use, mgt, etc. | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |
| `ch_prms%chg_typ` | `character(len=16)` |  | type of change (absval,abschg,pctchg) | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |
| `ch_prms%neg` | `real` |  | negative limit of change | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |
| `ch_prms%pos` | `real` |  | positive limit of change | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |
| `ch_prms%lo` | `real` |  | lower limit of parameter | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |
| `ch_prms%up` | `real` |  | upper limit of parameter | [[calibration_data_module.f90#ch_prms]] | [[ch_read_parms_cal.f90]]:34 |

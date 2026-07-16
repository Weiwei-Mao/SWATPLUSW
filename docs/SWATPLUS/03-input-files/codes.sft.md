---
type: input
tags:
  - swat/input
file: codes.sft
ext: sft
cio_field: codes_sft
read_by:
  - calsoft_read_codes.f90
purpose: ""
---

# codes.sft

> [!info] Input File
> Declared in `file.cio` field `codes_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `codes_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[calsoft_read_codes.f90]]

## File Structure
- [[calsoft_read_codes.f90]] source line 30: reads `titldum`
- [[calsoft_read_codes.f90]] source line 32: reads `header`
- [[calsoft_read_codes.f90]] source line 34: reads `cal_codes`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cal_codes%hyd_hru` | `character (len=1)` |  | if a, calibrate all hydrologic balance processes for hru by land use in each region if b, calibrate baseflow and total runoff for hru by land use in each region if y, defaults to b for existing NAM simulations | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%hyd_hrul` | `character (len=1)` |  | if y, calibrate hydrologic balance for hru_lte by land use in each region | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%plt` | `character (len=1)` |  | if y, calibrate plant growth by land use (by plant) in each region | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%sed` | `character (len=1)` |  | if y, calibrate sediment yield by land use in each region | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%nut` | `character (len=1)` |  | if y, calibrate nutrient balance by land use in each region | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%chsed` | `character (len=1)` |  | if y, calibrate channel widening and bank accretion by stream order | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%chnut` | `character (len=1)` |  | if y, calibrate channel nutrient balance by stream order | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |
| `cal_codes%res` | `character (len=1)` |  | if y, calibrate reservoir budgets by reservoir | [[calibration_data_module.f90#cal_codes]] | [[calsoft_read_codes.f90]]:34 |

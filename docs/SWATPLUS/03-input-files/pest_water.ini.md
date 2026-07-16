---
type: input
tags:
  - swat/input
file: pest_water.ini
ext: ini
cio_field: pest_water
read_by:
  - pest_cha_res_read.f90
purpose: ""
---

# pest_water.ini

> [!info] Input File
> Declared in `file.cio` field `pest_water`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pest_water`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pest_cha_res_read.f90]]

## File Structure
- [[pest_cha_res_read.f90]] source line 28: reads `titldum`
- [[pest_cha_res_read.f90]] source line 30: reads `header`
- [[pest_cha_res_read.f90]] source line 34: reads `titldum`
- [[pest_cha_res_read.f90]] source line 37: reads `titldum`
- [[pest_cha_res_read.f90]] source line 39: reads `titldum`
- [[pest_cha_res_read.f90]] source line 56: reads `titldum`
- [[pest_cha_res_read.f90]] source line 58: reads `header`
- [[pest_cha_res_read.f90]] source line 62: reads `pest_init_name(ipesti)`
- [[pest_cha_res_read.f90]] source line 64: reads `titldum`, `pest_water_ini(ipesti)%water`, `pest_water_ini(ipesti)%benthic`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pest_init_name` | `character(len=16), dimension(:), allocatable` |  |  | [[constituent_mass_module.f90#pest_init_name]] | [[pest_cha_res_read.f90]]:62 |
| `pest_water_ini%water` | `real, dimension (:), allocatable` | ppm,fracitons | amount of constituents (dissolved, salt minerals) in aquifer at start of simulation | [[constituent_mass_module.f90#pest_water_ini]] | [[pest_cha_res_read.f90]]:64 |
| `pest_water_ini%benthic` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent in benthic at start of simulation | [[constituent_mass_module.f90#pest_water_ini]] | [[pest_cha_res_read.f90]]:64 |

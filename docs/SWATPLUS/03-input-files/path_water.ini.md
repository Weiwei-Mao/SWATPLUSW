---
type: input
tags:
  - swat/input
file: path_water.ini
ext: ini
cio_field: path_water
read_by:
  - path_cha_res_read.f90
purpose: ""
---

# path_water.ini

> [!info] Input File
> Declared in `file.cio` field `path_water`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `path_water`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[path_cha_res_read.f90]]

## File Structure
- [[path_cha_res_read.f90]] source line 28: reads `titldum`
- [[path_cha_res_read.f90]] source line 30: reads `header`
- [[path_cha_res_read.f90]] source line 34: reads `titldum`
- [[path_cha_res_read.f90]] source line 37: reads `titldum`
- [[path_cha_res_read.f90]] source line 39: reads `titldum`
- [[path_cha_res_read.f90]] source line 55: reads `titldum`
- [[path_cha_res_read.f90]] source line 59: reads `header`
- [[path_cha_res_read.f90]] source line 61: reads `path_init_name(ipathi)`
- [[path_cha_res_read.f90]] source line 63: reads `titldum`, `path_water_ini(ipathi)%water`, `path_water_ini(ipathi)%benthic`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `path_init_name` | `character(len=16), dimension(:), allocatable` |  |  | [[constituent_mass_module.f90#path_init_name]] | [[path_cha_res_read.f90]]:61 |
| `path_water_ini%water` | `real, dimension (:), allocatable` | ppm,fracitons | amount of constituents (dissolved, salt minerals) in aquifer at start of simulation | [[constituent_mass_module.f90#path_water_ini]] | [[path_cha_res_read.f90]]:63 |
| `path_water_ini%benthic` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent in benthic at start of simulation | [[constituent_mass_module.f90#path_water_ini]] | [[path_cha_res_read.f90]]:63 |

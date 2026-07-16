---
type: input
tags:
  - swat/input
file: soil_plant.ini
ext: ini
cio_field: soil_plant_ini
read_by:
  - soil_plant_init.f90
purpose: ""
---

# soil_plant.ini

> [!info] Input File
> Declared in `file.cio` field `soil_plant_ini`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `soil_plant_ini`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[soil_plant_init.f90]]

## File Structure
- [[soil_plant_init.f90]] source line 25: reads `titldum`
- [[soil_plant_init.f90]] source line 27: reads `header`
- [[soil_plant_init.f90]] source line 31: reads `titldum`
- [[soil_plant_init.f90]] source line 40: reads `titldum`
- [[soil_plant_init.f90]] source line 42: reads `header`
- [[soil_plant_init.f90]] source line 47: reads `sol_plt_ini(ii)%name`, `sol_plt_ini(ii)%sw_frac`, `sol_plt_ini(ii)%nutc`, `sol_plt_ini(ii)%pestc`, `sol_plt_ini(ii)%pathc`, `sol_plt_ini(ii)%saltc`, `sol_plt_ini(ii)%hmetc`
- [[soil_plant_init.f90]] source line 50: reads `sol_plt_ini(ii)%name`, `sol_plt_ini(ii)%sw_frac`, `sol_plt_ini(ii)%nutc`, `sol_plt_ini(ii)%pestc`, `sol_plt_ini(ii)%pathc`, `sol_plt_ini(ii)%saltc`, `sol_plt_ini(ii)%hmetc`, `sol_plt_ini(ii)%csc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sol_plt_ini%name` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%sw_frac` | `real` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%nutc` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%pestc` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%pathc` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%saltc` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%hmetc` | `character(len=40)` |  |  | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:47 |
| `sol_plt_ini%csc` | `character(len=40)` |  | rtb cs | [[hru_module.f90#sol_plt_ini]] | [[soil_plant_init.f90]]:50 |

---
type: input
tags:
  - swat/input
file: pest_hru.ini
ext: ini
cio_field: pest_soil
read_by:
  - pest_hru_aqu_read.f90
purpose: ""
---

# pest_hru.ini

> [!info] Input File
> Declared in `file.cio` field `pest_soil`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pest_soil`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pest_hru_aqu_read.f90]]

## File Structure
- [[pest_hru_aqu_read.f90]] source line 24: reads `titldum`
- [[pest_hru_aqu_read.f90]] source line 28: reads `header`
- [[pest_hru_aqu_read.f90]] source line 30: reads `titldum`
- [[pest_hru_aqu_read.f90]] source line 33: reads `titldum`
- [[pest_hru_aqu_read.f90]] source line 50: reads `titldum`
- [[pest_hru_aqu_read.f90]] source line 52: reads `header`
- [[pest_hru_aqu_read.f90]] source line 56: reads `pest_soil_ini(ipesti)%name`
- [[pest_hru_aqu_read.f90]] source line 58: reads `titldum`, `pest_soil_ini(ipesti)%soil(ipest)`, `pest_soil_ini(ipesti)%plt(ipest)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pest_soil_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#pest_soil_ini]] | [[pest_hru_aqu_read.f90]]:56 |
| `pest_soil_ini%soil` | `real, dimension (:), allocatable` | ppm | amount of constituent in soil at start of simulation | [[constituent_mass_module.f90#pest_soil_ini]] | [[pest_hru_aqu_read.f90]]:58 |
| `pest_soil_ini%plt` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent on plant at start of simulation | [[constituent_mass_module.f90#pest_soil_ini]] | [[pest_hru_aqu_read.f90]]:58 |

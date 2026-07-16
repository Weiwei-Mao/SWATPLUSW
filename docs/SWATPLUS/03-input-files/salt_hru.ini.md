---
type: input
tags:
  - swat/input
file: salt_hru.ini
ext: ini
cio_field: salt_soil
read_by:
  - salt_hru_read.f90
purpose: ""
---

# salt_hru.ini

> [!info] Input File
> Declared in `file.cio` field `salt_soil`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `salt_soil`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_hru_read.f90]]

## File Structure
- [[salt_hru_read.f90]] source line 24: reads `titldum`
- [[salt_hru_read.f90]] source line 26: reads `header`
- [[salt_hru_read.f90]] source line 28: reads `header`
- [[salt_hru_read.f90]] source line 30: reads `header`
- [[salt_hru_read.f90]] source line 32: reads `header`
- [[salt_hru_read.f90]] source line 37: reads `titldum`
- [[salt_hru_read.f90]] source line 39: reads `titldum`
- [[salt_hru_read.f90]] source line 41: reads `titldum`
- [[salt_hru_read.f90]] source line 55: reads `titldum`
- [[salt_hru_read.f90]] source line 57: reads `header`
- [[salt_hru_read.f90]] source line 59: reads `header`
- [[salt_hru_read.f90]] source line 61: reads `header`
- [[salt_hru_read.f90]] source line 63: reads `header`
- [[salt_hru_read.f90]] source line 67: reads `salt_soil_ini(isalti)%name`
- [[salt_hru_read.f90]] source line 69: reads `salt_soil_ini(isalti)%soil`
- [[salt_hru_read.f90]] source line 71: reads `salt_soil_ini(isalti)%plt`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `salt_soil_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#salt_soil_ini]] | [[salt_hru_read.f90]]:67 |
| `salt_soil_ini%soil` | `real, dimension (:), allocatable` | ppm | amount of constituent in soil at start of simulation | [[constituent_mass_module.f90#salt_soil_ini]] | [[salt_hru_read.f90]]:69 |
| `salt_soil_ini%plt` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent on plant at start of simulation | [[constituent_mass_module.f90#salt_soil_ini]] | [[salt_hru_read.f90]]:71 |

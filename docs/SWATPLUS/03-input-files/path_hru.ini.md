---
type: input
tags:
  - swat/input
file: path_hru.ini
ext: ini
cio_field: path_soil
read_by:
  - path_hru_aqu_read.f90
purpose: ""
---

# path_hru.ini

> [!info] Input File
> Declared in `file.cio` field `path_soil`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `path_soil`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[path_hru_aqu_read.f90]]

## File Structure
- [[path_hru_aqu_read.f90]] source line 24: reads `titldum`
- [[path_hru_aqu_read.f90]] source line 28: reads `header`
- [[path_hru_aqu_read.f90]] source line 30: reads `titldum`
- [[path_hru_aqu_read.f90]] source line 33: reads `titldum`
- [[path_hru_aqu_read.f90]] source line 50: reads `titldum`
- [[path_hru_aqu_read.f90]] source line 54: reads `header`
- [[path_hru_aqu_read.f90]] source line 56: reads `path_soil_ini(ipathi)%name`
- [[path_hru_aqu_read.f90]] source line 58: reads `titldum`, `path_soil_ini(ipathi)%soil`, `path_soil_ini(ipathi)%plt`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `path_soil_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#path_soil_ini]] | [[path_hru_aqu_read.f90]]:56 |
| `path_soil_ini%soil` | `real, dimension (:), allocatable` | ppm | amount of constituent in soil at start of simulation | [[constituent_mass_module.f90#path_soil_ini]] | [[path_hru_aqu_read.f90]]:58 |
| `path_soil_ini%plt` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent on plant at start of simulation | [[constituent_mass_module.f90#path_soil_ini]] | [[path_hru_aqu_read.f90]]:58 |

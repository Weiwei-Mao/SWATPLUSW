---
type: input
tags:
  - swat/input
file: hmet_hru.ini
ext: ini
cio_field: hmet_soil
read_by:
  - hmet_hru_aqu_read.f90
purpose: ""
---

# hmet_hru.ini

> [!info] Input File
> Declared in `file.cio` field `hmet_soil`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hmet_soil`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[hmet_hru_aqu_read.f90]]

## File Structure
- [[hmet_hru_aqu_read.f90]] source line 25: reads `titldum`
- [[hmet_hru_aqu_read.f90]] source line 29: reads `header`
- [[hmet_hru_aqu_read.f90]] source line 31: reads `titldum`
- [[hmet_hru_aqu_read.f90]] source line 34: reads `titldum`
- [[hmet_hru_aqu_read.f90]] source line 51: reads `titldum`
- [[hmet_hru_aqu_read.f90]] source line 55: reads `header`
- [[hmet_hru_aqu_read.f90]] source line 57: reads `hmet_soil_ini(ihmeti)%name`
- [[hmet_hru_aqu_read.f90]] source line 60: reads `titldum`, `hmet_soil_ini(ihmeti)%soil(ihmet)`
- [[hmet_hru_aqu_read.f90]] source line 62: reads `titldum`, `hmet_soil_ini(ihmeti)%plt(ihmet)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `hmet_soil_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#hmet_soil_ini]] | [[hmet_hru_aqu_read.f90]]:57 |
| `hmet_soil_ini%soil` | `real, dimension (:), allocatable` | ppm | amount of constituent in soil at start of simulation | [[constituent_mass_module.f90#hmet_soil_ini]] | [[hmet_hru_aqu_read.f90]]:60 |
| `hmet_soil_ini%plt` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent on plant at start of simulation | [[constituent_mass_module.f90#hmet_soil_ini]] | [[hmet_hru_aqu_read.f90]]:62 |

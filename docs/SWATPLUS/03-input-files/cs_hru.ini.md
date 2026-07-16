---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_hru.ini
ext: ini
cio_field: []
read_by:
  - cs_hru_read.f90
purpose: ""
---

# cs_hru.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_hru_read.f90]]

## File Structure
- [[cs_hru_read.f90]] source line 24: reads `titldum`
- [[cs_hru_read.f90]] source line 26: reads `header`
- [[cs_hru_read.f90]] source line 28: reads `header`
- [[cs_hru_read.f90]] source line 30: reads `header`
- [[cs_hru_read.f90]] source line 32: reads `header`
- [[cs_hru_read.f90]] source line 37: reads `titldum`
- [[cs_hru_read.f90]] source line 39: reads `titldum`
- [[cs_hru_read.f90]] source line 41: reads `titldum`
- [[cs_hru_read.f90]] source line 56: reads `titldum`
- [[cs_hru_read.f90]] source line 58: reads `header`
- [[cs_hru_read.f90]] source line 60: reads `header`
- [[cs_hru_read.f90]] source line 62: reads `header`
- [[cs_hru_read.f90]] source line 64: reads `header`
- [[cs_hru_read.f90]] source line 68: reads `cs_soil_ini(ics)%name`
- [[cs_hru_read.f90]] source line 70: reads `cs_soil_ini(ics)%soil`
- [[cs_hru_read.f90]] source line 72: reads `cs_soil_ini(ics)%plt`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_soil_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#cs_soil_ini]] | [[cs_hru_read.f90]]:68 |
| `cs_soil_ini%soil` | `real, dimension (:), allocatable` | ppm | amount of constituent in soil at start of simulation | [[constituent_mass_module.f90#cs_soil_ini]] | [[cs_hru_read.f90]]:70 |
| `cs_soil_ini%plt` | `real, dimension (:), allocatable` | ppm or #cfu/m^2 | amount of constituent on plant at start of simulation | [[constituent_mass_module.f90#cs_soil_ini]] | [[cs_hru_read.f90]]:72 |

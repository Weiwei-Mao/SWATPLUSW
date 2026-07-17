---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_irrigation
ext: 
cio_field: []
read_by:
  - cs_irr_read.f90
purpose: ""
---

# cs_irrigation

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_irr_read.f90]]

## File Structure
- [[cs_irr_read.f90]] source line 25: reads `titldum`
- [[cs_irr_read.f90]] source line 27: reads `header`
- [[cs_irr_read.f90]] source line 33: reads `titldum`
- [[cs_irr_read.f90]] source line 47: reads `titldum`
- [[cs_irr_read.f90]] source line 49: reads `header`
- [[cs_irr_read.f90]] source line 52: reads `cs_water_irr(icsi)%name`, `cs_water_irr(icsi)%water`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_water_irr%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#cs_water_irr]] | [[cs_irr_read.f90]]:52 |
| `cs_water_irr%water` | `real, dimension (:), allocatable` | ppm | amount of constituent in water at start of simulation | [[constituent_mass_module.f90#cs_water_irr]] | [[cs_irr_read.f90]]:52 |

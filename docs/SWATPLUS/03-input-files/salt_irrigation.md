---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_irrigation
ext: 
cio_field: []
read_by:
  - salt_irr_read.f90
purpose: ""
---

# salt_irrigation

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_irr_read.f90]]

## File Structure
- [[salt_irr_read.f90]] source line 23: reads `titldum`
- [[salt_irr_read.f90]] source line 25: reads `header`
- [[salt_irr_read.f90]] source line 32: reads `titldum`
- [[salt_irr_read.f90]] source line 45: reads `titldum`
- [[salt_irr_read.f90]] source line 47: reads `header`
- [[salt_irr_read.f90]] source line 50: reads `salt_water_irr(isalti)%name`, `salt_water_irr(isalti)%water`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `salt_water_irr%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#salt_water_irr]] | [[salt_irr_read.f90]]:50 |
| `salt_water_irr%water` | `real, dimension (:), allocatable` | ppm | amount of constituent in water at start of simulation | [[constituent_mass_module.f90#salt_water_irr]] | [[salt_irr_read.f90]]:50 |

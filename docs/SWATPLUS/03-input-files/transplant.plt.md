---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: transplant.plt
ext: plt
cio_field: []
read_by:
  - plant_transplant_read.f90
purpose: ""
---

# transplant.plt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[plant_transplant_read.f90]]

## File Structure
- [[plant_transplant_read.f90]] source line 25: reads `titldum`
- [[plant_transplant_read.f90]] source line 27: reads `header`
- [[plant_transplant_read.f90]] source line 30: reads `titldum`
- [[plant_transplant_read.f90]] source line 37: reads `titldum`
- [[plant_transplant_read.f90]] source line 39: reads `header`
- [[plant_transplant_read.f90]] source line 43: reads `transpl(ic)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `transpl%name` | `character(len=40)` |  |  | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |
| `transpl%lai` | `real` | m**2/m**2 | leaf area index | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |
| `transpl%bioms` | `real` | kg/ha | land cover/crop biomass | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |
| `transpl%phuacc` | `real` | frac | frac of plant heat unit acc. | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |
| `transpl%fr_yrmat` | `real` | years | fraction of current year of growth to years to maturity | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |
| `transpl%pop` | `real` | plants/m^2 | plant population | [[plant_data_module.f90#transpl]] | [[plant_transplant_read.f90]]:43 |

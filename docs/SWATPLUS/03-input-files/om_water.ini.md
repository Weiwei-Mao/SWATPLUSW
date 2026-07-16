---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: om_water.ini
ext: ini
cio_field: []
read_by:
  - om_water_init.f90
purpose: ""
---

# om_water.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[om_water_init.f90]]

## File Structure
- [[om_water_init.f90]] source line 30: reads `titldum`
- [[om_water_init.f90]] source line 32: reads `header`
- [[om_water_init.f90]] source line 35: reads `titldum`
- [[om_water_init.f90]] source line 45: reads `titldum`
- [[om_water_init.f90]] source line 47: reads `header`
- [[om_water_init.f90]] source line 51: reads `titldum`
- [[om_water_init.f90]] source line 54: reads `om_init_name(ichi)`, `om_init_water(ichi)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `om_init_name` | `character(len=16), dimension(:), allocatable` |  |  | [[hydrograph_module.f90#om_init_name]] | [[om_water_init.f90]]:54 |
| `om_init_water%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%san` | `real` | tons | detached sand | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%grv` | `real` | tons | gravel | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |
| `om_init_water%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#om_init_water]] | [[om_water_init.f90]]:54 |

---
type: input
tags:
  - swat/input
file: exco_om.exc
ext: exc
cio_field: om
read_by:
  - exco_read_om.f90
purpose: ""
---

# exco_om.exc

> [!info] Input File
> Declared in `file.cio` field `om`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `om`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_read_om.f90]]

## File Structure
- [[exco_read_om.f90]] source line 32: reads `titldum`
- [[exco_read_om.f90]] source line 34: reads `header`
- [[exco_read_om.f90]] source line 36: reads `header`
- [[exco_read_om.f90]] source line 40: reads `titldum`
- [[exco_read_om.f90]] source line 51: reads `titldum`
- [[exco_read_om.f90]] source line 53: reads `header`
- [[exco_read_om.f90]] source line 55: reads `header`
- [[exco_read_om.f90]] source line 60: reads `exco_om_name(ii)`, `exco(ii)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `exco_om_name` | `character(len=16), dimension(:), allocatable` |  |  | [[exco_module.f90#exco_om_name]] | [[exco_read_om.f90]]:60 |
| `exco%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%san` | `real` | tons | detached sand | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%grv` | `real` | tons | gravel | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |
| `exco%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#exco]] | [[exco_read_om.f90]]:60 |

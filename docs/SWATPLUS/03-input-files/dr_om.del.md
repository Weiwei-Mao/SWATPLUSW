---
type: input
tags:
  - swat/input
file: dr_om.del
ext: del
cio_field: om
read_by:
  - dr_read_om.f90
purpose: ""
---

# dr_om.del

> [!info] Input File
> Declared in `file.cio` field `om`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `om`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_read_om.f90]]

## File Structure
- [[dr_read_om.f90]] source line 33: reads `titldum`
- [[dr_read_om.f90]] source line 35: reads `header`
- [[dr_read_om.f90]] source line 39: reads `titldum`
- [[dr_read_om.f90]] source line 50: reads `titldum`
- [[dr_read_om.f90]] source line 52: reads `header`
- [[dr_read_om.f90]] source line 57: reads `titldum`
- [[dr_read_om.f90]] source line 60: reads `dr_om_name(ii)`, `dr(ii)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_om_name` | `character(len=16), dimension(:), allocatable` |  |  | [[dr_module.f90#dr_om_name]] | [[dr_read_om.f90]]:60 |
| `dr%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%san` | `real` | tons | detached sand | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%grv` | `real` | tons | gravel | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |
| `dr%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#dr]] | [[dr_read_om.f90]]:60 |

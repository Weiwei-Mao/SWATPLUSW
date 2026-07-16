---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: om_use.wal
ext: wal
cio_field: []
read_by:
  - om_use_read.f90
purpose: ""
---

# om_use.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[om_use_read.f90]]

## File Structure
- [[om_use_read.f90]] source line 31: reads `titldum`
- [[om_use_read.f90]] source line 33: reads `imax`
- [[om_use_read.f90]] source line 34: reads `header`
- [[om_use_read.f90]] source line 43: reads `om_use_name(iom_use)`, `wuse_om_efflu(iom_use)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `om_use_read.f90:15` | [[om_use_read.f90]]:33 |
| `om_use_name` | `character(len=16), dimension(:), allocatable` |  |  | [[water_allocation_module.f90#om_use_name]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%san` | `real` | tons | detached sand | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%grv` | `real` | tons | gravel | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |
| `wuse_om_efflu%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#wuse_om_efflu]] | [[om_use_read.f90]]:43 |

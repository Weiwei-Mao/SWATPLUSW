---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: om_osrc.wal
ext: wal
cio_field: []
read_by:
  - om_osrc_read.f90
purpose: ""
---

# om_osrc.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[om_osrc_read.f90]]

## File Structure
- [[om_osrc_read.f90]] source line 32: reads `titldum`
- [[om_osrc_read.f90]] source line 34: reads `imax`
- [[om_osrc_read.f90]] source line 35: reads `header`
- [[om_osrc_read.f90]] source line 43: reads `om_osrc_name(iom_osrc)`, `osrc_om(iom_osrc)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `om_osrc_read.f90:15` | [[om_osrc_read.f90]]:34 |
| `om_osrc_name` | `character(len=16), dimension(:), allocatable` |  |  | [[water_allocation_module.f90#om_osrc_name]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%san` | `real` | tons | detached sand | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%grv` | `real` | tons | gravel | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |
| `osrc_om%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#osrc_om]] | [[om_osrc_read.f90]]:43 |

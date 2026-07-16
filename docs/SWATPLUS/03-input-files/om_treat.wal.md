---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: om_treat.wal
ext: wal
cio_field: []
read_by:
  - om_treat_read.f90
purpose: ""
---

# om_treat.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[om_treat_read.f90]]

## File Structure
- [[om_treat_read.f90]] source line 31: reads `titldum`
- [[om_treat_read.f90]] source line 33: reads `imax`
- [[om_treat_read.f90]] source line 34: reads `header`
- [[om_treat_read.f90]] source line 42: reads `om_treat_name(iom_tr)`, `wtp_om_treat(iom_tr)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `om_treat_read.f90:15` | [[om_treat_read.f90]]:33 |
| `om_treat_name` | `character(len=16), dimension(:), allocatable` |  |  | [[water_allocation_module.f90#om_treat_name]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%flo` | `real` | m^3 | volume of water | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%sed` | `real` | metric tons | sediment | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%orgn` | `real` | kg N | organic N | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%sedp` | `real` | kg P | organic P | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%no3` | `real` | kg N | NO3-N | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%solp` | `real` | kg P | mineral (soluble P) | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%chla` | `real` | kg | chlorophyll-a | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%nh3` | `real` | kg N | NH3 | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%no2` | `real` | kg N | NO2 | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%cbod` | `real` | kg | carbonaceous biological oxygen demand | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%dox` | `real` | kg | dissolved oxygen | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%san` | `real` | tons | detached sand | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%sil` | `real` | tons | detached silt | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%cla` | `real` | tons | detached clay | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%sag` | `real` | tons | detached small ag | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%lag` | `real` | tons | detached large ag | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%grv` | `real` | tons | gravel | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |
| `wtp_om_treat%temp` | `real` | deg c | temperature | [[hydrograph_module.f90#wtp_om_treat]] | [[om_treat_read.f90]]:42 |

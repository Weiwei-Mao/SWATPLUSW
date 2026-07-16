---
type: input
tags:
  - swat/input
file: hydrology.hyd
ext: hyd
cio_field: hydrol_hyd
read_by:
  - hydrol_read.f90
purpose: ""
---

# hydrology.hyd

> [!info] Input File
> Declared in `file.cio` field `hydrol_hyd`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hydrol_hyd`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[hydrol_read.f90]]

## File Structure
- [[hydrol_read.f90]] source line 28: reads `titldum`
- [[hydrol_read.f90]] source line 30: reads `header`
- [[hydrol_read.f90]] source line 33: reads `titldum`
- [[hydrol_read.f90]] source line 41: reads `titldum`
- [[hydrol_read.f90]] source line 43: reads `header`
- [[hydrol_read.f90]] source line 47: reads `hyd_db(ithyd)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `hyd_db%name` | `character(len=16)` | none | 0 \|0 \|name | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%lat_ttime` | `real` | days | 0-120 \|0 \|Exponential of the lateral flow travel time | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%lat_sed` | `real` | g/L | sediment concentration in lateral flow | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%canmx` | `real` | mm H2O | maximum canopy storage | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%esco` | `real` | none | soil evaporation compensation factor (0-1) | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%epco` | `real` | none | plant water uptake compensation factor (0-1) | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%erorgn` | `real` | none | organic N enrichment ratio, if left blank % \|the model will calculate for every event | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%erorgp` | `real` | none | organic P enrichment ratio, if left blank % \|the model will calculate for every event | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%cn3_swf` | `real` | none | soil water at cn3 - 0=fc; .99=near saturation | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%biomix` | `real` | none | biological mixing efficiency. % \|Mixing of soil due to activity of earthworms and other soil biota. % \|Mixing is performed at the end of every calendar year. | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%perco` | `real` | none | 0-1 \|percolation coefficient - linear adjustment to daily perc | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%lat_orgn` | `real` | ppm | organic N concentration in lateral flow | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%lat_orgp` | `real` | ppm | organic P concentration in lateral flow | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%pet_co` | `real` | none | coefficient related to radiation used in Hargreaves equation | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |
| `hyd_db%latq_co` | `real` | none | 0-1 \|lateral soil flow coefficient - linear adjustment to daily lat flow | [[hydrology_data_module.f90#hyd_db]] | [[hydrol_read.f90]]:47 |

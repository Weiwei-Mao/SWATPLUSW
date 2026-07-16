---
type: input
tags:
  - swat/input
file: topography.hyd
ext: hyd
cio_field: topogr_hyd
read_by:
  - topo_read.f90
purpose: ""
---

# topography.hyd

> [!info] Input File
> Declared in `file.cio` field `topogr_hyd`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `topogr_hyd`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[topo_read.f90]]

## File Structure
- [[topo_read.f90]] source line 32: reads `titldum`
- [[topo_read.f90]] source line 34: reads `header`
- [[topo_read.f90]] source line 37: reads `titldum`
- [[topo_read.f90]] source line 45: reads `titldum`
- [[topo_read.f90]] source line 47: reads `header`
- [[topo_read.f90]] source line 51: reads `topo_db(ith)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `topo_db%name` | `character(len=16)` |  |  | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |
| `topo_db%slope` | `real` | hru_slp(:) | m/m \|average slope steepness in HRU | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |
| `topo_db%slope_len` | `real` | slsubbsn(:) | m \|average slope length for erosion | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |
| `topo_db%lat_len` | `real` | slsoil(:) | m \|slope length for lateral subsurface flow | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |
| `topo_db%dis_stream` | `real` | dis_stream(:) | m \|average distance to stream | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |
| `topo_db%dep_co` | `real` |  | \|deposition coefficient | [[topography_data_module.f90#topo_db]] | [[topo_read.f90]]:51 |

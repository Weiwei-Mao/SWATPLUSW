---
type: input
tags:
  - swat/input
file: ovn_table.lum
ext: lum
cio_field: ovn_lum
read_by:
  - overland_n_read.f90
purpose: ""
---

# ovn_table.lum

> [!info] Input File
> Declared in `file.cio` field `ovn_lum`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ovn_lum`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[overland_n_read.f90]]

## File Structure
- [[overland_n_read.f90]] source line 25: reads `titldum`
- [[overland_n_read.f90]] source line 27: reads `header`
- [[overland_n_read.f90]] source line 30: reads `titldum`
- [[overland_n_read.f90]] source line 38: reads `titldum`
- [[overland_n_read.f90]] source line 40: reads `header`
- [[overland_n_read.f90]] source line 44: reads `overland_n(il)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `overland_n%name` | `character(len=40)` |  | name of conservation practice | [[landuse_data_module.f90#overland_n]] | [[overland_n_read.f90]]:44 |
| `overland_n%ovn` | `real` |  | overland flow mannings n - mean | [[landuse_data_module.f90#overland_n]] | [[overland_n_read.f90]]:44 |
| `overland_n%ovn_min` | `real` |  | overland flow mannings n - min | [[landuse_data_module.f90#overland_n]] | [[overland_n_read.f90]]:44 |
| `overland_n%ovn_max` | `real` |  | overland flow mannings n - max | [[landuse_data_module.f90#overland_n]] | [[overland_n_read.f90]]:44 |

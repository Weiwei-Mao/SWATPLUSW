---
type: input
tags:
  - swat/input
file: wetland.wet
ext: wet
cio_field: wet
read_by:
  - wet_read.f90
purpose: ""
---

# wetland.wet

> [!info] Input File
> Declared in `file.cio` field `wet`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `wet`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[wet_read.f90]]

## File Structure
- [[wet_read.f90]] source line 41: reads `titldum`
- [[wet_read.f90]] source line 43: reads `header`
- [[wet_read.f90]] source line 46: reads `i`
- [[wet_read.f90]] source line 57: reads `titldum`
- [[wet_read.f90]] source line 59: reads `header`
- [[wet_read.f90]] source line 63: reads `i`
- [[wet_read.f90]] source line 66: reads `k`, `wet_dat_c(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `wet_read.f90:25` | [[wet_read.f90]]:46 |
| `k` | `integer` | none | counter | `wet_read.f90:27` | [[wet_read.f90]]:66 |
| `wet_dat_c%name` | `character (len=25)` |  |  | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |
| `wet_dat_c%init` | `character (len=25)` |  | initial data-points to initial.res | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |
| `wet_dat_c%hyd` | `character (len=25)` |  | points to hydrology.res for hydrology inputs | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |
| `wet_dat_c%release` | `character (len=25)` |  | 0=simulated; 1=measured outflow | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |
| `wet_dat_c%sed` | `character (len=25)` |  | sediment inputs-points to sediment.res | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |
| `wet_dat_c%nut` | `character (len=25)` |  | nutrient inputs-points to nutrient.res | [[reservoir_data_module.f90#wet_dat_c]] | [[wet_read.f90]]:66 |

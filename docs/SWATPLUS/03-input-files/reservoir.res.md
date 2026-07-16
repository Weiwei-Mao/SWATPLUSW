---
type: input
tags:
  - swat/input
file: reservoir.res
ext: res
cio_field: res
read_by:
  - res_read.f90
purpose: ""
---

# reservoir.res

> [!info] Input File
> Declared in `file.cio` field `res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read.f90]]

## File Structure
- [[res_read.f90]] source line 50: reads `titldum`
- [[res_read.f90]] source line 52: reads `header`
- [[res_read.f90]] source line 55: reads `i`
- [[res_read.f90]] source line 65: reads `titldum`
- [[res_read.f90]] source line 67: reads `header`
- [[res_read.f90]] source line 71: reads `ires`
- [[res_read.f90]] source line 74: reads `k`, `res_dat_c(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `res_read.f90:22` | [[res_read.f90]]:55 |
| `ires` | `integer` | none | counter | `res_read.f90:29` | [[res_read.f90]]:71 |
| `k` | `integer` |  |  | `res_read.f90:30` | [[res_read.f90]]:74 |
| `res_dat_c%name` | `character (len=25)` |  |  | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |
| `res_dat_c%init` | `character (len=25)` |  | initial data-points to initial.res | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |
| `res_dat_c%hyd` | `character (len=25)` |  | points to hydrology.res for hydrology inputs | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |
| `res_dat_c%release` | `character (len=25)` |  | 0=simulated; 1=measured outflow | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |
| `res_dat_c%sed` | `character (len=25)` |  | sediment inputs-points to sediment.res | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |
| `res_dat_c%nut` | `character (len=25)` |  | nutrient inputs-points to nutrient.res | [[reservoir_data_module.f90#res_dat_c]] | [[res_read.f90]]:74 |

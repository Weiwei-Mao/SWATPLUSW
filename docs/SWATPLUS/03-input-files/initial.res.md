---
type: input
tags:
  - swat/input
file: initial.res
ext: res
cio_field: init_res
read_by:
  - res_read_init.f90
purpose: ""
---

# initial.res

> [!info] Input File
> Declared in `file.cio` field `init_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `init_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_init.f90]]

## File Structure
- [[res_read_init.f90]] source line 28: reads `titldum`
- [[res_read_init.f90]] source line 30: reads `header`
- [[res_read_init.f90]] source line 33: reads `titldum`
- [[res_read_init.f90]] source line 45: reads `titldum`
- [[res_read_init.f90]] source line 47: reads `header`
- [[res_read_init.f90]] source line 51: reads `res_init_dat_c(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_init_dat_c%init` | `character (len=25)` |  | initial data-points to initial.cha | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |
| `res_init_dat_c%org_min` | `character (len=25)` |  | points to initial organic-mineral input file | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |
| `res_init_dat_c%pest` | `character (len=25)` |  | points to initial pesticide input file | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |
| `res_init_dat_c%path` | `character (len=25)` |  | points to initial pathogen input file | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |
| `res_init_dat_c%hmet` | `character (len=25)` |  | points to initial heavy metals input file | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |
| `res_init_dat_c%salt` | `character (len=25)` |  | points to initial salt input file | [[reservoir_data_module.f90#res_init_dat_c]] | [[res_read_init.f90]]:51 |

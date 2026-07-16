---
type: input
tags:
  - swat/input
file: weir.res
ext: res
cio_field: weir_res
read_by:
  - res_read_weir.f90
purpose: ""
---

# weir.res

> [!info] Input File
> Declared in `file.cio` field `weir_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `weir_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_weir.f90]]

## File Structure
- [[res_read_weir.f90]] source line 32: reads `titldum`
- [[res_read_weir.f90]] source line 34: reads `header`
- [[res_read_weir.f90]] source line 37: reads `titldum`
- [[res_read_weir.f90]] source line 46: reads `titldum`
- [[res_read_weir.f90]] source line 48: reads `header`
- [[res_read_weir.f90]] source line 52: reads `titldum`
- [[res_read_weir.f90]] source line 55: reads `res_weir(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_weir%name` | `character(len=25)` |  |  | [[reservoir_data_module.f90#res_weir]] | [[res_read_weir.f90]]:55 |
| `res_weir%c` | `real` | none | weir discharge linear coefficient | [[reservoir_data_module.f90#res_weir]] | [[res_read_weir.f90]]:55 |
| `res_weir%k` | `real` | none | weir discharge exponential coefficient | [[reservoir_data_module.f90#res_weir]] | [[res_read_weir.f90]]:55 |
| `res_weir%w` | `real` | m | width | [[reservoir_data_module.f90#res_weir]] | [[res_read_weir.f90]]:55 |
| `res_weir%h` | `real` | m | height of weir above bottoom of impoundment | [[reservoir_data_module.f90#res_weir]] | [[res_read_weir.f90]]:55 |

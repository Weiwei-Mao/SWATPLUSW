---
type: input
tags:
  - swat/input
file: sediment.res
ext: res
cio_field: sed_res
read_by:
  - res_read_sed.f90
purpose: ""
---

# sediment.res

> [!info] Input File
> Declared in `file.cio` field `sed_res`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `sed_res`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_sed.f90]]

## File Structure
- [[res_read_sed.f90]] source line 32: reads `titldum`
- [[res_read_sed.f90]] source line 34: reads `header`
- [[res_read_sed.f90]] source line 37: reads `titldum`
- [[res_read_sed.f90]] source line 46: reads `titldum`
- [[res_read_sed.f90]] source line 48: reads `header`
- [[res_read_sed.f90]] source line 52: reads `titldum`
- [[res_read_sed.f90]] source line 55: reads `res_sed(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_sed%name` | `character(len=25)` |  |  | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%nsed` | `real` | kg/L | normal amt of sed in res (read in as mg/L and convert to kg/L) | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%d50` | `real` | um | median particle size of suspended and benthic sediment | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%carbon` | `real` | % | organic carbon in suspended and benthic sediment | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%bd` | `real` | t/m^3 | bulk density of benthic sediment | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%sed_stlr` | `real` | none | sediment settling rate | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |
| `res_sed%velsetlr` | `real` | m/d | sediment settling velocity | [[reservoir_data_module.f90#res_sed]] | [[res_read_sed.f90]]:55 |

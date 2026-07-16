---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: nutrients.res
ext: res
cio_field: []
read_by:
  - res_read_nut.f90
purpose: ""
---

# nutrients.res

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_nut.f90]]

## File Structure
- [[res_read_nut.f90]] source line 32: reads `titldum`
- [[res_read_nut.f90]] source line 34: reads `header`
- [[res_read_nut.f90]] source line 37: reads `titldum`
- [[res_read_nut.f90]] source line 46: reads `titldum`
- [[res_read_nut.f90]] source line 48: reads `header`
- [[res_read_nut.f90]] source line 52: reads `titldum`
- [[res_read_nut.f90]] source line 55: reads `res_nut(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_nut%name` | `character(len=25)` |  |  | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%ires1` | `integer` | none | beg of mid-year nutrient settling "season" | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%ires2` | `integer` | none | end of mid-year nutrient settling "season" | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%nsetlr1` | `real` | frac | nit mass loss rate for mid-year period | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%nsetlr2` | `real` | frac | nit mass loss rate for remainder of year | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%psetlr1` | `real` | frac | phos mass loss rate for mid-year period | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%psetlr2` | `real` | frac | phos mass loss rate for remainder of year | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%nsolr` | `real` | none | loss rate for souble n - no3, nh3, no2 | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%psolr` | `real` | none | loss rate for soluble p | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%theta_n` | `real` | none | temperature adjustment for nitrogen loss (settling) | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%theta_p` | `real` | none | temperature adjustment for phosphorus loss (settling) | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%conc_nmin` | `real` | ppm | minimum nitrogen concentration for settling | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |
| `res_nut%conc_pmin` | `real` | ppm | minimum phosphorus concentration for settling | [[reservoir_data_module.f90#res_nut]] | [[res_read_nut.f90]]:55 |

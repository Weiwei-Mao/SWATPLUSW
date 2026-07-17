---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_res
ext: 
cio_field: []
read_by:
  - res_read_csdb.f90
purpose: ""
---

# cs_res

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_csdb.f90]]

## File Structure
- [[res_read_csdb.f90]] source line 30: reads `titldum`
- [[res_read_csdb.f90]] source line 31: reads `titldum`
- [[res_read_csdb.f90]] source line 33: reads (no targets parsed)
- [[res_read_csdb.f90]] source line 37: reads `header`
- [[res_read_csdb.f90]] source line 40: reads `titldum`
- [[res_read_csdb.f90]] source line 49: reads `titldum`
- [[res_read_csdb.f90]] source line 51: reads `titldum`
- [[res_read_csdb.f90]] source line 53: reads (no targets parsed)
- [[res_read_csdb.f90]] source line 55: reads `header`
- [[res_read_csdb.f90]] source line 59: reads `titldum`
- [[res_read_csdb.f90]] source line 62: reads `res_cs_data(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `res_cs_data%name` | `character(len=25)` |  |  | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%v_seo4` | `real` | m/day | settling rate for selenate | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%v_seo3` | `real` | m/day | settling rate for selinite | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%v_born` | `real` | m/day | settling rate for boron | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%k_seo4` | `real` | 1/day | first-order degradation constant for selenate | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%k_seo3` | `real` | 1/day | first-order degradation constant for selenite | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%k_born` | `real` | 1/day | first-order degradation constant for boron | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%theta_seo4` | `real` | none | temperature adjustment for selenate degradation | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%theta_seo3` | `real` | none | temperature adjustment for selenite degradation | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%theta_born` | `real` | none | temperature adjustment for boron degradation | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%c_seo4` | `real` | g/m3 | initial concentration of selenate | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%c_seo3` | `real` | g/m3 | initial concentration of selenite | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |
| `res_cs_data%c_born` | `real` | g/m3 | initial concentration of boron | [[res_cs_module.f90#res_cs_data]] | [[res_read_csdb.f90]]:62 |

---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: reservoir.res_cs
ext: res_cs
cio_field: []
read_by:
  - res_read_salt_cs.f90
purpose: ""
---

# reservoir.res_cs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[res_read_salt_cs.f90]]

## File Structure
- [[res_read_salt_cs.f90]] source line 32: reads `header`
- [[res_read_salt_cs.f90]] source line 33: reads `header`
- [[res_read_salt_cs.f90]] source line 40: reads `ires`
- [[res_read_salt_cs.f90]] source line 43: reads `k`, `res_dat_c_cs(ires)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ires` | `integer` | none | counter | `res_read_salt_cs.f90:18` | [[res_read_salt_cs.f90]]:40 |
| `k` | `integer` |  |  | `res_read_salt_cs.f90:19` | [[res_read_salt_cs.f90]]:43 |
| `res_dat_c_cs%pst` | `character (len=25)` |  | pesticide inputs-points to pesticide.res | [[reservoir_data_module.f90#res_dat_c_cs]] | [[res_read_salt_cs.f90]]:43 |
| `res_dat_c_cs%weir` | `character (len=25)` |  | weir inputs-points to weir.res Jaehak 2022 | [[reservoir_data_module.f90#res_dat_c_cs]] | [[res_read_salt_cs.f90]]:43 |
| `res_dat_c_cs%salt` | `character (len=25)` |  | salt inputs - points to salt_res rtb salt | [[reservoir_data_module.f90#res_dat_c_cs]] | [[res_read_salt_cs.f90]]:43 |
| `res_dat_c_cs%cs` | `character (len=25)` |  | constituent inputs - points to cs_res rtb cs | [[reservoir_data_module.f90#res_dat_c_cs]] | [[res_read_salt_cs.f90]]:43 |

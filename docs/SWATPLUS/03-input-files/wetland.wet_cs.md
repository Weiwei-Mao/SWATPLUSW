---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: wetland.wet_cs
ext: wet_cs
cio_field: []
read_by:
  - wet_read_salt_cs.f90
purpose: ""
---

# wetland.wet_cs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[wet_read_salt_cs.f90]]

## File Structure
- [[wet_read_salt_cs.f90]] source line 32: reads `header`
- [[wet_read_salt_cs.f90]] source line 33: reads `header`
- [[wet_read_salt_cs.f90]] source line 40: reads `i`
- [[wet_read_salt_cs.f90]] source line 43: reads `k`, `wet_dat_c_cs(iwet)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `wet_read_salt_cs.f90:12` | [[wet_read_salt_cs.f90]]:40 |
| `k` | `integer` |  |  | `wet_read_salt_cs.f90:19` | [[wet_read_salt_cs.f90]]:43 |
| `wet_dat_c_cs%pst` | `character (len=25)` |  | pesticide inputs-points to pesticide.res | [[reservoir_data_module.f90#wet_dat_c_cs]] | [[wet_read_salt_cs.f90]]:43 |
| `wet_dat_c_cs%weir` | `character (len=25)` |  | weir inputs-points to weir.res Jaehak 2022 | [[reservoir_data_module.f90#wet_dat_c_cs]] | [[wet_read_salt_cs.f90]]:43 |
| `wet_dat_c_cs%salt` | `character (len=25)` |  | salt inputs - points to salt_res rtb salt | [[reservoir_data_module.f90#wet_dat_c_cs]] | [[wet_read_salt_cs.f90]]:43 |
| `wet_dat_c_cs%cs` | `character (len=25)` |  | constituent inputs - points to cs_res rtb cs | [[reservoir_data_module.f90#wet_dat_c_cs]] | [[wet_read_salt_cs.f90]]:43 |

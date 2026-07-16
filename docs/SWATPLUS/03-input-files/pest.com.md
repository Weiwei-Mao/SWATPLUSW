---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: pest.com
ext: com
cio_field: []
read_by:
  - recall_read.f90
purpose: ""
---

# pest.com

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[recall_read.f90]]

## File Structure
- [[recall_read.f90]] source line 234: reads `titldum`
- [[recall_read.f90]] source line 236: reads `header`
- [[recall_read.f90]] source line 240: reads `i`
- [[recall_read.f90]] source line 247: reads `titldum`
- [[recall_read.f90]] source line 249: reads `header`
- [[recall_read.f90]] source line 253: reads `ipestcom_db`
- [[recall_read.f90]] source line 257: reads `i`
- [[recall_read.f90]] source line 260: reads `k`, `rec_pest(i)%name`, `rec_pest(i)%typ`, `rec_pest(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `recall_read.f90:14` | [[recall_read.f90]]:240 |
| `ipestcom_db` | `integer` |  | none !pointer to pestcom_db - fix*** ?? | `recall_read.f90:103` | [[recall_read.f90]]:253 |
| `k` | `integer` |  |  | `recall_read.f90:16` | [[recall_read.f90]]:260 |
| `rec_pest%name` | `character (len=16)` |  |  | [[constituent_mass_module.f90#rec_pest]] | [[recall_read.f90]]:260 |
| `rec_pest%typ` | `integer` |  | recall type - 1=day, 2=mon, 3=year | [[constituent_mass_module.f90#rec_pest]] | [[recall_read.f90]]:260 |
| `rec_pest%filename` | `character(len=13)` |  | filename hyd_output units are in cms and mg/L | [[constituent_mass_module.f90#rec_pest]] | [[recall_read.f90]]:260 |

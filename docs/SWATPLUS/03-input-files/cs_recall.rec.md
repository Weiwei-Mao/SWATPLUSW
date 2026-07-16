---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_recall.rec
ext: rec
cio_field: []
read_by:
  - recall_read_cs.f90
purpose: ""
---

# cs_recall.rec

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[recall_read_cs.f90]]

## File Structure
- [[recall_read_cs.f90]] source line 44: reads `titldum`
- [[recall_read_cs.f90]] source line 46: reads `header`
- [[recall_read_cs.f90]] source line 52: reads `i`
- [[recall_read_cs.f90]] source line 98: reads `titldum`
- [[recall_read_cs.f90]] source line 100: reads `header`
- [[recall_read_cs.f90]] source line 105: reads `i`
- [[recall_read_cs.f90]] source line 108: reads `k`, `rec_cs(i)%name`, `rec_cs(i)%typ`, `rec_cs(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `recall_read_cs.f90:31` | [[recall_read_cs.f90]]:52 |
| `k` | `integer` |  |  | `recall_read_cs.f90:26` | [[recall_read_cs.f90]]:108 |
| `rec_cs%name` | `character (len=16)` |  |  | [[constituent_mass_module.f90#rec_cs]] | [[recall_read_cs.f90]]:108 |
| `rec_cs%typ` | `integer` |  | recall type - 1=day, 2=mon, 3=year | [[constituent_mass_module.f90#rec_cs]] | [[recall_read_cs.f90]]:108 |
| `rec_cs%filename` | `character(len=30)` |  | filename | [[constituent_mass_module.f90#rec_cs]] | [[recall_read_cs.f90]]:108 |

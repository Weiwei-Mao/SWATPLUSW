---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: initial.cha_cs
ext: cha_cs
cio_field: []
read_by:
  - ch_read_init_cs.f90
purpose: ""
---

# initial.cha_cs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_init_cs.f90]]

## File Structure
- [[ch_read_init_cs.f90]] source line 28: reads `titldum`
- [[ch_read_init_cs.f90]] source line 30: reads `header`
- [[ch_read_init_cs.f90]] source line 33: reads `titldum`
- [[ch_read_init_cs.f90]] source line 42: reads `titldum`
- [[ch_read_init_cs.f90]] source line 44: reads `header`
- [[ch_read_init_cs.f90]] source line 48: reads `ch_init_cs(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ch_init_cs%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |
| `ch_init_cs%pest` | `character(len=16)` |  | points to initial pesticide input file | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |
| `ch_init_cs%path` | `character(len=16)` |  | points to initial pathogen input file | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |
| `ch_init_cs%hmet` | `character(len=16)` |  | points to initial heavy metals input file | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |
| `ch_init_cs%salt` | `character(len=16)` |  | points to initial salt input file | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |
| `ch_init_cs%cs` | `character(len=16)` |  | points to initial constituent input file | [[channel_data_module.f90#ch_init_cs]] | [[ch_read_init_cs.f90]]:48 |

---
type: input
tags:
  - swat/input
file: initial.cha
ext: cha
cio_field: init
read_by:
  - ch_read_init.f90
purpose: ""
---

# initial.cha

> [!info] Input File
> Declared in `file.cio` field `init`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `init`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_init.f90]]

## File Structure
- [[ch_read_init.f90]] source line 28: reads `titldum`
- [[ch_read_init.f90]] source line 30: reads `header`
- [[ch_read_init.f90]] source line 33: reads `titldum`
- [[ch_read_init.f90]] source line 43: reads `titldum`
- [[ch_read_init.f90]] source line 45: reads `header`
- [[ch_read_init.f90]] source line 49: reads `ch_init(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ch_init%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |
| `ch_init%org_min` | `character(len=16)` |  | points to initial organic-mineral input file | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |
| `ch_init%pest` | `character(len=16)` |  | points to initial pesticide input file | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |
| `ch_init%path` | `character(len=16)` |  | points to initial pathogen input file | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |
| `ch_init%hmet` | `character(len=16)` |  | points to initial heavy metals input file | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |
| `ch_init%salt` | `character(len=16)` |  | points to initial salt input file | [[channel_data_module.f90#ch_init]] | [[ch_read_init.f90]]:49 |

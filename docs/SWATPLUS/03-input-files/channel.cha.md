---
type: input
tags:
  - swat/input
file: channel.cha
ext: cha
cio_field: dat
read_by:
  - ch_read.f90
purpose: ""
---

# channel.cha

> [!info] Input File
> Declared in `file.cio` field `dat`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `dat`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read.f90]]

## File Structure
- [[ch_read.f90]] source line 39: reads `titldum`
- [[ch_read.f90]] source line 41: reads `header`
- [[ch_read.f90]] source line 44: reads `i`
- [[ch_read.f90]] source line 55: reads `titldum`
- [[ch_read.f90]] source line 57: reads `header`
- [[ch_read.f90]] source line 61: reads `i`
- [[ch_read.f90]] source line 64: reads `k`, `ch_dat_c(ichi)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | units | description | `ch_read.f90:19` | [[ch_read.f90]]:44 |
| `k` | `integer` | units | description | `ch_read.f90:23` | [[ch_read.f90]]:64 |
| `ch_dat_c%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_dat_c]] | [[ch_read.f90]]:64 |
| `ch_dat_c%init` | `character(len=16)` |  | points to initial_cha | [[channel_data_module.f90#ch_dat_c]] | [[ch_read.f90]]:64 |
| `ch_dat_c%hyd` | `character(len=16)` |  | points to hydrology.res for hydrology inputs | [[channel_data_module.f90#ch_dat_c]] | [[ch_read.f90]]:64 |
| `ch_dat_c%sed` | `character(len=16)` |  | sediment inputs-points to sediment.res | [[channel_data_module.f90#ch_dat_c]] | [[ch_read.f90]]:64 |
| `ch_dat_c%nut` | `character(len=16)` |  | nutrient inputs-points to nutrient.res | [[channel_data_module.f90#ch_dat_c]] | [[ch_read.f90]]:64 |

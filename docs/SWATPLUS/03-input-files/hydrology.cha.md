---
type: input
tags:
  - swat/input
file: hydrology.cha
ext: cha
cio_field: hyd
read_by:
  - ch_read_hyd.f90
purpose: ""
---

# hydrology.cha

> [!info] Input File
> Declared in `file.cio` field `hyd`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hyd`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_hyd.f90]]

## File Structure
- [[ch_read_hyd.f90]] source line 26: reads `titldum`
- [[ch_read_hyd.f90]] source line 28: reads `header`
- [[ch_read_hyd.f90]] source line 31: reads `titldum`
- [[ch_read_hyd.f90]] source line 40: reads `titldum`
- [[ch_read_hyd.f90]] source line 42: reads `header`
- [[ch_read_hyd.f90]] source line 46: reads `titldum`
- [[ch_read_hyd.f90]] source line 49: reads `ch_hyd(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ch_hyd%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%w` | `real` | m | average width of main channel | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%d` | `real` | m | average depth of main channel | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%s` | `real` | m/m | average slope of main channel | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%l` | `real` | km | main channel length in subbasin | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%n` | `real` | none | Manning"s "n" value for the main channel | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%k` | `real` | mm/hr | effective hydraulic conductivity of main channel alluvium | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%wdr` | `real` | m/m | channel width to depth ratio | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%alpha_bnk` | `real` | days | alpha factor for bank storage recession curve | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |
| `ch_hyd%side` | `real` |  | change in horizontal distance per unit | [[channel_data_module.f90#ch_hyd]] | [[ch_read_hyd.f90]]:49 |

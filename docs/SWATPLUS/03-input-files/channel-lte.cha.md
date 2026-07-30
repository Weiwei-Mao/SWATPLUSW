---
type: input
tags:
  - swat/input
file: channel-lte.cha
ext: cha
cio_field: chan_ez
read_by:
  - sd_channel_read.f90
purpose: ""
---

# channel-lte.cha

> [!info] Input File
> Declared in `file.cio` field `chan_ez`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `chan_ez`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sd_channel_read.f90]]

## File Structure
- [[sd_channel_read.f90]] source line 195: reads `titldum`
- [[sd_channel_read.f90]] source line 197: reads `header`
- [[sd_channel_read.f90]] source line 200: reads `i`
- [[sd_channel_read.f90]] source line 210: reads `titldum`
- [[sd_channel_read.f90]] source line 212: reads `header`
- [[sd_channel_read.f90]] source line 216: reads `i`
- [[sd_channel_read.f90]] source line 219: reads `k`, `sd_dat(i)%name`, `sd_dat(i)%initc`, `sd_dat(i)%hydc`, `sd_dat(i)%sedc`, `sd_dat(i)%nutc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` | none | counter | `sd_channel_read.f90:30` | [[sd_channel_read.f90]]:200 |
| `k` | `integer` | none | counter | `sd_channel_read.f90:31` | [[sd_channel_read.f90]]:219 |
| `sd_dat%name` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_dat]] | [[sd_channel_read.f90]]:219 |
| `sd_dat%initc` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_dat]] | [[sd_channel_read.f90]]:219 |
| `sd_dat%hydc` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_dat]] | [[sd_channel_read.f90]]:219 |
| `sd_dat%sedc` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_dat]] | [[sd_channel_read.f90]]:219 |
| `sd_dat%nutc` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_dat]] | [[sd_channel_read.f90]]:219 |

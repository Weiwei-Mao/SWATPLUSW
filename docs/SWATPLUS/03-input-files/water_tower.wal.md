---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: water_tower.wal
ext: wal
cio_field: []
read_by:
  - water_tower_read.f90
purpose: ""
---

# water_tower.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_tower_read.f90]]

## File Structure
- [[water_tower_read.f90]] source line 33: reads `titldum`
- [[water_tower_read.f90]] source line 35: reads `imax`
- [[water_tower_read.f90]] source line 36: reads `header`
- [[water_tower_read.f90]] source line 46: reads `header`
- [[water_tower_read.f90]] source line 48: reads `i`, `wtow(iwtow)%name`, `wtow(iwtow)%stor_mx`, `wtow(iwtow)%ddown_days`, `wtow(iwtow)%loss_fr`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_tower_read.f90:15` | [[water_tower_read.f90]]:35 |
| `i` | `integer` | none | counter | `water_tower_read.f90:17` | [[water_tower_read.f90]]:48 |
| `wtow%name` | `character (len=25)` |  | name of the water tower or pipe | [[water_allocation_module.f90#wtow]] | [[water_tower_read.f90]]:48 |
| `wtow%stor_mx` | `real` |  | m3 !maximum storage in plant | [[water_allocation_module.f90#wtow]] | [[water_tower_read.f90]]:48 |
| `wtow%ddown_days` | `real` |  | days !days to drawdown the storage to zero | [[water_allocation_module.f90#wtow]] | [[water_tower_read.f90]]:48 |
| `wtow%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#wtow]] | [[water_tower_read.f90]]:48 |

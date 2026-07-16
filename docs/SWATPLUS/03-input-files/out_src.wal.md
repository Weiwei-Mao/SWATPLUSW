---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: out_src.wal
ext: wal
cio_field: []
read_by:
  - water_osrc_read.f90
purpose: ""
---

# out_src.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_osrc_read.f90]]

## File Structure
- [[water_osrc_read.f90]] source line 35: reads `titldum`
- [[water_osrc_read.f90]] source line 37: reads `imax`
- [[water_osrc_read.f90]] source line 38: reads `header`
- [[water_osrc_read.f90]] source line 45: reads `i`, `osrc(isrc)%name`, `osrc(isrc)%stor_mx`, `osrc(isrc)%lag_days`, `osrc(isrc)%loss_fr`
- [[water_osrc_read.f90]] source line 53: reads `header`
- [[water_osrc_read.f90]] source line 54: reads `osrc_cs(isrc)%pest`
- [[water_osrc_read.f90]] source line 60: reads `header`
- [[water_osrc_read.f90]] source line 61: reads `osrc_cs(isrc)%path`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_osrc_read.f90:17` | [[water_osrc_read.f90]]:37 |
| `i` | `integer` | none | counter | `water_osrc_read.f90:19` | [[water_osrc_read.f90]]:45 |
| `osrc%name` | `character (len=25)` |  | name of outside basin source | [[water_allocation_module.f90#osrc]] | [[water_osrc_read.f90]]:45 |
| `osrc%stor_mx` | `real` |  | m3 !maximum storage in plant | [[water_allocation_module.f90#osrc]] | [[water_osrc_read.f90]]:45 |
| `osrc%lag_days` | `real` |  | days !treatement time - lag outflow | [[water_allocation_module.f90#osrc]] | [[water_osrc_read.f90]]:45 |
| `osrc%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#osrc]] | [[water_osrc_read.f90]]:45 |
| `osrc_cs%pest` | `real, dimension (:), allocatable` |  | pesticide (kg/ha) | [[constituent_mass_module.f90#osrc_cs]] | [[water_osrc_read.f90]]:54 |
| `osrc_cs%path` | `real, dimension (:), allocatable` |  | pathogen (cfu) | [[constituent_mass_module.f90#osrc_cs]] | [[water_osrc_read.f90]]:61 |

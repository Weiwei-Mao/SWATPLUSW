---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: water_use.wal
ext: wal
cio_field: []
read_by:
  - water_use_read.f90
purpose: ""
---

# water_use.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_use_read.f90]]

## File Structure
- [[water_use_read.f90]] source line 33: reads `titldum`
- [[water_use_read.f90]] source line 35: reads `imax`
- [[water_use_read.f90]] source line 36: reads `header`
- [[water_use_read.f90]] source line 50: reads `i`, `wuse(iwuse)%name`, `wuse(iwuse)%stor_mx`, `wuse(iwuse)%lag_days`, `wuse(iwuse)%loss_fr`, `wuse(iwuse)%org_min`, `wuse(iwuse)%pests`, `wuse(iwuse)%paths`, `wuse(iwuse)%salts`, `wuse(iwuse)%constit`, `wuse(iwuse)%descrip`
- [[water_use_read.f90]] source line 68: reads `header`
- [[water_use_read.f90]] source line 69: reads `wuse_cs_efflu(iwuse)%pest`
- [[water_use_read.f90]] source line 75: reads `header`
- [[water_use_read.f90]] source line 76: reads `wuse_cs_efflu(iwuse)%path`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_use_read.f90:16` | [[water_use_read.f90]]:35 |
| `i` | `integer` | none | counter | `water_use_read.f90:18` | [[water_use_read.f90]]:50 |
| `wuse%name` | `character (len=25)` |  | name of the water treatment plant | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%stor_mx` | `real` |  | m3 !maximum storage in plant | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%lag_days` | `real` |  | days !treatement time - lag outflow | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%org_min` | `character (len=25)` |  | sediment, carbon, and nutrients | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%pests` | `character (len=25)` |  | pesticides - ppm | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%paths` | `character (len=25)` |  | pathogens - cfu | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%salts` | `character (len=25)` |  | salt ions - ppm | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%constit` | `character (len=25)` |  | other constituents - ppm | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse%descrip` | `character (len=80)` |  | description | [[water_allocation_module.f90#wuse]] | [[water_use_read.f90]]:50 |
| `wuse_cs_efflu%pest` | `real, dimension (:), allocatable` |  | pesticide (kg/ha) | [[constituent_mass_module.f90#wuse_cs_efflu]] | [[water_use_read.f90]]:69 |
| `wuse_cs_efflu%path` | `real, dimension (:), allocatable` |  | pathogen (cfu) | [[constituent_mass_module.f90#wuse_cs_efflu]] | [[water_use_read.f90]]:76 |

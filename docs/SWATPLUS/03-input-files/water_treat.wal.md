---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: water_treat.wal
ext: wal
cio_field: []
read_by:
  - water_treatment_read.f90
purpose: ""
---

# water_treat.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_treatment_read.f90]]

## File Structure
- [[water_treatment_read.f90]] source line 32: reads `titldum`
- [[water_treatment_read.f90]] source line 34: reads `imax`
- [[water_treatment_read.f90]] source line 35: reads `header`
- [[water_treatment_read.f90]] source line 49: reads `i`, `wtp(iwtp)%name`, `wtp(iwtp)%stor_mx`, `wtp(iwtp)%lag_days`, `wtp(iwtp)%loss_fr`, `wtp(iwtp)%org_min`, `wtp(iwtp)%pests`, `wtp(iwtp)%paths`, `wtp(iwtp)%salts`, `wtp(iwtp)%constit`, `wtp(iwtp)%descrip`
- [[water_treatment_read.f90]] source line 67: reads `header`
- [[water_treatment_read.f90]] source line 68: reads `wtp_cs_treat(iwtp)%pest`
- [[water_treatment_read.f90]] source line 74: reads `header`
- [[water_treatment_read.f90]] source line 75: reads `wtp_cs_treat(iwtp)%path`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_treatment_read.f90:15` | [[water_treatment_read.f90]]:34 |
| `i` | `integer` | none | counter | `water_treatment_read.f90:17` | [[water_treatment_read.f90]]:49 |
| `wtp%name` | `character (len=25)` |  | name of the water treatment plant | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%stor_mx` | `real` |  | m3 !maximum storage in plant | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%lag_days` | `real` |  | days !treatement time - lag outflow | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%org_min` | `character (len=25)` |  | sediment, carbon, and nutrients | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%pests` | `character (len=25)` |  | pesticides - ppm | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%paths` | `character (len=25)` |  | pathogens - cfu | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%salts` | `character (len=25)` |  | salt ions - ppm | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%constit` | `character (len=25)` |  | other constituents - ppm | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp%descrip` | `character (len=80)` |  | description | [[water_allocation_module.f90#wtp]] | [[water_treatment_read.f90]]:49 |
| `wtp_cs_treat%pest` | `real, dimension (:), allocatable` |  | pesticide (kg/ha) | [[constituent_mass_module.f90#wtp_cs_treat]] | [[water_treatment_read.f90]]:68 |
| `wtp_cs_treat%path` | `real, dimension (:), allocatable` |  | pathogen (cfu) | [[constituent_mass_module.f90#wtp_cs_treat]] | [[water_treatment_read.f90]]:75 |

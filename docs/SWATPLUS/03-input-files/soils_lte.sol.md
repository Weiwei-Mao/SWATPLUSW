---
type: input
tags:
  - swat/input
file: soils_lte.sol
ext: sol
cio_field: lte_sol
read_by:
  - soil_lte_db_read.f90
purpose: ""
---

# soils_lte.sol

> [!info] Input File
> Declared in `file.cio` field `lte_sol`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `lte_sol`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[soil_lte_db_read.f90]]

## File Structure
- [[soil_lte_db_read.f90]] source line 27: reads `titldum`
- [[soil_lte_db_read.f90]] source line 29: reads `header`
- [[soil_lte_db_read.f90]] source line 35: reads `soil_lte(k)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `soil_lte%texture` | `character(len=16)` |  |  | [[soil_data_module.f90#soil_lte]] | [[soil_lte_db_read.f90]]:35 |
| `soil_lte%awc` | `real` |  |  | [[soil_data_module.f90#soil_lte]] | [[soil_lte_db_read.f90]]:35 |
| `soil_lte%por` | `real` |  |  | [[soil_data_module.f90#soil_lte]] | [[soil_lte_db_read.f90]]:35 |
| `soil_lte%scon` | `real` |  |  | [[soil_data_module.f90#soil_lte]] | [[soil_lte_db_read.f90]]:35 |

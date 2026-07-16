---
type: input
tags:
  - swat/input
file: nutrients.sol
ext: sol
cio_field: nut_sol
read_by:
  - solt_db_read.f90
purpose: ""
---

# nutrients.sol

> [!info] Input File
> Declared in `file.cio` field `nut_sol`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `nut_sol`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[solt_db_read.f90]]

## File Structure
- [[solt_db_read.f90]] source line 28: reads `titldum`
- [[solt_db_read.f90]] source line 30: reads `header`
- [[solt_db_read.f90]] source line 33: reads `titldum`
- [[solt_db_read.f90]] source line 41: reads `titldum`
- [[solt_db_read.f90]] source line 43: reads `header`
- [[solt_db_read.f90]] source line 47: reads `solt_db(isolt)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `solt_db%name` | `character(len=16)` |  |  | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%exp_co` | `real` |  | depth coefficient to adjust concentrations for depth | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%lab_p` | `real` | ppm | labile P in soil surface | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%nitrate` | `real` | ppm | nitrate N in soil surface | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%fr_hum_act` | `real` | 0-1 | fraction of soil humus that is active | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%hum_c_n` | `real` | ratio | humus C:N ratio (range 8-12) | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%hum_c_p` | `real` | ratio | humus C:P ratio (range 70-90) | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%inorgp` | `real` | ppm | inorganic P in soil surface - not currently used | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%watersol_p` | `real` | ppm | water soluble P in soil surface - not currently used | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%h3a_p` | `real` | ppm | h3a P in soil surface - not currently used | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%mehlich_p` | `real` | ppm | Mehlich P in soil surface - not currently used | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |
| `solt_db%bray_strong_p` | `real` | ppm | Bray P in soil surface - not currently used | [[soil_data_module.f90#solt_db]] | [[solt_db_read.f90]]:47 |

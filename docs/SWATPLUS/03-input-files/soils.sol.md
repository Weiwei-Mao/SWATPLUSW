---
type: input
tags:
  - swat/input
file: soils.sol
ext: sol
cio_field: soils_sol
read_by:
  - soil_db_read.f90
purpose: ""
---

# soils.sol

> [!info] Input File
> Declared in `file.cio` field `soils_sol`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `soils_sol`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[soil_db_read.f90]]

## File Structure
- [[soil_db_read.f90]] source line 30: reads `titldum`
- [[soil_db_read.f90]] source line 32: reads `header`
- [[soil_db_read.f90]] source line 37: reads `titldum`, `nlyr`
- [[soil_db_read.f90]] source line 40: reads `titldum`
- [[soil_db_read.f90]] source line 51: reads `titldum`
- [[soil_db_read.f90]] source line 53: reads `header`
- [[soil_db_read.f90]] source line 58: reads `soildb(isol)%s%snam`, `soildb(isol)%s%nly`
- [[soil_db_read.f90]] source line 65: reads `soildb(isol)%s%snam`, `soildb(isol)%s%nly`, `soildb(isol)%s%hydgrp`, `soildb(isol)%s%zmx`, `soildb(isol)%s%anion_excl`, `soildb(isol)%s%crk`, `soildb(isol)%s%texture`
- [[soil_db_read.f90]] source line 71: reads `soildb(isol)%ly(j)%z`, `soildb(isol)%ly(j)%bd`, `soildb(isol)%ly(j)%awc`, `soildb(isol)%ly(j)%k`, `soildb(isol)%ly(j)%cbn`, `soildb(isol)%ly(j)%clay`, `soildb(isol)%ly(j)%silt`, `soildb(isol)%ly(j)%sand`, `soildb(isol)%ly(j)%rock`, `soildb(isol)%ly(j)%alb`, `soildb(isol)%ly(j)%usle_k`, `soildb(isol)%ly(j)%ec`, `soildb(isol)%ly(j)%cal`, `soildb(isol)%ly(j)%ph`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `nlyr` | `integer` |  |  | `soil_db_read.f90:15` | [[soil_db_read.f90]]:37 |
| `soildb%s%snam` | `character(len=20)` | NA | soil series name | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:58 |
| `soildb%s%nly` | `integer` | none | number of soil layers | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:58 |
| `soildb%s%hydgrp` | `character(len=16)` | NA | hydrologic soil group | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:65 |
| `soildb%s%zmx` | `real` | mm | maximum rooting depth | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:65 |
| `soildb%s%anion_excl` | `real` | none | fraction of porosity from which anions are excluded | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:65 |
| `soildb%s%crk` | `real` | none | crack volume potential of soil | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:65 |
| `soildb%s%texture` | `character(len=16)` |  | texture of soil | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:65 |
| `soildb%ly%z` | `real` | mm | depth to bottom of soil layer | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%bd` | `real` | Mg/m**3 | bulk density of the soil | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%awc` | `real` | mm H20/mm soil | available water capacity of soil layer | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%k` | `real` | mm/hr | saturated hydraulic conductivity of soil layer. Index:(layer,HRU) | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%cbn` | `real` | % | percent organic carbon in soil layer | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%clay` | `real` | none | fraction clay content in soil material (UNIT CHANGE!) | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%silt` | `real` | % | percent silt content in soil material | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%sand` | `real` | none | fraction of sand in soil material | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%rock` | `real` | % | percent of rock fragments in soil layer | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%alb` | `real` | none | albedo when soil is moist | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%usle_k` | `real` |  | USLE equation soil erodibility (K) factor | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%ec` | `real` | dS/m | electrical conductivity of soil layer | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%cal` | `real` | % | soil CaCo3 | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |
| `soildb%ly%ph` | `real` |  | soil Ph | [[soil_data_module.f90#soildb]] | [[soil_db_read.f90]]:71 |

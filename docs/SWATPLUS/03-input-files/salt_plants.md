---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_plants
ext: 
cio_field: []
read_by:
  - salt_plant_read.f90
purpose: ""
---

# salt_plants

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_plant_read.f90]]

## File Structure
- [[salt_plant_read.f90]] source line 23: reads `titldum`
- [[salt_plant_read.f90]] source line 26: reads `header`
- [[salt_plant_read.f90]] source line 27: reads `salt_tds_ec`
- [[salt_plant_read.f90]] source line 30: reads (no targets parsed)
- [[salt_plant_read.f90]] source line 31: reads `salt_tol_sim`
- [[salt_plant_read.f90]] source line 32: reads `salt_soil_type`
- [[salt_plant_read.f90]] source line 33: reads `salt_effect`
- [[salt_plant_read.f90]] source line 34: reads (no targets parsed)
- [[salt_plant_read.f90]] source line 35: reads (no targets parsed)
- [[salt_plant_read.f90]] source line 36: reads (no targets parsed)
- [[salt_plant_read.f90]] source line 37: reads (no targets parsed)
- [[salt_plant_read.f90]] source line 38: reads `header`
- [[salt_plant_read.f90]] source line 42: reads `plant_name`, `salt_stress_a(iplant)`, `salt_stress_b(iplant)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `salt_tds_ec` | `real` |  | total dissolved solids to electrical conductivity conversion factor | [[salt_data_module.f90#salt_tds_ec]] | [[salt_plant_read.f90]]:27 |
| `salt_tol_sim` | `integer` |  | flag to simulate salt effect on plant growth | [[salt_data_module.f90#salt_tol_sim]] | [[salt_plant_read.f90]]:31 |
| `salt_soil_type` | `integer` |  | soil type (1 = CaSO4 soils; 2 = NaCl soils) | [[salt_data_module.f90#salt_soil_type]] | [[salt_plant_read.f90]]:32 |
| `salt_effect` | `integer` |  | 1 = applied after other stresses; 2 = included with other stresses (min) | [[salt_data_module.f90#salt_effect]] | [[salt_plant_read.f90]]:33 |
| `plant_name` | `character (len=12)` |  |  | `salt_plant_read.f90:12` | [[salt_plant_read.f90]]:42 |
| `salt_stress_a` | `real, dimension (:), allocatable` |  | a and b parameters in salinity relative yield equations | [[salt_data_module.f90#salt_stress_a]] | [[salt_plant_read.f90]]:42 |
| `salt_stress_b` | `real, dimension (:), allocatable` |  | a and b parameters in salinity relative yield equations | [[salt_data_module.f90#salt_stress_b]] | [[salt_plant_read.f90]]:42 |

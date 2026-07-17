---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_plants_boron
ext: 
cio_field: []
read_by:
  - cs_plant_read.f90
purpose: ""
---

# cs_plants_boron

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cs_plant_read.f90]]

## File Structure
- [[cs_plant_read.f90]] source line 23: reads `titldum`
- [[cs_plant_read.f90]] source line 26: reads (no targets parsed)
- [[cs_plant_read.f90]] source line 27: reads `bor_tol_sim`
- [[cs_plant_read.f90]] source line 28: reads `header`
- [[cs_plant_read.f90]] source line 29: reads `header`
- [[cs_plant_read.f90]] source line 30: reads `header`
- [[cs_plant_read.f90]] source line 31: reads `header`
- [[cs_plant_read.f90]] source line 35: reads `plant_name`, `bor_stress_a(iplant)`, `bor_stress_b(iplant)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `bor_tol_sim` | `integer` |  | flag to simulate boron effect on plant growth | [[cs_data_module.f90#bor_tol_sim]] | [[cs_plant_read.f90]]:27 |
| `plant_name` | `character (len=12)` |  |  | `cs_plant_read.f90:12` | [[cs_plant_read.f90]]:35 |
| `bor_stress_a` | `real, dimension (:), allocatable` |  | a and b parameters in boron relative yield equations | [[cs_data_module.f90#bor_stress_a]] | [[cs_plant_read.f90]]:35 |
| `bor_stress_b` | `real, dimension (:), allocatable` |  | a and b parameters in boron relative yield equations | [[cs_data_module.f90#bor_stress_b]] | [[cs_plant_read.f90]]:35 |

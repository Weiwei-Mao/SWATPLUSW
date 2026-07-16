---
type: input
tags:
  - swat/input
file: exco_pest.exc
ext: exc
cio_field: pest
read_by:
  - exco_read_pest.f90
purpose: ""
---

# exco_pest.exc

> [!info] Input File
> Declared in `file.cio` field `pest`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pest`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_read_pest.f90]]

## File Structure
- [[exco_read_pest.f90]] source line 32: reads `titldum`
- [[exco_read_pest.f90]] source line 34: reads `header`
- [[exco_read_pest.f90]] source line 38: reads `titldum`
- [[exco_read_pest.f90]] source line 52: reads `titldum`
- [[exco_read_pest.f90]] source line 54: reads `header`
- [[exco_read_pest.f90]] source line 59: reads `titldum`
- [[exco_read_pest.f90]] source line 62: reads `exco_pest_name(ii)`, `(exco_pest(ii)%pest(ipest), ipest = 1, cs_db%num_pests)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `exco_pest_name` | `character(len=16), dimension(:), allocatable` |  |  | [[exco_module.f90#exco_pest_name]] | [[exco_read_pest.f90]]:62 |
| `exco_pest%pest%num_pests` | `real, dimension (:), allocatable` |  | pesticide hydrographs | [[constituent_mass_module.f90#exco_pest]] | [[exco_read_pest.f90]]:62 |

---
type: input
tags:
  - swat/input
file: exco_hmet.exc
ext: exc
cio_field: hmet
read_by:
  - exco_read_hmet.f90
purpose: ""
---

# exco_hmet.exc

> [!info] Input File
> Declared in `file.cio` field `hmet`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hmet`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_read_hmet.f90]]

## File Structure
- [[exco_read_hmet.f90]] source line 33: reads `titldum`
- [[exco_read_hmet.f90]] source line 35: reads `header`
- [[exco_read_hmet.f90]] source line 39: reads `titldum`
- [[exco_read_hmet.f90]] source line 53: reads `titldum`
- [[exco_read_hmet.f90]] source line 55: reads `header`
- [[exco_read_hmet.f90]] source line 60: reads `titldum`
- [[exco_read_hmet.f90]] source line 63: reads `exco_hmet_name(ii)`, `(exco_hmet(ii)%hmet(ihmet), ihmet = 1, cs_db%num_metals)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `exco_hmet_name` | `character(len=16), dimension(:), allocatable` |  |  | [[exco_module.f90#exco_hmet_name]] | [[exco_read_hmet.f90]]:63 |
| `exco_hmet%hmet%num_metals` | `real, dimension (:), allocatable` |  | heavy metals hydrographs | [[constituent_mass_module.f90#exco_hmet]] | [[exco_read_hmet.f90]]:63 |

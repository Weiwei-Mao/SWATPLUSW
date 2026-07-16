---
type: input
tags:
  - swat/input
file: dr_hmet.del
ext: del
cio_field: hmet
read_by:
  - dr_read_hmet.f90
purpose: ""
---

# dr_hmet.del

> [!info] Input File
> Declared in `file.cio` field `hmet`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hmet`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_read_hmet.f90]]

## File Structure
- [[dr_read_hmet.f90]] source line 34: reads `titldum`
- [[dr_read_hmet.f90]] source line 36: reads `header`
- [[dr_read_hmet.f90]] source line 40: reads `titldum`
- [[dr_read_hmet.f90]] source line 54: reads `titldum`
- [[dr_read_hmet.f90]] source line 56: reads `header`
- [[dr_read_hmet.f90]] source line 61: reads `titldum`
- [[dr_read_hmet.f90]] source line 64: reads `dr_hmet_name(ii)`, `(dr_hmet(ii)%hmet(ihmet), ihmet = 1, cs_db%num_metals)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_hmet_name` | `character(len=16), dimension(:), allocatable` |  |  | [[dr_module.f90#dr_hmet_name]] | [[dr_read_hmet.f90]]:64 |
| `dr_hmet%hmet%num_metals` | `real, dimension (:), allocatable` |  | heavy metals delivery | [[constituent_mass_module.f90#dr_hmet]] | [[dr_read_hmet.f90]]:64 |

---
type: input
tags:
  - swat/input
file: exco_path.exc
ext: exc
cio_field: path
read_by:
  - exco_read_path.f90
purpose: ""
---

# exco_path.exc

> [!info] Input File
> Declared in `file.cio` field `path`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `path`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_read_path.f90]]

## File Structure
- [[exco_read_path.f90]] source line 33: reads `titldum`
- [[exco_read_path.f90]] source line 35: reads `header`
- [[exco_read_path.f90]] source line 39: reads `titldum`
- [[exco_read_path.f90]] source line 53: reads `titldum`
- [[exco_read_path.f90]] source line 55: reads `header`
- [[exco_read_path.f90]] source line 60: reads `titldum`
- [[exco_read_path.f90]] source line 63: reads `exco_path_name(ii)`, `(exco_path(ii)%path(ipath), ipath = 1, cs_db%num_paths)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `exco_path_name` | `character(len=16), dimension(:), allocatable` |  |  | [[exco_module.f90#exco_path_name]] | [[exco_read_path.f90]]:63 |
| `exco_path%path%num_paths` | `real, dimension (:), allocatable` |  | pesticide hydrographs | [[constituent_mass_module.f90#exco_path]] | [[exco_read_path.f90]]:63 |

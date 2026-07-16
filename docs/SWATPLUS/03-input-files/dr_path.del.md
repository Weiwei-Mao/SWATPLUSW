---
type: input
tags:
  - swat/input
file: dr_path.del
ext: del
cio_field: path
read_by:
  - dr_path_read.f90
purpose: ""
---

# dr_path.del

> [!info] Input File
> Declared in `file.cio` field `path`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `path`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_path_read.f90]]

## File Structure
- [[dr_path_read.f90]] source line 33: reads `titldum`
- [[dr_path_read.f90]] source line 35: reads `header`
- [[dr_path_read.f90]] source line 39: reads `titldum`
- [[dr_path_read.f90]] source line 53: reads `titldum`
- [[dr_path_read.f90]] source line 55: reads `header`
- [[dr_path_read.f90]] source line 60: reads `titldum`
- [[dr_path_read.f90]] source line 63: reads `dr_path_name(ii)`, `(dr_path(ii)%path(ipath), ipath = 1, cs_db%num_paths)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_path_name` | `character(len=16), dimension(:), allocatable` |  |  | [[dr_module.f90#dr_path_name]] | [[dr_path_read.f90]]:63 |
| `dr_path%path%num_paths` | `real, dimension (:), allocatable` |  | pathogen delivery | [[constituent_mass_module.f90#dr_path]] | [[dr_path_read.f90]]:63 |

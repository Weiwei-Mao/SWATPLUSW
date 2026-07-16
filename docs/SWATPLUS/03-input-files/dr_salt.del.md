---
type: input
tags:
  - swat/input
file: dr_salt.del
ext: del
cio_field: salt
read_by:
  - dr_read_salt.f90
purpose: ""
---

# dr_salt.del

> [!info] Input File
> Declared in `file.cio` field `salt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `salt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[dr_read_salt.f90]]

## File Structure
- [[dr_read_salt.f90]] source line 33: reads `titldum`
- [[dr_read_salt.f90]] source line 35: reads `header`
- [[dr_read_salt.f90]] source line 39: reads `titldum`
- [[dr_read_salt.f90]] source line 53: reads `titldum`
- [[dr_read_salt.f90]] source line 55: reads `header`
- [[dr_read_salt.f90]] source line 60: reads `titldum`
- [[dr_read_salt.f90]] source line 63: reads `dr_salt_name(ii)`, `(dr_salt(ii)%salt(isalt), isalt = 1, cs_db%num_salts)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `dr_salt_name` | `character(len=16), dimension(:), allocatable` |  |  | [[dr_module.f90#dr_salt_name]] | [[dr_read_salt.f90]]:63 |
| `dr_salt%salt%num_salts` | `real, dimension (:), allocatable` |  | salts delivery | [[constituent_mass_module.f90#dr_salt]] | [[dr_read_salt.f90]]:63 |

---
type: input
tags:
  - swat/input
file: exco_salt.exc
ext: exc
cio_field: salt
read_by:
  - exco_read_salt.f90
purpose: ""
---

# exco_salt.exc

> [!info] Input File
> Declared in `file.cio` field `salt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `salt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[exco_read_salt.f90]]

## File Structure
- [[exco_read_salt.f90]] source line 33: reads `titldum`
- [[exco_read_salt.f90]] source line 35: reads `header`
- [[exco_read_salt.f90]] source line 39: reads `titldum`
- [[exco_read_salt.f90]] source line 53: reads `titldum`
- [[exco_read_salt.f90]] source line 55: reads `header`
- [[exco_read_salt.f90]] source line 60: reads `titldum`
- [[exco_read_salt.f90]] source line 63: reads `exco_salt_name(ii)`, `(exco_salt(ii)%salt(isalt), isalt = 1, cs_db%num_salts)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `exco_salt_name` | `character(len=16), dimension(:), allocatable` |  |  | [[exco_module.f90#exco_salt_name]] | [[exco_read_salt.f90]]:63 |
| `exco_salt%salt%num_salts` | `real, dimension (:), allocatable` |  | salts hydrographs | [[constituent_mass_module.f90#exco_salt]] | [[exco_read_salt.f90]]:63 |

---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_aqu.ini
ext: ini
cio_field: []
read_by:
  - salt_aqu_read.f90
purpose: ""
---

# salt_aqu.ini

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_aqu_read.f90]]

## File Structure
- [[salt_aqu_read.f90]] source line 24: reads `titldum`
- [[salt_aqu_read.f90]] source line 26: reads `header`
- [[salt_aqu_read.f90]] source line 28: reads `header`
- [[salt_aqu_read.f90]] source line 30: reads `header`
- [[salt_aqu_read.f90]] source line 35: reads `titldum`
- [[salt_aqu_read.f90]] source line 53: reads `titldum`
- [[salt_aqu_read.f90]] source line 55: reads `header`
- [[salt_aqu_read.f90]] source line 57: reads `header`
- [[salt_aqu_read.f90]] source line 59: reads `header`
- [[salt_aqu_read.f90]] source line 63: reads `salt_aqu_ini(isalt)%name`, `salt_aqu_ini(isalt)%conc`, `salt_aqu_ini(isalt)%frac`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `salt_aqu_ini%name` | `character (len=16)` |  | name of the constituent - points to constituent database | [[constituent_mass_module.f90#salt_aqu_ini]] | [[salt_aqu_read.f90]]:63 |
| `salt_aqu_ini%conc` | `real, dimension (:), allocatable` | g/m3 | salt ion concentration at start of simulation | [[constituent_mass_module.f90#salt_aqu_ini]] | [[salt_aqu_read.f90]]:63 |
| `salt_aqu_ini%frac` | `real, dimension (:), allocatable` | fractions | salt mineral fractions at start of simulation | [[constituent_mass_module.f90#salt_aqu_ini]] | [[salt_aqu_read.f90]]:63 |

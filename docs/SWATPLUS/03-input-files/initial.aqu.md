---
type: input
tags:
  - swat/input
file: initial.aqu
ext: aqu
cio_field: init
read_by:
  - aqu_read_init.f90
purpose: ""
---

# initial.aqu

> [!info] Input File
> Declared in `file.cio` field `init`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `init`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu_read_init.f90]]

## File Structure
- [[aqu_read_init.f90]] source line 33: reads `titldum`
- [[aqu_read_init.f90]] source line 35: reads `header`
- [[aqu_read_init.f90]] source line 38: reads `titldum`
- [[aqu_read_init.f90]] source line 47: reads `titldum`
- [[aqu_read_init.f90]] source line 49: reads `header`
- [[aqu_read_init.f90]] source line 53: reads `aqu_init_dat_c(iaqu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `aqu_init_dat_c%name` | `character (len=16)` |  | xwalk with aqudb(iaqu)%aqu_ini | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |
| `aqu_init_dat_c%org_min` | `character (len=16)` |  | points to initial organic-mineral input file | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |
| `aqu_init_dat_c%pest` | `character (len=16)` |  | points to initial pesticide input file | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |
| `aqu_init_dat_c%path` | `character (len=16)` |  | points to initial pathogen input file | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |
| `aqu_init_dat_c%hmet` | `character (len=16)` |  | points to initial heavy metals input file | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |
| `aqu_init_dat_c%salt` | `character (len=16)` |  | points to initial salt input file | [[aquifer_module.f90#aqu_init_dat_c]] | [[aqu_read_init.f90]]:53 |

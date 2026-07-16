---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: initial.aqu_cs
ext: aqu_cs
cio_field: []
read_by:
  - aqu_read_init_cs.f90
purpose: ""
---

# initial.aqu_cs

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[aqu_read_init_cs.f90]]

## File Structure
- [[aqu_read_init_cs.f90]] source line 43: reads `titldum`
- [[aqu_read_init_cs.f90]] source line 45: reads `header`
- [[aqu_read_init_cs.f90]] source line 48: reads `titldum`
- [[aqu_read_init_cs.f90]] source line 58: reads `titldum`
- [[aqu_read_init_cs.f90]] source line 60: reads `header`
- [[aqu_read_init_cs.f90]] source line 63: reads `aqu_init_dat_c_cs(iaqu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `aqu_init_dat_c_cs%name` | `character (len=16)` |  | xwalk with aqudb(iaqu)%aqu_ini | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |
| `aqu_init_dat_c_cs%pest` | `character (len=16)` |  | points to initial pesticide input file | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |
| `aqu_init_dat_c_cs%path` | `character (len=16)` |  | points to initial pathogen input file | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |
| `aqu_init_dat_c_cs%hmet` | `character (len=16)` |  | points to initial heavy metals input file | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |
| `aqu_init_dat_c_cs%salt` | `character (len=16)` |  | points to initial salt input file (salt_aqu.ini) | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |
| `aqu_init_dat_c_cs%cs` | `character (len=16)` |  | points to initial constituent input file (cs_aqu.ini) | [[aquifer_module.f90#aqu_init_dat_c_cs]] | [[aqu_read_init_cs.f90]]:63 |

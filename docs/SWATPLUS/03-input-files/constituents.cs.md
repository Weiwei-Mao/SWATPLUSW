---
type: input
tags:
  - swat/input
file: constituents.cs
ext: cs
cio_field: cs_db
read_by:
  - constit_db_read.f90
purpose: ""
---

# constituents.cs

> [!info] Input File
> Declared in `file.cio` field `cs_db`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `cs_db`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[constit_db_read.f90]]

## File Structure
- [[constit_db_read.f90]] source line 34: reads `titldum`
- [[constit_db_read.f90]] source line 36: reads `cs_db%num_pests`
- [[constit_db_read.f90]] source line 40: reads `(cs_db%pests(i), i = 1, cs_db%num_pests)`
- [[constit_db_read.f90]] source line 42: reads `cs_db%num_paths`
- [[constit_db_read.f90]] source line 46: reads `(cs_db%paths(i), i = 1, cs_db%num_paths)`
- [[constit_db_read.f90]] source line 48: reads `cs_db%num_metals`
- [[constit_db_read.f90]] source line 52: reads `(cs_db%metals(i), i = 1, cs_db%num_metals)`
- [[constit_db_read.f90]] source line 55: reads `cs_db%num_salts`
- [[constit_db_read.f90]] source line 59: reads `(cs_db%salts(i), i = 1, cs_db%num_salts)`
- [[constit_db_read.f90]] source line 61: reads `cs_db%num_cs`
- [[constit_db_read.f90]] source line 65: reads `(cs_db%cs(i), i = 1, cs_db%num_cs)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `cs_db%num_pests` | `integer` |  | number of pesticides simulated | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:36 |
| `cs_db%pests%num_pests` | `character (len=16), dimension(:), allocatable` |  | name of the pesticides- points to pesticide database need to crosswalk pests to get pest_num for database - use sequential for object | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:40 |
| `cs_db%num_paths` | `integer` |  | number of pathogens simulated | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:42 |
| `cs_db%paths%num_paths` | `character (len=16), dimension(:), allocatable` |  | name of the pathogens- points to pathogens database | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:46 |
| `cs_db%num_metals` | `integer` |  | number of heavy metals simulated | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:48 |
| `cs_db%metals%num_metals` | `character (len=16), dimension(:), allocatable` |  | name of the heavy metals- points to heavy metals database | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:52 |
| `cs_db%num_salts` | `integer` |  | number of salt ions simulated | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:55 |
| `cs_db%salts%num_salts` | `character (len=16), dimension(:), allocatable` |  | name of the salts - points to salts database | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:59 |
| `cs_db%num_cs` | `integer` |  | number of other constituents simulated | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:61 |
| `cs_db%cs%num_cs` | `character (len=16), dimension(:), allocatable` |  | name of the constituents - points to cs database | [[constituent_mass_module.f90#cs_db]] | [[constit_db_read.f90]]:65 |

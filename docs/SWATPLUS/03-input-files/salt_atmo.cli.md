---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_atmo.cli
ext: cli
cio_field: []
read_by:
  - cli_read_atmodep_salt.f90
purpose: ""
---

# salt_atmo.cli

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_read_atmodep_salt.f90]]

## File Structure
- [[cli_read_atmodep_salt.f90]] source line 34: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 35: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 36: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 37: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 38: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 39: reads (no targets parsed)
- [[cli_read_atmodep_salt.f90]] source line 52: reads `station_name`
- [[cli_read_atmodep_salt.f90]] source line 55: reads `salt_ion`, `atmodep_salt(iadep)%salt(isalt)%rf`
- [[cli_read_atmodep_salt.f90]] source line 59: reads `salt_ion`, `atmodep_salt(iadep)%salt(isalt)%dry`
- [[cli_read_atmodep_salt.f90]] source line 65: reads `station_name`
- [[cli_read_atmodep_salt.f90]] source line 68: reads `salt_ion`, `(atmodep_salt(iadep)%salt(isalt)%rfmo(imo),imo=1,atmodep_cont%num)`
- [[cli_read_atmodep_salt.f90]] source line 72: reads `salt_ion`, `(atmodep_salt(iadep)%salt(isalt)%drymo(imo),imo=1,atmodep_cont%num)`
- [[cli_read_atmodep_salt.f90]] source line 78: reads `station_name`
- [[cli_read_atmodep_salt.f90]] source line 81: reads `salt_ion`, `(atmodep_salt(iadep)%salt(isalt)%rfyr(iyr),iyr=1,atmodep_cont%num)`
- [[cli_read_atmodep_salt.f90]] source line 85: reads `salt_ion`, `(atmodep_salt(iadep)%salt(isalt)%dryyr(iyr),iyr=1,atmodep_cont%num)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `station_name` | `character (len=15)` |  |  | `cli_read_atmodep_salt.f90:15` | [[cli_read_atmodep_salt.f90]]:52 |
| `salt_ion` | `character (len=4)` |  |  | `cli_read_atmodep_salt.f90:14` | [[cli_read_atmodep_salt.f90]]:55 |
| `atmodep_salt%salt%rf` | `real` |  | concentration in rainfall - mg/l | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:55 |
| `atmodep_salt%salt%dry` | `real` |  | dry deposition - kg/ha/yr | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:59 |
| `atmodep_salt%salt%rfmo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:68 |
| `atmodep_salt%salt%drymo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:72 |
| `atmodep_salt%salt%rfyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:81 |
| `atmodep_salt%salt%dryyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_salt]] | [[cli_read_atmodep_salt.f90]]:85 |

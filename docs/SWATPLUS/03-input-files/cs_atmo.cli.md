---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: cs_atmo.cli
ext: cli
cio_field: []
read_by:
  - cli_read_atmodep_cs.f90
purpose: ""
---

# cs_atmo.cli

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_read_atmodep_cs.f90]]

## File Structure
- [[cli_read_atmodep_cs.f90]] source line 33: reads (no targets parsed)
- [[cli_read_atmodep_cs.f90]] source line 34: reads (no targets parsed)
- [[cli_read_atmodep_cs.f90]] source line 35: reads (no targets parsed)
- [[cli_read_atmodep_cs.f90]] source line 48: reads `station_name`
- [[cli_read_atmodep_cs.f90]] source line 51: reads `atmodep_cs(iadep)%cs(ics)%rf`
- [[cli_read_atmodep_cs.f90]] source line 55: reads `atmodep_cs(iadep)%cs(ics)%dry`
- [[cli_read_atmodep_cs.f90]] source line 61: reads `station_name`
- [[cli_read_atmodep_cs.f90]] source line 67: reads `(atmodep_cs(iadep)%cs(ics)%rfmo(imo),imo=1,atmodep_cont%num)`
- [[cli_read_atmodep_cs.f90]] source line 74: reads `(atmodep_cs(iadep)%cs(ics)%drymo(imo),imo=1,atmodep_cont%num)`
- [[cli_read_atmodep_cs.f90]] source line 80: reads `station_name`
- [[cli_read_atmodep_cs.f90]] source line 86: reads `(atmodep_cs(iadep)%cs(ics)%rfyr(iyr),iyr=1,atmodep_cont%num)`
- [[cli_read_atmodep_cs.f90]] source line 93: reads `(atmodep_cs(iadep)%cs(ics)%dryyr(iyr),iyr=1,atmodep_cont%num)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `station_name` | `real` |  |  | `cli_read_atmodep_cs.f90:20` | [[cli_read_atmodep_cs.f90]]:48 |
| `atmodep_cs%cs%rf` | `real` |  | concentration in rainfall - mg/l | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:51 |
| `atmodep_cs%cs%dry` | `real` |  | dry deposition - kg/ha/yr | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:55 |
| `atmodep_cs%cs%rfmo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:67 |
| `atmodep_cs%cs%drymo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:74 |
| `atmodep_cs%cs%rfyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:86 |
| `atmodep_cs%cs%dryyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep_cs]] | [[cli_read_atmodep_cs.f90]]:93 |

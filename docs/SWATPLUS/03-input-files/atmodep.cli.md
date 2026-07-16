---
type: input
tags:
  - swat/input
file: atmodep.cli
ext: cli
cio_field: atmo_cli
read_by:
  - cli_read_atmodep.f90
purpose: ""
---

# atmodep.cli

> [!info] Input File
> Declared in `file.cio` field `atmo_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `atmo_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_read_atmodep.f90]]

## File Structure
- [[cli_read_atmodep.f90]] source line 32: reads `titldum`
- [[cli_read_atmodep.f90]] source line 34: reads `header`
- [[cli_read_atmodep.f90]] source line 36: reads `atmodep_cont%num_sta`, `atmodep_cont%timestep`, `atmodep_cont%mo_init`, `atmodep_cont%yr_init`, `atmodep_cont%num`
- [[cli_read_atmodep.f90]] source line 74: reads `atmodep(iadep)%name`
- [[cli_read_atmodep.f90]] source line 77: reads `atmodep(iadep)%nh4_rf`
- [[cli_read_atmodep.f90]] source line 79: reads `atmodep(iadep)%no3_rf`
- [[cli_read_atmodep.f90]] source line 81: reads `atmodep(iadep)%nh4_dry`
- [[cli_read_atmodep.f90]] source line 83: reads `atmodep(iadep)%no3_dry`
- [[cli_read_atmodep.f90]] source line 92: reads `atmodep(iadep)%name`
- [[cli_read_atmodep.f90]] source line 95: reads `(atmodep(iadep)%nh4_rfmo(imo), imo = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 97: reads `(atmodep(iadep)%no3_rfmo(imo), imo = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 99: reads `(atmodep(iadep)%nh4_drymo(imo),imo = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 101: reads `(atmodep(iadep)%no3_drymo(imo),imo = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 110: reads `atmodep(iadep)%name`
- [[cli_read_atmodep.f90]] source line 113: reads `(atmodep(iadep)%nh4_rfyr(iyr), iyr = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 115: reads `(atmodep(iadep)%no3_rfyr(iyr), iyr = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 117: reads `(atmodep(iadep)%nh4_dryyr(iyr),iyr = 1,atmodep_cont%num)`
- [[cli_read_atmodep.f90]] source line 119: reads `(atmodep(iadep)%no3_dryyr(iyr),iyr = 1,atmodep_cont%num)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `atmodep_cont%num_sta` | `integer` |  |  | [[climate_module.f90#atmodep_cont]] | [[cli_read_atmodep.f90]]:36 |
| `atmodep_cont%timestep` | `character(len=2)` |  |  | [[climate_module.f90#atmodep_cont]] | [[cli_read_atmodep.f90]]:36 |
| `atmodep_cont%mo_init` | `integer` |  |  | [[climate_module.f90#atmodep_cont]] | [[cli_read_atmodep.f90]]:36 |
| `atmodep_cont%yr_init` | `integer` |  |  | [[climate_module.f90#atmodep_cont]] | [[cli_read_atmodep.f90]]:36 |
| `atmodep_cont%num` | `integer` |  |  | [[climate_module.f90#atmodep_cont]] | [[cli_read_atmodep.f90]]:36 |
| `atmodep%name` | `character(len=50)` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:74 |
| `atmodep%nh4_rf` | `real` |  | ave annual ammonia in rainfall - mg/l | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:77 |
| `atmodep%no3_rf` | `real` |  | ave annual nitrate in rainfall - mg/l | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:79 |
| `atmodep%nh4_dry` | `real` |  | ave annual ammonia dry deposition - kg/ha/yr | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:81 |
| `atmodep%no3_dry` | `real` |  | ave annual nitrate dry deposition - kg/ha/yr | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:83 |
| `atmodep%nh4_rfmo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:95 |
| `atmodep%no3_rfmo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:97 |
| `atmodep%nh4_drymo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:99 |
| `atmodep%no3_drymo%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:101 |
| `atmodep%nh4_rfyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:113 |
| `atmodep%no3_rfyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:115 |
| `atmodep%nh4_dryyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:117 |
| `atmodep%no3_dryyr%num` | `real, dimension(:), allocatable` |  |  | [[climate_module.f90#atmodep]] | [[cli_read_atmodep.f90]]:119 |

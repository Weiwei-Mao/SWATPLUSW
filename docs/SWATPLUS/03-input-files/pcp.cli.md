---
type: input
tags:
  - swat/input
file: pcp.cli
ext: cli
cio_field: pcp_cli
read_by:
  - cli_pmeas.f90
purpose: ""
---

# pcp.cli

> [!info] Input File
> Declared in `file.cio` field `pcp_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pcp_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_pmeas.f90]]

## File Structure
- [[cli_pmeas.f90]] source line 39: reads `titldum`
- [[cli_pmeas.f90]] source line 41: reads `header`
- [[cli_pmeas.f90]] source line 44: reads `titldum`
- [[cli_pmeas.f90]] source line 53: reads `titldum`
- [[cli_pmeas.f90]] source line 55: reads `header`
- [[cli_pmeas.f90]] source line 58: reads `pcp_n(i)`
- [[cli_pmeas.f90]] source line 63: reads `titldum`
- [[cli_pmeas.f90]] source line 65: reads `header`
- [[cli_pmeas.f90]] source line 69: reads `pcp(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pcp_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#pcp_n]] | [[cli_pmeas.f90]]:58 |
| `pcp%filename` | `character (len=50)` |  |  | [[climate_module.f90#pcp]] | [[cli_pmeas.f90]]:69 |

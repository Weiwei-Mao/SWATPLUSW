---
type: input
tags:
  - swat/input
file: hmd.cli
ext: cli
cio_field: hmd_cli
read_by:
  - cli_hmeas.f90
purpose: ""
---

# hmd.cli

> [!info] Input File
> Declared in `file.cio` field `hmd_cli`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hmd_cli`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[cli_hmeas.f90]]

## File Structure
- [[cli_hmeas.f90]] source line 32: reads `titldum`
- [[cli_hmeas.f90]] source line 34: reads `header`
- [[cli_hmeas.f90]] source line 37: reads `titldum`
- [[cli_hmeas.f90]] source line 46: reads `titldum`
- [[cli_hmeas.f90]] source line 48: reads `header`
- [[cli_hmeas.f90]] source line 51: reads `hmd_n(i)`
- [[cli_hmeas.f90]] source line 56: reads `titldum`
- [[cli_hmeas.f90]] source line 58: reads `header`
- [[cli_hmeas.f90]] source line 62: reads `hmd(i)%filename`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `hmd_n` | `character(len=50), dimension(:), allocatable` |  |  | [[climate_module.f90#hmd_n]] | [[cli_hmeas.f90]]:51 |
| `hmd%filename` | `character (len=50)` |  |  | [[climate_module.f90#hmd]] | [[cli_hmeas.f90]]:62 |

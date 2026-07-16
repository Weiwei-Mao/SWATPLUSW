---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: soil_lyr_depths.sol
ext: sol
cio_field: []
read_by:
  - soils_init.f90
purpose: ""
---

# soil_lyr_depths.sol

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[soils_init.f90]]

## File Structure
- [[soils_init.f90]] source line 167: reads `titldum`
- [[soils_init.f90]] source line 169: reads `header`
- [[soils_init.f90]] source line 171: reads `units`
- [[soils_init.f90]] source line 175: reads `csld`
- [[soils_init.f90]] source line 204: reads `titldum`
- [[soils_init.f90]] source line 205: reads `header`
- [[soils_init.f90]] source line 206: reads `units`
- [[soils_init.f90]] source line 212: reads `csld`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `units` | `character (len=16)` |  | name | `soils_init.f90:52` | [[soils_init.f90]]:171 |
| `csld` | `integer` | mm | current custom soil layer depth in millimeters | `soils_init.f90:28` | [[soils_init.f90]]:175 |

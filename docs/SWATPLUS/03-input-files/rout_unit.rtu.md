---
type: input
tags:
  - swat/input
file: rout_unit.rtu
ext: rtu
cio_field: ru
read_by:
  - ru_read.f90
purpose: ""
---

# rout_unit.rtu

> [!info] Input File
> Declared in `file.cio` field `ru`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ru`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ru_read.f90]]

## File Structure
- [[ru_read.f90]] source line 40: reads `titldum`
- [[ru_read.f90]] source line 42: reads `header`
- [[ru_read.f90]] source line 45: reads `i`
- [[ru_read.f90]] source line 220: reads `titldum`
- [[ru_read.f90]] source line 222: reads `header`
- [[ru_read.f90]] source line 227: reads `i`
- [[ru_read.f90]] source line 230: reads `k`, `ru(i)%name`, `ru(i)%dbsc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `ru_read.f90:22` | [[ru_read.f90]]:45 |
| `k` | `integer` |  |  | `ru_read.f90:24` | [[ru_read.f90]]:230 |
| `ru%name` | `character(len=16)` |  |  | [[ru_module.f90#ru]] | [[ru_read.f90]]:230 |
| `ru%dbsc` | `ru_databases_char` |  |  | [[ru_module.f90#ru]] | [[ru_read.f90]]:230 |

---
type: input
tags:
  - swat/input
file: hru-data.hru
ext: hru
cio_field: hru_data
read_by:
  - hru_read.f90
purpose: ""
---

# hru-data.hru

> [!info] Input File
> Declared in `file.cio` field `hru_data`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hru_data`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[hru_read.f90]]

## File Structure
- [[hru_read.f90]] source line 45: reads `titldum`
- [[hru_read.f90]] source line 47: reads `header`
- [[hru_read.f90]] source line 50: reads `i`
- [[hru_read.f90]] source line 58: reads `titldum`
- [[hru_read.f90]] source line 60: reads `header`
- [[hru_read.f90]] source line 64: reads `i`
- [[hru_read.f90]] source line 67: reads `k`, `hru_db(i)%dbsc`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `i` | `integer` |  |  | `hru_read.f90:22` | [[hru_read.f90]]:50 |
| `k` | `integer` |  |  | `hru_read.f90:24` | [[hru_read.f90]]:67 |
| `hru_db%dbsc` | `hru_databases_char` |  |  | [[hru_module.f90#hru_db]] | [[hru_read.f90]]:67 |

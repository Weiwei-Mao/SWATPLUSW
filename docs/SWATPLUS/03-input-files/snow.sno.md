---
type: input
tags:
  - swat/input
file: snow.sno
ext: sno
cio_field: snow
read_by:
  - snowdb_read.f90
purpose: ""
---

# snow.sno

> [!info] Input File
> Declared in `file.cio` field `snow`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `snow`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[snowdb_read.f90]]

## File Structure
- [[snowdb_read.f90]] source line 29: reads `titldum`
- [[snowdb_read.f90]] source line 31: reads `header`
- [[snowdb_read.f90]] source line 34: reads `titldum`
- [[snowdb_read.f90]] source line 40: reads `titldum`
- [[snowdb_read.f90]] source line 42: reads `header`
- [[snowdb_read.f90]] source line 48: reads `snodb(isno)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `snodb%name` | `character (len=40)` |  |  | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%falltmp` | `real` | deg C | snowfall temp | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%melttmp` | `real` | deg C | snow melt base temp | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%meltmx` | `real` | mm/deg C/day | Max melt rate for snow during year (June 21) | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%meltmn` | `real` | mm/deg C/day | Min melt rate for snow during year (Dec 21) | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%timp` | `real` | none | snow pack temp lag factor (0-1) | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%covmx` | `real` | mm H20 | snow water content at full ground cover | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%cov50` | `real` | none | frac of covmx at 50% snow cover | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |
| `snodb%init_mm` | `real` | mm H20 | initial snow water content at start of simulation | [[hru_module.f90#snodb]] | [[snowdb_read.f90]]:48 |

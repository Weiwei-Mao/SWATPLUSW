---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: co2_yr.dat
ext: dat
cio_field: []
read_by:
  - co2_read.f90
purpose: ""
---

# co2_yr.dat

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[co2_read.f90]]

## File Structure
- [[co2_read.f90]] source line 47: reads `titldum`
- [[co2_read.f90]] source line 49: reads `co2_inc%yrs`
- [[co2_read.f90]] source line 51: reads `header`
- [[co2_read.f90]] source line 57: reads `co2_inc%co2_yr(itot)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `co2_inc%yrs` | `` |  |  | `co2_read.f90:32` | [[co2_read.f90]]:49 |
| `co2_inc%co2_yr` | `` |  |  | `co2_read.f90:32` | [[co2_read.f90]]:57 |

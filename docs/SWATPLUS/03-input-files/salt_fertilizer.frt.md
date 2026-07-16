---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: salt_fertilizer.frt
ext: frt
cio_field: []
read_by:
  - salt_fert_read.f90
purpose: ""
---

# salt_fertilizer.frt

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[salt_fert_read.f90]]

## File Structure
- [[salt_fert_read.f90]] source line 25: reads `titldum`
- [[salt_fert_read.f90]] source line 26: reads `header`
- [[salt_fert_read.f90]] source line 36: reads `fert_salt(isalti)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `fert_salt%fertnm` | `character(len=16)` |  |  | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%so4` | `real` | kg so4/ha | fertilizer load of so4 (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%ca` | `real` | kg ca/ha | fertilizer load of ca (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%mg` | `real` | kg mg/ha | fertilizer load of mg (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%na` | `real` | kg na/ha | fertilizer load of na (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%k` | `real` | kg k/ha | fertilizer load of k (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%cl` | `real` | kg cl/ha | fertilizer load of cl (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%co3` | `real` | kg co3/ha | fertilizer load of co3 (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |
| `fert_salt%hco3` | `real` | kg hco3/ha | fertilizer load of hco3 (kg/ha) | [[salt_module.f90#fert_salt]] | [[salt_fert_read.f90]]:36 |

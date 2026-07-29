---
type: input
tags:
  - swat/input
file: landuse.lum
ext: lum
cio_field: landuse_lum
read_by:
  - landuse_read.f90
purpose: ""
---

# landuse.lum

> [!info] Input File
> Declared in `file.cio` field `landuse_lum`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `landuse_lum`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[landuse_read.f90]]

## File Structure
- [[landuse_read.f90]] source line 36: reads `titldum`
- [[landuse_read.f90]] source line 38: reads `header`
- [[landuse_read.f90]] source line 41: reads `titldum`
- [[landuse_read.f90]] source line 50: reads `titldum`
- [[landuse_read.f90]] source line 52: reads `header`
- [[landuse_read.f90]] source line 56: reads `lum(ilu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `lum%name` | `character (len=40)` |  | name of the land use and management (from hru-data.hru pointer) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%cal_group` | `character (len=40)` |  | calibration group (not currently used) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%plant_cov` | `character (len=40)` |  | plant community initialization (pointer to plants.ini) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%mgt_ops` | `character (len=40)` |  | management operations (pointer to management.sch) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%cn_lu` | `character (len=40)` |  | land use for curve number table (pointer to cntable.lum) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%cons_prac` | `character (len=40)` |  | conservation practice from table (cons_practice.lum) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%urb_lu` | `character (len=40)` |  | type of urban land use- ie. residential, industrial, etc (urban.urb) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%urb_ro` | `character (len=40)` |  | urban runoff model "usgs_reg", simulate using USGS regression eqs "buildup_washoff", simulate using build up/wash off alg | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%ovn` | `character (len=40)` |  | Manning"s "n" land use type for overland flow (ovn_table.lum) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%tiledrain` | `character (len=40)` |  | tile drainage (pointer to tiledrain.str | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%septic` | `character (len=40)` |  | septic tanks (pointer to septic.str) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%fstrip` | `character (len=40)` |  | filter strips (pointer to filterstrip.str) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%grassww` | `character (len=40)` |  | grass waterways (pointer to grassedww.str) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |
| `lum%bmpuser` | `character (len=40)` |  | user specified removal efficiency (pointer to bmpuser.str) | [[landuse_data_module.f90#lum]] | [[landuse_read.f90]]:56 |

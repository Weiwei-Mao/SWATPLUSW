---
type: input
tags:
  - swat/input
file: object.cnt
ext: cnt
cio_field: object_cnt
read_by:
  - basin_read_objs.f90
purpose: ""
---

# object.cnt

> [!info] Input File
> Declared in `file.cio` field `object_cnt`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `object_cnt`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_read_objs.f90]]

## File Structure
- [[basin_read_objs.f90]] source line 34: reads `titldum`
- [[basin_read_objs.f90]] source line 36: reads `header`
- [[basin_read_objs.f90]] source line 38: reads `bsn`, `sp_ob`

## Parameters
| Parameter         | Type                | Units | Meaning                                                                  | Source                          |                Reader line |
| ----------------- | ------------------- | ----- | ------------------------------------------------------------------------ | ------------------------------- | -------------------------: |
| `bsn%name`        | `character(len=25)` |       |                                                                          | [[basin_module.f90#bsn]]        | [[basin_read_objs.f90]]:38 |
| `bsn%area_ls_ha`  | `real`              | ha    | Land area of the watershed in ha                                         | [[basin_module.f90#bsn]]        | [[basin_read_objs.f90]]:38 |
| `bsn%area_tot_ha` | `real`              | ha    | Total area of the watershed in ha                                        | [[basin_module.f90#bsn]]        | [[basin_read_objs.f90]]:38 |
| `sp_ob%objs`      | `integer`           |       | number of objects or 1st object command                                  | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%hru`       | `integer`           |       | 1-number of hru"s or 1st hru command                                     | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%hru_lte`   | `integer`           |       | 2-number of hru_lte"s or 1st hru_lte command                             | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%ru`        | `integer`           |       | 3-number of ru"s or 1st ru command                                       | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%gwflow`    | `integer`           |       | 4-number of gwflow"s or 1st gwflow command !rtb gwflow                   | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%aqu`       | `integer`           |       | 5-number of aquifer"s or 1st aquifer command                             | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%chan`      | `integer`           |       | 6-number of chan"s or 1st chan command                                   | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%res`       | `integer`           |       | 7-number of res"s or 1st res command                                     | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%recall`    | `integer`           |       | 8-number of recdays"s or 1st recday command                              | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%exco`      | `integer`           |       | 11-number of exco"s or 1st export coeff command                          | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%dr`        | `integer`           |       | 12-number of dr"s or 1st del ratio command                               | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%canal`     | `integer`           |       | 13-number of canal"s or 1st canal command                                | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%pump`      | `integer`           |       | 14-number of pump"s or 1st pump command                                  | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%outlet`    | `integer`           |       | 15-number of outlet"s or 1st outlet command                              | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%chandeg`   | `integer`           |       | 16-number of swat-deg channel"s or 1st swat-deg channel command          | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%aqu2d`     | `integer`           |       | 17-not currently used (number of 2D aquifer"s or 1st 2D aquifer command) | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%herd`      | `integer`           |       | 18-not currently used (number of herds)                                  | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |
| `sp_ob%wro`       | `integer`           |       | 19-not currently used (number of water rights)                           | [[hydrograph_module.f90#sp_ob]] | [[basin_read_objs.f90]]:38 |

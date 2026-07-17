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

`hru-data.hru` defines reusable HRU database records. Each record is read into
`hru_db(id)%dbsc`, a character-pointer bundle whose fields name other database
records. Later, `hru_read.f90` resolves most of those names into integer
pointers in `hru_db(id)%dbs`; `hrudb_init.f90` copies the selected `hru_db`
record into each active `hru()` object based on the object property pointer.

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

## `hru_db%dbsc` Row Layout

Because the reader uses:

```fortran
read (113,*,iostat=eof) k, hru_db(i)%dbsc
```

the values after `id` are consumed in the declaration order of
`hru_databases_char` in [[hru_module.f90]]. A row must provide:

| Column | Stored Field | Meaning / Target Database |
|---|---|---|
| `id` | `k` / `i` | HRU database record number; used as the `hru-data.hru` property pointer from object definitions. |
| `name` | `hru_db(id)%dbsc%name` | Text name for this HRU database record. |
| `topo` | `hru_db(id)%dbsc%topo` | Name in [[topography.hyd]]; resolved to `hru_db(id)%dbs%topo`. |
| `hyd` | `hru_db(id)%dbsc%hyd` | Name in [[hydrology.hyd]]; resolved to `hru_db(id)%dbs%hyd`. |
| `soil` | `hru_db(id)%dbsc%soil` | Soil name from [[soils.sol]]; resolved to `hru_db(id)%dbs%soil`. |
| `land_use_mgt` | `hru_db(id)%dbsc%land_use_mgt` | Land-use/management name from [[landuse.lum]]; resolved to `hru_db(id)%dbs%land_use_mgt`. |
| `soil_plant_init` | `hru_db(id)%dbsc%soil_plant_init` | Soil/plant initialization name; resolved through `soil_plant.ini` records loaded into `sol_plt_ini`. |
| `surf_stor` | `hru_db(id)%dbsc%surf_stor` | Surface-storage/wetland name from [[wetland.wet]], or `null`; resolved later during wetland initialization. |
| `snow` | `hru_db(id)%dbsc%snow` | Snow parameter name from [[snow.sno]], or `null`; resolved to `hru_db(id)%dbs%snow`. |
| `field` | `hru_db(id)%dbsc%field` | Field boundary/geometry name from [[field.fld]], or `null`; resolved to `hru_db(id)%dbs%field`. |

The `dbsc` values are the original text names from the input file. The matching
`dbs` fields are the integer indices used by the simulation after crosswalking.

---
type: input
tags:
  - swat/input
file: plant.ini
ext: ini
cio_field: plant
read_by:
  - readpcom.f90
purpose: ""
---

# plant.ini

> [!info] Input File
> Declared in `file.cio` field `plant`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `plant`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[readpcom.f90]]

## File Structure
- [[readpcom.f90]] source line 37: reads `titldum`
- [[readpcom.f90]] source line 39: reads `header`
- [[readpcom.f90]] source line 42: reads `name`, `numb`
- [[readpcom.f90]] source line 45: reads `name`
- [[readpcom.f90]] source line 55: reads `titldum`
- [[readpcom.f90]] source line 57: reads `header`
- [[readpcom.f90]] source line 62: reads `pcomdb(icom)%name`, `pcomdb(icom)%plants_com`, `pcomdb(icom)%rot_yr_ini`
- [[readpcom.f90]] source line 68: reads `pcomdb(icom)%pl(iplt)%cpnm`, `pcomdb(icom)%pl(iplt)%igro`, `pcomdb(icom)%pl(iplt)%lai`, `pcomdb(icom)%pl(iplt)%bioms`, `pcomdb(icom)%pl(iplt)%phuacc`, `pcomdb(icom)%pl(iplt)%pop`, `pcomdb(icom)%pl(iplt)%fr_yrmat`, `pcomdb(icom)%pl(iplt)%rsdin`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `name` | `character (len=13)` |  |  | `readpcom.f90:11` | [[readpcom.f90]]:42 |
| `numb` | `integer` | none | end of loop | `readpcom.f90:17` | [[readpcom.f90]]:42 |
| `pcomdb%name` | `character(len=40)` |  |  | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:62 |
| `pcomdb%plants_com` | `integer` |  |  | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:62 |
| `pcomdb%rot_yr_ini` | `integer` |  |  | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:62 |
| `pcomdb%pl%cpnm` | `character(len=40)` |  |  | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%igro` | `character(len=1)` |  | land cover status n = no land cover growing y = land cover growing | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%lai` | `real` | m**2/m**2 | leaf area index | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%bioms` | `real` | kg/ha | land cover/crop biomass | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%phuacc` | `real` |  | frac of plant heat unit acc. | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%pop` | `real` |  |  | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%fr_yrmat` | `real` | years | fraction of current year of growth to years to maturity | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |
| `pcomdb%pl%rsdin` | `real` | kg/ha | initial residue cover | [[plant_data_module.f90#pcomdb]] | [[readpcom.f90]]:68 |

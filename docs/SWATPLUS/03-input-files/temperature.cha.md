---
type: input
tags:
  - swat/input
file: temperature.cha
ext: cha
cio_field: temp
read_by:
  - ch_read_temp.f90
purpose: ""
---

# temperature.cha

> [!info] Input File
> Declared in `file.cio` field `temp`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `temp`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_temp.f90]]

## File Structure
- [[ch_read_temp.f90]] source line 28: reads `titldum`
- [[ch_read_temp.f90]] source line 30: reads `header`
- [[ch_read_temp.f90]] source line 34: reads `titldum`
- [[ch_read_temp.f90]] source line 45: reads `titldum`
- [[ch_read_temp.f90]] source line 47: reads `header`
- [[ch_read_temp.f90]] source line 51: reads `titldum`
- [[ch_read_temp.f90]] source line 54: reads `w_temp(ich_temp)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `w_temp%name` | `character(len=13)` |  |  | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%sno_mlt` | `real` | none | coefficient influencing snowmelt temperature contributions | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%gw` | `real` | none | coefficient influencing groundwater temperature contributions | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%sur_lat` | `real` | none | coefficient influencing surface and lateral flow temperature contributions | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%sno_lag` | `real` | days | average air temperature lag to snowmelt (1-3) | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%gw_lag` | `real` | days | average air temperature lag to gw flow (200-365) | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%surf_lag` | `real` | days | average air temperature lag to surface runoff (2-5) | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%lat_lag` | `real` | days | average air temperature lag to lateral flow (5-10) | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%lat_lag_coef` | `real` | none | lat air lag coefficient | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%surf_lag_coef` | `real` | none | surf air lag coefficient (used also for snow) | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%gw_lag_coef` | `real` | none | gw air lag coefficient | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%hex_coef1` | `real` | none | calibrate dew point | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%hex_coef2` | `real` | none | calibrate channel geometry | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%sf_on` | `integer` | none | shade factor file activation, 1= file, 0= take value from cal file | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |
| `w_temp%ssff` | `real` | none | ssff value default 0.5, range 0-1 | [[channel_data_module.f90#w_temp]] | [[ch_read_temp.f90]]:54 |

---
type: input
tags:
  - swat/input
file: ch_sed_budget.sft
ext: sft
cio_field: ch_sed_budget_sft
read_by:
  - ch_read_orders_cal.f90
purpose: ""
---

# ch_sed_budget.sft

> [!info] Input File
> Declared in `file.cio` field `ch_sed_budget_sft`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ch_sed_budget_sft`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_orders_cal.f90]]

## File Structure
- [[ch_read_orders_cal.f90]] source line 41: reads `titldum`
- [[ch_read_orders_cal.f90]] source line 43: reads `mreg`
- [[ch_read_orders_cal.f90]] source line 45: reads `header`
- [[ch_read_orders_cal.f90]] source line 51: reads `chcal(i)%name`, `chcal(i)%ord_num`, `nspu`
- [[ch_read_orders_cal.f90]] source line 56: reads `chcal(i)%name`, `chcal(i)%ord_num`, `nspu`, `(elem_cnt(isp), isp = 1, nspu)`
- [[ch_read_orders_cal.f90]] source line 116: reads `header`
- [[ch_read_orders_cal.f90]] source line 122: reads `chcal(i)%ord(iord)%meas`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `mreg` | `integer` | units | description | `ch_read_orders_cal.f90:18` | [[ch_read_orders_cal.f90]]:43 |
| `chcal%name` | `character(len=16)` |  | name of region - (number of regions = db_mx%lsu_reg) | [[calibration_data_module.f90#chcal]] | [[ch_read_orders_cal.f90]]:51 |
| `chcal%ord_num` | `integer` |  | number of stream orders in each region | [[calibration_data_module.f90#chcal]] | [[ch_read_orders_cal.f90]]:51 |
| `nspu` | `integer` | units | description | `ch_read_orders_cal.f90:20` | [[ch_read_orders_cal.f90]]:51 |
| `elem_cnt` | `integer, dimension (:), allocatable` |  |  | [[hydrograph_module.f90#elem_cnt]] | [[ch_read_orders_cal.f90]]:56 |
| `chcal%ord%meas` | `soft_calib_chan_processes` |  | dimension for stream order within a region / input soft calibration parms of each land use - ratio,t/ha,kg/ha | [[calibration_data_module.f90#chcal]] | [[ch_read_orders_cal.f90]]:122 |

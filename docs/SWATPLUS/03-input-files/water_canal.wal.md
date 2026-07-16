---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: water_canal.wal
ext: wal
cio_field: []
read_by:
  - water_canal_read.f90
purpose: ""
---

# water_canal.wal

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[water_canal_read.f90]]

## File Structure
- [[water_canal_read.f90]] source line 33: reads `titldum`
- [[water_canal_read.f90]] source line 35: reads `imax`
- [[water_canal_read.f90]] source line 36: reads `header`
- [[water_canal_read.f90]] source line 46: reads `i`, `canal(ic)%name`, `canal(ic)%w_sta`, `canal(ic)%init`, `canal(ic)%dtbl`, `canal(ic)%ddown_days`, `canal(ic)%w`, `canal(ic)%d`, `canal(ic)%s`, `canal(ic)%ss`, `canal(ic)%sat_con`, `canal(ic)%loss_fr`, `canal(ic)%bed_thick`, `canal(ic)%div_id`, `canal(ic)%day_beg`, `canal(ic)%day_end`, `num_aqu`
- [[water_canal_read.f90]] source line 56: reads `i`, `canal(ic)%name`, `canal(ic)%w_sta`, `canal(ic)%init`, `canal(ic)%dtbl`, `canal(ic)%ddown_days`, `canal(ic)%w`, `canal(ic)%d`, `canal(ic)%s`, `canal(ic)%ss`, `canal(ic)%sat_con`, `canal(ic)%loss_fr`, `canal(ic)%bed_thick`, `canal(ic)%div_id`, `canal(ic)%day_beg`, `canal(ic)%day_end`, `canal(ic)%num_aqu`, `(canal(ic)%aqu_loss(iaq), iaq = 1, num_aqu)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `imax` | `integer` | none | determine max number for array (imax) and total number in file | `water_canal_read.f90:15` | [[water_canal_read.f90]]:35 |
| `i` | `integer` | none | counter | `water_canal_read.f90:17` | [[water_canal_read.f90]]:46 |
| `canal%name` | `character (len=25)` |  | name of the canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%w_sta` | `character (len=25)` |  | name of nearby weather station | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%init` | `character (len=25)` |  | name of the intitial concentrations in canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%dtbl` | `character (len=25)` |  | name of decision table to determine canal outflow | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%ddown_days` | `real` |  | days !days to drawdown the storage to zero | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%w` | `real` |  | m !top width of canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%d` | `real` |  | m !depth of canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%s` | `real` |  | m !slope of canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%ss` | `real` |  | m/m !side slope of trapezoidal canal | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%sat_con` | `real` |  | to compute percolation from canal to groundwater | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%loss_fr` | `real` |  | water loss during treament | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%bed_thick` | `real` |  | m !bed sediment thickness for Darcy seepage (gwflow; 0 if not used) | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%div_id` | `integer` |  | recall diversion ID (gwflow; 0 if wallo-routed) | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%day_beg` | `integer` |  | Julian day canal begins operation (gwflow external; 0 otherwise) | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `canal%day_end` | `integer` |  | Julian day canal ends operation (gwflow external; 0 otherwise) | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:46 |
| `num_aqu` | `integer` |  |  | `water_canal_read.f90:19` | [[water_canal_read.f90]]:46 |
| `canal%num_aqu` | `integer` |  | number of aquifers | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:56 |
| `canal%aqu_loss` | `aquifer_loss` |  |  | [[water_allocation_module.f90#canal]] | [[water_canal_read.f90]]:56 |

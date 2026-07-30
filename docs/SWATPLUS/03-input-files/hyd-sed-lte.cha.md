---
type: input
tags:
  - swat/input
file: hyd-sed-lte.cha
ext: cha
cio_field: hyd_sed
read_by:
  - sd_hydsed_read.f90
purpose: ""
---

# hyd-sed-lte.cha

> [!info] Input File
> Declared in `file.cio` field `hyd_sed`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hyd_sed`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sd_hydsed_read.f90]]

## File Structure
- [[sd_hydsed_read.f90]] source line 36: reads `titldum`
- [[sd_hydsed_read.f90]] source line 38: reads `header`
- [[sd_hydsed_read.f90]] source line 41: reads `titldum`
- [[sd_hydsed_read.f90]] source line 55: reads `titldum`
- [[sd_hydsed_read.f90]] source line 57: reads `header`
- [[sd_hydsed_read.f90]] source line 61: reads `sd_chd(idb)`

## Parameters
| Parameter             | Type                | Units | Meaning                                                       | Source                           |               Reader line |
| --------------------- | ------------------- | ----- | ------------------------------------------------------------- | -------------------------------- | ------------------------: |
| `sd_chd%name`         | `character(len=25)` |       |                                                               | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%order`        | `integer`           |       |                                                               | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chw`          | `real`              | m     | channel top width                                             | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chd`          | `real`              | m     | channel depth                                                 | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chs`          | `real`              | m/m   | channel slope                                                 | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chl`          | `real`              | km    | channel length                                                | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chn`          | `real`              |       | channel Manning's n                                           | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chk`          | `real`              | mm/h  | channel bottom conductivity                                   | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%bank_exp`     | `real`              |       | bank erosion exponent                                         | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%cov`          | `real`              | 0-1   | channel cover factor                                          | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%sinu`         | `real`              | none  | sinuousity - ratio of channel length and straight line length | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%vcr_coef`     | `real`              |       | critical velocity coefficient                                 | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%d50`          | `real`              | mm    | channel median sediment size                                  | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%ch_clay`      | `real`              | %     | clay percent of bank and bed                                  | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%carbon`       | `real`              | %     | carbon percent of bank and bed                                | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%ch_bd`        | `real`              | t/m3  | dry bulk density                                              | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%chss`         | `real`              |       | channel side slope                                            | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%bankfull_flo` | `real`              |       | ==Dimensionless bankfull-flow adjustment factor==             | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%fps`          | `real`              | m/m   | flood plain slope                                             | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%fpn`          | `real`              |       | flood plain Manning's n                                       | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%n_conc`       | `real`              | mg/kg | nitrogen concentration in channel bank                        | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%p_conc`       | `real`              | mg/kg | phosphorus concentration in channel bank                      | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |
| `sd_chd%p_bio`        | `real`              | frac  | fraction of p in bank that is bioavailable                    | [[sd_channel_module.f90#sd_chd]] | [[sd_hydsed_read.f90]]:61 |

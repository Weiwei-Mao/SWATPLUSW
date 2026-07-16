---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: nutrients.rte
ext: rte
cio_field: []
read_by:
  - rte_read_nut.f90
purpose: ""
---

# nutrients.rte

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[rte_read_nut.f90]]

## File Structure
- [[rte_read_nut.f90]] source line 30: reads `titldum`
- [[rte_read_nut.f90]] source line 32: reads `header`
- [[rte_read_nut.f90]] source line 35: reads `titldum`
- [[rte_read_nut.f90]] source line 42: reads `titldum`
- [[rte_read_nut.f90]] source line 44: reads `header`
- [[rte_read_nut.f90]] source line 48: reads `titldum`
- [[rte_read_nut.f90]] source line 51: reads `rte_nut(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `rte_nut%name` | `character(len=16)` |  |  | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%len_inc` | `real` | m | segment length for reduction | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_slp` | `real` | (mgN/m2/h)/ppm | slope of denitrification (y-axis) and inflow no3 (x-axis) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_int` | `real` | mgN/m2/h | intercept of denitrification rate equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_slp_ob` | `real` | (mgN/m2/h)/ppm | slope of denitrification (y-axis) and inflow no3 (x-axis) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_int_ob` | `real` | mgN/m2/h | intercept of denitrification rate equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_slp_ub` | `real` | (mgN/m2/h)/ppm | slope of denitrification (y-axis) and inflow no3 (x-axis) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_int_ub` | `real` | mgN/m2/h | intercept of denitrification rate equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%turb_slp` | `real` | (del ppm/ppm) | slope of turbidity reduction (y) and inflow turbidity (x) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%turb_int` | `real` | ppm | intecept of turbidity reduction equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tss_slp` | `real` | (del ppm/ppm) | slope of total suspended solids (y) and inflow turbidity (x) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tss_int` | `real` | ppm | intecept of tss reduction equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tp_slp` | `real` | (del ppm/ppm) | slope of total P reduction (y) and turbidity reduction (x) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tp_int` | `real` | ppm | intecept of total P reduction equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%srp_slp` | `real` | (del ppm/ppm) | slope of soluble reactive P reduction (y) and total P reduction (x) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%srp_int` | `real` | ppm | intecept of soluble reactive P reduction equation | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%turb_tss_slp` | `real` | ppm | slope of turbidity and total suspended solids (0.2-0.4) | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%no3_min_conc` | `real` | ppm | minimum no3 concentration | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tp_min_conc` | `real` | ppm | minimum tp concentration | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%tss_min_conc` | `real` | ppm | minimum tss concentration | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |
| `rte_nut%srp_min_conc` | `real` | ppm | minimum srp concentration | [[channel_data_module.f90#rte_nut]] | [[rte_read_nut.f90]]:51 |

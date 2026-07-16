---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: sed_nut.cha
ext: cha
cio_field: []
read_by:
  - sd_hydsed_read.f90
purpose: ""
---

# sed_nut.cha

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[sd_hydsed_read.f90]]

## File Structure
- [[sd_hydsed_read.f90]] source line 75: reads `titldum`
- [[sd_hydsed_read.f90]] source line 77: reads `header`
- [[sd_hydsed_read.f90]] source line 80: reads `titldum`
- [[sd_hydsed_read.f90]] source line 90: reads `titldum`
- [[sd_hydsed_read.f90]] source line 92: reads `header`
- [[sd_hydsed_read.f90]] source line 96: reads `sd_chd1(idb)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `sd_chd1%name` | `character(len=25)` |  |  | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%order` | `character(len=16)` |  |  | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%pk_rto` | `real` | ratio | ratio of peak to mean daily flow in channel | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%fp_inun_days` | `real` | days | number of days fllod plain is inundated after flood | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%n_setl` | `real` | ratio | ratio of amount of N settling and sediment settling | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%p_setl` | `real` | ratio | ratio of amount of P settling and sediment settling | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%n_sol_part` | `real` |  | instream nitrogen soluble to particulate transformation coefficient | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%p_sol_part` | `real` |  | instream phosphorus soluble to particulate transformation coefficient | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%n_dep_enr` | `real` |  | enrichment of N in remaining water - deposition = 1/enrichment ratio | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%p_dep_enr` | `real` |  | enrichment of P in remaining water - deposition = 1/enrichment ratio | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%arc_len_fr` | `real` | frac | fraction of arc length where bank erosion occurs | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%bed_exp` | `real` |  | bed erosion exponential coefficient | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |
| `sd_chd1%wash_bed_fr` | `real` | frac | fraction of bank erosion that is washload | [[sd_channel_module.f90#sd_chd1]] | [[sd_hydsed_read.f90]]:96 |

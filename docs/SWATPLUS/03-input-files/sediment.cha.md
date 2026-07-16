---
type: input
tags:
  - swat/input
file: sediment.cha
ext: cha
cio_field: sed
read_by:
  - ch_read_sed.f90
purpose: ""
---

# sediment.cha

> [!info] Input File
> Declared in `file.cio` field `sed`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `sed`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[ch_read_sed.f90]]

## File Structure
- [[ch_read_sed.f90]] source line 34: reads `titldum`
- [[ch_read_sed.f90]] source line 36: reads `header`
- [[ch_read_sed.f90]] source line 39: reads `titldum`
- [[ch_read_sed.f90]] source line 48: reads `titldum`
- [[ch_read_sed.f90]] source line 50: reads `header`
- [[ch_read_sed.f90]] source line 54: reads `titldum`
- [[ch_read_sed.f90]] source line 57: reads `ch_sed(ich)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `ch_sed%name` | `character(len=16)` |  |  | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%eqn` | `integer` |  | sediment routine methods: 0 = original SWAT method 1 = Bagnold"seqn 2 = Kodatie 3 = Molinas WU 4 = Yang | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%cov1` | `real` | none | channel erodibility factor (0.0-1.0) | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%cov2` | `real` | none | channel cover factor (0.0-1.0) | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bnk_bd` | `real` | (g/cc) | bulk density of channel bank sediment (1.1-1.9) | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bed_bd` | `real` | (g/cc) | bulk density of channel bed sediment (1.1-1.9) | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bnk_kd` | `real` |  | erodibility of channel bank sediment by jet test | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bed_kd` | `real` |  | erodibility of channel bed sediment by jet test | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bnk_d50` | `real` |  | D50(median) particle size diameter of channel | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%bed_d50` | `real` |  | D50(median) particle size diameter of channel | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%tc_bnk` | `real` | N/m2 | critical shear stress of channel bank | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%tc_bed` | `real` | N/m2 | critical shear stress of channel bed | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |
| `ch_sed%erod` | `real, dimension(12)` |  | value of 0.0 indicates a non-erosive channel while a value of 1.0 indicates no resistance to erosion | [[channel_data_module.f90#ch_sed]] | [[ch_read_sed.f90]]:57 |

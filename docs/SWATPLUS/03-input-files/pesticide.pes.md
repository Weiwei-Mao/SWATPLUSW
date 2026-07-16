---
type: input
tags:
  - swat/input
file: pesticide.pes
ext: pes
cio_field: pest
read_by:
  - pest_parm_read.f90
purpose: ""
---

# pesticide.pes

> [!info] Input File
> Declared in `file.cio` field `pest`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pest`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[pest_parm_read.f90]]

## File Structure
- [[pest_parm_read.f90]] source line 28: reads `titldum`
- [[pest_parm_read.f90]] source line 30: reads `header`
- [[pest_parm_read.f90]] source line 33: reads `titldum`
- [[pest_parm_read.f90]] source line 42: reads `titldum`
- [[pest_parm_read.f90]] source line 44: reads `header`
- [[pest_parm_read.f90]] source line 48: reads `pestdb(ip)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `pestdb%name` | `character(len=16)` |  | pesticide name | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%koc` | `real` | (mL/g) | soil adsorption coeff normalized for soil org carbon content | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%washoff` | `real` | none | frac of pesticide on foliage which is washed off by rainfall event | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%foliar_hlife` | `real` | days | half-life of pest on foliage | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%soil_hlife` | `real` | days | half-life of pest in soil | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%solub` | `real` | mg/L (ppm) | solubility of chemical in water | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%aq_hlife` | `real` | days | aquatic half-life | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%aq_volat` | `real` | m/day | aquatic volatilization coeff | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%mol_wt` | `real` | g/mol | molecular weight - to calculate mixing velocity | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%aq_resus` | `real` | m/day | aquatic resuspension velocity for pesticide sorbed to sediment | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%aq_settle` | `real` | m/day | aquatic settling velocity for pesticide sorbed to sediment | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%ben_act_dep` | `real` | m | depth of active benthic layer | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%ben_bury` | `real` | m/day | burial velocity in benthic sediment | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%ben_hlife` | `real` | days | half-life of pest in benthic sediment | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%pl_uptake` | `real` | none | fraction taken up by plant | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |
| `pestdb%descrip` | `character(len=32)` |  | pesticide description | [[pesticide_data_module.f90#pestdb]] | [[pest_parm_read.f90]]:48 |

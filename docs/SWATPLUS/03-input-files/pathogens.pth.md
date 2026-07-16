---
type: input
tags:
  - swat/input
file: pathogens.pth
ext: pth
cio_field: pathcom_db
read_by:
  - path_parm_read.f90
purpose: ""
---

# pathogens.pth

> [!info] Input File
> Declared in `file.cio` field `pathcom_db`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `pathcom_db`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[path_parm_read.f90]]

## File Structure
- [[path_parm_read.f90]] source line 26: reads `titldum`
- [[path_parm_read.f90]] source line 28: reads `header`
- [[path_parm_read.f90]] source line 31: reads `titldum`
- [[path_parm_read.f90]] source line 40: reads `titldum`
- [[path_parm_read.f90]] source line 42: reads `header`
- [[path_parm_read.f90]] source line 46: reads `titldum`
- [[path_parm_read.f90]] source line 49: reads `path_db(ibac)`

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `path_db%pathnm` | `character(len=16)` |  |  | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%do_soln` | `real` | 1/day | Die-off factor for pers bac in soil solution | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%gr_soln` | `real` | 1/day | Growth factor for pers bac in soil solution | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%do_sorb` | `real` | 1/day | Die-off factor for pers bac adsorbed to soil part | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%gr_sorb` | `real` | 1/day | Growth factor for pers bac adsorbed to soil part | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%kd` | `real` | none | Pathogen part coeff bet sol and sorbed phase in surf runoff | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%t_adj` | `real` | none | temp adj factor for bac die-off/growth | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%washoff` | `real` | none | frac of pers bac on foliage washed off by a rainfall event | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%do_plnt` | `real` | 1/day | Die-off factor for pers bac on foliage | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%gr_plnt` | `real` | 1/day | Growth factor for persistent pathogen on foliage | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%fr_manure` | `real` | none | frac of manure containing active colony forming units (cfu) | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%perco` | `real` | none | Pathogen perc coeff ratio of solution bacteria in surf layer | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%det_thrshd` | `real` | # cfu/m^2 | Threshold detection level for less pers bac when pathogen levels drop to this amt the model considers bac in the soil to be insignificant and sets the levels to zero | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%do_stream` | `real` | 1/day | Die-off factor for persistent pathogen in streams | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%gr_stream` | `real` | 1/day | growth factor for persistent pathogen in streams | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%do_res` | `real` | 1/day | Die-off factor for less persistent pathogen in reservoirs | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%gr_res` | `real` | 1/day | growth factor for less persistent pathogen in reservoirs | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |
| `path_db%conc_min` | `real` |  | minimum pathogen concentration | [[pathogen_data_module.f90#path_db]] | [[path_parm_read.f90]]:49 |

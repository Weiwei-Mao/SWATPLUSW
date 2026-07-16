---
type: module
tags:
  - swat/module
  - swat/to-read
file: pathogen_data_module.f90
note_file: pathogen_data_module.f90
module_name: pathogen_data_module
defines_types:
  - pathogen_db
defines_vars:
  - path_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# pathogen_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### pathogen_db

- **Defined in source**: `pathogen_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pathnm` | `character(len=16)` | 6 |  |
| `do_soln` | `real` | 7 | 1/day \|Die-off factor for pers bac in soil solution |
| `gr_soln` | `real` | 8 | 1/day \|Growth factor for pers bac in soil solution |
| `do_sorb` | `real` | 9 | 1/day \|Die-off factor for pers bac adsorbed to soil part |
| `gr_sorb` | `real` | 10 | 1/day \|Growth factor for pers bac adsorbed to soil part |
| `kd` | `real` | 11 | none \|Pathogen part coeff bet sol and sorbed phase in surf runoff |
| `t_adj` | `real` | 12 | none \|temp adj factor for bac die-off/growth |
| `washoff` | `real` | 13 | none \|frac of pers bac on foliage washed off by a rainfall event |
| `do_plnt` | `real` | 14 | 1/day \|Die-off factor for pers bac on foliage |
| `gr_plnt` | `real` | 15 | 1/day \|Growth factor for persistent pathogen on foliage |
| `fr_manure` | `real` | 16 | none \|frac of manure containing active colony forming units (cfu) |
| `perco` | `real` | 17 | none \|Pathogen perc coeff ratio of solution bacteria in surf layer |
| `det_thrshd` | `real` | 18 | # cfu/m^2 \|Threshold detection level for less pers bac when pathogen levels drop to this amt the model considers bac in the soil to be insignificant and sets the levels to zero |
| `do_stream` | `real` | 21 | 1/day \|Die-off factor for persistent pathogen in streams |
| `gr_stream` | `real` | 22 | 1/day \|growth factor for persistent pathogen in streams |
| `do_res` | `real` | 23 | 1/day \|Die-off factor for less persistent pathogen in reservoirs |
| `gr_res` | `real` | 24 | 1/day \|growth factor for less persistent pathogen in reservoirs |
| `conc_min` | `real` | 25 | \|minimum pathogen concentration |

## Variables Defined
### path_db

- **Type**: `pathogen_db`
- **Defined in source**: `pathogen_data_module.f90:27`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/module
  - swat/to-read
file: landuse_data_module.f90
note_file: landuse_data_module.f90
module_name: landuse_data_module
defines_types:
  - land_use_management
  - land_use_structures
  - curvenumber_table
  - land_use_mgt_groups
  - conservation_practice_table
  - overlandflow_n_table
defines_vars:
  - lum_grp
  - name
  - cal_group
  - plant_cov
  - mgt_ops
  - cn_lu
  - cons_prac
  - urb_lu
  - urb_ro
  - ovn
  - tiledrain
  - septic
  - fstrip
  - grassww
  - bmpuser
purpose: ""
---

# landuse_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `land_use_management` |  |
| `land_use_structures` |  |
| `curvenumber_table` |  |
| `land_use_mgt_groups` |  |
| `conservation_practice_table` |  |
| `overlandflow_n_table` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `lum_grp` |  |  |
| `name` |  |  |
| `cal_group` |  |  |
| `plant_cov` |  |  |
| `mgt_ops` |  |  |
| `cn_lu` |  |  |
| `cons_prac` |  |  |
| `urb_lu` |  |  |
| `urb_ro` |  |  |
| `ovn` |  |  |
| `tiledrain` |  |  |
| `septic` |  |  |
| `fstrip` |  |  |
| `grassww` |  |  |
| `bmpuser` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

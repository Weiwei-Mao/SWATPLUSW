---
type: module
tags:
  - swat/module
  - swat/to-read
file: plant_data_module.f90
note_file: plant_data_module.f90
module_name: plant_data_module
defines_types:
  - residue_partition_fracs
  - lignin_derived_partition_fracs
  - plant_db
  - plant_cp
  - plant_init_db
  - plant_community_db
  - plant_transplant_db
defines_vars:
  - res_part_fracs
  - plantnm
  - typ
  - trig
  - cpnm
  - igro
  - name
purpose: ""
---

# plant_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `residue_partition_fracs` |  |
| `lignin_derived_partition_fracs` |  |
| `plant_db` |  |
| `plant_cp` |  |
| `plant_init_db` |  |
| `plant_community_db` |  |
| `plant_transplant_db` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `res_part_fracs` |  |  |
| `plantnm` |  |  |
| `typ` |  |  |
| `trig` |  |  |
| `cpnm` |  |  |
| `igro` |  |  |
| `name` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

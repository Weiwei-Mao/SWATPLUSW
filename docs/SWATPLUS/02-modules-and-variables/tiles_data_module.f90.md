---
type: module
tags:
  - swat/module
  - swat/to-read
file: tiles_data_module.f90
note_file: tiles_data_module.f90
module_name: tiles_data_module
defines_types:
  - subsurface_drainage
defines_vars:
  - sdr
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# tiles_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### subsurface_drainage

- **Defined in source**: `tiles_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 6 |  |
| `depth` | `real` | 7 | \|mm \|depth of drain tube from the soil surface |
| `time` | `real` | 8 | \|hrs \|time to drain soil to field capacity |
| `lag` | `real` | 9 | \|hours \|drain tile lag time |
| `radius` | `real` | 10 | \|mm \|effective radius of drains |
| `dist` | `real` | 11 | \|m \|distance between two drain tubes or tiles |
| `drain_co` | `real` | 12 | \|mm/day \|drainage coefficient |
| `pumpcap` | `real` | 13 | \|mm/hr \|pump capacity (default pump capacity = 1.042mm/hr or 25mm/day) |
| `latksat` | `real` | 14 | \|none \|multiplication factor to determine conk(j1,j) from sol_k(j1,j) for HRU |

## Variables Defined
### sdr

- **Type**: `subsurface_drainage`
- **Defined in source**: `tiles_data_module.f90:16`

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

---
type: module
tags:
  - swat/module
  - swat/to-read
file: hydrology_data_module.f90
note_file: hydrology_data_module.f90
module_name: hydrology_data_module
defines_types:
  - hydrology_db
defines_vars:
  - hyd_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# hydrology_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### hydrology_db

- **Defined in source**: `hydrology_data_module.f90:6`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 7 | none \|0 \|0 \|name |
| `lat_ttime` | `real` | 8 | days \|0-120 \|0 \|Exponential of the lateral flow travel time |
| `lat_sed` | `real` | 9 | g/L \|sediment concentration in lateral flow |
| `canmx` | `real` | 10 | mm H2O \|maximum canopy storage |
| `esco` | `real` | 11 | none \|soil evaporation compensation factor (0-1) |
| `epco` | `real` | 12 | none \|plant water uptake compensation factor (0-1) |
| `erorgn` | `real` | 13 | none \|organic N enrichment ratio, if left blank % \|the model will calculate for every event |
| `erorgp` | `real` | 15 | none \|organic P enrichment ratio, if left blank % \|the model will calculate for every event |
| `cn3_swf` | `real` | 17 | none \|soil water at cn3 - 0=fc; .99=near saturation |
| `biomix` | `real` | 18 | none \|biological mixing efficiency. % \|Mixing of soil due to activity of earthworms and other soil biota. % \|Mixing is performed at the end of every calendar year. |
| `perco` | `real` | 21 | none \|0-1 \|percolation coefficient - linear adjustment to daily perc |
| `lat_orgn` | `real` | 22 | ppm \|organic N concentration in lateral flow |
| `lat_orgp` | `real` | 23 | ppm \|organic P concentration in lateral flow |
| `pet_co` | `real` | 24 | none \|coefficient related to radiation used in Hargreaves equation |
| `latq_co` | `real` | 25 | none \|0-1 \|lateral soil flow coefficient - linear adjustment to daily lat flow |

## Variables Defined
### hyd_db

- **Type**: `hydrology_db`
- **Defined in source**: `hydrology_data_module.f90:27`

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

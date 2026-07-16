---
type: module
tags:
  - swat/module
  - swat/to-read
file: topography_data_module.f90
note_file: topography_data_module.f90
module_name: topography_data_module
defines_types:
  - topography_db
  - fields_db
defines_vars:
  - topo_db
  - field_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# topography_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### topography_db

- **Defined in source**: `topography_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 6 |  |
| `slope` | `real` | 7 | hru_slp(:) \|m/m \|average slope steepness in HRU |
| `slope_len` | `real` | 8 | slsubbsn(:) \|m \|average slope length for erosion |
| `lat_len` | `real` | 9 | slsoil(:) \|m \|slope length for lateral subsurface flow |
| `dis_stream` | `real` | 10 | dis_stream(:) \|m \|average distance to stream |
| `dep_co` | `real` | 11 | \| \|deposition coefficient |

### fields_db

- **Defined in source**: `topography_data_module.f90:15`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 16 |  |
| `length` | `real` | 17 | \|m \|field length for wind erosion |
| `wid` | `real` | 18 | \|m \|field width for wind erosion |
| `ang` | `real` | 19 | \|deg \|field angle for wind erosion |

## Variables Defined
### topo_db

- **Type**: `topography_db`
- **Defined in source**: `topography_data_module.f90:13`

### field_db

- **Type**: `fields_db`
- **Defined in source**: `topography_data_module.f90:21`

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

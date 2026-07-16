---
type: module
tags:
  - swat/module
  - swat/to-read
file: ru_module.f90
note_file: ru_module.f90
module_name: ru_module
defines_types:
  - ru_databases_char
  - ru_databases
  - field
  - ru_parameters
defines_vars:
  - iru
  - mru_db
  - ru_tc
  - ru_n
  - itsb
  - ru
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# ru_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### ru_databases_char

- **Defined in source**: `ru_module.f90:11`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `elem_def` | `character(len=16)` | 12 |  |
| `elem_dr` | `character(len=16)` | 13 |  |
| `toposub_db` | `character(len=16)` | 14 |  |
| `field_db` | `character(len=16)` | 15 |  |

### ru_databases

- **Defined in source**: `ru_module.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `elem_def` | `integer` | 19 |  |
| `elem_dr` | `integer` | 20 |  |
| `toposub_db` | `integer` | 21 |  |
| `field_db` | `integer` | 22 |  |

### field

- **Defined in source**: `ru_module.f90:25`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 26 |  |
| `length` | `real` | 27 | \|m \|field length for wind erosion |
| `wid` | `real` | 28 | \|m \|field width for wind erosion |
| `ang` | `real` | 29 | \|deg \|field angle for wind erosion |

### ru_parameters

- **Defined in source**: `ru_module.f90:32`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 33 |  |
| `da_km2` | `real` | 34 | km2 \|drainage area |
| `dbsc` | `ru_databases_char` | 35 |  |
| `dbs` | `ru_databases` | 36 |  |
| `field` | `field` | 37 |  |

## Variables Defined
### iru

- **Type**: `integer`
- **Defined in source**: `ru_module.f90:5`
- **Source note**: none            |counter

### mru_db

- **Type**: `integer`
- **Defined in source**: `ru_module.f90:6`
- **Source note**: |

### ru_tc

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `ru_module.f90:7`
- **Source note**: |

### ru_n

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `ru_module.f90:8`
- **Source note**: |

### itsb

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `ru_module.f90:9`
- **Source note**: none            |end of loop

### ru

- **Type**: `ru_parameters`
- **Defined in source**: `ru_module.f90:39`

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

---
type: module
tags:
  - swat/module
  - swat/to-read
file: reservoir_conditions_module.f90
note_file: reservoir_conditions_module.f90
module_name: reservoir_conditions_module
defines_types:
  - cond
  - conditions
  - modules
  - reservoir_condition_tables
defines_vars:
  - release
  - day
  - hit
  - ctbl
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# reservoir_conditions_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### cond

- **Defined in source**: `reservoir_conditions_module.f90:11`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `var` | `character(10)` | 12 |  |
| `op` | `character(2)` | 13 |  |
| `val` | `real` | 14 |  |

### conditions

- **Defined in source**: `reservoir_conditions_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num_conds` | `integer` | 18 |  |
| `action` | `real` | 19 |  |
| `scon` | `cond` | 20 |  |

### modules

- **Defined in source**: `reservoir_conditions_module.f90:23`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num_conds` | `integer` | 24 |  |
| `con` | `conditions` | 25 |  |

### reservoir_condition_tables

- **Defined in source**: `reservoir_conditions_module.f90:28`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(25)` | 29 |  |
| `num_tbl` | `integer` | 30 |  |
| `num_conds` | `integer` | 31 |  |
| `num_modules` | `integer` | 32 |  |
| `conds` | `conditions` | 33 |  |
| `mods` | `modules` | 34 |  |

## Variables Defined
### release

- **Type**: `real`
- **Defined in source**: `reservoir_conditions_module.f90:7`

### day

- **Type**: `integer`
- **Defined in source**: `reservoir_conditions_module.f90:8`

### hit

- **Type**: `character(1)`
- **Defined in source**: `reservoir_conditions_module.f90:9`

### ctbl

- **Type**: `reservoir_condition_tables`
- **Defined in source**: `reservoir_conditions_module.f90:36`

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

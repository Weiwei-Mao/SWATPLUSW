---
type: module
tags:
  - swat/module
  - swat/to-read
file: exco_module.f90
note_file: exco_module.f90
module_name: exco_module
defines_types:
  - export_coefficient_datafiles
defines_vars:
  - exco_om_num
  - exco_pest_num
  - exco_path_num
  - exco_hmet_num
  - exco_salt_num
  - exco_om_name
  - exco_pest_name
  - exco_path_name
  - exco_hmet_name
  - exco_salt_name
  - exco_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# exco_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### export_coefficient_datafiles

- **Defined in source**: `exco_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 17 |  |
| `om_file` | `character(len=16)` | 18 |  |
| `pest_file` | `character(len=16)` | 19 |  |
| `path_file` | `character(len=16)` | 20 |  |
| `hmet_file` | `character(len=16)` | 21 |  |
| `salts_file` | `character(len=16)` | 22 |  |
| `constit_file` | `character(len=16)` | 23 |  |
| `descrip` | `character(len=40)` | 24 |  |

## Variables Defined
### exco_om_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:5`

### exco_pest_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:6`

### exco_path_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:7`

### exco_hmet_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:8`

### exco_salt_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:9`

### exco_om_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:10`

### exco_pest_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:11`

### exco_path_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:12`

### exco_hmet_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:13`

### exco_salt_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `exco_module.f90:14`

### exco_db

- **Type**: `export_coefficient_datafiles`
- **Defined in source**: `exco_module.f90:26`

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

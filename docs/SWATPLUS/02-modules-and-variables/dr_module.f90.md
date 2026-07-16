---
type: module
tags:
  - swat/module
  - swat/to-read
file: dr_module.f90
note_file: dr_module.f90
module_name: dr_module
defines_types:
  - delivery_ratio_datafiles
defines_vars:
  - dr_om_num
  - dr_pest_num
  - dr_path_num
  - dr_hmet_num
  - dr_salt_num
  - dr_om_name
  - dr_pest_name
  - dr_path_name
  - dr_hmet_name
  - dr_salt_name
  - dr_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# dr_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### delivery_ratio_datafiles

- **Defined in source**: `dr_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 17 |  |
| `om_file` | `character(len=16)` | 18 |  |
| `pest_file` | `character(len=16)` | 19 |  |
| `path_file` | `character(len=16)` | 20 |  |
| `hmet_file` | `character(len=16)` | 21 |  |
| `salts_file` | `character(len=16)` | 22 |  |

## Variables Defined
### dr_om_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:5`

### dr_pest_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:6`

### dr_path_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:7`

### dr_hmet_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:8`

### dr_salt_num

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:9`

### dr_om_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:10`

### dr_pest_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:11`

### dr_path_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:12`

### dr_hmet_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:13`

### dr_salt_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `dr_module.f90:14`

### dr_db

- **Type**: `delivery_ratio_datafiles`
- **Defined in source**: `dr_module.f90:24`

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

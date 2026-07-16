---
type: module
tags:
  - swat/module
  - swat/to-read
file: recall_module.f90
note_file: recall_module.f90
module_name: recall_module
defines_types:
  - constituent_file_data
  - recall_databases
defines_vars:
  - recall_db
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# recall_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### constituent_file_data

- **Defined in source**: `recall_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 6 |  |
| `units` | `character(len=13)` | 7 | mass, conc |
| `tstep` | `character(len=13)` | 8 | day, mo, yr |

### recall_databases

- **Defined in source**: `recall_module.f90:11`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=13)` | 12 |  |
| `org_min` | `constituent_file_data` | 13 |  |
| `pest` | `constituent_file_data` | 14 |  |
| `path` | `constituent_file_data` | 15 |  |
| `hmet` | `constituent_file_data` | 16 |  |
| `salt` | `constituent_file_data` | 17 |  |
| `constit` | `constituent_file_data` | 18 |  |
| `iorg_min` | `integer` | 19 |  |
| `ipest` | `integer` | 20 |  |
| `ipath` | `integer` | 21 |  |
| `ihmet` | `integer` | 22 |  |
| `isalt` | `integer` | 23 |  |
| `iconstit` | `integer` | 24 |  |

## Variables Defined
### recall_db

- **Type**: `recall_databases`
- **Defined in source**: `recall_module.f90:30`

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

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
  - dbsc
  - dbs
  - field
  - elem_def
  - elem_dr
  - toposub_db
  - field_db
  - name
purpose: ""
---

# ru_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `ru_databases_char` |  |
| `ru_databases` |  |
| `field` |  |
| `ru_parameters` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `dbsc` |  |  |
| `dbs` |  |  |
| `field` |  |  |
| `elem_def` |  |  |
| `elem_dr` |  |  |
| `toposub_db` |  |  |
| `field_db` |  |  |
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

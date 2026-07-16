---
type: module
tags:
  - swat/module
  - swat/to-read
file: conditional_module.f90
note_file: conditional_module.f90
module_name: conditional_module
defines_types:
  - conditions_var
  - actions_var
  - decision_table
defines_vars:
  - var
  - ob
  - lim_var
  - lim_op
  - typ
  - name
  - option
  - file_pointer
purpose: ""
---

# conditional_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `conditions_var` |  |
| `actions_var` |  |
| `decision_table` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `var` |  |  |
| `ob` |  |  |
| `lim_var` |  |  |
| `lim_op` |  |  |
| `typ` |  |  |
| `name` |  |  |
| `option` |  |  |
| `file_pointer` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

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
  - name
  - om_file
  - pest_file
  - path_file
  - hmet_file
  - salts_file
purpose: ""
---

# dr_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `delivery_ratio_datafiles` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `name` |  |  |
| `om_file` |  |  |
| `pest_file` |  |  |
| `path_file` |  |  |
| `hmet_file` |  |  |
| `salts_file` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

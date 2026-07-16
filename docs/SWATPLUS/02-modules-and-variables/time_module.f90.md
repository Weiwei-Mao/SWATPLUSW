---
type: module
tags:
  - swat/module
  - swat/to-read
file: time_module.f90
note_file: time_module.f90
module_name: time_module
defines_types:
  - time_current
defines_vars:
  - time
  - time_init
  - cal_sim
  - day_print
purpose: ""
---

# time_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `time_current` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `time` |  |  |
| `time_init` |  |  |
| `cal_sim` |  |  |
| `day_print` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

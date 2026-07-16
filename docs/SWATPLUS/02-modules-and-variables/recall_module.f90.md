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
  - org_min
  - pest
  - path
  - hmet
  - salt
  - constit
  - name
  - units
  - tstep
purpose: ""
---

# recall_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `constituent_file_data` |  |
| `recall_databases` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |
| `salt` |  |  |
| `constit` |  |  |
| `name` |  |  |
| `units` |  |  |
| `tstep` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

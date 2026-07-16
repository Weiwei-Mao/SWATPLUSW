---
type: module
tags:
  - swat/module
  - swat/to-read
file: fertilizer_data_module.f90
note_file: fertilizer_data_module.f90
module_name: fertilizer_data_module
defines_types:
  - fertilizer_db
  - manure_database
  - manure_attributes
defines_vars:
  - fertnm
  - name
  - org_min
  - pests
  - paths
  - hmets
  - salts
  - constit
  - descrip
  - description
purpose: ""
---

# fertilizer_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `fertilizer_db` |  |
| `manure_database` |  |
| `manure_attributes` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `fertnm` |  |  |
| `name` |  |  |
| `org_min` |  |  |
| `pests` |  |  |
| `paths` |  |  |
| `hmets` |  |  |
| `salts` |  |  |
| `constit` |  |  |
| `descrip` |  |  |
| `description` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

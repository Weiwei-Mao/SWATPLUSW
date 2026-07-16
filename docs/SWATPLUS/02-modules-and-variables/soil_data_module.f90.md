---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_data_module.f90
note_file: soil_data_module.f90
module_name: soil_data_module
defines_types:
  - soil_lte_database
  - soiltest_db
  - soiltest_db_old
  - soilayer_db
  - soil_profile_db
  - soil_database
defines_vars:
  - s
  - texture
  - name
  - snam
  - hydgrp
purpose: ""
---

# soil_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `soil_lte_database` |  |
| `soiltest_db` |  |
| `soiltest_db_old` |  |
| `soilayer_db` |  |
| `soil_profile_db` |  |
| `soil_database` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `s` |  |  |
| `texture` |  |  |
| `name` |  |  |
| `snam` |  |  |
| `hydgrp` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

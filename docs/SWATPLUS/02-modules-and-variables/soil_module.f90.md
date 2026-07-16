---
type: module
tags:
  - swat/module
  - swat/to-read
file: soil_module.f90
note_file: soil_module.f90
module_name: soil_module
defines_types:
  - soilayer
  - soil_physical_properties
  - soil_test
  - soil_profile
  - soil_hru_database
defines_vars:
  - s
  - snam
  - hydgrp
  - texture
purpose: ""
---

# soil_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `soilayer` |  |
| `soil_physical_properties` |  |
| `soil_test` |  |
| `soil_profile` |  |
| `soil_hru_database` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `s` |  |  |
| `snam` |  |  |
| `hydgrp` |  |  |
| `texture` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

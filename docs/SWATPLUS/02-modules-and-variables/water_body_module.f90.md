---
type: module
tags:
  - swat/module
  - swat/to-read
file: water_body_module.f90
note_file: water_body_module.f90
module_name: water_body_module
defines_types:
  - water_body
defines_vars:
  - wbodz
  - bch_wat_d
  - bch_wat_m
  - bch_wat_y
  - bch_wat_a
  - bres_wat_d
  - bres_wat_m
  - bres_wat_y
  - bres_wat_a
purpose: ""
---

# water_body_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `water_body` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `wbodz` |  |  |
| `bch_wat_d` |  |  |
| `bch_wat_m` |  |  |
| `bch_wat_y` |  |  |
| `bch_wat_a` |  |  |
| `bres_wat_d` |  |  |
| `bres_wat_m` |  |  |
| `bres_wat_y` |  |  |
| `bres_wat_a` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

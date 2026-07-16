---
type: module
tags:
  - swat/module
  - swat/to-read
file: mgt_operations_module.f90
note_file: mgt_operations_module.f90
module_name: mgt_operations_module
defines_types:
  - irrigation_operation
  - puddle_operation
  - filtstrip_operation
  - fire_operation
  - grwaterway_operation
  - bmpuser_operation
  - bmpuser_operation1
  - chemical_application_operation
  - harvest_operation
  - grazing_operation
  - streetsweep_operation
  - management_ops
  - management_schedule
defines_vars:
  - harvop
  - hkop
  - graze
  - sweepop
  - mgt
  - mgt1
  - name
  - form
  - op_typ
  - typ
  - fertnm
  - op
  - op_char
  - op_plant
purpose: ""
---

# mgt_operations_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `irrigation_operation` |  |
| `puddle_operation` |  |
| `filtstrip_operation` |  |
| `fire_operation` |  |
| `grwaterway_operation` |  |
| `bmpuser_operation` |  |
| `bmpuser_operation1` |  |
| `chemical_application_operation` |  |
| `harvest_operation` |  |
| `grazing_operation` |  |
| `streetsweep_operation` |  |
| `management_ops` |  |
| `management_schedule` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `harvop` |  |  |
| `hkop` |  |  |
| `graze` |  |  |
| `sweepop` |  |  |
| `mgt` |  |  |
| `mgt1` |  |  |
| `name` |  |  |
| `form` |  |  |
| `op_typ` |  |  |
| `typ` |  |  |
| `fertnm` |  |  |
| `op` |  |  |
| `op_char` |  |  |
| `op_plant` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

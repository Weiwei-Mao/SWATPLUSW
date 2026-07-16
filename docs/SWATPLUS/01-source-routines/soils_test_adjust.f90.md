---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soils_test_adjust.f90
note_file: soils_test_adjust.f90
subroutine: soils_test_adjust
module:
  - soil_module
  - soil_data_module
calls: []
uses_variables:
  - soil_data_module.f90#soildb
  - soil_module.f90#nmbr_soil_test_layers
  - soil_module.f90#sol
  - soil_module.f90#sol_test
input_variables: []
reads: []
writes: []
purpose: ""
---

# soils_test_adjust

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soils_test_adjust.f90`
- **Modules used**:
  - [[soil_module.f90]]
  - [[soil_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[soils_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[soil_data_module.f90#soildb]] - `soil_database`
- [[soil_module.f90#nmbr_soil_test_layers]] - `integer`
- [[soil_module.f90#sol]] - `soil_hru_database`
- [[soil_module.f90#sol_test]] - `soil_test`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

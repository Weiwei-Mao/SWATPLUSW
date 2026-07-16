---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_plant_zero.f90
note_file: calsoft_plant_zero.f90
subroutine: calsoft_plant_zero
module:
  - calibration_data_module
  - maximum_data_module
calls: []
uses_variables:
  - calibration_data_module.f90#plcal
  - calibration_data_module.f90#plcal_z
  - maximum_data_module.f90#db_mx
input_variables: []
reads: []
writes: []
purpose: ""
---

# calsoft_plant_zero

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_plant_zero.f90`
- **Modules used**:
  - [[calibration_data_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[calsoft_plant.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[calibration_data_module.f90#plcal_z]] - `soft_calib_pl_processes`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

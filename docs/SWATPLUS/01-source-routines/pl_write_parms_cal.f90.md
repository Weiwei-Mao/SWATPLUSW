---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_write_parms_cal.f90
note_file: pl_write_parms_cal.f90
subroutine: pl_write_parms_cal
module:
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - input_file_module
  - plant_module
calls: []
reads: []
writes:
  - plant_parms.cal
purpose: ""
---

# pl_write_parms_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_write_parms_cal.f90`
- **Modules used**: [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[input_file_module.f90]], [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 1

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `plant_parms.cal`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

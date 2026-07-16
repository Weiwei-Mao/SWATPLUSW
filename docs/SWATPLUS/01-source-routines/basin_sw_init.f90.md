---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_sw_init.f90
note_file: basin_sw_init.f90
subroutine: basin_sw_init
module:
  - time_module
  - hydrograph_module
  - calibration_data_module
  - output_landscape_module
  - basin_module
  - maximum_data_module
  - soil_module
  - hru_module
calls: []
reads: []
writes: []
purpose: ""
---

# basin_sw_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_sw_init.f90`
- **Modules used**: [[time_module.f90]], [[hydrograph_module.f90]], [[calibration_data_module.f90]], [[output_landscape_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[soil_module.f90]], [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

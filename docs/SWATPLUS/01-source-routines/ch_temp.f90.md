---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_temp.f90
note_file: ch_temp.f90
subroutine: ch_temp
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - sd_channel_module
  - hydrograph_module
  - climate_module
  - output_landscape_module
  - aquifer_module
  - calibration_data_module
  - time_module
  - channel_velocity_module
calls: []
reads: []
writes: []
purpose: ""
---

# ch_temp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_temp.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[channel_data_module.f90]], [[sd_channel_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[output_landscape_module.f90]], [[aquifer_module.f90]], [[calibration_data_module.f90]], [[time_module.f90]], [[channel_velocity_module.f90]]
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

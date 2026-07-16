---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtday.f90
note_file: ch_rtday.f90
subroutine: ch_rtday
module:
  - basin_module
  - channel_data_module
  - channel_module
  - hydrograph_module
  - hru_module
  - channel_velocity_module
  - maximum_data_module
  - reservoir_module
  - reservoir_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine routes the daily flow through the reach using a; variable storage coefficient"
---

# ch_rtday

> [!info] Summary
> this subroutine routes the daily flow through the reach using a; variable storage coefficient

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtday.f90`
- **Modules used**: [[basin_module.f90]], [[channel_data_module.f90]], [[channel_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[channel_velocity_module.f90]], [[maximum_data_module.f90]], [[reservoir_module.f90]], [[reservoir_data_module.f90]]
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

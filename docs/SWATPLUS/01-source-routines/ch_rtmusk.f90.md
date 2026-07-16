---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtmusk.f90
note_file: ch_rtmusk.f90
subroutine: ch_rtmusk
module:
  - basin_module
  - channel_data_module
  - channel_module
  - hydrograph_module
  - time_module
  - channel_velocity_module
  - sd_channel_module
  - climate_module
  - reservoir_module
  - reservoir_data_module
  - water_body_module
  - conditional_module
calls:
  - rcurv_interp_flo
reads: []
writes: []
purpose: "this subroutine routes a daily flow through a reach using the; Muskingum method; code provided by Dr. Valentina Krysanova, Pottsdam Institute for"
---

# ch_rtmusk

> [!info] Summary
> this subroutine routes a daily flow through a reach using the; Muskingum method; code provided by Dr. Valentina Krysanova, Pottsdam Institute for

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtmusk.f90`
- **Modules used**: [[basin_module.f90]], [[channel_data_module.f90]], [[channel_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[channel_velocity_module.f90]], [[sd_channel_module.f90]], [[climate_module.f90]], [[reservoir_module.f90]], [[reservoir_data_module.f90]], [[water_body_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[rcurv_interp_flo.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

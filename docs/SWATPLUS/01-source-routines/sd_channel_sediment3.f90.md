---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_sediment3.f90
note_file: sd_channel_sediment3.f90
subroutine: sd_channel_sediment3
module:
  - climate_module
  - sd_channel_module
  - channel_module
  - hydrograph_module
  - time_module
  - hru_module
  - water_body_module
  - reservoir_module
  - utils
  - basin_module
  - gwflow_module
  - channel_velocity_module
calls:
  - rcurv_interp_flo
  - gwflow_floodplain
reads: []
writes: []
purpose: ""
---

# sd_channel_sediment3

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_sediment3.f90`
- **Modules used**: [[climate_module.f90]], [[sd_channel_module.f90]], [[channel_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[hru_module.f90]], [[water_body_module.f90]], [[reservoir_module.f90]], [[utils.f90]], [[basin_module.f90]], [[gwflow_module.f90]], [[channel_velocity_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[rcurv_interp_flo.f90]]
- [[gwflow_floodplain.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

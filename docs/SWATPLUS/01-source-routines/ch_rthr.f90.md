---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rthr.f90
note_file: ch_rthr.f90
subroutine: ch_rthr
module:
  - basin_module
  - climate_module
  - channel_data_module
  - time_module
  - channel_module
  - hydrograph_module
  - sd_channel_module
calls:
  - chrc_interp
reads: []
writes: []
purpose: "This subroutine routes flow at any required time step through the reach; using a constant storage coefficient; Routing method: Variable Storage routing"
---

# ch_rthr

> [!info] Summary
> This subroutine routes flow at any required time step through the reach; using a constant storage coefficient; Routing method: Variable Storage routing

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rthr.f90`
- **Modules used**: [[basin_module.f90]], [[climate_module.f90]], [[channel_data_module.f90]], [[time_module.f90]], [[channel_module.f90]], [[hydrograph_module.f90]], [[sd_channel_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `chrc_interp`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

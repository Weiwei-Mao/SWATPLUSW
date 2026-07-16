---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: channel_output.f90
note_file: channel_output.f90
subroutine: channel_output
module:
  - time_module
  - basin_module
  - hydrograph_module
  - channel_module
  - climate_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - channel_module.f90#ch_a
  - channel_module.f90#ch_d
  - channel_module.f90#ch_m
  - channel_module.f90#ch_y
  - channel_module.f90#chz
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# channel_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `channel_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[channel_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[channel_module.f90#ch_a]] - `ch_output`
- [[channel_module.f90#ch_d]] - `ch_output`
- [[channel_module.f90#ch_m]] - `ch_output`
- [[channel_module.f90#ch_y]] - `ch_output`
- [[channel_module.f90#chz]] - `ch_output`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

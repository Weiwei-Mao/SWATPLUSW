---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_channel_output.f90
note_file: basin_channel_output.f90
subroutine: basin_channel_output
module:
  - time_module
  - basin_module
  - channel_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - channel_module.f90#bch_a
  - channel_module.f90#bch_d
  - channel_module.f90#bch_m
  - channel_module.f90#bch_y
  - channel_module.f90#ch_d
  - channel_module.f90#chz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#sp_ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_channel_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_channel_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[channel_module.f90#bch_a]] - `ch_output`
- [[channel_module.f90#bch_d]] - `ch_output`
- [[channel_module.f90#bch_m]] - `ch_output`
- [[channel_module.f90#bch_y]] - `ch_output`
- [[channel_module.f90#ch_d]] - `ch_output`
- [[channel_module.f90#chz]] - `ch_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

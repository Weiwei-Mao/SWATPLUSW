---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_output.f90
note_file: sd_channel_output.f90
subroutine: sd_channel_output
module:
  - sd_channel_module
  - basin_module
  - time_module
  - hydrograph_module
  - water_body_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#ch_in_a
  - hydrograph_module.f90#ch_in_d
  - hydrograph_module.f90#ch_in_m
  - hydrograph_module.f90#ch_in_y
  - hydrograph_module.f90#ch_out_a
  - hydrograph_module.f90#ch_out_d
  - hydrograph_module.f90#ch_out_m
  - hydrograph_module.f90#ch_out_y
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#chaz
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - sd_channel_module.f90#wtemp
  - time_module.f90#ndays
  - time_module.f90#time
  - water_body_module.f90#ch_wat_a
  - water_body_module.f90#ch_wat_d
  - water_body_module.f90#ch_wat_m
  - water_body_module.f90#ch_wat_y
  - water_body_module.f90#wbodz
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_channel_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_output.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_body_module.f90]]
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
- [[hydrograph_module.f90#ch_in_a]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_m]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_a]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_m]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#chaz]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[sd_channel_module.f90#wtemp]] - `real`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`
- [[water_body_module.f90#ch_wat_a]] - `water_body`
- [[water_body_module.f90#ch_wat_d]] - `water_body`
- [[water_body_module.f90#ch_wat_m]] - `water_body`
- [[water_body_module.f90#ch_wat_y]] - `water_body`
- [[water_body_module.f90#wbodz]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

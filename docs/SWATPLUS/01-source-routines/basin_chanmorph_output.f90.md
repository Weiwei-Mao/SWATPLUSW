---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_chanmorph_output.f90
note_file: basin_chanmorph_output.f90
subroutine: basin_chanmorph_output
module:
  - time_module
  - basin_module
  - sd_channel_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#sp_ob
  - sd_channel_module.f90#bchsd_a
  - sd_channel_module.f90#bchsd_d
  - sd_channel_module.f90#bchsd_m
  - sd_channel_module.f90#bchsd_y
  - sd_channel_module.f90#chsd_d
  - sd_channel_module.f90#chsdz
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_chanmorph_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_chanmorph_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[sd_channel_module.f90]]
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
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[sd_channel_module.f90#bchsd_a]] - `sd_ch_output`
- [[sd_channel_module.f90#bchsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#bchsd_m]] - `sd_ch_output`
- [[sd_channel_module.f90#bchsd_y]] - `sd_ch_output`
- [[sd_channel_module.f90#chsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#chsdz]] - `sd_ch_output`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

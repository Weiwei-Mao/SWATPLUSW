---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_chanbud_output.f90
note_file: sd_chanbud_output.f90
subroutine: sd_chanbud_output
module:
  - sd_channel_module
  - basin_module
  - time_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - sd_channel_module.f90#ch_sed_bud
  - sd_channel_module.f90#ch_sed_bud_a
  - sd_channel_module.f90#ch_sed_bud_m
  - sd_channel_module.f90#ch_sed_bud_y
  - sd_channel_module.f90#ch_sed_budz
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_chanbud_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_chanbud_output.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
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
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[sd_channel_module.f90#ch_sed_bud]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_a]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_m]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_y]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_budz]] - `channel_sediment_budget_output`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

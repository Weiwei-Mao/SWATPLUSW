---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wetland_output.f90
note_file: wetland_output.f90
subroutine: wetland_output
module:
  - time_module
  - basin_module
  - reservoir_module
  - hydrograph_module
  - water_body_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#resmz
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_a
  - hydrograph_module.f90#wet_in_d
  - hydrograph_module.f90#wet_in_m
  - hydrograph_module.f90#wet_in_y
  - hydrograph_module.f90#wet_out_a
  - hydrograph_module.f90#wet_out_d
  - hydrograph_module.f90#wet_out_m
  - hydrograph_module.f90#wet_out_y
  - time_module.f90#ndays
  - time_module.f90#time
  - water_body_module.f90#wbodz
  - water_body_module.f90#wet_wat_a
  - water_body_module.f90#wet_wat_d
  - water_body_module.f90#wet_wat_m
  - water_body_module.f90#wet_wat_y
input_variables: []
reads: []
writes: []
purpose: ""
---

# wetland_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wetland_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
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
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#resmz]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_a]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_m]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_y]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_a]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_m]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_y]] - `hyd_output`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`
- [[water_body_module.f90#wbodz]] - `water_body`
- [[water_body_module.f90#wet_wat_a]] - `water_body`
- [[water_body_module.f90#wet_wat_d]] - `water_body`
- [[water_body_module.f90#wet_wat_m]] - `water_body`
- [[water_body_module.f90#wet_wat_y]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

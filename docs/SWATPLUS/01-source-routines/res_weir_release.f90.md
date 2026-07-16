---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_weir_release.f90
note_file: res_weir_release.f90
subroutine: res_weir_release
module:
  - reservoir_data_module
  - reservoir_module
  - conditional_module
  - climate_module
  - time_module
  - hydrograph_module
  - water_body_module
  - soil_module
  - hru_module
  - water_allocation_module
  - basin_module
calls: []
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#hru
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#wbody
  - reservoir_data_module.f90#res_weir
  - reservoir_data_module.f90#wet_hyd
  - reservoir_module.f90#wet_ob
  - water_body_module.f90#wbody_wb
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_weir_release

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_weir_release.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[conditional_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_body_module.f90]]
  - [[soil_module.f90]]
  - [[hru_module.f90]]
  - [[water_allocation_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#wbody]] - `hyd_output`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[water_body_module.f90#wbody_wb]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_hydro.f90
note_file: res_hydro.f90
subroutine: res_hydro
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
  - recall_module
  - water_allocation_module
calls: []
uses_variables:
  - climate_module.f90#w
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_res
  - hru_module.f90#mo
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#wbody
  - recall_module.f90#recall_db
  - reservoir_data_module.f90#res_weir
  - reservoir_module.f90#res_ob
  - reservoir_module.f90#wet_ob
  - time_module.f90#time
  - water_allocation_module.f90#wallo
  - water_body_module.f90#wbody_wb
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_hydro

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_hydro.f90`
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
  - [[recall_module.f90]]
  - [[water_allocation_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[res_control.f90]]
- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#wbody]] - `hyd_output`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_body_module.f90#wbody_wb]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

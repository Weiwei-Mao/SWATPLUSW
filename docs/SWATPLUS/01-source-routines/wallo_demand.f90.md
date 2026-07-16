---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_demand.f90
note_file: wallo_demand.f90
subroutine: wallo_demand
module:
  - water_allocation_module
  - hru_module
  - hydrograph_module
  - conditional_module
  - recall_module
  - exco_module
calls:
  - conditions
  - actions
uses_variables:
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_flo
  - conditional_module.f90#dtbl_lum
  - hru_module.f90#mo
  - hydrograph_module.f90#canal_om_out
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#wtp_om_out
  - hydrograph_module.f90#wuse_om_out
  - recall_module.f90#recall_db
  - water_allocation_module.f90#osrc
  - water_allocation_module.f90#trn_m3
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#wallod_out
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_demand

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_demand.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[conditional_module.f90]]
  - [[recall_module.f90]]
  - [[exco_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]

**Called by:**

- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_flo]] - `decision_table`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#canal_om_out]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#wtp_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_out]] - `hyd_output`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[water_allocation_module.f90#osrc]] - `outside_basin_source`
- [[water_allocation_module.f90#trn_m3]] - `real`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

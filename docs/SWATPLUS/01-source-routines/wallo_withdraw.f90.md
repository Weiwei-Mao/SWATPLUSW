---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_withdraw.f90
note_file: wallo_withdraw.f90
subroutine: wallo_withdraw
module:
  - water_allocation_module
  - hydrograph_module
  - aquifer_module
  - reservoir_module
  - time_module
  - recall_module
  - basin_module
calls:
  - gwflow_pump_allo
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_prm
  - basin_module.f90#bsn_cc
  - hydrograph_module.f90#canal_om_stor
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#res
  - hydrograph_module.f90#wal_omd
  - hydrograph_module.f90#wdraw_om
  - hydrograph_module.f90#wtow_om_out
  - hydrograph_module.f90#wtow_om_stor
  - hydrograph_module.f90#wtp_om_out
  - hydrograph_module.f90#wuse_om_out
  - recall_module.f90#recall_db
  - reservoir_module.f90#res_ob
  - time_module.f90#time
  - water_allocation_module.f90#osrc
  - water_allocation_module.f90#trn_m3
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#wallod_out
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_withdraw

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_withdraw.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[hydrograph_module.f90]]
  - [[aquifer_module.f90]]
  - [[reservoir_module.f90]]
  - [[time_module.f90]]
  - [[recall_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_pump_allo.f90]]

**Called by:**

- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[hydrograph_module.f90#canal_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#wal_omd]] - `water_allocation_object`
- [[hydrograph_module.f90#wdraw_om]] - `hyd_output`
- [[hydrograph_module.f90#wtow_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wtow_om_stor]] - `hyd_output`
- [[hydrograph_module.f90#wtp_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_out]] - `hyd_output`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#osrc]] - `outside_basin_source`
- [[water_allocation_module.f90#trn_m3]] - `real`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

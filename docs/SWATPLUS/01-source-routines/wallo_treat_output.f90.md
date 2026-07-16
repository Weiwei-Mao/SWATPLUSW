---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_treat_output.f90
note_file: wallo_treat_output.f90
subroutine: wallo_treat_output
module:
  - time_module
  - hydrograph_module
  - water_allocation_module
  - maximum_data_module
calls: []
uses_variables:
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#wal_tr_oma
  - hydrograph_module.f90#wal_tr_omd
  - hydrograph_module.f90#wal_tr_omm
  - hydrograph_module.f90#wal_tr_omy
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
  - water_allocation_module.f90#om_treat_name
  - water_allocation_module.f90#wtp
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_treat_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_treat_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_allocation_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_oma]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omd]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omm]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omy]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#om_treat_name]] - `character(len=16), dimension(:), allocatable`
- [[water_allocation_module.f90#wtp]] - `water_treatment_use_data`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

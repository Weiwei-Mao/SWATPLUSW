---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_dtbl_actions_init.f90
note_file: hru_dtbl_actions_init.f90
subroutine: hru_dtbl_actions_init
module:
  - conditional_module
  - mgt_operations_module
  - hydrograph_module
  - hru_module
  - plant_module
  - maximum_data_module
  - fertilizer_data_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_lum
  - fertilizer_data_module.f90#fertdb
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mgt_ops
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#chemapp_db
  - mgt_operations_module.f90#sched
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_dtbl_actions_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_dtbl_actions_init.f90`
- **Modules used**:
  - [[conditional_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[maximum_data_module.f90]]
  - [[fertilizer_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

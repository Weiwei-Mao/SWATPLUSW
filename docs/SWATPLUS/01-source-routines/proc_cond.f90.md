---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_cond.f90
note_file: proc_cond.f90
subroutine: proc_cond
module:
  - hru_module
  - mgt_operations_module
  - hydrograph_module
  - maximum_data_module
  - conditional_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_lum
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mgt_ops
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#sched
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_cond

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_cond.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[conditional_module.f90]]
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
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#sched]] - `management_schedule`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

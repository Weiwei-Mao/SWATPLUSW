---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_operatn.f90
note_file: mgt_operatn.f90
subroutine: mgt_operatn
module:
  - mgt_operations_module
  - hru_module
  - plant_module
  - time_module
calls:
  - mgt_sched
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#phubase
  - hru_module.f90#yr_skip
  - mgt_operations_module.f90#mgt
  - mgt_operations_module.f90#sched
  - plant_module.f90#pcom
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs all management operations"
---

# mgt_operatn

> [!info] Summary
> this subroutine performs all management operations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_operatn.f90`
- **Modules used**:
  - [[mgt_operations_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[mgt_sched.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#yr_skip]] - `integer, dimension (:), allocatable`
- [[mgt_operations_module.f90#mgt]] - `management_ops`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[plant_module.f90#pcom]] - `plant_community`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

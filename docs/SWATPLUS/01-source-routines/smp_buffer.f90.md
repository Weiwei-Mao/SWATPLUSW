---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: smp_buffer.f90
note_file: smp_buffer.f90
subroutine: smp_buffer
module:
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#filterw
  - hru_module.f90#ihru
  - hru_module.f90#latno3
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the reduction of nitrates through a riparian; buffer system - developed for Sushama at NC State"
---

# smp_buffer

> [!info] Summary
> this subroutine calculates the reduction of nitrates through a riparian; buffer system - developed for Sushama at NC State

## Basic Information
- **Type**: `subroutine`
- **Source file**: `smp_buffer.f90`
- **Modules used**:
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#filterw]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_crackflow.f90
note_file: sq_crackflow.f90
subroutine: sq_crackflow
module:
  - basin_module
  - hru_module
  - time_module
calls: []
uses_variables:
  - hru_module.f90#hhqday
  - hru_module.f90#ihru
  - hru_module.f90#surfq
  - hru_module.f90#voltot
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this surboutine modifies surface runoff to account for crack flow"
---

# sq_crackflow

> [!info] Summary
> this surboutine modifies surface runoff to account for crack flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_crackflow.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[surface.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hhqday]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#voltot]] - `real`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

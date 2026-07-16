---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_crackvol.f90
note_file: sq_crackvol.f90
subroutine: sq_crackvol
module:
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#volcrmin
  - hru_module.f90#voltot
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this surboutine computes total crack volume for the soil profile and; modifies surface runoff to account for crack flow"
---

# sq_crackvol

> [!info] Summary
> this surboutine computes total crack volume for the soil profile and; modifies surface runoff to account for crack flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_crackvol.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
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
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#volcrmin]] - `real`
- [[hru_module.f90#voltot]] - `real`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

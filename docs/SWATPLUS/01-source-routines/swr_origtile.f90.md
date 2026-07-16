---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_origtile.f90
note_file: swr_origtile.f90
subroutine: swr_origtile
module:
  - hru_module
  - soil_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#qtile
  - hru_module.f90#sdr
  - hru_module.f90#sw_excess
  - hru_module.f90#wt_shall
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes tile drainage using basic tile equations"
---

# swr_origtile

> [!info] Summary
> this subroutine computes tile drainage using basic tile equations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_origtile.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hru_module.f90#sw_excess]] - `real`
- [[hru_module.f90#wt_shall]] - `real`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

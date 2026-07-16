---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_weatgn.f90
note_file: cli_weatgn.f90
subroutine: cli_weatgn
module:
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#idg
  - climate_module.f90#rnd2
  - climate_module.f90#rnd8
  - climate_module.f90#rnd9
  - climate_module.f90#rndseed
  - climate_module.f90#wgncur
  - climate_module.f90#wgnold
input_variables: []
reads: []
writes: []
purpose: "this subroutine generates weather parameters used to simulate the impact; of precipitation on the other climatic processes"
---

# cli_weatgn

> [!info] Summary
> this subroutine generates weather parameters used to simulate the impact; of precipitation on the other climatic processes

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_weatgn.f90`
- **Modules used**:
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[climate_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#idg]] - `integer, dimension (:), allocatable`
- [[climate_module.f90#rnd2]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd8]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd9]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#wgncur]] - `real, dimension (:,:), allocatable`
- [[climate_module.f90#wgnold]] - `real, dimension (:,:), allocatable`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

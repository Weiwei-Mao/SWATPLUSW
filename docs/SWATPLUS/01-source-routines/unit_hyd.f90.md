---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: unit_hyd.f90
note_file: unit_hyd.f90
subroutine: unit_hyd
module:
  - basin_module
  - time_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel"
---

# unit_hyd

> [!info] Summary
> This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel

## Basic Information
- **Type**: `subroutine`
- **Source file**: `unit_hyd.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[unit_hyd_ru_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

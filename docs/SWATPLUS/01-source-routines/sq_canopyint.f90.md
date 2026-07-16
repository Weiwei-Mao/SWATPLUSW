---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_canopyint.f90
note_file: sq_canopyint.f90
subroutine: sq_canopyint
module:
  - basin_module
  - time_module
  - climate_module
  - hru_module
  - plant_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes canopy interception of rainfall; used for methods other than curve number"
---

# sq_canopyint

> [!info] Summary
> this subroutine computes canopy interception of rainfall; used for methods other than curve number

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_canopyint.f90`
- **Modules used**: [[basin_module.f90]], [[time_module.f90]], [[climate_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

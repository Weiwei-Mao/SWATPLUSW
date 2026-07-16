---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_greenampt.f90
note_file: sq_greenampt.f90
subroutine: sq_greenampt
module:
  - urban_data_module
  - climate_module
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - time_module
calls: []
reads: []
writes: []
purpose: "Predicts daily runoff given breakpoint precipitation and snow melt; using the Green & Ampt technique"
---

# sq_greenampt

> [!info] Summary
> Predicts daily runoff given breakpoint precipitation and snow melt; using the Green & Ampt technique

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_greenampt.f90`
- **Modules used**: [[urban_data_module.f90]], [[climate_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]]
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

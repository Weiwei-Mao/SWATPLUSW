---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_pkq.f90
note_file: ero_pkq.f90
subroutine: ero_pkq
module:
  - hru_module
  - hydrograph_module
  - climate_module
  - basin_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the peak runoff rate for each HRU; and the entire subbasin using a modification of the rational formula"
---

# ero_pkq

> [!info] Summary
> this subroutine computes the peak runoff rate for each HRU; and the entire subbasin using a modification of the rational formula

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_pkq.f90`
- **Modules used**: [[hru_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[basin_module.f90]]
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

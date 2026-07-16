---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_ysed.f90
note_file: ero_ysed.f90
subroutine: ero_ysed
module:
  - hru_module
  - soil_module
  - erosion_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation"
---

# ero_ysed

> [!info] Summary
> this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_ysed.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[erosion_module.f90]], [[climate_module.f90]]
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

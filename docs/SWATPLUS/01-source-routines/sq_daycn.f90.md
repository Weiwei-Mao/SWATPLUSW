---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_daycn.f90
note_file: sq_daycn.f90
subroutine: sq_daycn
module:
  - urban_data_module
  - hru_module
calls: []
reads: []
writes: []
purpose: "Predicts daily runoff given daily precipitation and snow melt; using a modified SCS curve number approach"
---

# sq_daycn

> [!info] Summary
> Predicts daily runoff given daily precipitation and snow melt; using a modified SCS curve number approach

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_daycn.f90`
- **Modules used**: [[urban_data_module.f90]], [[hru_module.f90]]
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

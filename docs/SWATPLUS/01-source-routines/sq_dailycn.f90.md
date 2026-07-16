---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_dailycn.f90
note_file: sq_dailycn.f90
subroutine: sq_dailycn
module:
  - basin_module
  - hru_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "Calculates curve number for the day in the HRU"
---

# sq_dailycn

> [!info] Summary
> Calculates curve number for the day in the HRU

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_dailycn.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[soil_module.f90]]
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

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zeroini.f90
note_file: zeroini.f90
subroutine: zeroini
module:
  - hru_module
  - soil_module
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine zeros values for single array variables"
---

# zeroini

> [!info] Summary
> this subroutine zeros values for single array variables

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zeroini.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]]
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

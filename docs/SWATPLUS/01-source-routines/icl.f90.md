---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: icl.f90
note_file: icl.f90
subroutine: icl
module:
  - time_module
calls: []
uses_variables:
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the month and day, given the julian date"
---

# icl

> [!info] Summary
> this subroutine determines the month and day, given the julian date

## Basic Information
- **Type**: `subroutine`
- **Source file**: `icl.f90`
- **Modules used**:
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

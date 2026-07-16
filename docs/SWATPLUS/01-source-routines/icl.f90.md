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
- **Modules used**: [[time_module.f90]]
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

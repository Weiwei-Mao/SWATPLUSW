---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zero1.f90
note_file: zero1.f90
subroutine: zero1
module:
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine initializes the values for some of the arrays"
---

# zero1

> [!info] Summary
> this subroutine initializes the values for some of the arrays

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zero1.f90`
- **Modules used**: [[hru_module.f90]]
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

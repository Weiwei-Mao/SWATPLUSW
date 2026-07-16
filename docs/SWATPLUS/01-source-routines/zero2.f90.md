---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: zero2.f90
note_file: zero2.f90
subroutine: zero2
module:
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine zeros all array values"
---

# zero2

> [!info] Summary
> this subroutine zeros all array values

## Basic Information
- **Type**: `subroutine`
- **Source file**: `zero2.f90`
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

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: xmon.f90
note_file: xmon.f90
subroutine: xmon
module:
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the month, given the julian date and leap; year flag"
---

# xmon

> [!info] Summary
> this subroutine determines the month, given the julian date and leap; year flag

## Basic Information
- **Type**: `subroutine`
- **Source file**: `xmon.f90`
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

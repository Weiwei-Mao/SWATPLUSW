---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: jdt.f90
note_file: jdt.f90
subroutine: jdt
module:
  - time_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the julian date given the month and; the day of the month"
---

# jdt

> [!info] Summary
> this subroutine computes the julian date given the month and; the day of the month

## Basic Information
- **Type**: `subroutine`
- **Source file**: `jdt.f90`
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

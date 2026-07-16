---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: smp_buffer.f90
note_file: smp_buffer.f90
subroutine: smp_buffer
module:
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the reduction of nitrates through a riparian; buffer system - developed for Sushama at NC State"
---

# smp_buffer

> [!info] Summary
> this subroutine calculates the reduction of nitrates through a riparian; buffer system - developed for Sushama at NC State

## Basic Information
- **Type**: `subroutine`
- **Source file**: `smp_buffer.f90`
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

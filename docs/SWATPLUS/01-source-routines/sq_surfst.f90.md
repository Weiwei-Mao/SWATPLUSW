---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_surfst.f90
note_file: sq_surfst.f90
subroutine: sq_surfst
module:
  - basin_module
  - time_module
  - hru_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the net surface runoff reaching the; main channel on a given day. The net amount of water reaching; the main channel can include water in surface runoff from the"
---

# sq_surfst

> [!info] Summary
> this subroutine determines the net surface runoff reaching the; main channel on a given day. The net amount of water reaching; the main channel can include water in surface runoff from the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_surfst.f90`
- **Modules used**: [[basin_module.f90]], [[time_module.f90]], [[hru_module.f90]]
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

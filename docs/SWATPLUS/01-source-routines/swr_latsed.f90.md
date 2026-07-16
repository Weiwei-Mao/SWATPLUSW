---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_latsed.f90
note_file: swr_latsed.f90
subroutine: swr_latsed
module:
  - hru_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the sediment load contributed in lateral flow"
---

# swr_latsed

> [!info] Summary
> this subroutine calculates the sediment load contributed in lateral flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_latsed.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]]
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

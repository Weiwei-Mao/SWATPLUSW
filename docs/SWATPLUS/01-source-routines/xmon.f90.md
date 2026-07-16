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
uses_variables:
  - time_module.f90#ndays
input_variables: []
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
- **Modules used**:
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[cli_tmeas.f90]]
- [[plant_init.f90]]
- [[time_control.f90]]
- [[time_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[time_module.f90#ndays]] - `integer, dimension (13)`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

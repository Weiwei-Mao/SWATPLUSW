---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_bounds_check.f90
note_file: cli_bounds_check.f90
subroutine: cli_bounds_check
module:
  - time_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine checks to see if climate data is in current simulation day"
---

# cli_bounds_check

> [!info] Summary
> this subroutine checks to see if climate data is in current simulation day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_bounds_check.f90`
- **Modules used**: [[time_module.f90]], [[climate_module.f90]]
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

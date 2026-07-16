---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_read_prm.f90
note_file: basin_read_prm.f90
subroutine: basin_read_prm
module:
  - input_file_module
  - basin_module
calls: []
reads:
  - in_basin%parms_bas
writes: []
purpose: ""
---

# basin_read_prm

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_read_prm.f90`
- **Modules used**: [[input_file_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_basin%parms_bas` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

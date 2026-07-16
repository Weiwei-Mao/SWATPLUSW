---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_print_codes_read.f90
note_file: basin_print_codes_read.f90
subroutine: basin_print_codes_read
module:
  - input_file_module
  - basin_module
  - time_module
calls: []
reads:
  - in_sim%prt
writes: []
purpose: ""
---

# basin_print_codes_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_print_codes_read.f90`
- **Modules used**: [[input_file_module.f90]], [[basin_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_sim%prt` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read.f90
note_file: ch_read.f90
subroutine: ch_read
module:
  - basin_module
  - input_file_module
  - channel_data_module
  - maximum_data_module
  - hydrograph_module
  - pesticide_data_module
calls: []
reads:
  - in_cha%dat
writes: []
purpose: ""
---

# ch_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[channel_data_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[pesticide_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cha%dat` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

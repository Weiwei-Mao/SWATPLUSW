---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_temp.f90
note_file: ch_read_temp.f90
subroutine: ch_read_temp
module:
  - basin_module
  - time_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - hydrograph_module
calls: []
reads:
  - in_cha%temp
writes: []
purpose: ""
---

# ch_read_temp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_temp.f90`
- **Modules used**: [[basin_module.f90]], [[time_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[channel_data_module.f90]], [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cha%temp` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

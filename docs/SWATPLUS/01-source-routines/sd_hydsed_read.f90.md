---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_hydsed_read.f90
note_file: sd_hydsed_read.f90
subroutine: sd_hydsed_read
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - time_module
calls: []
reads:
  - in_cha%hyd_sed
  - sed_nut.cha
writes: []
purpose: ""
---

# sd_hydsed_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_hydsed_read.f90`
- **Modules used**: [[input_file_module.f90]], [[sd_channel_module.f90]], [[channel_velocity_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cha%hyd_sed` _(variable; see file.cio)_, `sed_nut.cha`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

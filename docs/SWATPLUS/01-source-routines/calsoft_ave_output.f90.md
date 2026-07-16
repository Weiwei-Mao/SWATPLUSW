---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_ave_output.f90
note_file: calsoft_ave_output.f90
subroutine: calsoft_ave_output
module:
  - sd_channel_module
  - hru_lte_module
  - maximum_data_module
  - calibration_data_module
  - time_module
calls: []
reads: []
writes: []
purpose: ""
---

# calsoft_ave_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_ave_output.f90`
- **Modules used**: [[sd_channel_module.f90]], [[hru_lte_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[time_module.f90]]
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

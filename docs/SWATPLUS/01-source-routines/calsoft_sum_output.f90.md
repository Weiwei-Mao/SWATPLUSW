---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_sum_output.f90
note_file: calsoft_sum_output.f90
subroutine: calsoft_sum_output
module:
  - sd_channel_module
  - hru_lte_module
  - hru_module
  - output_landscape_module
  - maximum_data_module
  - calibration_data_module
calls: []
reads: []
writes: []
purpose: ""
---

# calsoft_sum_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_sum_output.f90`
- **Modules used**: [[sd_channel_module.f90]], [[hru_lte_module.f90]], [[hru_module.f90]], [[output_landscape_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]]
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

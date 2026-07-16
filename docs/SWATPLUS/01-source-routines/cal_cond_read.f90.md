---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_cond_read.f90
note_file: cal_cond_read.f90
subroutine: cal_cond_read
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - conditional_module
calls: []
reads:
  - scen_dtl.upd
writes: []
purpose: "this function computes new parameter value based on; user defined change"
---

# cal_cond_read

> [!info] Summary
> this function computes new parameter value based on; user defined change

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_cond_read.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `scen_dtl.upd`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

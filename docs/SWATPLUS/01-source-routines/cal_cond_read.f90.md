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
uses_variables:
  - calibration_data_module.f90#upd_cond
  - conditional_module.f90#dtbl_scen
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#upd_cond
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
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#upd_cond]] - `update_conditional`
- [[conditional_module.f90#dtbl_scen]] - `decision_table`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#upd_cond]]

## File I/O
- **Reads**:
  - [[scen_dtl.upd]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

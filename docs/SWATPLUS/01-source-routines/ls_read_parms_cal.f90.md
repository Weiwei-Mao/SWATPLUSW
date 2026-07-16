---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ls_read_parms_cal.f90
note_file: ls_read_parms_cal.f90
subroutine: ls_read_lsparms_cal
module:
  - maximum_data_module
  - calibration_data_module
  - input_file_module
calls: []
uses_variables:
  - calibration_data_module.f90#ls_prms
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#ls_prms
reads:
  - in_chg%wb_parms_sft
writes: []
purpose: ""
---

# ls_read_lsparms_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ls_read_parms_cal.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[input_file_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#ls_prms]] - `soft_calib_parms`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#ls_prms]]

## File I/O
- **Reads**:
  - [[wb_parms.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

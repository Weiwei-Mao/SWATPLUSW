---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_parms_cal.f90
note_file: ch_read_parms_cal.f90
subroutine: ch_read_parms_cal
module:
  - calibration_data_module
  - input_file_module
calls: []
uses_variables:
  - calibration_data_module.f90#ch_prms
  - input_file_module.f90#in_chg
input_variables:
  - calibration_data_module.f90#ch_prms
reads:
  - in_chg%ch_sed_parms_sft
writes: []
purpose: ""
---

# ch_read_parms_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_parms_cal.f90`
- **Modules used**:
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
- [[calibration_data_module.f90#ch_prms]] - `soft_calib_parms`
- [[input_file_module.f90#in_chg]] - `input_chg`

**Populated by file reads:**

- [[calibration_data_module.f90#ch_prms]]

## File I/O
- **Reads**:
  - [[ch_sed_parms.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

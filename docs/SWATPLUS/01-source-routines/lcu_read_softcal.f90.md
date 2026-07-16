---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lcu_read_softcal.f90
note_file: lcu_read_softcal.f90
subroutine: lcu_read_softcal
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - hru_module
  - hru_lte_module
  - output_landscape_module
  - basin_module
calls: []
reads:
  - in_chg%water_balance_sft
writes: []
purpose: ""
---

# lcu_read_softcal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lcu_read_softcal.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[hru_lte_module.f90]], [[output_landscape_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_chg%water_balance_sft` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

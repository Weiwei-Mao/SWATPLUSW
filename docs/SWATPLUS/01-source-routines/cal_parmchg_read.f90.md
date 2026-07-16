---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_parmchg_read.f90
note_file: cal_parmchg_read.f90
subroutine: cal_parmchg_read
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - gwflow_module
calls:
  - define_unit_elements
reads:
  - in_chg%cal_upd
writes: []
purpose: "this function computes new parameter value based on; user defined change"
---

# cal_parmchg_read

> [!info] Summary
> this function computes new parameter value based on; user defined change

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_parmchg_read.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[gwflow_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_chg%cal_upd` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

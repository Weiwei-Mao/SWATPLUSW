---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_fr_change.f90
note_file: hru_fr_change.f90
subroutine: hru_fr_change
module:
  - hydrograph_module
  - maximum_data_module
  - dr_module
  - calibration_data_module
  - hru_module
  - reservoir_data_module
  - reservoir_module
  - ru_module
calls: []
reads:
  - ru_elem_upd
  - lsu_elem_upd
writes: []
purpose: ""
---

# hru_fr_change

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_fr_change.f90`
- **Modules used**: [[hydrograph_module.f90]], [[maximum_data_module.f90]], [[dr_module.f90]], [[calibration_data_module.f90]], [[hru_module.f90]], [[reservoir_data_module.f90]], [[reservoir_module.f90]], [[ru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `ru_elem_upd` _(variable; see file.cio)_, `lsu_elem_upd` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

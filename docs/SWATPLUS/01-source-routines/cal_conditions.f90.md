---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_conditions.f90
note_file: cal_conditions.f90
subroutine: cal_conditions
module:
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - hru_lte_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - time_module
  - reservoir_module
  - climate_module
  - landuse_data_module
calls:
  - cal_parm_select
reads: []
writes: []
purpose: ""
---

# cal_conditions

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_conditions.f90`
- **Modules used**: [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[conditional_module.f90]], [[hru_lte_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[time_module.f90]], [[reservoir_module.f90]], [[climate_module.f90]], [[landuse_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cal_parm_select.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

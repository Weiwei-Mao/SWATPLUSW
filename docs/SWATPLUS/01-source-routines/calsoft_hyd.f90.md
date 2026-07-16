---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calsoft_hyd.f90
note_file: calsoft_hyd.f90
subroutine: calsoft_hyd
module:
  - hru_module
  - soil_module
  - plant_module
  - hydrograph_module
  - ru_module
  - aquifer_module
  - channel_module
  - hru_lte_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - reservoir_module
  - organic_mineral_mass_module
  - time_module
calls:
  - re_initialize
  - time_control
  - curno
reads: []
writes: []
purpose: ""
---

# calsoft_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calsoft_hyd.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[hydrograph_module.f90]], [[ru_module.f90]], [[aquifer_module.f90]], [[channel_module.f90]], [[hru_lte_module.f90]], [[sd_channel_module.f90]], [[basin_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[conditional_module.f90]], [[reservoir_module.f90]], [[organic_mineral_mass_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[re_initialize.f90]]
- [[time_control.f90]]
- [[curno.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_parm_select.f90
note_file: cal_parm_select.f90
subroutine: cal_parm_select
module:
  - basin_module
  - channel_data_module
  - reservoir_data_module
  - hru_module
  - soil_module
  - channel_module
  - conditional_module
  - sd_channel_module
  - reservoir_module
  - aquifer_module
  - hru_lte_module
  - organic_mineral_mass_module
  - hydrograph_module
  - pesticide_data_module
  - plant_module
  - plant_data_module
  - gwflow_module
  - carbon_module
  - tillage_data_module
calls:
  - curno
  - soil_awc_init
  - soil_text_init
reads: []
writes: []
purpose: "this subroutine finds the current parameter value based on; user defined change"
---

# cal_parm_select

> [!info] Summary
> this subroutine finds the current parameter value based on; user defined change

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_parm_select.f90`
- **Modules used**: [[basin_module.f90]], [[channel_data_module.f90]], [[reservoir_data_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[channel_module.f90]], [[conditional_module.f90]], [[sd_channel_module.f90]], [[reservoir_module.f90]], [[aquifer_module.f90]], [[hru_lte_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[pesticide_data_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[gwflow_module.f90]], [[carbon_module.f90]], [[tillage_data_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[curno.f90]]
- [[soil_awc_init.f90]]
- [[soil_text_init.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

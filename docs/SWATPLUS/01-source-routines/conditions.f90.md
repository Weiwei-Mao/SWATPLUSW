---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: conditions.f90
note_file: conditions.f90
subroutine: conditions
module:
  - conditional_module
  - climate_module
  - time_module
  - hru_module
  - soil_module
  - plant_module
  - reservoir_module
  - reservoir_data_module
  - sd_channel_module
  - hydrograph_module
  - output_landscape_module
  - aquifer_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - water_allocation_module
calls:
  - cond_real
  - cond_integer
reads: []
writes: []
purpose: ""
---

# conditions

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `conditions.f90`
- **Modules used**: [[conditional_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[reservoir_module.f90]], [[reservoir_data_module.f90]], [[sd_channel_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]], [[aquifer_module.f90]], [[organic_mineral_mass_module.f90]], [[mgt_operations_module.f90]], [[water_allocation_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cond_real.f90]]
- [[cond_integer.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

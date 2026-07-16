---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_allo.f90
note_file: hru_allo.f90
subroutine: hru_allo
module:
  - hru_module
  - hydrograph_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - reservoir_module
  - reservoir_data_module
  - carbon_module
  - plant_module
  - soil_module
  - water_body_module
  - channel_velocity_module
  - res_salt_module
  - res_cs_module
calls: []
reads: []
writes: []
purpose: ""
---

# hru_allo

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_allo.f90`
- **Modules used**: [[hru_module.f90]], [[hydrograph_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]], [[reservoir_module.f90]], [[reservoir_data_module.f90]], [[carbon_module.f90]], [[plant_module.f90]], [[soil_module.f90]], [[water_body_module.f90]], [[channel_velocity_module.f90]], [[res_salt_module.f90]], [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

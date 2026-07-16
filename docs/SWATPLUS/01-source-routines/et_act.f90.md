---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: et_act.f90
note_file: et_act.f90
subroutine: et_act
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - climate_module
  - hydrograph_module
  - water_body_module
  - reservoir_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates potential plant transpiration for Priestley-; Taylor and Hargreaves ET methods, and potential and actual soil; evaporation. NO3 movement into surface soil layer due to evaporation"
---

# et_act

> [!info] Summary
> this subroutine calculates potential plant transpiration for Priestley-; Taylor and Hargreaves ET methods, and potential and actual soil; evaporation. NO3 movement into surface soil layer due to evaporation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `et_act.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[climate_module.f90]], [[hydrograph_module.f90]], [[water_body_module.f90]], [[reservoir_data_module.f90]]
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

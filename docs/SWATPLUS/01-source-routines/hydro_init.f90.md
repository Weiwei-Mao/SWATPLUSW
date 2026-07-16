---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hydro_init.f90
note_file: hydro_init.f90
subroutine: hydro_init
module:
  - hru_module
  - soil_module
  - plant_module
  - climate_module
  - plant_data_module
  - pesticide_data_module
  - basin_module
  - channel_module
  - time_module
  - organic_mineral_mass_module
  - hydrograph_module
  - constituent_mass_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: "This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel"
---

# hydro_init

> [!info] Summary
> This subroutine computes variables related to the watershed hydrology:; the time of concentration for the subbasins, lagged surface runoff,; the coefficient for the peak runoff rate equation, and lateral flow travel

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hydro_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[climate_module.f90]], [[plant_data_module.f90]], [[pesticide_data_module.f90]], [[basin_module.f90]], [[channel_module.f90]], [[time_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[output_landscape_module.f90]]
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

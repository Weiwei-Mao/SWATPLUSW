---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wetland_control.f90
note_file: wetland_control.f90
subroutine: wetland_control
module:
  - reservoir_data_module
  - reservoir_module
  - hru_module
  - conditional_module
  - climate_module
  - hydrograph_module
  - time_module
  - basin_module
  - channel_module
  - water_body_module
  - soil_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - constituent_mass_module
  - aquifer_module
  - gwflow_module
calls:
  - gwflow_wetland
  - res_weir_release
  - conditions
  - res_hydro
  - res_sediment
  - res_nutrient
  - wet_salt
  - wet_cs
  - ero_cfactor
reads: []
writes: []
purpose: ""
---

# wetland_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wetland_control.f90`
- **Modules used**: [[reservoir_data_module.f90]], [[reservoir_module.f90]], [[hru_module.f90]], [[conditional_module.f90]], [[climate_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]], [[basin_module.f90]], [[channel_module.f90]], [[water_body_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[mgt_operations_module.f90]], [[constituent_mass_module.f90]], [[aquifer_module.f90]], [[gwflow_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_wetland.f90]]
- [[res_weir_release.f90]]
- [[conditions.f90]]
- [[res_hydro.f90]]
- [[res_sediment.f90]]
- [[res_nutrient.f90]]
- [[wet_salt.f90]]
- [[wet_cs.f90]]
- [[ero_cfactor.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

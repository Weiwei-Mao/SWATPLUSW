---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pathogen_init.f90
note_file: pathogen_init.f90
subroutine: pathogen_init
module:
  - hru_module
  - soil_module
  - plant_module
  - pathogen_data_module
  - channel_module
  - basin_module
  - conditional_module
  - organic_mineral_mass_module
  - hydrograph_module
  - constituent_mass_module
  - output_ls_pathogen_module
calls: []
reads: []
writes: []
purpose: "this subroutine calls subroutines which read input data for the; databases and the HRUs"
---

# pathogen_init

> [!info] Summary
> this subroutine calls subroutines which read input data for the; databases and the HRUs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pathogen_init.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[pathogen_data_module.f90]], [[channel_module.f90]], [[basin_module.f90]], [[conditional_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pathogen_module.f90]]
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

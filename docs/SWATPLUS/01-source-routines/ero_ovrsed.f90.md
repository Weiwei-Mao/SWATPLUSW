---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_ovrsed.f90
note_file: ero_ovrsed.f90
subroutine: ero_ovrsed
module:
  - urban_data_module
  - basin_module
  - climate_module
  - time_module
  - hydrograph_module
  - hru_module
  - soil_module
  - plant_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes splash erosion by raindrop impact and flow erosion by overland flow"
---

# ero_ovrsed

> [!info] Summary
> this subroutine computes splash erosion by raindrop impact and flow erosion by overland flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_ovrsed.f90`
- **Modules used**: [[urban_data_module.f90]], [[basin_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[organic_mineral_mass_module.f90]]
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

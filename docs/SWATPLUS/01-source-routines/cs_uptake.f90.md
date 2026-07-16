---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_uptake.f90
note_file: cs_uptake.f90
subroutine: cs_uptake
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
  - output_landscape_module
  - cs_module
  - constituent_mass_module
  - plant_data_module
  - plant_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this subroutine simulates constituent uptake in the root zone"
---

# cs_uptake

> [!info] Summary
> this subroutine simulates constituent uptake in the root zone

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_uptake.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]], [[cs_module.f90]], [[constituent_mass_module.f90]], [[plant_data_module.f90]], [[plant_module.f90]], [[soil_module.f90]]
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

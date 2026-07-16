---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_mortality.f90
note_file: pl_mortality.f90
subroutine: pl_mortality
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - soil_module
calls: []
reads: []
writes: []
purpose: ""
---

# pl_mortality

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_mortality.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[carbon_module.f90]], [[organic_mineral_mass_module.f90]], [[soil_module.f90]]
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

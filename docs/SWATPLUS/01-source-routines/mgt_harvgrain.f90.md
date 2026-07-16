---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_harvgrain.f90
note_file: mgt_harvgrain.f90
subroutine: mgt_harvgrain
module:
  - basin_module
  - hru_module
  - plant_module
  - plant_data_module
  - mgt_operations_module
  - carbon_module
  - organic_mineral_mass_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine performs the harvest grain only operation"
---

# mgt_harvgrain

> [!info] Summary
> this subroutine performs the harvest grain only operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_harvgrain.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[carbon_module.f90]], [[organic_mineral_mass_module.f90]], [[constituent_mass_module.f90]]
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

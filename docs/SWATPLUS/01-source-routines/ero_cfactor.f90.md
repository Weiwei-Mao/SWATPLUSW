---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_cfactor.f90
note_file: ero_cfactor.f90
subroutine: ero_cfactor
module:
  - basin_module
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - time_module
  - erosion_module
  - utils
calls: []
reads: []
writes: []
purpose: "this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation"
---

# ero_cfactor

> [!info] Summary
> this subroutine predicts daily soil loss caused by water erosion; using the modified universal soil loss equation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_cfactor.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[organic_mineral_mass_module.f90]], [[time_module.f90]], [[erosion_module.f90]], [[utils.f90]]
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

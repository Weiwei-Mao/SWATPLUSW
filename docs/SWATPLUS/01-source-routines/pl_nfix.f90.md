---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nfix.f90
note_file: pl_nfix.f90
subroutine: pl_nfix
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine estimates nitrogen fixation by legumes"
---

# pl_nfix

> [!info] Summary
> this subroutine estimates nitrogen fixation by legumes

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nfix.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]]
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

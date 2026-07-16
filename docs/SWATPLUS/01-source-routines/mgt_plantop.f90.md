---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_plantop.f90
note_file: mgt_plantop.f90
subroutine: mgt_plantop
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine performs the plant operation"
---

# mgt_plantop

> [!info] Summary
> this subroutine performs the plant operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_plantop.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]], [[organic_mineral_mass_module.f90]]
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

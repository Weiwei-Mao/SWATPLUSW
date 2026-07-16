---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: obj_output.f90
note_file: obj_output.f90
subroutine: obj_output
module:
  - time_module
  - hydrograph_module
  - soil_module
  - hru_module
  - organic_mineral_mass_module
  - plant_module
calls: []
reads: []
writes: []
purpose: ""
---

# obj_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `obj_output.f90`
- **Modules used**: [[time_module.f90]], [[hydrograph_module.f90]], [[soil_module.f90]], [[hru_module.f90]], [[organic_mineral_mass_module.f90]], [[plant_module.f90]]
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

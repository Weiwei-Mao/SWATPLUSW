---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_psed.f90
note_file: nut_psed.f90
subroutine: nut_psed
module:
  - hru_module
  - soil_module
  - plant_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of organic and mineral phosphorus; attached to sediment in surface runoff"
---

# nut_psed

> [!info] Summary
> this subroutine calculates the amount of organic and mineral phosphorus; attached to sediment in surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_psed.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[organic_mineral_mass_module.f90]]
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

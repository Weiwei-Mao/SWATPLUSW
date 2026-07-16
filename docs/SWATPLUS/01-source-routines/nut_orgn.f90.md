---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_orgn.f90
note_file: nut_orgn.f90
subroutine: nut_orgn
module:
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of organic nitrogen removed in; surface runoff"
---

# nut_orgn

> [!info] Summary
> this subroutine calculates the amount of organic nitrogen removed in; surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_orgn.f90`
- **Modules used**: [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]]
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

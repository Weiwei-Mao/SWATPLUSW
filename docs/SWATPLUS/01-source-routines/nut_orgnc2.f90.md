---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_orgnc2.f90
note_file: nut_orgnc2.f90
subroutine: nut_orgnc2
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - plant_module
  - plant_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of organic nitrogen removed in; surface runoff - when using CSWAT==2 it"
---

# nut_orgnc2

> [!info] Summary
> this subroutine calculates the amount of organic nitrogen removed in; surface runoff - when using CSWAT==2 it

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_orgnc2.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[plant_module.f90]], [[plant_data_module.f90]]
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

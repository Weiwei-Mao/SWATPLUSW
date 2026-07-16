---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_pminrl.f90
note_file: nut_pminrl.f90
subroutine: nut_pminrl
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes p flux between the labile, active mineral; and stable mineral p pools."
---

# nut_pminrl

> [!info] Summary
> this subroutine computes p flux between the labile, active mineral; and stable mineral p pools.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_pminrl.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[output_landscape_module.f90]]
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

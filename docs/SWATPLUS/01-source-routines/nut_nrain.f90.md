---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_nrain.f90
note_file: nut_nrain.f90
subroutine: nut_nrain
module:
  - basin_module
  - organic_mineral_mass_module
  - hydrograph_module
  - hru_module
  - climate_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: "this subroutine adds nitrate from rainfall to the soil profile"
---

# nut_nrain

> [!info] Summary
> this subroutine adds nitrate from rainfall to the soil profile

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_nrain.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[climate_module.f90]], [[output_landscape_module.f90]]
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

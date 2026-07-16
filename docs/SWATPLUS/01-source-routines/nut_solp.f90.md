---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_solp.f90
note_file: nut_solp.f90
subroutine: nut_solp
module:
  - basin_module
  - organic_mineral_mass_module
  - gwflow_module
  - hru_module
  - soil_module
  - output_landscape_module
  - hydrograph_module
  - utils
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of phosphorus lost from the soil; profile in runoff and the movement of soluble phosphorus from the first; to the second layer via percolation"
---

# nut_solp

> [!info] Summary
> this subroutine calculates the amount of phosphorus lost from the soil; profile in runoff and the movement of soluble phosphorus from the first; to the second layer via percolation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_solp.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[gwflow_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[output_landscape_module.f90]], [[hydrograph_module.f90]], [[utils.f90]]
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

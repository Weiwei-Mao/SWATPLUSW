---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: et_pot.f90
note_file: et_pot.f90
subroutine: et_pot
module:
  - plant_data_module
  - basin_module
  - hydrograph_module
  - climate_module
  - hru_module
  - plant_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates potential evapotranspiration using one; of three methods. If Penman-Monteith is being used, potential plant; transpiration is also calculated."
---

# et_pot

> [!info] Summary
> this subroutine calculates potential evapotranspiration using one; of three methods. If Penman-Monteith is being used, potential plant; transpiration is also calculated.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `et_pot.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]], [[climate_module.f90]], [[hru_module.f90]], [[plant_module.f90]]
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

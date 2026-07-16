---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_satexcess.f90
note_file: swr_satexcess.f90
subroutine: swr_satexcess
module:
  - hru_module
  - soil_module
  - hydrograph_module
  - basin_module
  - organic_mineral_mass_module
  - gwflow_module
  - reservoir_module
calls: []
reads: []
writes: []
purpose: "this subroutine moves water to upper layers if saturated and can't perc"
---

# swr_satexcess

> [!info] Summary
> this subroutine moves water to upper layers if saturated and can't perc

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_satexcess.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[hydrograph_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[gwflow_module.f90]], [[reservoir_module.f90]]
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

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sim_initday.f90
note_file: sim_initday.f90
subroutine: sim_initday
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - hydrograph_module
  - reservoir_module
  - maximum_data_module
  - res_cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine initialized arrays at the beginning of the day"
---

# sim_initday

> [!info] Summary
> this subroutine initialized arrays at the beginning of the day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sim_initday.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[hydrograph_module.f90]], [[reservoir_module.f90]], [[maximum_data_module.f90]], [[res_cs_module.f90]]
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

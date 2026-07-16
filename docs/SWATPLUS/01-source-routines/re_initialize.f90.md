---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: re_initialize.f90
note_file: re_initialize.f90
subroutine: re_initialize
module:
  - hru_module
  - soil_module
  - plant_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - hydrograph_module
  - hru_lte_module
  - sd_channel_module
  - aquifer_module
calls: []
reads: []
writes: []
purpose: ""
---

# re_initialize

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `re_initialize.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[organic_mineral_mass_module.f90]], [[mgt_operations_module.f90]], [[hydrograph_module.f90]], [[hru_lte_module.f90]], [[sd_channel_module.f90]], [[aquifer_module.f90]]
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

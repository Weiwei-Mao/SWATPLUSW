---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: stmp_solt.f90
note_file: stmp_solt.f90
subroutine: stmp_solt
module:
  - climate_module
  - septic_data_module
  - hru_module
  - soil_module
  - time_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine estimates daily average temperature at the bottom; of each soil layer"
---

# stmp_solt

> [!info] Summary
> this subroutine estimates daily average temperature at the bottom; of each soil layer

## Basic Information
- **Type**: `subroutine`
- **Source file**: `stmp_solt.f90`
- **Modules used**: [[climate_module.f90]], [[septic_data_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]], [[organic_mineral_mass_module.f90]]
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

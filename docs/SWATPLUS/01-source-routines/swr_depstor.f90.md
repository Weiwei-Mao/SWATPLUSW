---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_depstor.f90
note_file: swr_depstor.f90
subroutine: swr_depstor
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes maximum surface depressional storage depth based on; random and oriented roughness and slope steepness"
---

# swr_depstor

> [!info] Summary
> this subroutine computes maximum surface depressional storage depth based on; random and oriented roughness and slope steepness

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_depstor.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]]
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

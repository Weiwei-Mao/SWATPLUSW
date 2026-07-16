---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: albedo.f90
note_file: albedo.f90
subroutine: albedo
module:
  - hru_module
  - soil_module
  - plant_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates albedo in the HRU for the day"
---

# albedo

> [!info] Summary
> this subroutine calculates albedo in the HRU for the day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `albedo.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[organic_mineral_mass_module.f90]]
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

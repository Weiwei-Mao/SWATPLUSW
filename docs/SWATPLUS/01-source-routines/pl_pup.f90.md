---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_pup.f90
note_file: pl_pup.f90
subroutine: pl_pup
module:
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - output_landscape_module
  - utils
calls:
  - nuts
reads: []
writes: []
purpose: "this subroutine calculates plant phosphorus uptake"
---

# pl_pup

> [!info] Summary
> this subroutine calculates plant phosphorus uptake

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_pup.f90`
- **Modules used**: [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[output_landscape_module.f90]], [[utils.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[nuts.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

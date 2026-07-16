---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_nup.f90
note_file: pl_nup.f90
subroutine: pl_nup
module:
  - plant_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - output_landscape_module
calls:
  - pl_nfix
  - nuts
reads: []
writes: []
purpose: "This subroutine calculates plant nitrogen uptake"
---

# pl_nup

> [!info] Summary
> This subroutine calculates plant nitrogen uptake

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_nup.f90`
- **Modules used**: [[plant_data_module.f90]], [[basin_module.f90]], [[organic_mineral_mass_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[plant_module.f90]], [[output_landscape_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_nfix.f90]]
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

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nut_denit.f90
note_file: nut_denit.f90
subroutine: nut_denit
module:
  - basin_module
  - organic_mineral_mass_module
  - soil_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - organic_mineral_mass_module.f90#soil1
input_variables: []
reads: []
writes: []
purpose: ""
---

# nut_denit

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nut_denit.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rls_routeaqu.f90
note_file: rls_routeaqu.f90
subroutine: rls_routeaqu
module:
  - hru_module
  - soil_module
  - hydrograph_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hydrograph_module.f90#ob
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# rls_routeaqu

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rls_routeaqu.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[hydrograph_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

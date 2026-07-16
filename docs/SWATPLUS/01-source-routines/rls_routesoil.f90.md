---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rls_routesoil.f90
note_file: rls_routesoil.f90
subroutine: rls_routesoil
module:
  - hru_module
  - soil_module
  - hydrograph_module
calls: []
uses_variables:
  - hru_module.f90#ihru
  - hru_module.f90#latqrunon
  - hydrograph_module.f90#ob
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: ""
---

# rls_routesoil

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rls_routesoil.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[hru_module.f90#latqrunon]] - `real`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

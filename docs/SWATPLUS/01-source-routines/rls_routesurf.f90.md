---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rls_routesurf.f90
note_file: rls_routesurf.f90
subroutine: rls_routesurf
module:
  - hru_module
  - hydrograph_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ls_overq
  - hru_module.f90#precip_eff
  - hru_module.f90#usle_cfac
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ts
input_variables: []
reads: []
writes: []
purpose: ""
---

# rls_routesurf

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rls_routesurf.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
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
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ls_overq]] - `real`
- [[hru_module.f90#precip_eff]] - `real`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ts]] - `timestep`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

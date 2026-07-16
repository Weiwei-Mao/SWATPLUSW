---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_eiusle.f90
note_file: ero_eiusle.f90
subroutine: ero_eiusle
module:
  - climate_module
  - hydrograph_module
  - hru_module
calls: []
uses_variables:
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#usle_ei
  - hru_module.f90#usle_eifac
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
input_variables: []
reads: []
writes: []
purpose: "This subroutine computes the USLE erosion index (EI)"
---

# ero_eiusle

> [!info] Summary
> This subroutine computes the USLE erosion index (EI)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_eiusle.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[surface.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#usle_ei]] - `real`
- [[hru_module.f90#usle_eifac]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

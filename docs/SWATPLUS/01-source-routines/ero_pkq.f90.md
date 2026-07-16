---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_pkq.f90
note_file: ero_pkq.f90
subroutine: ero_pkq
module:
  - hru_module
  - hydrograph_module
  - climate_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#qday
  - hru_module.f90#qp_cms
  - hru_module.f90#tconc
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes the peak runoff rate for each HRU; and the entire subbasin using a modification of the rational formula"
---

# ero_pkq

> [!info] Summary
> this subroutine computes the peak runoff rate for each HRU; and the entire subbasin using a modification of the rational formula

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_pkq.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[basin_module.f90]]
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
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#qday]] - `real`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_urban.f90
note_file: hru_urban.f90
subroutine: hru_urban
module:
  - hru_module
  - urban_data_module
  - hydrograph_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#w
  - climate_module.f90#wst
  - hru_module.f90#clayld
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#luse
  - hru_module.f90#qp_cms
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#surfq
  - hru_module.f90#surqno3
  - hru_module.f90#surqsolp
  - hru_module.f90#tconc
  - hru_module.f90#twash
  - hru_module.f90#ulu
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes loadings from urban areas using the; USGS regression equations or a build-up/wash-off algorithm"
---

# hru_urban

> [!info] Summary
> this subroutine computes loadings from urban areas using the; USGS regression equations or a build-up/wash-off algorithm

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_urban.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[urban_data_module.f90]]
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
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#twash]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ulu]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

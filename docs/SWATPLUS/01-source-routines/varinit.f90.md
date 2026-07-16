---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: varinit.f90
note_file: varinit.f90
subroutine: varinit
module:
  - time_module
  - hru_module
  - soil_module
  - hydrograph_module
calls: []
uses_variables:
  - hru_module.f90#albday
  - hru_module.f90#bioday
  - hru_module.f90#bsprev
  - hru_module.f90#canev
  - hru_module.f90#enratio
  - hru_module.f90#ep_day
  - hru_module.f90#ep_max
  - hru_module.f90#es_day
  - hru_module.f90#etday
  - hru_module.f90#fertn
  - hru_module.f90#fertp
  - hru_module.f90#fixn
  - hru_module.f90#grazn
  - hru_module.f90#grazp
  - hru_module.f90#hhqday
  - hru_module.f90#hhsedy
  - hru_module.f90#ihru
  - hru_module.f90#inflpcp
  - hru_module.f90#latqrunon
  - hru_module.f90#ls_overq
  - hru_module.f90#lyrtile
  - hru_module.f90#pet_day
  - hru_module.f90#qday
  - hru_module.f90#qp_cms
  - hru_module.f90#qtile
  - hru_module.f90#sepday
  - hru_module.f90#snoev
  - hru_module.f90#snofall
  - hru_module.f90#snomlt
  - hru_module.f90#sw_excess
  - hru_module.f90#ubnrunoff
  - hru_module.f90#ubntss
  - hru_module.f90#uno3d
  - hru_module.f90#usle
  - hru_module.f90#usle_ei
  - hru_module.f90#voltot
  - hru_module.f90#vpd
  - hydrograph_module.f90#wet_seep_day
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes variables for the daily simulation of the; land phase of the hydrologic cycle (the subbasin command loop)"
---

# varinit

> [!info] Summary
> this subroutine initializes variables for the daily simulation of the; land phase of the hydrologic cycle (the subbasin command loop)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `varinit.f90`
- **Modules used**:
  - [[time_module.f90]]
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
- [[hru_module.f90#albday]] - `real`
- [[hru_module.f90#bioday]] - `real`
- [[hru_module.f90#bsprev]] - `real`
- [[hru_module.f90#canev]] - `real`
- [[hru_module.f90#enratio]] - `real`
- [[hru_module.f90#ep_day]] - `real`
- [[hru_module.f90#ep_max]] - `real`
- [[hru_module.f90#es_day]] - `real`
- [[hru_module.f90#etday]] - `real`
- [[hru_module.f90#fertn]] - `real`
- [[hru_module.f90#fertp]] - `real`
- [[hru_module.f90#fixn]] - `real`
- [[hru_module.f90#grazn]] - `real`
- [[hru_module.f90#grazp]] - `real`
- [[hru_module.f90#hhqday]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhsedy]] - `real, dimension(:,:), allocatable`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#inflpcp]] - `real`
- [[hru_module.f90#latqrunon]] - `real`
- [[hru_module.f90#ls_overq]] - `real`
- [[hru_module.f90#lyrtile]] - `real`
- [[hru_module.f90#pet_day]] - `real`
- [[hru_module.f90#qday]] - `real`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sepday]] - `real`
- [[hru_module.f90#snoev]] - `real`
- [[hru_module.f90#snofall]] - `real`
- [[hru_module.f90#snomlt]] - `real`
- [[hru_module.f90#sw_excess]] - `real`
- [[hru_module.f90#ubnrunoff]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubntss]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle]] - `real`
- [[hru_module.f90#usle_ei]] - `real`
- [[hru_module.f90#voltot]] - `real`
- [[hru_module.f90#vpd]] - `real`
- [[hydrograph_module.f90#wet_seep_day]] - `hyd_output`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

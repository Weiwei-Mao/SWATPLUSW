---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sim_initday.f90
note_file: sim_initday.f90
subroutine: sim_initday
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - hydrograph_module
  - reservoir_module
  - maximum_data_module
  - res_cs_module
calls: []
uses_variables:
  - hru_module.f90#cbodu
  - hru_module.f90#chl_a
  - hru_module.f90#clayld
  - hru_module.f90#cnday
  - hru_module.f90#doxq
  - hru_module.f90#grayld
  - hru_module.f90#gwsoiln
  - hru_module.f90#gwsoilp
  - hru_module.f90#gwsoilq
  - hru_module.f90#gwupcs
  - hru_module.f90#gwupsalt
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#irgwcs
  - hru_module.f90#irswcs
  - hru_module.f90#lagyld
  - hru_module.f90#latno3
  - hru_module.f90#latq
  - hru_module.f90#latqcs
  - hru_module.f90#latqsalt
  - hru_module.f90#nplnt
  - hru_module.f90#perccs
  - hru_module.f90#percn
  - hru_module.f90#percsalt
  - hru_module.f90#pplnt
  - hru_module.f90#qdr
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#satexn
  - hru_module.f90#satexq
  - hru_module.f90#sedmcs
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#sepbtm
  - hru_module.f90#silyld
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - hru_module.f90#surfq
  - hru_module.f90#surqcs
  - hru_module.f90#surqno3
  - hru_module.f90#surqsalt
  - hru_module.f90#surqsolp
  - hru_module.f90#tilecs
  - hru_module.f90#tileno3
  - hru_module.f90#tilesalt
  - hru_module.f90#ubnrunoff
  - hru_module.f90#ubntss
  - hru_module.f90#urbqcs
  - hru_module.f90#urbqsalt
  - hru_module.f90#wetqcs
  - hru_module.f90#wetqsalt
  - hru_module.f90#wtspcs
  - hru_module.f90#wtspsalt
  - hydrograph_module.f90#sp_ob
  - organic_mineral_mass_module.f90#soil1
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine initialized arrays at the beginning of the day"
---

# sim_initday

> [!info] Summary
> this subroutine initialized arrays at the beginning of the day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sim_initday.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[carbon_module.f90]]
  - [[hydrograph_module.f90]]
  - [[reservoir_module.f90]]
  - [[maximum_data_module.f90]]
  - [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#cbodu]] - `real, dimension (:), allocatable`
- [[hru_module.f90#chl_a]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cnday]] - `real, dimension (:), allocatable`
- [[hru_module.f90#doxq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#grayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwsoiln]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwsoilp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwsoilq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwupcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#gwupsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#irgwcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#irswcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#latqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#nplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#perccs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#percn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#percsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#pplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qdr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#satexn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#satexq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedmcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sepbtm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilecs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#tileno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilesalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#ubnrunoff]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubntss]] - `real, dimension (:), allocatable`
- [[hru_module.f90#urbqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#urbqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wtspcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wtspsalt]] - `real, dimension (:,:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

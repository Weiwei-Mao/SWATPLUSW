---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_hyds.f90
note_file: hru_hyds.f90
subroutine: hru_hyds
module:
  - hru_module
  - hydrograph_module
  - basin_module
  - time_module
  - constituent_mass_module
  - output_landscape_module
  - output_ls_pesticide_module
  - climate_module
calls:
  - flow_hyd_ru_hru
uses_variables:
  - basin_module.f90#bsn_cc
  - climate_module.f90#w
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - hru_module.f90#cbodu
  - hru_module.f90#chl_a
  - hru_module.f90#clayld
  - hru_module.f90#doxq
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#latno3
  - hru_module.f90#latq
  - hru_module.f90#latqcs
  - hru_module.f90#latqsalt
  - hru_module.f90#perccs
  - hru_module.f90#percn
  - hru_module.f90#percsalt
  - hru_module.f90#qday
  - hru_module.f90#qp_cms
  - hru_module.f90#qtile
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#satexq_chan
  - hru_module.f90#sedmcs
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#sepbtm
  - hru_module.f90#silyld
  - hru_module.f90#snomlt
  - hru_module.f90#surqcs
  - hru_module.f90#surqno3
  - hru_module.f90#surqsalt
  - hru_module.f90#surqsolp
  - hru_module.f90#tconc
  - hru_module.f90#tilecs
  - hru_module.f90#tileno3
  - hru_module.f90#tilesalt
  - hru_module.f90#urbqcs
  - hru_module.f90#urbqsalt
  - hru_module.f90#wetqcs
  - hru_module.f90#wetqsalt
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - output_landscape_module.f90#hls_d
  - output_ls_pesticide_module.f90#hpestb_d
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine summarizes data for subbasins with multiple HRUs and; prints the daily output.hru file"
---

# hru_hyds

> [!info] Summary
> this subroutine summarizes data for subbasins with multiple HRUs and; prints the daily output.hru file

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_hyds.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_landscape_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[flow_hyd_ru_hru.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[climate_module.f90#w]] - `weather_daily`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hru_module.f90#cbodu]] - `real, dimension (:), allocatable`
- [[hru_module.f90#chl_a]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#doxq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#latqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#perccs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#percn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#percsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#qday]] - `real`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#qtile]] - `real`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#satexq_chan]] - `real`
- [[hru_module.f90#sedmcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sepbtm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#snomlt]] - `real`
- [[hru_module.f90#surqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilecs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#tileno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilesalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#urbqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#urbqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqsalt]] - `real, dimension (:,:), allocatable`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

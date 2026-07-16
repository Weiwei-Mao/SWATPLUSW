---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_conc_init.f90
note_file: time_conc_init.f90
subroutine: time_conc_init
module:
  - ru_module
  - hru_module
  - hydrograph_module
  - topography_data_module
  - time_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#brt
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#luse
  - hru_module.f90#t_ov
  - hru_module.f90#tconc
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - ru_module.f90#iru
  - ru_module.f90#ru
  - ru_module.f90#ru_n
  - ru_module.f90#ru_tc
  - time_module.f90#time
  - topography_data_module.f90#topo_db
input_variables: []
reads: []
writes: []
purpose: ""
---

# time_conc_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_conc_init.f90`
- **Modules used**:
  - [[ru_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[topography_data_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#brt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#t_ov]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_n]] - `real, dimension (:), allocatable`
- [[ru_module.f90#ru_tc]] - `real, dimension (:), allocatable`
- [[time_module.f90#time]] - `time_current`
- [[topography_data_module.f90#topo_db]] - `topography_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

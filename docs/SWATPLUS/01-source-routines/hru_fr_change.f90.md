---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_fr_change.f90
note_file: hru_fr_change.f90
subroutine: hru_fr_change
module:
  - hydrograph_module
  - maximum_data_module
  - dr_module
  - calibration_data_module
  - hru_module
  - reservoir_data_module
  - reservoir_module
  - ru_module
calls: []
uses_variables:
  - calibration_data_module.f90#lsu_elem
  - dr_module.f90#dr_db
  - dr_module.f90#dr_om_num
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#luse
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - hydrograph_module.f90#sp_ob
  - maximum_data_module.f90#db_mx
  - reservoir_data_module.f90#wet_dat
  - reservoir_data_module.f90#wet_hyd
  - reservoir_module.f90#wet_ob
  - ru_module.f90#iru
  - ru_module.f90#ru
  - ru_module.f90#ru_n
input_variables:
  - calibration_data_module.f90#lsu_elem
  - hydrograph_module.f90#ru_elem
reads:
  - ru_elem_upd
  - lsu_elem_upd
writes: []
purpose: ""
---

# hru_fr_change

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_fr_change.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[dr_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hru_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[ru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[dr_module.f90#dr_db]] - `delivery_ratio_datafiles`
- [[dr_module.f90#dr_om_num]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_n]] - `real, dimension (:), allocatable`

**Populated by file reads:**

- [[calibration_data_module.f90#lsu_elem]]
- [[hydrograph_module.f90#ru_elem]]

## File I/O
- **Reads**:
  - `ru_elem_upd` _(variable; see [[file.cio]])_
  - `lsu_elem_upd` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

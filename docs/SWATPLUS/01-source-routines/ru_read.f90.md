---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_read.f90
note_file: ru_read.f90
subroutine: ru_read
module:
  - basin_module
  - input_file_module
  - time_module
  - ru_module
  - hydrograph_module
  - maximum_data_module
  - topography_data_module
  - constituent_mass_module
  - salt_module
  - cs_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rucsb_a
  - constituent_mass_module.f90#rucsb_d
  - constituent_mass_module.f90#rucsb_m
  - constituent_mass_module.f90#rucsb_y
  - constituent_mass_module.f90#rusaltb_a
  - constituent_mass_module.f90#rusaltb_d
  - constituent_mass_module.f90#rusaltb_m
  - constituent_mass_module.f90#rusaltb_y
  - cs_module.f90#ru_hru_csb_a
  - cs_module.f90#ru_hru_csb_d
  - cs_module.f90#ru_hru_csb_m
  - cs_module.f90#ru_hru_csb_y
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ru_a
  - hydrograph_module.f90#ru_d
  - hydrograph_module.f90#ru_m
  - hydrograph_module.f90#ru_y
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_ru
  - maximum_data_module.f90#db_mx
  - ru_module.f90#iru
  - ru_module.f90#itsb
  - ru_module.f90#mru_db
  - ru_module.f90#ru
  - ru_module.f90#ru_n
  - ru_module.f90#ru_tc
  - salt_module.f90#ru_hru_saltb_a
  - salt_module.f90#ru_hru_saltb_d
  - salt_module.f90#ru_hru_saltb_m
  - salt_module.f90#ru_hru_saltb_y
  - topography_data_module.f90#field_db
  - topography_data_module.f90#topo_db
input_variables:
  - ru_module.f90#ru
reads:
  - in_ru%ru
writes: []
purpose: ""
---

# ru_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[time_module.f90]]
  - [[ru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
  - [[topography_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[salt_module.f90]]
  - [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hyd_connect.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rucsb_a]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rucsb_d]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rucsb_m]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rucsb_y]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_a]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_d]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_m]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_y]] - `all_constituent_hydrograph`
- [[cs_module.f90#ru_hru_csb_a]] - `object_cs_balance`
- [[cs_module.f90#ru_hru_csb_d]] - `object_cs_balance`
- [[cs_module.f90#ru_hru_csb_m]] - `object_cs_balance`
- [[cs_module.f90#ru_hru_csb_y]] - `object_cs_balance`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ru_a]] - `hyd_output`
- [[hydrograph_module.f90#ru_d]] - `hyd_output`
- [[hydrograph_module.f90#ru_m]] - `hyd_output`
- [[hydrograph_module.f90#ru_y]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_ru]] - `input_ru`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#itsb]] - `integer, dimension (:), allocatable`
- [[ru_module.f90#mru_db]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_n]] - `real, dimension (:), allocatable`
- [[ru_module.f90#ru_tc]] - `real, dimension (:), allocatable`
- [[salt_module.f90#ru_hru_saltb_a]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_d]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_m]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_y]] - `object_salt_balance`
- [[topography_data_module.f90#field_db]] - `fields_db`
- [[topography_data_module.f90#topo_db]] - `topography_db`

**Populated by file reads:**

- [[ru_module.f90#ru]]

## File I/O
- **Reads**:
  - [[rout_unit.rtu]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

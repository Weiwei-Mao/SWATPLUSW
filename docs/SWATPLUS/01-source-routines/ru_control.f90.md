---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ru_control.f90
note_file: ru_control.f90
subroutine: ru_control
module:
  - hru_module
  - ru_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - output_landscape_module
  - salt_module
  - cs_module
calls:
  - flow_hyd_ru_hru
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#rucsb_d
  - constituent_mass_module.f90#rusaltb_d
  - cs_module.f90#hcsb_d
  - cs_module.f90#ru_hru_csb_d
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#delrto
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#ht3
  - hydrograph_module.f90#ht4
  - hydrograph_module.f90#ht5
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ru_d
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - ru_module.f90#iru
  - ru_module.f90#ru
  - ru_module.f90#ru_tc
  - salt_module.f90#hsaltb_d
  - salt_module.f90#ru_hru_saltb_d
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# ru_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ru_control.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[ru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_landscape_module.f90]]
  - [[salt_module.f90]]
  - [[cs_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[flow_hyd_ru_hru.f90]]

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rucsb_d]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#rusaltb_d]] - `all_constituent_hydrograph`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[cs_module.f90#ru_hru_csb_d]] - `object_cs_balance`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#delrto]] - `hyd_output`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#ht3]] - `hyd_output`
- [[hydrograph_module.f90#ht4]] - `hyd_output`
- [[hydrograph_module.f90#ht5]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ru_d]] - `hyd_output`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[ru_module.f90#ru_tc]] - `real, dimension (:), allocatable`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`
- [[salt_module.f90#ru_hru_saltb_d]] - `object_salt_balance`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

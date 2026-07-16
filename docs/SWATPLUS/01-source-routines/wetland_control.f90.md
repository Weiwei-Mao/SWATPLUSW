---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wetland_control.f90
note_file: wetland_control.f90
subroutine: wetland_control
module:
  - reservoir_data_module
  - reservoir_module
  - hru_module
  - conditional_module
  - climate_module
  - hydrograph_module
  - time_module
  - basin_module
  - channel_module
  - water_body_module
  - soil_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - constituent_mass_module
  - aquifer_module
  - gwflow_module
calls:
  - gwflow_wetland
  - res_weir_release
  - conditions
  - res_hydro
  - res_sediment
  - res_nutrient
  - wet_salt
  - wet_cs
  - ero_cfactor
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - basin_module.f90#pco
  - climate_module.f90#w
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_res
  - hru_module.f90#cklsp
  - hru_module.f90#clayld
  - hru_module.f90#grayld
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#lagyld
  - hru_module.f90#mgt_ops
  - hru_module.f90#qp_cms
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#silyld
  - hru_module.f90#surfq
  - hru_module.f90#surqno3
  - hru_module.f90#tconc
  - hru_module.f90#usle_cfac
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#resz
  - hydrograph_module.f90#wbody
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_d
  - hydrograph_module.f90#wet_out_d
  - hydrograph_module.f90#wet_seep_day
  - organic_mineral_mass_module.f90#soil1
  - reservoir_data_module.f90#wbody_prm
  - reservoir_data_module.f90#wet_dat
  - reservoir_data_module.f90#wet_dat_c
  - reservoir_data_module.f90#wet_hyd
  - reservoir_data_module.f90#wet_prm
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
  - time_module.f90#time
  - water_body_module.f90#wbody_wb
  - water_body_module.f90#wet_wat_d
input_variables: []
reads: []
writes: []
purpose: ""
---

# wetland_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wetland_control.f90`
- **Modules used**:
  - [[reservoir_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[hru_module.f90]]
  - [[conditional_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[channel_module.f90]]
  - [[water_body_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[aquifer_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_wetland.f90]]
- [[res_weir_release.f90]]
- [[conditions.f90]]
- [[res_hydro.f90]]
- [[res_sediment.f90]]
- [[res_nutrient.f90]]
- [[wet_salt.f90]]
- [[wet_cs.f90]]
- [[ero_cfactor.f90]]

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[climate_module.f90#w]] - `weather_daily`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[hru_module.f90#cklsp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#grayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#qp_cms]] - `real`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#resz]] - `hyd_output`
- [[hydrograph_module.f90#wbody]] - `hyd_output`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_seep_day]] - `hyd_output`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[reservoir_data_module.f90#wbody_prm]] - `water_body_data_parameters`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#wet_dat_c]] - `reservoir_data_char_input`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_data_module.f90#wet_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[water_body_module.f90#wbody_wb]] - `water_body`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

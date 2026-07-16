---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_parm_select.f90
note_file: cal_parm_select.f90
subroutine: cal_parm_select
module:
  - basin_module
  - channel_data_module
  - reservoir_data_module
  - hru_module
  - soil_module
  - channel_module
  - conditional_module
  - sd_channel_module
  - reservoir_module
  - aquifer_module
  - hru_lte_module
  - organic_mineral_mass_module
  - hydrograph_module
  - pesticide_data_module
  - plant_module
  - plant_data_module
  - gwflow_module
  - carbon_module
  - tillage_data_module
calls:
  - curno
  - soil_awc_init
  - soil_text_init
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_dat
  - aquifer_module.f90#aqu_prm
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - carbon_module.f90#carbdb
  - carbon_module.f90#cb_wtr_coef
  - carbon_module.f90#cnr_cap
  - carbon_module.f90#cnr_ref
  - carbon_module.f90#cpr_cap
  - carbon_module.f90#cpr_ref
  - carbon_module.f90#man_coef
  - carbon_module.f90#n_act_frac
  - carbon_module.f90#org_allo
  - carbon_module.f90#org_con
  - carbon_module.f90#org_frac
  - channel_data_module.f90#ch_nut
  - conditional_module.f90#dtbl_res
  - gwflow_module.f90#gw_bed_change
  - gwflow_module.f90#gw_delay
  - gwflow_module.f90#gw_npond
  - gwflow_module.f90#gw_pond_info
  - gwflow_module.f90#gw_state
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_db
  - hru_module.f90#brt
  - hru_module.f90#cn2
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#luse
  - hru_module.f90#sdr
  - hru_module.f90#tconc
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - organic_mineral_mass_module.f90#soil1
  - pesticide_data_module.f90#pestdb
  - plant_data_module.f90#photo_degrade_factor
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_prm
  - reservoir_module.f90#res_ob
  - sd_channel_module.f90#sd_ch
  - soil_module.f90#soil
  - tillage_data_module.f90#bio_consf
  - tillage_data_module.f90#bmix_a
  - tillage_data_module.f90#bmix_b
  - tillage_data_module.f90#bmix_c
  - tillage_data_module.f90#till_consf
  - tillage_data_module.f90#tillmix_a
  - tillage_data_module.f90#tillmix_b
  - tillage_data_module.f90#tillmix_c
input_variables: []
reads: []
writes: []
purpose: "this subroutine finds the current parameter value based on; user defined change"
---

# cal_parm_select

> [!info] Summary
> this subroutine finds the current parameter value based on; user defined change

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_parm_select.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[channel_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[channel_module.f90]]
  - [[conditional_module.f90]]
  - [[sd_channel_module.f90]]
  - [[reservoir_module.f90]]
  - [[aquifer_module.f90]]
  - [[hru_lte_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[gwflow_module.f90]]
  - [[carbon_module.f90]]
  - [[tillage_data_module.f90]]
- **Subroutine calls**: 3 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[curno.f90]]
- [[soil_awc_init.f90]]
- [[soil_text_init.f90]]

**Called by:**

- [[cal_conditions.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_dat]] - `aquifer_database`
- [[aquifer_module.f90#aqu_prm]] - `aquifer_data_parameters`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[carbon_module.f90#carbdb]] - `carbon_inputs`
- [[carbon_module.f90#cb_wtr_coef]] - `carbon_water_coef`
- [[carbon_module.f90#cnr_cap]] - `real`
- [[carbon_module.f90#cnr_ref]] - `real`
- [[carbon_module.f90#cpr_cap]] - `real`
- [[carbon_module.f90#cpr_ref]] - `real`
- [[carbon_module.f90#man_coef]] - `manure_coef`
- [[carbon_module.f90#n_act_frac]] - `real`
- [[carbon_module.f90#org_allo]] - `organic_allocations`
- [[carbon_module.f90#org_con]] - `organic_controls`
- [[carbon_module.f90#org_frac]] - `organic_fractions`
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[gwflow_module.f90#gw_bed_change]] - `real`
- [[gwflow_module.f90#gw_delay]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_npond]] - `integer`
- [[gwflow_module.f90#gw_pond_info]] - `cell_pond_info`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_db]] - `swatdeg_hru_data`
- [[hru_module.f90#brt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[plant_data_module.f90#photo_degrade_factor]] - `real`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[soil_module.f90#soil]] - `soil_profile`
- [[tillage_data_module.f90#bio_consf]] - `real`
- [[tillage_data_module.f90#bmix_a]] - `real`
- [[tillage_data_module.f90#bmix_b]] - `real`
- [[tillage_data_module.f90#bmix_c]] - `real`
- [[tillage_data_module.f90#till_consf]] - `real`
- [[tillage_data_module.f90#tillmix_a]] - `real`
- [[tillage_data_module.f90#tillmix_b]] - `real`
- [[tillage_data_module.f90#tillmix_c]] - `real`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_allo_init.f90
note_file: cal_allo_init.f90
subroutine: cal_allo_init
module:
  - sd_channel_module
  - hru_lte_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - hydrograph_module
  - calibration_data_module
  - reservoir_data_module
  - aquifer_module
  - mgt_operations_module
  - conditional_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_om_init
  - conditional_module.f90#dtbl_lum
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_init
  - hru_module.f90#bss
  - hru_module.f90#hru
  - hru_module.f90#hru_init
  - hru_module.f90#mgt_ops
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ch_om_water_init
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#fp_om_water_init
  - hydrograph_module.f90#fp_stor
  - hydrograph_module.f90#res
  - hydrograph_module.f90#res_om_init
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_om_init
  - mgt_operations_module.f90#sched
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#pl_mass_init
  - organic_mineral_mass_module.f90#soil1
  - organic_mineral_mass_module.f90#soil1_init
  - plant_data_module.f90#pcomdb
  - plant_module.f90#pcom
  - plant_module.f90#pcom_init
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sdch_init
  - soil_module.f90#soil
  - soil_module.f90#soil_init
input_variables: []
reads: []
writes: []
purpose: ""
---

# cal_allo_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_allo_init.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[calibration_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[aquifer_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_om_init]] - `aquifer_dynamic`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_init]] - `swatdeg_hru_dynamic`
- [[hru_module.f90#bss]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#hru_init]] - `hydrologic_response_unit`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ch_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#fp_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#fp_stor]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#res_om_init]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_om_init]] - `hyd_output`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#pl_mass_init]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[organic_mineral_mass_module.f90#soil1_init]] - `soil_profile_mass`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[plant_module.f90#pcom_init]] - `plant_community`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sdch_init]] - `swatdeg_channel_dynamic`
- [[soil_module.f90#soil]] - `soil_profile`
- [[soil_module.f90#soil_init]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

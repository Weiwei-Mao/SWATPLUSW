---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: conditions.f90
note_file: conditions.f90
subroutine: conditions
module:
  - conditional_module
  - climate_module
  - time_module
  - hru_module
  - soil_module
  - plant_module
  - reservoir_module
  - reservoir_data_module
  - sd_channel_module
  - hydrograph_module
  - output_landscape_module
  - aquifer_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - water_allocation_module
calls:
  - cond_real
  - cond_integer
uses_variables:
  - aquifer_module.f90#aqu_d
  - climate_module.f90#rndseed_cond
  - climate_module.f90#tmp
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wst
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_lum
  - hru_module.f90#hru
  - hru_module.f90#ipl
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#qtile
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wet
  - mgt_operations_module.f90#sched
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - output_landscape_module.f90#hwb_d
  - plant_module.f90#pcom
  - reservoir_module.f90#res_ob
  - reservoir_module.f90#wet_ob
  - sd_channel_module.f90#sd_ch
  - soil_module.f90#soil
  - time_module.f90#time
  - water_allocation_module.f90#wallo
input_variables: []
reads: []
writes: []
purpose: ""
---

# conditions

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `conditions.f90`
- **Modules used**:
  - [[conditional_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[sd_channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
  - [[aquifer_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[water_allocation_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cond_real.f90]]
- [[cond_integer.f90]]

**Called by:**

- [[hru_control.f90]]
- [[hru_lte_control.f90]]
- [[mallo_control.f90]]
- [[res_control.f90]]
- [[time_control.f90]]
- [[wallo_demand.f90]]
- [[wetland_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[climate_module.f90#rndseed_cond]] - `integer`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#qtile]] - `real`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[plant_module.f90#pcom]] - `plant_community`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#wallo]] - `water_allocation`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

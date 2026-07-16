---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plant_init.f90
note_file: plant_init.f90
subroutine: plant_init
module:
  - hru_module
  - soil_module
  - plant_module
  - hydrograph_module
  - climate_module
  - time_module
  - maximum_data_module
  - plant_data_module
  - landuse_data_module
  - mgt_operations_module
  - urban_data_module
  - conditional_module
  - organic_mineral_mass_module
calls:
  - xmon
  - pl_root_gro
  - pl_seed_gro
  - pl_partition
  - pl_rootfr
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wst
  - hru_module.f90#cvm_com
  - hru_module.f90#hru
  - hru_module.f90#ipl
  - hru_module.f90#luse
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#uptake
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - landuse_data_module.f90#cons_prac
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_str
  - landuse_data_module.f90#overland_n
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#sched
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#plt_mass_z
  - organic_mineral_mass_module.f90#soil1
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#time
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: ""
---

# plant_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plant_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[plant_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[urban_data_module.f90]]
  - [[conditional_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]
- [[pl_root_gro.f90]]
- [[pl_seed_gro.f90]]
- [[pl_partition.f90]]
- [[pl_rootfr.f90]]

**Called by:**

- [[actions.f90]]
- [[plant_all_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#cvm_com]] - `real, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#uptake]] - `uptake_parameters`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[landuse_data_module.f90#cons_prac]] - `conservation_practice_table`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`
- [[landuse_data_module.f90#overland_n]] - `overlandflow_n_table`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#plt_mass_z]] - `organic_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

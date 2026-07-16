---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lum_init.f90
note_file: hru_lum_init.f90
subroutine: hru_lum_init
module:
  - hru_module
  - plant_module
  - landuse_data_module
  - hydrograph_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ilu
  - hru_module.f90#luse
  - hru_module.f90#mgt_ops
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - landuse_data_module.f90#cons_prac
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_grp
  - landuse_data_module.f90#lum_str
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_lum_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lum_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[landuse_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[actions.f90]]
- [[hru_lum_init_all.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[landuse_data_module.f90#cons_prac]] - `conservation_practice_table`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_grp]] - `land_use_mgt_groups`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lte_read.f90
note_file: hru_lte_read.f90
subroutine: hru_lte_read
module:
  - maximum_data_module
  - plant_data_module
  - hru_lte_module
  - hydrograph_module
  - input_file_module
  - output_landscape_module
  - climate_module
  - time_module
  - soil_data_module
  - conditional_module
calls:
  - ascrv
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wst
  - conditional_module.f90#dtbl_lum
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_db
  - hru_lte_module.f90#scon
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_hru
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hltls_a
  - output_landscape_module.f90#hltls_d
  - output_landscape_module.f90#hltls_m
  - output_landscape_module.f90#hltls_y
  - output_landscape_module.f90#hltnb_a
  - output_landscape_module.f90#hltnb_d
  - output_landscape_module.f90#hltnb_m
  - output_landscape_module.f90#hltnb_y
  - output_landscape_module.f90#hltpw_a
  - output_landscape_module.f90#hltpw_d
  - output_landscape_module.f90#hltpw_m
  - output_landscape_module.f90#hltpw_y
  - output_landscape_module.f90#hltwb_a
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hltwb_m
  - output_landscape_module.f90#hltwb_y
  - plant_data_module.f90#pldb
  - soil_data_module.f90#soil_lte
  - time_module.f90#ndays
  - time_module.f90#time
input_variables:
  - hru_lte_module.f90#hlt_db
reads:
  - in_hru%hru_ez
writes: []
purpose: ""
---

# hru_lte_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lte_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[hru_lte_module.f90]]
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[output_landscape_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[soil_data_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_db]] - `swatdeg_hru_data`
- [[hru_lte_module.f90#scon]] - `real, dimension(12)`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_hru]] - `input_hru`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hltls_a]] - `output_losses`
- [[output_landscape_module.f90#hltls_d]] - `output_losses`
- [[output_landscape_module.f90#hltls_m]] - `output_losses`
- [[output_landscape_module.f90#hltls_y]] - `output_losses`
- [[output_landscape_module.f90#hltnb_a]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_m]] - `output_nutbal`
- [[output_landscape_module.f90#hltnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hltpw_a]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_m]] - `output_plantweather`
- [[output_landscape_module.f90#hltpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hltwb_y]] - `output_waterbal`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[soil_data_module.f90#soil_lte]] - `soil_lte_database`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[hru_lte_module.f90#hlt_db]]

## File I/O
- **Reads**:
  - [[hru-lte.hru]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

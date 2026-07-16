---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lte_control.f90
note_file: hru_lte_control.f90
subroutine: hru_lte_control
module:
  - hru_lte_module
  - hydrograph_module
  - output_landscape_module
  - basin_module
  - climate_module
  - time_module
  - plant_data_module
  - conditional_module
calls:
  - conditions
  - actions
uses_variables:
  - basin_module.f90#pco
  - climate_module.f90#wgn
  - climate_module.f90#wst
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_lum
  - hru_lte_module.f90#hlt
  - hru_lte_module.f90#hlt_db
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - output_landscape_module.f90#hltls_d
  - output_landscape_module.f90#hltpw_d
  - output_landscape_module.f90#hltwb_d
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_lte_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lte_control.f90`
- **Modules used**:
  - [[hru_lte_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
  - [[basin_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[plant_data_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[hru_lte_module.f90#hlt]] - `swatdeg_hru_dynamic`
- [[hru_lte_module.f90#hlt_db]] - `swatdeg_hru_data`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[output_landscape_module.f90#hltls_d]] - `output_losses`
- [[output_landscape_module.f90#hltpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

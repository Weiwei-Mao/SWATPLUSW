---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_temp.f90
note_file: ch_temp.f90
subroutine: ch_temp
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - sd_channel_module
  - hydrograph_module
  - climate_module
  - output_landscape_module
  - aquifer_module
  - calibration_data_module
  - time_module
  - channel_velocity_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - channel_data_module.f90#w_temp
  - channel_velocity_module.f90#sd_ch_vel
  - climate_module.f90#tmp
  - climate_module.f90#w
  - climate_module.f90#wst
  - hydrograph_module.f90#ch_out_d
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hdsep1
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#hyd_sep_array
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#shf_db
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#ts
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hltwb_d
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwbz
  - output_landscape_module.f90#lsu_wb_d
  - output_landscape_module.f90#ruwb_d
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#wtemp
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# ch_temp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_temp.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[sd_channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[output_landscape_module.f90]]
  - [[aquifer_module.f90]]
  - [[calibration_data_module.f90]]
  - [[time_module.f90]]
  - [[channel_velocity_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[channel_data_module.f90#w_temp]] - `water_temperature_data`
- [[channel_velocity_module.f90#sd_ch_vel]] - `channel_velocity_parameters`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hdsep1]] - `hyd_sep`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#hyd_sep_array]] - `real, dimension(:,:),allocatable`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#shf_db]] - `shade_factor_data`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hltwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[output_landscape_module.f90#lsu_wb_d]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_d]] - `output_waterbal`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`
- [[sd_channel_module.f90#wtemp]] - `real`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

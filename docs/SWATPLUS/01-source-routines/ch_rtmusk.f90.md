---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtmusk.f90
note_file: ch_rtmusk.f90
subroutine: ch_rtmusk
module:
  - basin_module
  - channel_data_module
  - channel_module
  - hydrograph_module
  - time_module
  - channel_velocity_module
  - sd_channel_module
  - climate_module
  - reservoir_module
  - reservoir_data_module
  - water_body_module
  - conditional_module
calls:
  - rcurv_interp_flo
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - channel_module.f90#jhyd
  - climate_module.f90#wst
  - hydrograph_module.f90#ch_fp_wb
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#fp_stor
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#tot_stor
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_stor
  - reservoir_module.f90#wet_ob
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#flo_dep
  - sd_channel_module.f90#hyd_rad
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#rcz
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_dat
  - sd_channel_module.f90#trav_time
  - time_module.f90#time
  - water_body_module.f90#ch_wat_d
input_variables: []
reads: []
writes: []
purpose: "this subroutine routes a daily flow through a reach using the; Muskingum method; code provided by Dr. Valentina Krysanova, Pottsdam Institute for"
---

# ch_rtmusk

> [!info] Summary
> this subroutine routes a daily flow through a reach using the; Muskingum method; code provided by Dr. Valentina Krysanova, Pottsdam Institute for

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtmusk.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[channel_data_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[sd_channel_module.f90]]
  - [[climate_module.f90]]
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[water_body_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[rcurv_interp_flo.f90]]

**Called by:**

- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[channel_module.f90#jhyd]] - `integer`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#ch_fp_wb]] - `channel_floodplain_water_balance`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#fp_stor]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#tot_stor]] - `hyd_output`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_stor]] - `hyd_output`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#flo_dep]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#hyd_rad]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#rcz]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[sd_channel_module.f90#trav_time]] - `real, dimension(:), allocatable`
- [[time_module.f90#time]] - `time_current`
- [[water_body_module.f90#ch_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

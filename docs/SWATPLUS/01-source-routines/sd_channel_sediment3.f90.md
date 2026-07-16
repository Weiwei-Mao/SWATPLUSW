---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_sediment3.f90
note_file: sd_channel_sediment3.f90
subroutine: sd_channel_sediment3
module:
  - climate_module
  - sd_channel_module
  - channel_module
  - hydrograph_module
  - time_module
  - hru_module
  - water_body_module
  - reservoir_module
  - utils
  - basin_module
  - gwflow_module
  - channel_velocity_module
calls:
  - rcurv_interp_flo
  - gwflow_floodplain
uses_variables:
  - basin_module.f90#bsn_cc
  - channel_module.f90#rttime
  - channel_velocity_module.f90#sd_ch_vel
  - climate_module.f90#wst
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#bank_ero
  - hydrograph_module.f90#bed_ero
  - hydrograph_module.f90#ch_dep
  - hydrograph_module.f90#ch_trans
  - hydrograph_module.f90#fp_dep
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_d
  - reservoir_module.f90#wet_ob
  - sd_channel_module.f90#ch_morph
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#peakrate
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_ch
  - water_body_module.f90#ch_wat_d
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_channel_sediment3

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_sediment3.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[sd_channel_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[hru_module.f90]]
  - [[water_body_module.f90]]
  - [[reservoir_module.f90]]
  - [[utils.f90]]
  - [[basin_module.f90]]
  - [[gwflow_module.f90]]
  - [[channel_velocity_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[rcurv_interp_flo.f90]]
- [[gwflow_floodplain.f90]]

**Called by:**

- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[channel_module.f90#rttime]] - `real`
- [[channel_velocity_module.f90#sd_ch_vel]] - `channel_velocity_parameters`
- [[climate_module.f90#wst]] - `weather_station`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#bank_ero]] - `hyd_output`
- [[hydrograph_module.f90#bed_ero]] - `hyd_output`
- [[hydrograph_module.f90#ch_dep]] - `hyd_output`
- [[hydrograph_module.f90#ch_trans]] - `hyd_output`
- [[hydrograph_module.f90#fp_dep]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[sd_channel_module.f90#ch_morph]] - `channel_morphology_output`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#peakrate]] - `real`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[water_body_module.f90#ch_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

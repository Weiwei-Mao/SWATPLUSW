---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_watqual4.f90
note_file: ch_watqual4.f90
subroutine: ch_watqual4
module:
  - channel_module
  - hydrograph_module
  - climate_module
  - channel_data_module
  - sd_channel_module
  - water_body_module
calls:
  - rcurv_interp_flo
uses_variables:
  - channel_data_module.f90#ch_nut
  - channel_module.f90#ben_area
  - channel_module.f90#jnut
  - channel_module.f90#rchdep
  - channel_module.f90#rt_delt
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wst
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#ht3
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#sp_ob1
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_chd
input_variables: []
reads: []
writes: []
purpose: "this subroutine performs in-stream nutrient transformations and water; quality calculations"
---

# ch_watqual4

> [!info] Summary
> this subroutine performs in-stream nutrient transformations and water; quality calculations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_watqual4.f90`
- **Modules used**:
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[channel_data_module.f90]]
  - [[sd_channel_module.f90]]
  - [[water_body_module.f90]]
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
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[channel_module.f90#ben_area]] - `real`
- [[channel_module.f90#jnut]] - `integer`
- [[channel_module.f90#rchdep]] - `real`
- [[channel_module.f90#rt_delt]] - `real`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#ht3]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rthr.f90
note_file: ch_rthr.f90
subroutine: ch_rthr
module:
  - basin_module
  - climate_module
  - channel_data_module
  - time_module
  - channel_module
  - hydrograph_module
  - sd_channel_module
calls:
  - chrc_interp
uses_variables:
  - basin_module.f90#bsn_prm
  - channel_module.f90#jhyd
  - climate_module.f90#wst
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#flo_dep
  - sd_channel_module.f90#hyd_rad
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_dat
  - sd_channel_module.f90#trav_time
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "This subroutine routes flow at any required time step through the reach; using a constant storage coefficient; Routing method: Variable Storage routing"
---

# ch_rthr

> [!info] Summary
> This subroutine routes flow at any required time step through the reach; using a constant storage coefficient; Routing method: Variable Storage routing

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rthr.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[climate_module.f90]]
  - [[channel_data_module.f90]]
  - [[time_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[sd_channel_module.f90#chrc_interp]]

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[channel_module.f90#jhyd]] - `integer`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#flo_dep]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#hyd_rad]] - `real, dimension(:), allocatable`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[sd_channel_module.f90#trav_time]] - `real, dimension(:), allocatable`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

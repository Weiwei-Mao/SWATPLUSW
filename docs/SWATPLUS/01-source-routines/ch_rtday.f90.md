---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtday.f90
note_file: ch_rtday.f90
subroutine: ch_rtday
module:
  - basin_module
  - channel_data_module
  - channel_module
  - hydrograph_module
  - hru_module
  - channel_velocity_module
  - maximum_data_module
  - reservoir_module
  - reservoir_data_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - channel_data_module.f90#ch_hyd
  - channel_module.f90#ch
  - channel_module.f90#jhyd
  - channel_module.f90#pet_ch
  - channel_module.f90#rcharea
  - channel_module.f90#rchdep
  - channel_module.f90#rt_delt
  - channel_module.f90#rtevp
  - channel_module.f90#rttime
  - channel_module.f90#rttlc
  - channel_module.f90#rtwtr
  - channel_module.f90#sdti
  - channel_module.f90#wtrin
  - channel_velocity_module.f90#ch_vel
  - hru_module.f90#hru
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_d
  - reservoir_module.f90#wet_ob
input_variables: []
reads: []
writes: []
purpose: "this subroutine routes the daily flow through the reach using a; variable storage coefficient"
---

# ch_rtday

> [!info] Summary
> this subroutine routes the daily flow through the reach using a; variable storage coefficient

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtday.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[channel_data_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[channel_data_module.f90#ch_hyd]] - `channel_hyd_data`
- [[channel_module.f90#ch]] - `channel`
- [[channel_module.f90#jhyd]] - `integer`
- [[channel_module.f90#pet_ch]] - `real`
- [[channel_module.f90#rcharea]] - `real`
- [[channel_module.f90#rchdep]] - `real`
- [[channel_module.f90#rt_delt]] - `real`
- [[channel_module.f90#rtevp]] - `real`
- [[channel_module.f90#rttime]] - `real`
- [[channel_module.f90#rttlc]] - `real`
- [[channel_module.f90#rtwtr]] - `real`
- [[channel_module.f90#sdti]] - `real`
- [[channel_module.f90#wtrin]] - `real`
- [[channel_velocity_module.f90#ch_vel]] - `channel_velocity_parameters`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[reservoir_module.f90#wet_ob]] - `wetland`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

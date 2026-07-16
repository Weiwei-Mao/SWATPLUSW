---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_rtpath.f90
note_file: ch_rtpath.f90
subroutine: ch_rtpath
module:
  - basin_module
  - time_module
  - pathogen_data_module
  - channel_module
  - hydrograph_module
  - climate_module
  - constituent_mass_module
calls: []
uses_variables:
  - channel_module.f90#ch
  - channel_module.f90#rchdep
  - channel_module.f90#rttime
  - channel_module.f90#rtwtr
  - climate_module.f90#wst
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#obcs
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - pathogen_data_module.f90#path_db
input_variables: []
reads: []
writes: []
purpose: "this subroutine routes bacteria through the stream network"
---

# ch_rtpath

> [!info] Summary
> this subroutine routes bacteria through the stream network

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_rtpath.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[pathogen_data_module.f90]]
  - [[channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[channel_module.f90#ch]] - `channel`
- [[channel_module.f90#rchdep]] - `real`
- [[channel_module.f90#rttime]] - `real`
- [[channel_module.f90#rtwtr]] - `real`
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[pathogen_data_module.f90#path_db]] - `pathogen_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

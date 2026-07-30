---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_lapse.f90
note_file: cli_lapse.f90
subroutine: cli_lapse
module:
  - basin_module
  - climate_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#pcp
  - climate_module.f90#tmp
  - climate_module.f90#wgn
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes: []
purpose: "this subroutine adjusts precip and temperature for elevation"
---

# cli_lapse

> [!info] Summary
> this subroutine adjusts precip and temperature for elevation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_lapse.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]
- [[res_control.f90]]
- [[sd_channel_control3.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#pcp]] - `climate_measured_data`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

Adjust precip and temperature for elevation for each spatial_object

- plaps and tlaps are defined in [[basin_module.f90#bsn_prm]]
- plaps, mm/km, precipitation lapse rate: mm per km of elevation difference
- tlpas, deg C/km, temperature lapse rate: deg C per km of elevation difference
- If precip is simulated,
	- use weather generator elevation to adjust
- else
	- use weather station elevation to adjust
- same as temperature
- End
<!-- USER-NOTES-END -->

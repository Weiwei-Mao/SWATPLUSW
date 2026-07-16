---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: climate_control.f90
note_file: climate_control.f90
subroutine: climate_control
module:
  - climate_module
  - basin_module
  - time_module
  - hydrograph_module
  - maximum_data_module
calls:
  - cli_precip_control
  - cli_weatgn
  - cli_tgen
  - cli_bounds_check
  - cli_clgen
  - cli_slrgen
  - cli_rhgen
  - cli_wndgen
uses_variables:
  - climate_module.f90#hmd
  - climate_module.f90#petm
  - climate_module.f90#ppet_mce
  - climate_module.f90#ppet_ndays
  - climate_module.f90#rndseed
  - climate_module.f90#slr
  - climate_module.f90#tmp
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wnd
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ts
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine controls weather inputs to SWAT. Precipitation and; temperature data is read in and the weather generator is called to; fill in radiation, wind speed and relative humidity as well as"
---

# climate_control

> [!info] Summary
> this subroutine controls weather inputs to SWAT. Precipitation and; temperature data is read in and the weather generator is called to; fill in radiation, wind speed and relative humidity as well as

## Basic Information
- **Type**: `subroutine`
- **Source file**: `climate_control.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 8 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cli_precip_control.f90]]
- [[cli_weatgn.f90]]
- [[cli_tgen.f90]]
- [[cli_bounds_check.f90]]
- [[cli_clgen.f90]]
- [[cli_slrgen.f90]]
- [[cli_rhgen.f90]]
- [[cli_wndgen.f90]]

**Called by:**

- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#hmd]] - `climate_measured_data`
- [[climate_module.f90#petm]] - `climate_measured_data`
- [[climate_module.f90#ppet_mce]] - `integer`
- [[climate_module.f90#ppet_ndays]] - `integer`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#slr]] - `climate_measured_data`
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wnd]] - `climate_measured_data`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

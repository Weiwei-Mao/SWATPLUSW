---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_wndgen.f90
note_file: cli_wndgen.f90
subroutine: cli_wndgen
module:
  - hydrograph_module
  - climate_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#idg
  - climate_module.f90#rndseed
  - climate_module.f90#wgn
  - climate_module.f90#wnd_dir
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine generates wind speed"
---

# cli_wndgen

> [!info] Summary
> this subroutine generates wind speed

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_wndgen.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[climate_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#idg]] - `integer, dimension (:), allocatable`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wnd_dir]] - `wind_direction_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

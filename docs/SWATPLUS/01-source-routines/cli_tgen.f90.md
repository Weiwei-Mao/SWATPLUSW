---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_tgen.f90
note_file: cli_tgen.f90
subroutine: cli_tgen
module:
  - climate_module
  - hydrograph_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wgncur
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine generates temperature data when the user chooses to; simulate or when data is missing for particular days in the; weather file"
---

# cli_tgen

> [!info] Summary
> this subroutine generates temperature data when the user chooses to; simulate or when data is missing for particular days in the; weather file

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_tgen.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wgncur]] - `real, dimension (:,:), allocatable`
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

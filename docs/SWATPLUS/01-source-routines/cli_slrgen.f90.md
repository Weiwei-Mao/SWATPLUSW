---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_slrgen.f90
note_file: cli_slrgen.f90
subroutine: cli_slrgen
module:
  - hydrograph_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - climate_module.f90#wgncur
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
input_variables: []
reads: []
writes: []
purpose: "this subroutine generates solar radiation"
---

# cli_slrgen

> [!info] Summary
> this subroutine generates solar radiation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_slrgen.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[climate_module.f90]]
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

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

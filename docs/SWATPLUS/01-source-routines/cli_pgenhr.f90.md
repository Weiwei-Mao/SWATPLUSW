---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_pgenhr.f90
note_file: cli_pgenhr.f90
subroutine: cli_pgenhr
module:
  - climate_module
  - time_module
  - hydrograph_module
calls: []
uses_variables:
  - climate_module.f90#wst
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ts
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine distributes daily rainfall exponentially within the day"
---

# cli_pgenhr

> [!info] Summary
> this subroutine distributes daily rainfall exponentially within the day

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_pgenhr.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[cli_precip_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wst]] - `weather_station`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

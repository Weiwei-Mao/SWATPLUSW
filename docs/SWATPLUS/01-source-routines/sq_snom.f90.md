---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_snom.f90
note_file: sq_snom.f90
subroutine: sq_snom
module:
  - time_module
  - hydrograph_module
  - hru_module
  - climate_module
  - output_landscape_module
calls: []
uses_variables:
  - climate_module.f90#w
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#precip_eff
  - hru_module.f90#snocov1
  - hru_module.f90#snocov2
  - hru_module.f90#snofall
  - hru_module.f90#snomlt
  - hydrograph_module.f90#ts
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine predicts daily snom melt when the average air; temperature exceeds 0 degrees Celsius"
---

# sq_snom

> [!info] Summary
> this subroutine predicts daily snom melt when the average air; temperature exceeds 0 degrees Celsius

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_snom.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[climate_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[hru_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#precip_eff]] - `real`
- [[hru_module.f90#snocov1]] - `real`
- [[hru_module.f90#snocov2]] - `real`
- [[hru_module.f90#snofall]] - `real`
- [[hru_module.f90#snomlt]] - `real`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

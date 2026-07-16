---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_tstr.f90
note_file: pl_tstr.f90
subroutine: pl_tstr
module:
  - climate_module
  - plant_data_module
  - hru_module
  - plant_module
calls: []
uses_variables:
  - climate_module.f90#w
  - climate_module.f90#wgn_pms
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#iwgen
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
input_variables: []
reads: []
writes: []
purpose: "computes temperature stress for crop growth - strstmp"
---

# pl_tstr

> [!info] Summary
> computes temperature stress for crop growth - strstmp

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_tstr.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[plant_data_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[pl_biomass_gro.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#iwgen]] - `integer`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

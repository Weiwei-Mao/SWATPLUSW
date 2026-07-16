---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_satexcess.f90
note_file: swr_satexcess.f90
subroutine: swr_satexcess
module:
  - hru_module
  - soil_module
  - hydrograph_module
  - basin_module
  - organic_mineral_mass_module
  - gwflow_module
  - reservoir_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#satexq
  - hru_module.f90#surfq
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_seep_day
  - organic_mineral_mass_module.f90#soil1
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine moves water to upper layers if saturated and can't perc"
---

# swr_satexcess

> [!info] Summary
> this subroutine moves water to upper layers if saturated and can't perc

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_satexcess.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[hydrograph_module.f90]]
  - [[basin_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[gwflow_module.f90]]
  - [[reservoir_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[swr_percmain.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#satexq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_seep_day]] - `hyd_output`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

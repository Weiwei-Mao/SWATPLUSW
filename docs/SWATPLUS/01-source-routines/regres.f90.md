---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: regres.f90
note_file: regres.f90
subroutine: regres
module:
  - hru_module
  - climate_module
  - urban_data_module
calls: []
uses_variables:
  - climate_module.f90#w
  - climate_module.f90#wgn_pms
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#iwgen
  - hru_module.f90#luse
  - hru_module.f90#ulu
  - urban_data_module.f90#urbdb
input_variables: []
reads: []
writes: []
purpose: "this function calculates constituent loadings to the main channel using; USGS regression equations"
---

# regres

> [!info] Summary
> this function calculates constituent loadings to the main channel using; USGS regression equations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `regres.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[climate_module.f90]]
  - [[urban_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#iwgen]] - `integer`
- [[hru_module.f90#luse]] - `landuse`
- [[hru_module.f90#ulu]] - `integer`
- [[urban_data_module.f90#urbdb]] - `urban_db`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

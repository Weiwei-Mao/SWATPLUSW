---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_subwq.f90
note_file: swr_subwq.f90
subroutine: swr_subwq
module:
  - basin_module
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - carbon_module
  - climate_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes HRU loadings of chlorophyll-a, CBOD,; and dissolved oxygen to the main channel"
---

# swr_subwq

> [!info] Summary
> this subroutine computes HRU loadings of chlorophyll-a, CBOD,; and dissolved oxygen to the main channel

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_subwq.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[organic_mineral_mass_module.f90]], [[carbon_module.f90]], [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

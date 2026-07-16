---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_initwgn.f90
note_file: cli_initwgn.f90
subroutine: cli_initwgn
module:
  - basin_module
  - climate_module
  - time_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#idg
  - climate_module.f90#ppet_ndays
  - climate_module.f90#rndseed
  - climate_module.f90#wgn
  - climate_module.f90#wgn_pms
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine initializes the HRU weather generator parameters from the; .wgn file"
---

# cli_initwgn

> [!info] Summary
> this subroutine initializes the HRU weather generator parameters from the; .wgn file

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_initwgn.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[cli_wgnread.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#idg]] - `integer, dimension (:), allocatable`
- [[climate_module.f90#ppet_ndays]] - `integer`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

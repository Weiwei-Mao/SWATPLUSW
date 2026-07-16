---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_phreatophyte.f90
note_file: gwflow_phreatophyte.f90
subroutine: gwflow_phreatophyte
module:
  - gwflow_module
calls: []
uses_variables:
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_phyt_area
  - gwflow_module.f90#gw_phyt_dep
  - gwflow_module.f90#gw_phyt_flag
  - gwflow_module.f90#gw_phyt_ids
  - gwflow_module.f90#gw_phyt_ncells
  - gwflow_module.f90#gw_phyt_npts
  - gwflow_module.f90#gw_phyt_rate
  - gwflow_module.f90#gw_state
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the water removed from the aquifer via phreatophyte extraction; (extraction volumes are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_phreatophyte

> [!info] Summary
> this subroutine calculates the water removed from the aquifer via phreatophyte extraction; (extraction volumes are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_phreatophyte.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[gwflow_simulate.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_phyt_area]] - `real, allocatable`
- [[gwflow_module.f90#gw_phyt_dep]] - `real, allocatable`
- [[gwflow_module.f90#gw_phyt_flag]] - `integer`
- [[gwflow_module.f90#gw_phyt_ids]] - `integer, allocatable`
- [[gwflow_module.f90#gw_phyt_ncells]] - `integer`
- [[gwflow_module.f90#gw_phyt_npts]] - `integer`
- [[gwflow_module.f90#gw_phyt_rate]] - `real, allocatable`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

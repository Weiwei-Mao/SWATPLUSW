---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_chan_read.f90
note_file: gwflow_chan_read.f90
subroutine: gwflow_chan_read
module:
  - gwflow_module
  - hydrograph_module
  - utils
calls:
  - split_line
uses_variables:
  - gwflow_module.f90#gw_chan_chan
  - gwflow_module.f90#gw_chan_dep
  - gwflow_module.f90#gw_chan_dep_flag
  - gwflow_module.f90#gw_chan_dpzn
  - gwflow_module.f90#gw_chan_elev
  - gwflow_module.f90#gw_chan_id
  - gwflow_module.f90#gw_chan_len
  - gwflow_module.f90#gw_chan_ndpzn
  - gwflow_module.f90#gw_chan_obs
  - gwflow_module.f90#gw_chan_zone
  - gwflow_module.f90#num_chancells
  - gwflow_module.f90#out_gw
  - hydrograph_module.f90#sp_ob
input_variables: []
reads:
  - chancell.gw
  - chan_depth.gw
writes: []
purpose: ""
---

# gwflow_chan_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_chan_read.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[utils.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[utils.f90#split_line]]

**Called by:**

- [[hyd_connect.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[gwflow_module.f90#gw_chan_chan]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_dep]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_dep_flag]] - `integer`
- [[gwflow_module.f90#gw_chan_dpzn]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_elev]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_id]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_len]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_ndpzn]] - `integer`
- [[gwflow_module.f90#gw_chan_obs]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_chan_zone]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#num_chancells]] - `integer`
- [[gwflow_module.f90#out_gw]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

## File I/O
- **Reads**:
  - [[chancell.gw]]
  - [[chan_depth.gw]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

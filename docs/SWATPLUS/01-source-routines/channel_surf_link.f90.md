---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: channel_surf_link.f90
note_file: channel_surf_link.f90
subroutine: channel_surf_link
module:
  - hydrograph_module
  - channel_module
  - ru_module
  - maximum_data_module
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#ch_sur
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - ru_module.f90#iru
input_variables: []
reads: []
writes: []
purpose: ""
---

# channel_surf_link

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `channel_surf_link.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[channel_module.f90]]
  - [[ru_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hru_module.f90]]
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
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#ch_sur]] - `channel_surface_elements`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[ru_module.f90#iru]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

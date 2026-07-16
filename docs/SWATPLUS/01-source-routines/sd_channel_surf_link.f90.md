---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_surf_link.f90
note_file: sd_channel_surf_link.f90
subroutine: sd_channel_surf_link
module:
  - hydrograph_module
  - sd_channel_module
  - ru_module
  - hru_module
  - topography_data_module
calls: []
uses_variables:
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#sp_ob
  - ru_module.f90#iru
  - sd_channel_module.f90#sd_ch
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_channel_surf_link

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_surf_link.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[ru_module.f90]]
  - [[hru_module.f90]]
  - [[topography_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[ru_module.f90#iru]] - `integer`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

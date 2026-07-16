---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu2d_init.f90
note_file: aqu2d_init.f90
subroutine: aqu2d_init
module:
  - hydrograph_module
  - sd_channel_module
  - maximum_data_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#aq_chcs
  - constituent_mass_module.f90#cs_db
  - hydrograph_module.f90#aq_ch
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#aqu_cha
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_chd
input_variables: []
reads: []
writes: []
purpose: ""
---

# aqu2d_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu2d_init.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[constituent_mass_module.f90#aq_chcs]] - `gw_load_hydrograph`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hydrograph_module.f90#aq_ch]] - `channel_aquifer_elements`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#aqu_cha]] - `geomorphic_baseflow_channel_data`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

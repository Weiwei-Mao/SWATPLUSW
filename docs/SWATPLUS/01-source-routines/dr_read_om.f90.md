---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_read_om.f90
note_file: dr_read_om.f90
subroutine: dr_read_om
module:
  - dr_module
  - constituent_mass_module
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - maximum_data_module
calls: []
uses_variables:
  - dr_module.f90#dr_db
  - dr_module.f90#dr_om_name
  - dr_module.f90#dr_om_num
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_delr
  - maximum_data_module.f90#db_mx
  - organic_mineral_mass_module.f90#dr_om
input_variables:
  - dr_module.f90#dr_om_name
  - hydrograph_module.f90#dr
reads:
  - in_delr%om
writes: []
purpose: ""
---

# dr_read_om

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_read_om.f90`
- **Modules used**:
  - [[dr_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[dr_db_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[dr_module.f90#dr_db]] - `delivery_ratio_datafiles`
- [[dr_module.f90#dr_om_name]] - `character(len=16), dimension(:), allocatable`
- [[dr_module.f90#dr_om_num]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_delr]] - `input_delr`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[organic_mineral_mass_module.f90#dr_om]] - `organic_mineral_hydrograph`

**Populated by file reads:**

- [[dr_module.f90#dr_om_name]]
- [[hydrograph_module.f90#dr]]

## File I/O
- **Reads**:
  - [[dr_om.del]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

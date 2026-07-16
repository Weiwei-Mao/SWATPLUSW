---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hrudb_init.f90
note_file: hrudb_init.f90
subroutine: hrudb_init
module:
  - hydrograph_module
  - hru_module
  - landuse_data_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - hru_module.f90#hru
  - hru_module.f90#hru_db
  - hru_module.f90#ihru
  - hru_module.f90#ilu
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - landuse_data_module.f90#lum
input_variables: []
reads: []
writes: []
purpose: ""
---

# hrudb_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hrudb_init.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[landuse_data_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#hru_db]] - `hydrologic_response_unit_db`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ilu]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[landuse_data_module.f90#lum]] - `land_use_management`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

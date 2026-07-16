---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: structure_init.f90
note_file: structure_init.f90
subroutine: structure_init
module:
  - hydrograph_module
  - hru_module
  - landuse_data_module
calls:
  - structure_set_parms
uses_variables:
  - hru_module.f90#hru
  - hydrograph_module.f90#sp_ob
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_str
input_variables: []
reads: []
writes: []
purpose: ""
---

# structure_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `structure_init.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[landuse_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[structure_set_parms.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

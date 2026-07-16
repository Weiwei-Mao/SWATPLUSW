---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lum_init_all.f90
note_file: hru_lum_init_all.f90
subroutine: hru_lum_init_all
module:
  - hru_module
  - hydrograph_module
calls:
  - hru_lum_init
uses_variables:
  - hru_module.f90#hru
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_lum_init_all

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lum_init_all.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hru_lum_init.f90]]

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

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

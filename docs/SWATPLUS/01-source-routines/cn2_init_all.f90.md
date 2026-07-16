---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cn2_init_all.f90
note_file: cn2_init_all.f90
subroutine: cn2_init_all
module:
  - soil_module
  - maximum_data_module
  - landuse_data_module
  - hydrograph_module
calls:
  - cn2_init
uses_variables:
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes: []
purpose: ""
---

# cn2_init_all

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cn2_init_all.f90`
- **Modules used**:
  - [[soil_module.f90]]
  - [[maximum_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cn2_init.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

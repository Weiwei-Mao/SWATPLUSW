---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyd_connect_out.f90
note_file: hyd_connect_out.f90
subroutine: hyd_connect_out
module:
  - basin_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
input_variables: []
reads: []
writes: []
purpose: ""
---

# hyd_connect_out

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyd_connect_out.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_objects.f90
note_file: res_objects.f90
subroutine: res_objects
module:
  - reservoir_module
  - hydrograph_module
calls: []
uses_variables:
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - reservoir_module.f90#res_ob
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_objects

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_objects.f90`
- **Modules used**:
  - [[reservoir_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_res.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[reservoir_module.f90#res_ob]] - `reservoir`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

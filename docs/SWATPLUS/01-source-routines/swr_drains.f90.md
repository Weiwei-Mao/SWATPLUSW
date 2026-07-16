---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_drains.f90
note_file: swr_drains.f90
subroutine: swr_drains
module:
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - time_module
  - reservoir_module
calls:
  - swr_depstor
reads: []
writes: []
purpose: "this subroutine finds the effective lateral hydraulic conductivity; and computes drainage or subirrigation flux"
---

# swr_drains

> [!info] Summary
> this subroutine finds the effective lateral hydraulic conductivity; and computes drainage or subirrigation flux

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_drains.f90`
- **Modules used**: [[basin_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[time_module.f90]], [[reservoir_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[swr_depstor.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

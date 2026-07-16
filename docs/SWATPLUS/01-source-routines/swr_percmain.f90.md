---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_percmain.f90
note_file: swr_percmain.f90
subroutine: swr_percmain
module:
  - hru_module
  - soil_module
  - septic_data_module
  - hydrograph_module
  - basin_module
calls:
  - gwflow_soil
  - swr_percmacro
  - swr_percmicro
  - swr_satexcess
  - swr_drains
  - swr_origtile
reads: []
writes: []
purpose: "this subroutine is the master soil percolation component."
---

# swr_percmain

> [!info] Summary
> this subroutine is the master soil percolation component.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_percmain.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]], [[septic_data_module.f90]], [[hydrograph_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 6 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gwflow_soil.f90]]
- [[swr_percmacro.f90]]
- [[swr_percmicro.f90]]
- [[swr_satexcess.f90]]
- [[swr_drains.f90]]
- [[swr_origtile.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

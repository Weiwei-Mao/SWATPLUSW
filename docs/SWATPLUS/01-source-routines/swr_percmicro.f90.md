---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: swr_percmicro.f90
note_file: swr_percmicro.f90
subroutine: swr_percmicro
module:
  - septic_data_module
  - hru_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes percolation and lateral subsurface flow; from a soil layer when field capacity is exceeded"
---

# swr_percmicro

> [!info] Summary
> this subroutine computes percolation and lateral subsurface flow; from a soil layer when field capacity is exceeded

## Basic Information
- **Type**: `subroutine`
- **Source file**: `swr_percmicro.f90`
- **Modules used**: [[septic_data_module.f90]], [[hru_module.f90]], [[soil_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

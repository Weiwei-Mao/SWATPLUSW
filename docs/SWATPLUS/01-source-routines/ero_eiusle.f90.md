---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ero_eiusle.f90
note_file: ero_eiusle.f90
subroutine: ero_eiusle
module:
  - climate_module
  - hydrograph_module
  - hru_module
calls: []
reads: []
writes: []
purpose: "This subroutine computes the USLE erosion index (EI)"
---

# ero_eiusle

> [!info] Summary
> This subroutine computes the USLE erosion index (EI)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ero_eiusle.f90`
- **Modules used**: [[climate_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]]
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

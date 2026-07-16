---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_tstr.f90
note_file: pl_tstr.f90
subroutine: pl_tstr
module:
  - climate_module
  - plant_data_module
  - hru_module
  - plant_module
calls: []
reads: []
writes: []
purpose: "computes temperature stress for crop growth - strstmp"
---

# pl_tstr

> [!info] Summary
> computes temperature stress for crop growth - strstmp

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_tstr.f90`
- **Modules used**: [[climate_module.f90]], [[plant_data_module.f90]], [[hru_module.f90]], [[plant_module.f90]]
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

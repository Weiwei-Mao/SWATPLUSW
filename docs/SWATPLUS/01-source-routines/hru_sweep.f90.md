---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_sweep.f90
note_file: hru_sweep.f90
subroutine: hru_sweep
module:
  - hru_module
  - urban_data_module
calls: []
reads: []
writes: []
purpose: "the subroutine performs the street sweeping operation"
---

# hru_sweep

> [!info] Summary
> the subroutine performs the street sweeping operation

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_sweep.f90`
- **Modules used**: [[hru_module.f90]], [[urban_data_module.f90]]
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

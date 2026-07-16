---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_snom.f90
note_file: sq_snom.f90
subroutine: sq_snom
module:
  - time_module
  - hydrograph_module
  - hru_module
  - climate_module
  - output_landscape_module
calls: []
reads: []
writes: []
purpose: "this subroutine predicts daily snom melt when the average air; temperature exceeds 0 degrees Celsius"
---

# sq_snom

> [!info] Summary
> this subroutine predicts daily snom melt when the average air; temperature exceeds 0 degrees Celsius

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_snom.f90`
- **Modules used**: [[time_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[climate_module.f90]], [[output_landscape_module.f90]]
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

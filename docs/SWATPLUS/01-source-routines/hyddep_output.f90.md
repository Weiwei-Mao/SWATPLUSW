---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyddep_output.f90
note_file: hyddep_output.f90
subroutine: hyddep_output
module:
  - hydrograph_module
  - time_module
  - basin_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs hyd variables on daily, monthly and annual time steps; 0 = average annual (always print); 1 = yearly"
---

# hyddep_output

> [!info] Summary
> this subroutine outputs hyd variables on daily, monthly and annual time steps; 0 = average annual (always print); 1 = yearly

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyddep_output.f90`
- **Modules used**: [[hydrograph_module.f90]], [[time_module.f90]], [[basin_module.f90]]
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

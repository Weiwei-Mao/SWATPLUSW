---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_output.f90
note_file: recall_output.f90
subroutine: recall_output
module:
  - time_module
  - basin_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs SUBBASIN variables on daily, monthly and annual time steps; sum monthly variables"
---

# recall_output

> [!info] Summary
> this subroutine outputs SUBBASIN variables on daily, monthly and annual time steps; sum monthly variables

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_output.f90`
- **Modules used**: [[time_module.f90]], [[basin_module.f90]], [[hydrograph_module.f90]]
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

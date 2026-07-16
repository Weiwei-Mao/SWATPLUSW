---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: flow_hyd_ru_hru.f90
note_file: flow_hyd_ru_hru.f90
subroutine: flow_hyd_ru_hru
module:
  - hydrograph_module
  - time_module
  - basin_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the subdaily flow hydrographs for hru's, ru's and inflow fractions"
---

# flow_hyd_ru_hru

> [!info] Summary
> this subroutine determines the subdaily flow hydrographs for hru's, ru's and inflow fractions

## Basic Information
- **Type**: `subroutine`
- **Source file**: `flow_hyd_ru_hru.f90`
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

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_nut.f90
note_file: recall_nut.f90
subroutine: recall_nut
module:
  - basin_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
calls: []
uses_variables:
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#recall
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# recall_nut

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_nut.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

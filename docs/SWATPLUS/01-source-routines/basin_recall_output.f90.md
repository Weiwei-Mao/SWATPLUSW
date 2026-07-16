---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_recall_output.f90
note_file: basin_recall_output.f90
subroutine: basin_recall_output
module:
  - time_module
  - basin_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - hydrograph_module.f90#brec_a
  - hydrograph_module.f90#brec_d
  - hydrograph_module.f90#brec_m
  - hydrograph_module.f90#brec_y
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#rec_d
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#sp_ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# basin_recall_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_recall_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hydrograph_module.f90#brec_a]] - `hyd_output`
- [[hydrograph_module.f90#brec_d]] - `hyd_output`
- [[hydrograph_module.f90#brec_m]] - `hyd_output`
- [[hydrograph_module.f90#brec_y]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#rec_d]] - `hyd_output`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: flow_dur_curve.f90
note_file: flow_dur_curve.f90
subroutine: flow_dur_curve
module:
  - time_module
  - hydrograph_module
calls: []
uses_variables:
  - hydrograph_module.f90#fdc_days
  - hydrograph_module.f90#fdc_npts
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: ""
---

# flow_dur_curve

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `flow_dur_curve.f90`
- **Modules used**:
  - [[time_module.f90]]
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
- [[hydrograph_module.f90#fdc_days]] - `integer, dimension (27)`
- [[hydrograph_module.f90#fdc_npts]] - `integer`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wallo_trn_output.f90
note_file: wallo_trn_output.f90
subroutine: wallo_trn_output
module:
  - time_module
  - hydrograph_module
  - water_allocation_module
calls: []
uses_variables:
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#wal_oma
  - hydrograph_module.f90#wal_omd
  - hydrograph_module.f90#wal_omm
  - hydrograph_module.f90#wal_omy
  - time_module.f90#time
  - water_allocation_module.f90#wallo
input_variables: []
reads: []
writes: []
purpose: ""
---

# wallo_trn_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wallo_trn_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[water_allocation_module.f90]]
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
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#wal_oma]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omd]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omm]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omy]] - `water_allocation_object`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#wallo]] - `water_allocation`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

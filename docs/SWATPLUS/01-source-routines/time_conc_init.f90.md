---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_conc_init.f90
note_file: time_conc_init.f90
subroutine: time_conc_init
module:
  - ru_module
  - hru_module
  - hydrograph_module
  - topography_data_module
  - time_module
  - basin_module
calls: []
reads: []
writes: []
purpose: ""
---

# time_conc_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_conc_init.f90`
- **Modules used**: [[ru_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[topography_data_module.f90]], [[time_module.f90]], [[basin_module.f90]]
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

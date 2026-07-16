---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_pipe_read.f90
note_file: water_pipe_read.f90
subroutine: water_pipe_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
calls: []
reads:
  - water_pipe.wal
writes: []
purpose: ""
---

# water_pipe_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_pipe_read.f90`
- **Modules used**: [[input_file_module.f90]], [[water_allocation_module.f90]], [[mgt_operations_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `water_pipe.wal`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

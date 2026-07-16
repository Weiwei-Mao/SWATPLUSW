---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_osrc_read.f90
note_file: water_osrc_read.f90
subroutine: water_osrc_read
module:
  - input_file_module
  - water_allocation_module
  - recall_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - sd_channel_module
calls: []
reads:
  - out_src.wal
writes: []
purpose: ""
---

# water_osrc_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_osrc_read.f90`
- **Modules used**: [[input_file_module.f90]], [[water_allocation_module.f90]], [[recall_module.f90]], [[mgt_operations_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[constituent_mass_module.f90]], [[sd_channel_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `out_src.wal`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

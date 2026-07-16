---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_temp.f90
note_file: ch_read_temp.f90
subroutine: ch_read_temp
module:
  - basin_module
  - time_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - hydrograph_module
calls: []
uses_variables:
  - channel_data_module.f90#w_temp
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
input_variables:
  - channel_data_module.f90#w_temp
reads:
  - in_cha%temp
writes: []
purpose: ""
---

# ch_read_temp

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_temp.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_data_module.f90#w_temp]] - `water_temperature_data`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[channel_data_module.f90#w_temp]]

## File I/O
- **Reads**:
  - [[temperature.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

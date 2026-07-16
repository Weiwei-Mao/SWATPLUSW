---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_nut.f90
note_file: ch_read_nut.f90
subroutine: ch_read_nut
module:
  - input_file_module
  - basin_module
  - time_module
  - maximum_data_module
  - channel_data_module
calls: []
uses_variables:
  - channel_data_module.f90#ch_nut
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - channel_data_module.f90#ch_nut
reads:
  - in_cha%nut
writes: []
purpose: "this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the"
---

# ch_read_nut

> [!info] Summary
> this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_nut.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[channel_data_module.f90#ch_nut]]

## File I/O
- **Reads**:
  - [[nutrients.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

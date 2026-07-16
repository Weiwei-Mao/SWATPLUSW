---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sat_buff_read.f90
note_file: sat_buff_read.f90
subroutine: sat_buff_read
module:
  - input_file_module
  - maximum_data_module
  - hru_module
  - conditional_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_flo
  - hru_module.f90#hru
  - hru_module.f90#satbuff_db
  - maximum_data_module.f90#db_mx
input_variables:
  - hru_module.f90#satbuff_db
reads:
  - satbuffer.str
writes: []
purpose: ""
---

# sat_buff_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sat_buff_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hru_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_db.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#dtbl_flo]] - `decision_table`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#satbuff_db]] - `saturated_buffer_parameters`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hru_module.f90#satbuff_db]]

## File I/O
- **Reads**:
  - [[satbuffer.str]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

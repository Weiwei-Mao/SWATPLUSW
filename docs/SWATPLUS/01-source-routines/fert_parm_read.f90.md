---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: fert_parm_read.f90
note_file: fert_parm_read.f90
subroutine: fert_parm_read
module:
  - input_file_module
  - maximum_data_module
  - fertilizer_data_module
calls: []
uses_variables:
  - fertilizer_data_module.f90#fertdb
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
input_variables:
  - fertilizer_data_module.f90#fertdb
reads:
  - in_parmdb%fert_frt
writes: []
purpose: ""
---

# fert_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `fert_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[fertilizer_data_module.f90]]
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
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[input_file_module.f90#in_parmdb]] - `input_parameter_databases`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[fertilizer_data_module.f90#fertdb]]

## File I/O
- **Reads**:
  - [[fertilizer.frt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 22, check [[input_file_module.f90#in_parmdb]] %fert_frt
- if it does not exist, return
- Line 27, else, open the file
- Line 28-36, count, imax
- Line 47, get [[fertilizer_data_module.f90#fertdb]]
- End











<!-- USER-NOTES-END -->

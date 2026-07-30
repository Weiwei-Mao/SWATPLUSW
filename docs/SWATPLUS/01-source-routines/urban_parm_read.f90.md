---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: urban_parm_read.f90
note_file: urban_parm_read.f90
subroutine: urban_parm_read
module:
  - input_file_module
  - maximum_data_module
  - urban_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - urban_data_module.f90#urbdb
input_variables:
  - urban_data_module.f90#urbdb
reads:
  - in_parmdb%urban_urb
writes: []
purpose: ""
---

# urban_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `urban_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[urban_data_module.f90]]
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
- [[input_file_module.f90#in_parmdb]] - `input_parameter_databases`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[urban_data_module.f90#urbdb]] - `urban_db`

**Populated by file reads:**

- [[urban_data_module.f90#urbdb]]

## File I/O
- **Reads**:
  - [[urban.urb]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Read from [[urban.urb]] to get [[urban_data_module.f90#urbdb]]
<!-- USER-NOTES-END -->

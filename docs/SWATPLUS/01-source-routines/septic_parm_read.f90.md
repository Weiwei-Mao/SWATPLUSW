---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: septic_parm_read.f90
note_file: septic_parm_read.f90
subroutine: septic_parm_read
module:
  - input_file_module
  - maximum_data_module
  - septic_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - septic_data_module.f90#sep
  - septic_data_module.f90#sepdb
input_variables:
  - septic_data_module.f90#sepdb
reads:
  - in_parmdb%septic_sep
writes: []
purpose: ""
---

# septic_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `septic_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[septic_data_module.f90]]
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
- [[septic_data_module.f90#sep]] - `septic_system`
- [[septic_data_module.f90#sepdb]] - `septic_db`

**Populated by file reads:**

- [[septic_data_module.f90#sepdb]]

## File I/O
- **Reads**:
  - [[septic.sep]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

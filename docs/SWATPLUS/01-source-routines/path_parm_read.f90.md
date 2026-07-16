---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: path_parm_read.f90
note_file: path_parm_read.f90
subroutine: path_parm_read
module:
  - input_file_module
  - pathogen_data_module
  - maximum_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - pathogen_data_module.f90#path_db
input_variables:
  - pathogen_data_module.f90#path_db
reads:
  - in_parmdb%pathcom_db
writes: []
purpose: ""
---

# path_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `path_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[pathogen_data_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[pathogen_data_module.f90#path_db]] - `pathogen_db`

**Populated by file reads:**

- [[pathogen_data_module.f90#path_db]]

## File I/O
- **Reads**:
  - [[pathogens.pth]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

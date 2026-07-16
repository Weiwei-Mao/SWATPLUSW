---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_parm_read.f90
note_file: pest_parm_read.f90
subroutine: pest_parm_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - pesticide_data_module
  - utils
calls: []
uses_variables:
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - pesticide_data_module.f90#pestcp
  - pesticide_data_module.f90#pestdb
  - utils.f90#titldum
input_variables:
  - pesticide_data_module.f90#pestdb
  - utils.f90#titldum
reads:
  - in_parmdb%pest
writes: []
purpose: ""
---

# pest_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_parm_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[utils.f90]]
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
- [[pesticide_data_module.f90#pestcp]] - `pesticide_cp`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[utils.f90#titldum]] - `character (len=80)`

**Populated by file reads:**

- [[pesticide_data_module.f90#pestdb]]
- [[utils.f90#titldum]]

## File I/O
- **Reads**:
  - [[pesticide.pes]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

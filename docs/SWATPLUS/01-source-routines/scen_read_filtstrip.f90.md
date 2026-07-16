---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: scen_read_filtstrip.f90
note_file: scen_read_filtstrip.f90
subroutine: scen_read_filtstrip
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
calls: []
uses_variables:
  - input_file_module.f90#in_str
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#filtstrip_db
input_variables:
  - mgt_operations_module.f90#filtstrip_db
reads:
  - in_str%fstrip_str
writes: []
purpose: ""
---

# scen_read_filtstrip

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `scen_read_filtstrip.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[mgt_operations_module.f90]]
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
- [[input_file_module.f90#in_str]] - `input_structural`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#filtstrip_db]] - `filtstrip_operation`

**Populated by file reads:**

- [[mgt_operations_module.f90#filtstrip_db]]

## File I/O
- **Reads**:
  - [[filterstrip.str]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_read_irrops.f90
note_file: mgt_read_irrops.f90
subroutine: mgt_read_irrops
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
calls: []
uses_variables:
  - input_file_module.f90#in_ops
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#irrop_db
input_variables:
  - mgt_operations_module.f90#irrop_db
reads:
  - in_ops%irr_ops
writes: []
purpose: ""
---

# mgt_read_irrops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_read_irrops.f90`
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
- [[input_file_module.f90#in_ops]] - `input_ops`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`

**Populated by file reads:**

- [[mgt_operations_module.f90#irrop_db]]

## File I/O
- **Reads**:
  - [[irr.ops]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

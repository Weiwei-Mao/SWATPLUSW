---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_read_grazeops.f90
note_file: mgt_read_grazeops.f90
subroutine: mgt_read_grazeops
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
  - fertilizer_data_module
calls: []
uses_variables:
  - fertilizer_data_module.f90#fertdb
  - input_file_module.f90#in_ops
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#grazeop_db
input_variables:
  - mgt_operations_module.f90#grazeop_db
reads:
  - in_ops%graze_ops
writes: []
purpose: ""
---

# mgt_read_grazeops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_read_grazeops.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[mgt_operations_module.f90]]
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
- [[input_file_module.f90#in_ops]] - `input_ops`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#grazeop_db]] - `grazing_operation`

**Populated by file reads:**

- [[mgt_operations_module.f90#grazeop_db]]

## File I/O
- **Reads**:
  - [[graze.ops]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

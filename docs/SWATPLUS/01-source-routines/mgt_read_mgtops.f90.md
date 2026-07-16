---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_read_mgtops.f90
note_file: mgt_read_mgtops.f90
subroutine: mgt_read_mgtops
module:
  - input_file_module
  - maximum_data_module
  - mgt_operations_module
calls:
  - read_mgtops
uses_variables:
  - input_file_module.f90#in_lum
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#sched
input_variables:
  - mgt_operations_module.f90#sched
reads:
  - in_lum%management_sch
writes: []
purpose: ""
---

# mgt_read_mgtops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_read_mgtops.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[mgt_operations_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[read_mgtops.f90]]

**Called by:**

- [[proc_db.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[input_file_module.f90#in_lum]] - `input_lum`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#sched]] - `management_schedule`

**Populated by file reads:**

- [[mgt_operations_module.f90#sched]]

## File I/O
- **Reads**:
  - [[management.sch]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

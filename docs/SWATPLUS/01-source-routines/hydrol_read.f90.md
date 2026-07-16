---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hydrol_read.f90
note_file: hydrol_read.f90
subroutine: hydrol_read
module:
  - input_file_module
  - maximum_data_module
  - hydrology_data_module
calls: []
uses_variables:
  - hydrology_data_module.f90#hyd_db
  - input_file_module.f90#in_hyd
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrology_data_module.f90#hyd_db
reads:
  - in_hyd%hydrol_hyd
writes: []
purpose: ""
---

# hydrol_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hydrol_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrology_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrology_data_module.f90#hyd_db]] - `hydrology_db`
- [[input_file_module.f90#in_hyd]] - `input_hydrology`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrology_data_module.f90#hyd_db]]

## File I/O
- **Reads**:
  - [[hydrology.hyd]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

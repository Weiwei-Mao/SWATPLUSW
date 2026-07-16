---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sdr_read.f90
note_file: sdr_read.f90
subroutine: sdr_read
module:
  - input_file_module
  - maximum_data_module
  - hru_module
calls: []
uses_variables:
  - hru_module.f90#sdr
  - input_file_module.f90#in_str
  - maximum_data_module.f90#db_mx
input_variables:
  - hru_module.f90#sdr
reads:
  - in_str%tiledrain_str
writes: []
purpose: ""
---

# sdr_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sdr_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hru_module.f90]]
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
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[input_file_module.f90#in_str]] - `input_structural`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hru_module.f90#sdr]]

## File I/O
- **Reads**:
  - [[tiledrain.str]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

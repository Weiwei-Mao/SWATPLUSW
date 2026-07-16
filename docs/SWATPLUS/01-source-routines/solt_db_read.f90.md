---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: solt_db_read.f90
note_file: solt_db_read.f90
subroutine: solt_db_read
module:
  - input_file_module
  - maximum_data_module
  - soil_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_sol
  - maximum_data_module.f90#db_mx
  - soil_data_module.f90#solt_db
input_variables:
  - soil_data_module.f90#solt_db
reads:
  - in_sol%nut_sol
writes: []
purpose: ""
---

# solt_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `solt_db_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[soil_data_module.f90]]
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
- [[input_file_module.f90#in_sol]] - `input_soils`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[soil_data_module.f90#solt_db]] - `soiltest_db`

**Populated by file reads:**

- [[soil_data_module.f90#solt_db]]

## File I/O
- **Reads**:
  - [[nutrients.sol]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

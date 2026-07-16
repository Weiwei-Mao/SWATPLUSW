---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_db_read.f90
note_file: soil_db_read.f90
subroutine: soil_db_read
module:
  - input_file_module
  - maximum_data_module
  - soil_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_sol
  - maximum_data_module.f90#db_mx
  - soil_data_module.f90#soildb
input_variables:
  - soil_data_module.f90#soildb
reads:
  - in_sol%soils_sol
writes: []
purpose: ""
---

# soil_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_db_read.f90`
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
- [[soil_data_module.f90#soildb]] - `soil_database`

**Populated by file reads:**

- [[soil_data_module.f90#soildb]]

## File I/O
- **Reads**:
  - [[soils.sol]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: overland_n_read.f90
note_file: overland_n_read.f90
subroutine: overland_n_read
module:
  - input_file_module
  - maximum_data_module
  - landuse_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_lum
  - landuse_data_module.f90#overland_n
  - maximum_data_module.f90#db_mx
input_variables:
  - landuse_data_module.f90#overland_n
reads:
  - in_lum%ovn_lum
writes: []
purpose: ""
---

# overland_n_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `overland_n_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[landuse_data_module.f90]]
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
- [[input_file_module.f90#in_lum]] - `input_lum`
- [[landuse_data_module.f90#overland_n]] - `overlandflow_n_table`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[landuse_data_module.f90#overland_n]]

## File I/O
- **Reads**:
  - [[ovn_table.lum]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: topo_read.f90
note_file: topo_read.f90
subroutine: topo_read
module:
  - input_file_module
  - maximum_data_module
  - topography_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_hyd
  - maximum_data_module.f90#db_mx
  - topography_data_module.f90#topo_db
input_variables:
  - topography_data_module.f90#topo_db
reads:
  - in_hyd%topogr_hyd
writes: []
purpose: ""
---

# topo_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `topo_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[topography_data_module.f90]]
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
- [[input_file_module.f90#in_hyd]] - `input_hydrology`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[topography_data_module.f90#topo_db]] - `topography_db`

**Populated by file reads:**

- [[topography_data_module.f90#topo_db]]

## File I/O
- **Reads**:
  - [[topography.hyd]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

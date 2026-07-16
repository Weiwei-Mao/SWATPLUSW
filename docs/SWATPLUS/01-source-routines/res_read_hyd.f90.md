---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_hyd.f90
note_file: res_read_hyd.f90
subroutine: res_read_hyd
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_hyddb
input_variables:
  - reservoir_data_module.f90#res_hyddb
reads:
  - in_res%hyd_res
writes: []
purpose: ""
---

# res_read_hyd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_hyd.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_res.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[input_file_module.f90#in_res]] - `input_res`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_hyddb]] - `reservoir_hyd_data`

**Populated by file reads:**

- [[reservoir_data_module.f90#res_hyddb]]

## File I/O
- **Reads**:
  - [[hydrology.res]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

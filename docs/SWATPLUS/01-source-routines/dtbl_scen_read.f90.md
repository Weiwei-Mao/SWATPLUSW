---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dtbl_scen_read.f90
note_file: dtbl_scen_read.f90
subroutine: dtbl_scen_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - input_file_module
  - conditional_module
  - hru_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_scen
  - hru_module.f90#snodb
  - input_file_module.f90#in_cond
  - landuse_data_module.f90#lum
  - maximum_data_module.f90#db_mx
input_variables:
  - conditional_module.f90#dtbl_scen
reads:
  - in_cond%dtbl_scen
writes: []
purpose: ""
---

# dtbl_scen_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dtbl_scen_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[tillage_data_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[input_file_module.f90]]
  - [[conditional_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#dtbl_scen]] - `decision_table`
- [[hru_module.f90#snodb]] - `snow_parameters`
- [[input_file_module.f90#in_cond]] - `input_condition`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[conditional_module.f90#dtbl_scen]]

## File I/O
- **Reads**:
  - [[scen_lu.dtl]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

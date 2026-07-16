---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dtbl_flocon_read.f90
note_file: dtbl_flocon_read.f90
subroutine: dtbl_flocon_read
module:
  - maximum_data_module
  - hydrograph_module
  - input_file_module
  - conditional_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_flo
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_cond
  - maximum_data_module.f90#db_mx
input_variables:
  - conditional_module.f90#dtbl_flo
reads:
  - in_cond%dtbl_flo
writes: []
purpose: ""
---

# dtbl_flocon_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dtbl_flocon_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[conditional_module.f90]]
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
- [[conditional_module.f90#dtbl_flo]] - `decision_table`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_cond]] - `input_condition`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[conditional_module.f90#dtbl_flo]]

## File I/O
- **Reads**:
  - [[flo_con.dtl]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

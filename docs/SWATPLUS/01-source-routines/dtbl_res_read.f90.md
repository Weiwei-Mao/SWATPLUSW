---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dtbl_res_read.f90
note_file: dtbl_res_read.f90
subroutine: dtbl_res_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - input_file_module
  - conditional_module
  - recall_module
  - hydrograph_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_res
  - hydrograph_module.f90#recall
  - input_file_module.f90#in_cond
  - maximum_data_module.f90#db_mx
  - recall_module.f90#recall_db
  - reservoir_data_module.f90#res_weir
input_variables:
  - conditional_module.f90#dtbl_res
reads:
  - in_cond%dtbl_res
writes: []
purpose: ""
---

# dtbl_res_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dtbl_res_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[tillage_data_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[input_file_module.f90]]
  - [[conditional_module.f90]]
  - [[recall_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[input_file_module.f90#in_cond]] - `input_condition`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`

**Populated by file reads:**

- [[conditional_module.f90#dtbl_res]]

## File I/O
- **Reads**:
  - [[res_rel.dtl]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

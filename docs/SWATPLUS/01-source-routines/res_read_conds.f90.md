---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_conds.f90
note_file: res_read_conds.f90
subroutine: res_read_conds
module:
  - reservoir_conditions_module
  - maximum_data_module
calls: []
uses_variables:
  - maximum_data_module.f90#db_mx
  - reservoir_conditions_module.f90#ctbl
input_variables:
  - reservoir_conditions_module.f90#ctbl
reads:
  - res_conds.dat
writes: []
purpose: ""
---

# res_read_conds

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_conds.f90`
- **Modules used**:
  - [[reservoir_conditions_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_conditions_module.f90#ctbl]] - `reservoir_condition_tables`

**Populated by file reads:**

- [[reservoir_conditions_module.f90#ctbl]]

## File I/O
- **Reads**:
  - [[res_conds.dat]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

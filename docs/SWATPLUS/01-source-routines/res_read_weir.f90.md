---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_weir.f90
note_file: res_read_weir.f90
subroutine: res_read_weir
module:
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - reservoir_data_module.f90#res_weir
input_variables:
  - reservoir_data_module.f90#res_weir
reads:
  - in_res%weir_res
writes: []
purpose: "this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the"
---

# res_read_weir

> [!info] Summary
> this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_weir.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
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
- [[input_file_module.f90#in_res]] - `input_res`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`

**Populated by file reads:**

- [[reservoir_data_module.f90#res_weir]]

## File I/O
- **Reads**:
  - [[weir.res]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

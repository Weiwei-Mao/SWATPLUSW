---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_csdb.f90
note_file: res_read_csdb.f90
subroutine: res_read_csdb
module:
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - res_cs_module
calls: []
uses_variables:
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - res_cs_module.f90#res_cs_data
input_variables:
  - res_cs_module.f90#res_cs_data
reads:
  - cs_res
writes: []
purpose: "this subroutine reads reservoir water quality parameters for constituents"
---

# res_read_csdb

> [!info] Summary
> this subroutine reads reservoir water quality parameters for constituents

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_csdb.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[res_cs_module.f90]]
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
- [[res_cs_module.f90#res_cs_data]] - `reservoir_cs_data`

**Populated by file reads:**

- [[res_cs_module.f90#res_cs_data]]

## File I/O
- **Reads**:
  - `cs_res` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

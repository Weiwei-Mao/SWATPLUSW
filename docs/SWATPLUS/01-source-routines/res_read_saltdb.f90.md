---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_saltdb.f90
note_file: res_read_saltdb.f90
subroutine: res_read_saltdb
module:
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - res_salt_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - res_salt_module.f90#res_salt_data
input_variables:
  - res_salt_module.f90#res_salt_data
reads:
  - salt_res
writes: []
purpose: "this subroutine reads reservoir water quality parameters for salt ions"
---

# res_read_saltdb

> [!info] Summary
> this subroutine reads reservoir water quality parameters for salt ions

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_saltdb.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[res_salt_module.f90]]
  - [[constituent_mass_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[input_file_module.f90#in_res]] - `input_res`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[res_salt_module.f90#res_salt_data]] - `reservoir_salt_data`

**Populated by file reads:**

- [[res_salt_module.f90#res_salt_data]]

## File I/O
- **Reads**:
  - [[salt_res]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

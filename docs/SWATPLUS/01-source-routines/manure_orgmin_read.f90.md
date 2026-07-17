---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: manure_orgmin_read.f90
note_file: manure_orgmin_read.f90
subroutine: manure_orgmin_read
module:
  - input_file_module
  - maximum_data_module
  - fertilizer_data_module
calls: []
uses_variables:
  - fertilizer_data_module.f90#manure_om
  - maximum_data_module.f90#db_mx
input_variables:
  - fertilizer_data_module.f90#manure_om
reads:
  - manure_om.frt
writes: []
purpose: ""
---

# manure_orgmin_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `manure_orgmin_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[fertilizer_data_module.f90]]
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
- [[fertilizer_data_module.f90#manure_om]] - `manure_attributes`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[fertilizer_data_module.f90#manure_om]]

## File I/O
- **Reads**:
  - [[manure_om.frt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Check file [[manure_om.frt]]
- add to [[fertilizer_data_module.f90#manure_db]]
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: manure_db_read.f90
note_file: manure_db_read.f90
subroutine: manure_db_read
module:
  - input_file_module
  - maximum_data_module
  - fertilizer_data_module
calls: []
uses_variables:
  - fertilizer_data_module.f90#manure_db
  - fertilizer_data_module.f90#manure_om
  - maximum_data_module.f90#db_mx
input_variables:
  - fertilizer_data_module.f90#manure_db
reads:
  - manure_db.frt
writes: []
purpose: "Reads hardcoded extended manure database records from manure_db.frt and cross-references organic/mineral manure definitions."
---

# manure_db_read

> [!info] Summary
> Reads `manure_db.frt`, stores manure database names and constituent cross-reference names, and resolves `org_min` to `manure_om` via `iorg_min`.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `manure_db_read.f90`
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
- [[fertilizer_data_module.f90#manure_db]] - `manure_database`
- [[fertilizer_data_module.f90#manure_om]] - `manure_attributes`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[fertilizer_data_module.f90#manure_db]]

## File I/O
- **Reads**:
  - [[manure_db.frt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Opens [[manure_db.frt]] and reads manure database records: record name plus cross-reference names (`org_min`, `pests`, `paths`, `hmets`, `salts`, `constit`) and description. The active implemented cross-reference maps `org_min` to [[fertilizer_data_module.f90#manure_om]] and stores the index in `manure_db(:)%iorg_min`.
<!-- USER-NOTES-END -->

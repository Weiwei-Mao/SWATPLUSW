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
reads:
  - manure_db.frt
writes: []
purpose: ""
---

# manure_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `manure_db_read.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[fertilizer_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `manure_db.frt`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

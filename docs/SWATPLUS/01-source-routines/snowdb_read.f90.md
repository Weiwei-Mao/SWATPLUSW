---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: snowdb_read.f90
note_file: snowdb_read.f90
subroutine: snowdb_read
module:
  - input_file_module
  - maximum_data_module
  - hru_module
calls: []
reads:
  - in_parmdb%snow
writes: []
purpose: ""
---

# snowdb_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `snowdb_read.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[hru_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_parmdb%snow` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

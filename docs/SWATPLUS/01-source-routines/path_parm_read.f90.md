---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: path_parm_read.f90
note_file: path_parm_read.f90
subroutine: path_parm_read
module:
  - input_file_module
  - pathogen_data_module
  - maximum_data_module
calls: []
reads:
  - in_parmdb%pathcom_db
writes: []
purpose: ""
---

# path_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `path_parm_read.f90`
- **Modules used**: [[input_file_module.f90]], [[pathogen_data_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_parmdb%pathcom_db` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

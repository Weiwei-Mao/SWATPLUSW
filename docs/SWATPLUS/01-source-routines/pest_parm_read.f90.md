---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_parm_read.f90
note_file: pest_parm_read.f90
subroutine: pest_parm_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - pesticide_data_module
  - utils
calls: []
reads:
  - in_parmdb%pest
writes: []
purpose: ""
---

# pest_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_parm_read.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[pesticide_data_module.f90]], [[utils.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_parmdb%pest` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

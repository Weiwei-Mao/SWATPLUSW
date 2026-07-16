---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_init.f90
note_file: res_read_init.f90
subroutine: res_read_init
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
calls: []
reads:
  - in_res%init_res
writes: []
purpose: ""
---

# res_read_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_init.f90`
- **Modules used**: [[basin_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]], [[reservoir_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_res%init_res` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

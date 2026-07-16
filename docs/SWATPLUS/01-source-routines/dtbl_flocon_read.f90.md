---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dtbl_flocon_read.f90
note_file: dtbl_flocon_read.f90
subroutine: dtbl_flocon_read
module:
  - maximum_data_module
  - hydrograph_module
  - input_file_module
  - conditional_module
calls: []
reads:
  - in_cond%dtbl_flo
writes: []
purpose: ""
---

# dtbl_flocon_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dtbl_flocon_read.f90`
- **Modules used**: [[maximum_data_module.f90]], [[hydrograph_module.f90]], [[input_file_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_cond%dtbl_flo` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

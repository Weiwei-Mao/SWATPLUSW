---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: object_read_output.f90
note_file: object_read_output.f90
subroutine: object_read_output
module:
  - input_file_module
  - hydrograph_module
  - maximum_data_module
calls: []
reads:
  - in_sim%object_prt
  - ob_out(i
writes: []
purpose: ""
---

# object_read_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `object_read_output.f90`
- **Modules used**: [[input_file_module.f90]], [[hydrograph_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_sim%object_prt` _(variable; see file.cio)_, `ob_out(i` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

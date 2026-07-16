---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: readpcom.f90
note_file: readpcom.f90
subroutine: readpcom
module:
  - input_file_module
  - maximum_data_module
  - plant_data_module
calls: []
reads:
  - in_init%plant
writes: []
purpose: ""
---

# readpcom

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `readpcom.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[plant_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_init%plant` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_read.f90
note_file: time_read.f90
subroutine: time_read
module:
  - time_module
  - input_file_module
calls:
  - xmon
reads:
  - in_sim%time
writes: []
purpose: ""
---

# time_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_read.f90`
- **Modules used**: [[time_module.f90]], [[input_file_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_sim%time` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

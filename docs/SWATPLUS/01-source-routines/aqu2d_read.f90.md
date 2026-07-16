---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu2d_read.f90
note_file: aqu2d_read.f90
subroutine: aqu2d_read
module:
  - hydrograph_module
  - input_file_module
  - maximum_data_module
calls:
  - define_unit_elements
reads:
  - in_link%aqu_cha
writes: []
purpose: ""
---

# aqu2d_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu2d_read.f90`
- **Modules used**: [[hydrograph_module.f90]], [[input_file_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_link%aqu_cha` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

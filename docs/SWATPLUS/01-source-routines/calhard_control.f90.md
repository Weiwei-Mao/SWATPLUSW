---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: calhard_control.f90
note_file: calhard_control.f90
subroutine: calhard_control
module:
  - aquifer_module
  - maximum_data_module
  - hydrograph_module
calls:
  - re_initialize
  - time_control
reads: []
writes: []
purpose: ""
---

# calhard_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `calhard_control.f90`
- **Modules used**: [[aquifer_module.f90]], [[maximum_data_module.f90]], [[hydrograph_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[re_initialize.f90]]
- [[time_control.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

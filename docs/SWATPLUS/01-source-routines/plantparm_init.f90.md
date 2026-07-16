---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plantparm_init.f90
note_file: plantparm_init.f90
subroutine: plantparm_init
module:
  - basin_module
  - maximum_data_module
  - plant_data_module
calls:
  - ascrv
reads: []
writes: []
purpose: ""
---

# plantparm_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plantparm_init.f90`
- **Modules used**: [[basin_module.f90]], [[maximum_data_module.f90]], [[plant_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

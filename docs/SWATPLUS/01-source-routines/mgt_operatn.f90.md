---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: mgt_operatn.f90
note_file: mgt_operatn.f90
subroutine: mgt_operatn
module:
  - mgt_operations_module
  - hru_module
  - plant_module
  - time_module
calls:
  - mgt_sched
reads: []
writes: []
purpose: "this subroutine performs all management operations"
---

# mgt_operatn

> [!info] Summary
> this subroutine performs all management operations

## Basic Information
- **Type**: `subroutine`
- **Source file**: `mgt_operatn.f90`
- **Modules used**: [[mgt_operations_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[mgt_sched.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

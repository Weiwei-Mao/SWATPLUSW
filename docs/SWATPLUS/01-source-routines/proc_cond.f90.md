---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_cond.f90
note_file: proc_cond.f90
subroutine: proc_cond
module:
  - hru_module
  - mgt_operations_module
  - hydrograph_module
  - maximum_data_module
  - conditional_module
calls: []
reads: []
writes: []
purpose: ""
---

# proc_cond

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_cond.f90`
- **Modules used**: [[hru_module.f90]], [[mgt_operations_module.f90]], [[hydrograph_module.f90]], [[maximum_data_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

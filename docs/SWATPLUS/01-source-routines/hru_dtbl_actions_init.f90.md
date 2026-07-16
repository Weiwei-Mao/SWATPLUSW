---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_dtbl_actions_init.f90
note_file: hru_dtbl_actions_init.f90
subroutine: hru_dtbl_actions_init
module:
  - conditional_module
  - mgt_operations_module
  - hydrograph_module
  - hru_module
  - plant_module
  - maximum_data_module
  - fertilizer_data_module
calls: []
reads: []
writes: []
purpose: ""
---

# hru_dtbl_actions_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_dtbl_actions_init.f90`
- **Modules used**: [[conditional_module.f90]], [[mgt_operations_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]], [[plant_module.f90]], [[maximum_data_module.f90]], [[fertilizer_data_module.f90]]
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

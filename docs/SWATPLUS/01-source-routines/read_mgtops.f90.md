---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: read_mgtops.f90
note_file: read_mgtops.f90
subroutine: read_mgtops
module:
  - maximum_data_module
  - plant_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - pesticide_data_module
  - time_module
calls: []
reads: []
writes: []
purpose: ""
---

# read_mgtops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `read_mgtops.f90`
- **Modules used**: [[maximum_data_module.f90]], [[plant_data_module.f90]], [[mgt_operations_module.f90]], [[tillage_data_module.f90]], [[fertilizer_data_module.f90]], [[pesticide_data_module.f90]], [[time_module.f90]]
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

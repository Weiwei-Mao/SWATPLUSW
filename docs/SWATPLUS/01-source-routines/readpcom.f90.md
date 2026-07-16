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
uses_variables:
  - input_file_module.f90#in_init
  - maximum_data_module.f90#db_mx
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#pldb
input_variables:
  - plant_data_module.f90#pcomdb
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
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[plant_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_db.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[input_file_module.f90#in_init]] - `input_init`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#pldb]] - `plant_db`

**Populated by file reads:**

- [[plant_data_module.f90#pcomdb]]

## File I/O
- **Reads**:
  - [[plant.ini]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

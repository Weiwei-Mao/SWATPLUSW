---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_fert_read.f90
note_file: salt_fert_read.f90
subroutine: salt_fert_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - salt_module
calls: []
uses_variables:
  - maximum_data_module.f90#db_mx
  - salt_module.f90#fert_salt
  - salt_module.f90#fert_salt_flag
input_variables:
  - salt_module.f90#fert_salt
reads:
  - salt_fertilizer.frt
writes: []
purpose: "this subroutine reads salt ion fertilizer loading (kg/ha) for various fertilizer types"
---

# salt_fert_read

> [!info] Summary
> this subroutine reads salt ion fertilizer loading (kg/ha) for various fertilizer types

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_fert_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[salt_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[salt_module.f90#fert_salt]] - `fert_db_salt`
- [[salt_module.f90#fert_salt_flag]] - `integer`

**Populated by file reads:**

- [[salt_module.f90#fert_salt]]

## File I/O
- **Reads**:
  - [[salt_fertilizer.frt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

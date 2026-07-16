---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: till_parm_read.f90
note_file: till_parm_read.f90
subroutine: till_parm_read
module:
  - input_file_module
  - maximum_data_module
  - tillage_data_module
calls: []
uses_variables:
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - tillage_data_module.f90#bmix_depth
  - tillage_data_module.f90#bmix_eff
  - tillage_data_module.f90#bmix_idtill
  - tillage_data_module.f90#tilldb
input_variables:
  - tillage_data_module.f90#tilldb
reads:
  - in_parmdb%till_til
writes: []
purpose: ""
---

# till_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `till_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[tillage_data_module.f90]]
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
- [[input_file_module.f90#in_parmdb]] - `input_parameter_databases`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[tillage_data_module.f90#bmix_depth]] - `real`
- [[tillage_data_module.f90#bmix_eff]] - `real`
- [[tillage_data_module.f90#bmix_idtill]] - `integer`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`

**Populated by file reads:**

- [[tillage_data_module.f90#tilldb]]

## File I/O
- **Reads**:
  - [[tillage.til]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 22, check [[input_file_module.f90#in_parmdb]] %till_til, [[tillage.til]]
- if it does not exist, return
- Line 27, Else, open the file [[tillage.til]] 
- Line 28-38, count the numbers, imax
- Line 40-56, read [[tillage_data_module.f90#tilldb]]
- Line 48-52, biomix
  biological mixing, by earthworms, not real tillage, slowly mix soil surface residue and organic material,
  The default value of bmix_eff is 0.2, and bmix_depth is 50 mm
- End















<!-- USER-NOTES-END -->

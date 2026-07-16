---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_db_read.f90
note_file: dr_db_read.f90
subroutine: dr_db_read
module:
  - dr_module
  - input_file_module
  - constituent_mass_module
  - maximum_data_module
calls:
  - dr_read_om
  - dr_read_pest
  - dr_path_read
  - dr_read_hmet
  - dr_read_salt
uses_variables:
  - constituent_mass_module.f90#cs_db
  - dr_module.f90#dr_db
  - input_file_module.f90#in_delr
  - maximum_data_module.f90#db_mx
input_variables:
  - dr_module.f90#dr_db
reads:
  - in_delr%del_ratio
writes: []
purpose: ""
---

# dr_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_db_read.f90`
- **Modules used**:
  - [[dr_module.f90]]
  - [[input_file_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[dr_read_om.f90]]
- [[dr_read_pest.f90]]
- [[dr_path_read.f90]]
- [[dr_read_hmet.f90]]
- [[dr_read_salt.f90]]

**Called by:**

- [[hyd_connect.f90]]
- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[dr_module.f90#dr_db]] - `delivery_ratio_datafiles`
- [[input_file_module.f90#in_delr]] - `input_delr`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[dr_module.f90#dr_db]]

## File I/O
- **Reads**:
  - [[delratio.del]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: constit_db_read.f90
note_file: constit_db_read.f90
subroutine: constit_db_read
module:
  - basin_module
  - input_file_module
  - constituent_mass_module
  - maximum_data_module
  - pesticide_data_module
  - pathogen_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - input_file_module.f90#in_sim
  - maximum_data_module.f90#db_mx
  - pathogen_data_module.f90#path_db
  - pesticide_data_module.f90#pestdb
input_variables:
  - constituent_mass_module.f90#cs_db
reads:
  - in_sim%cs_db
writes: []
purpose: ""
---

# constit_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `constit_db_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[maximum_data_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[pathogen_data_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[pathogen_data_module.f90#path_db]] - `pathogen_db`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`

**Populated by file reads:**

- [[constituent_mass_module.f90#cs_db]]

## File I/O
- **Reads**:
  - [[constituents.cs]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_urban_read.f90
note_file: cs_urban_read.f90
subroutine: cs_urban_read
module:
  - maximum_data_module
  - urban_data_module
  - constituent_mass_module
  - cs_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - cs_module.f90#cs_urban_conc
  - maximum_data_module.f90#db_mx
  - urban_data_module.f90#urbdb
input_variables: []
reads:
  - cs_urban
writes: []
purpose: ""
---

# cs_urban_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_urban_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[urban_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[cs_module.f90]]
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
- [[cs_module.f90#cs_urban_conc]] - `real, dimension(:,:), allocatable`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[urban_data_module.f90#urbdb]] - `urban_db`

## File I/O
- **Reads**:
  - [[cs_urban]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

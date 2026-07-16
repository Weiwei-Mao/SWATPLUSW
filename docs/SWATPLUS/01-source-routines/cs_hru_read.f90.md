---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_hru_read.f90
note_file: cs_hru_read.f90
subroutine: cs_hru_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil_ini
  - maximum_data_module.f90#db_mx
input_variables:
  - constituent_mass_module.f90#cs_soil_ini
reads:
  - cs_hru.ini
writes: []
purpose: ""
---

# cs_hru_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_hru_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[constituent_mass_module.f90#cs_soil_ini]] - `cs_soil_init_concentrations`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[constituent_mass_module.f90#cs_soil_ini]]

## File I/O
- **Reads**:
  - [[cs_hru.ini]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

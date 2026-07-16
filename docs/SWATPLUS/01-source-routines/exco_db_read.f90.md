---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: exco_db_read.f90
note_file: exco_db_read.f90
subroutine: exco_db_read
module:
  - exco_module
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
calls:
  - exco_read_om
  - exco_read_pest
  - exco_read_path
  - exco_read_hmet
  - exco_read_salt
uses_variables:
  - constituent_mass_module.f90#cs_db
  - exco_module.f90#exco_db
  - input_file_module.f90#in_exco
  - maximum_data_module.f90#db_mx
input_variables:
  - exco_module.f90#exco_db
reads:
  - in_exco%exco
writes: []
purpose: ""
---

# exco_db_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `exco_db_read.f90`
- **Modules used**:
  - [[exco_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[exco_read_om.f90]]
- [[exco_read_pest.f90]]
- [[exco_read_path.f90]]
- [[exco_read_hmet.f90]]
- [[exco_read_salt.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[exco_module.f90#exco_db]] - `export_coefficient_datafiles`
- [[input_file_module.f90#in_exco]] - `input_exco`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[exco_module.f90#exco_db]]

## File I/O
- **Reads**:
  - [[exco.exc]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

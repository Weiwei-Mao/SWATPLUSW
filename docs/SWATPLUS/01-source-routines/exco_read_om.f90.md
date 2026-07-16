---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: exco_read_om.f90
note_file: exco_read_om.f90
subroutine: exco_read_om
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - maximum_data_module
  - exco_module
calls: []
uses_variables:
  - exco_module.f90#exco_om_name
  - exco_module.f90#exco_om_num
  - hydrograph_module.f90#exco
  - input_file_module.f90#in_exco
  - maximum_data_module.f90#db_mx
  - organic_mineral_mass_module.f90#exco_om
input_variables:
  - exco_module.f90#exco_om_name
  - hydrograph_module.f90#exco
reads:
  - in_exco%om
writes: []
purpose: ""
---

# exco_read_om

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `exco_read_om.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[maximum_data_module.f90]]
  - [[exco_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[exco_db_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[exco_module.f90#exco_om_name]] - `character(len=16), dimension(:), allocatable`
- [[exco_module.f90#exco_om_num]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[input_file_module.f90#in_exco]] - `input_exco`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[organic_mineral_mass_module.f90#exco_om]] - `organic_mineral_hydrograph`

**Populated by file reads:**

- [[exco_module.f90#exco_om_name]]
- [[hydrograph_module.f90#exco]]

## File I/O
- **Reads**:
  - [[exco_om.exc]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

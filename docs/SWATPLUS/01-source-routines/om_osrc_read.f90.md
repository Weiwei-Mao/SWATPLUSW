---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: om_osrc_read.f90
note_file: om_osrc_read.f90
subroutine: om_osrc_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
calls: []
uses_variables:
  - hydrograph_module.f90#osrc_om
  - maximum_data_module.f90#db_mx
  - water_allocation_module.f90#om_osrc_name
input_variables:
  - hydrograph_module.f90#osrc_om
  - water_allocation_module.f90#om_osrc_name
reads:
  - om_osrc.wal
writes: []
purpose: ""
---

# om_osrc_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `om_osrc_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[water_allocation_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#osrc_om]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[water_allocation_module.f90#om_osrc_name]] - `character(len=16), dimension(:), allocatable`

**Populated by file reads:**

- [[hydrograph_module.f90#osrc_om]]
- [[water_allocation_module.f90#om_osrc_name]]

## File I/O
- **Reads**:
  - [[om_osrc.wal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

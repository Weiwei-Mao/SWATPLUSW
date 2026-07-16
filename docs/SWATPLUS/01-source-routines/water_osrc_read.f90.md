---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_osrc_read.f90
note_file: water_osrc_read.f90
subroutine: water_osrc_read
module:
  - input_file_module
  - water_allocation_module
  - recall_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - sd_channel_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#osrc_cs
  - maximum_data_module.f90#db_mx
  - water_allocation_module.f90#osrc
input_variables:
  - constituent_mass_module.f90#osrc_cs
  - water_allocation_module.f90#osrc
reads:
  - out_src.wal
writes: []
purpose: ""
---

# water_osrc_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_osrc_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[water_allocation_module.f90]]
  - [[recall_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[sd_channel_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#osrc_cs]] - `constituent_mass`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[water_allocation_module.f90#osrc]] - `outside_basin_source`

**Populated by file reads:**

- [[constituent_mass_module.f90#osrc_cs]]
- [[water_allocation_module.f90#osrc]]

## File I/O
- **Reads**:
  - [[out_src.wal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

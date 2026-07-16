---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_use_read.f90
note_file: water_use_read.f90
subroutine: water_use_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - sd_channel_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#wuse_cs_efflu
  - constituent_mass_module.f90#wuse_cs_stor
  - hydrograph_module.f90#wal_use_oma
  - hydrograph_module.f90#wal_use_omd
  - hydrograph_module.f90#wal_use_omm
  - hydrograph_module.f90#wal_use_omy
  - hydrograph_module.f90#wuse_om_out
  - hydrograph_module.f90#wuse_om_stor
  - maximum_data_module.f90#db_mx
  - water_allocation_module.f90#om_use_name
  - water_allocation_module.f90#wuse
input_variables:
  - constituent_mass_module.f90#wuse_cs_efflu
  - water_allocation_module.f90#wuse
reads:
  - water_use.wal
writes: []
purpose: ""
---

# water_use_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_use_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[water_allocation_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[sd_channel_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#wuse_cs_efflu]] - `constituent_mass`
- [[constituent_mass_module.f90#wuse_cs_stor]] - `constituent_mass`
- [[hydrograph_module.f90#wal_use_oma]] - `hyd_output`
- [[hydrograph_module.f90#wal_use_omd]] - `hyd_output`
- [[hydrograph_module.f90#wal_use_omm]] - `hyd_output`
- [[hydrograph_module.f90#wal_use_omy]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_stor]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[water_allocation_module.f90#om_use_name]] - `character(len=16), dimension(:), allocatable`
- [[water_allocation_module.f90#wuse]] - `water_treatment_use_data`

**Populated by file reads:**

- [[constituent_mass_module.f90#wuse_cs_efflu]]
- [[water_allocation_module.f90#wuse]]

## File I/O
- **Reads**:
  - [[water_use.wal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

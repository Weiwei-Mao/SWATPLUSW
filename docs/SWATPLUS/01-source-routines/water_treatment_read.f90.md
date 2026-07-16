---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_treatment_read.f90
note_file: water_treatment_read.f90
subroutine: water_treatment_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#wtp_cs_stor
  - constituent_mass_module.f90#wtp_cs_treat
  - hydrograph_module.f90#wal_tr_oma
  - hydrograph_module.f90#wal_tr_omd
  - hydrograph_module.f90#wal_tr_omm
  - hydrograph_module.f90#wal_tr_omy
  - hydrograph_module.f90#wtp_om_out
  - hydrograph_module.f90#wtp_om_stor
  - maximum_data_module.f90#db_mx
  - water_allocation_module.f90#om_treat_name
  - water_allocation_module.f90#wtp
input_variables:
  - constituent_mass_module.f90#wtp_cs_treat
  - water_allocation_module.f90#wtp
reads:
  - water_treat.wal
writes: []
purpose: ""
---

# water_treatment_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_treatment_read.f90`
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#wtp_cs_stor]] - `constituent_mass`
- [[constituent_mass_module.f90#wtp_cs_treat]] - `constituent_mass`
- [[hydrograph_module.f90#wal_tr_oma]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omd]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omm]] - `hyd_output`
- [[hydrograph_module.f90#wal_tr_omy]] - `hyd_output`
- [[hydrograph_module.f90#wtp_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wtp_om_stor]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[water_allocation_module.f90#om_treat_name]] - `character(len=16), dimension(:), allocatable`
- [[water_allocation_module.f90#wtp]] - `water_treatment_use_data`

**Populated by file reads:**

- [[constituent_mass_module.f90#wtp_cs_treat]]
- [[water_allocation_module.f90#wtp]]

## File I/O
- **Reads**:
  - [[water_treat.wal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

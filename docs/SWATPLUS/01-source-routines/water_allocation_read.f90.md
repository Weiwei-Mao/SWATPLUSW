---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: water_allocation_read.f90
note_file: water_allocation_read.f90
subroutine: water_allocation_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - sd_channel_module
  - conditional_module
  - constituent_mass_module
  - recall_module
  - exco_module
  - hru_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_flo
  - conditional_module.f90#dtbl_lum
  - exco_module.f90#exco_db
  - exco_module.f90#exco_om_name
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#wal_oma
  - hydrograph_module.f90#wal_omd
  - hydrograph_module.f90#wal_omm
  - hydrograph_module.f90#wal_omy
  - input_file_module.f90#in_watrts
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#irrop_db
  - recall_module.f90#recall_db
  - water_allocation_module.f90#osrc
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#walloa_out
  - water_allocation_module.f90#wallod_out
  - water_allocation_module.f90#wallom_out
  - water_allocation_module.f90#walloy_out
  - water_allocation_module.f90#walloz
input_variables:
  - water_allocation_module.f90#wallo
reads:
  - in_watrts%transfer_wro
writes: []
purpose: ""
---

# water_allocation_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `water_allocation_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[water_allocation_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[maximum_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[conditional_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[recall_module.f90]]
  - [[exco_module.f90]]
  - [[hru_module.f90]]
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
- [[conditional_module.f90#dtbl_flo]] - `decision_table`
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[exco_module.f90#exco_db]] - `export_coefficient_datafiles`
- [[exco_module.f90#exco_om_name]] - `character(len=16), dimension(:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#wal_oma]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omd]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omm]] - `water_allocation_object`
- [[hydrograph_module.f90#wal_omy]] - `water_allocation_object`
- [[input_file_module.f90#in_watrts]] - `input_water_rights`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[water_allocation_module.f90#osrc]] - `outside_basin_source`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#walloa_out]] - `water_allocation_output`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`
- [[water_allocation_module.f90#wallom_out]] - `water_allocation_output`
- [[water_allocation_module.f90#walloy_out]] - `water_allocation_output`
- [[water_allocation_module.f90#walloz]] - `source_output`

**Populated by file reads:**

- [[water_allocation_module.f90#wallo]]

## File I/O
- **Reads**:
  - [[water_allocation.wro]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

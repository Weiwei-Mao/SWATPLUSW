---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dtbl_lum_read.f90
note_file: dtbl_lum_read.f90
subroutine: dtbl_lum_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - input_file_module
  - conditional_module
  - pesticide_data_module
  - plant_data_module
  - constituent_mass_module
  - hydrograph_module
  - hru_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_lum
  - constituent_mass_module.f90#cs_db
  - fertilizer_data_module.f90#fertdb
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#snodb
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_cond
  - landuse_data_module.f90#lum
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#chemapp_db
  - mgt_operations_module.f90#fire_db
  - mgt_operations_module.f90#grazeop_db
  - mgt_operations_module.f90#harvop_db
  - mgt_operations_module.f90#irrop_db
  - mgt_operations_module.f90#pudl_db
  - plant_data_module.f90#transpl
  - tillage_data_module.f90#tilldb
input_variables:
  - conditional_module.f90#dtbl_lum
reads:
  - in_cond%dtbl_lum
writes: []
purpose: ""
---

# dtbl_lum_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dtbl_lum_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[tillage_data_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[input_file_module.f90]]
  - [[conditional_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[conditional_module.f90#dtbl_lum]] - `decision_table`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#snodb]] - `snow_parameters`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_cond]] - `input_condition`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[mgt_operations_module.f90#fire_db]] - `fire_operation`
- [[mgt_operations_module.f90#grazeop_db]] - `grazing_operation`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`
- [[mgt_operations_module.f90#pudl_db]] - `puddle_operation`
- [[plant_data_module.f90#transpl]] - `plant_transplant_db`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`

**Populated by file reads:**

- [[conditional_module.f90#dtbl_lum]]

## File I/O
- **Reads**:
  - [[lum.dtl]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

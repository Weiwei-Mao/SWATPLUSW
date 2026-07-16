---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: landuse_read.f90
note_file: landuse_read.f90
subroutine: landuse_read
module:
  - input_file_module
  - maximum_data_module
  - septic_data_module
  - plant_data_module
  - hru_module
  - landuse_data_module
  - mgt_operations_module
calls: []
uses_variables:
  - hru_module.f90#ilu
  - hru_module.f90#mgt_ops
  - hru_module.f90#sdr
  - input_file_module.f90#in_lum
  - landuse_data_module.f90#cn
  - landuse_data_module.f90#cons_prac
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_str
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#bmpuser_db
  - mgt_operations_module.f90#filtstrip_db
  - mgt_operations_module.f90#grwaterway_db
  - mgt_operations_module.f90#sched
  - plant_data_module.f90#pcomdb
  - septic_data_module.f90#sep
input_variables:
  - landuse_data_module.f90#lum
reads:
  - in_lum%landuse_lum
writes: []
purpose: ""
---

# landuse_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `landuse_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[septic_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[hru_module.f90]]
  - [[landuse_data_module.f90]]
  - [[mgt_operations_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_db.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#sdr]] - `subsurface_drainage_parameters`
- [[input_file_module.f90#in_lum]] - `input_lum`
- [[landuse_data_module.f90#cn]] - `curvenumber_table`
- [[landuse_data_module.f90#cons_prac]] - `conservation_practice_table`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_str]] - `land_use_structures`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#bmpuser_db]] - `bmpuser_operation`
- [[mgt_operations_module.f90#filtstrip_db]] - `filtstrip_operation`
- [[mgt_operations_module.f90#grwaterway_db]] - `grwaterway_operation`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[septic_data_module.f90#sep]] - `septic_system`

**Populated by file reads:**

- [[landuse_data_module.f90#lum]]

## File I/O
- **Reads**:
  - [[landuse.lum]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

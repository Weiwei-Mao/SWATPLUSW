---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plant_parm_read.f90
note_file: plant_parm_read.f90
subroutine: plant_parm_read
module:
  - input_file_module
  - maximum_data_module
  - plant_data_module
  - basin_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - input_file_module.f90#in_parmdb
  - maximum_data_module.f90#db_mx
  - plant_data_module.f90#cswat_1_part_fracs
  - plant_data_module.f90#pl_class
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
input_variables:
  - plant_data_module.f90#pl_class
  - plant_data_module.f90#pldb
reads:
  - in_parmdb%plants_plt
writes: []
purpose: ""
---

# plant_parm_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plant_parm_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
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
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[input_file_module.f90#in_parmdb]] - `input_parameter_databases`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_data_module.f90#cswat_1_part_fracs]] - `lignin_derived_partition_fracs`
- [[plant_data_module.f90#pl_class]] - `character(len=25), dimension(:), allocatable`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`

**Populated by file reads:**

- [[plant_data_module.f90#pl_class]]
- [[plant_data_module.f90#pldb]]

## File I/O
- **Reads**:
  - [[plants.plt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 24, check [[input_file_module.f90#in_parmdb]] %plants_plt exist or not
- if it does not exist, return
- Else, open file at line 32
- Line 33-45, count line numbers, imax, and allocation
	- Line 54-58, if [[basin_module.f90#bsn_cc]] %nam1 == 0
	  input plant name, [[plant_data_module.f90#pldb]]
	- Else  [[basin_module.f90#bsn_cc]] %nam1 == 1
	  input plant name + plant class
- Line 61-73, if [[basin_module.f90#bsn_cc]] == 2 is selected, there are some excess calculation
- End
<!-- USER-NOTES-END -->

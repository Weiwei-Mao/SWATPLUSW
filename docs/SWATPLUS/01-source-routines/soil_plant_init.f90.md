---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: soil_plant_init.f90
note_file: soil_plant_init.f90
subroutine: soil_plant_init
module:
  - hru_module
  - basin_module
  - input_file_module
  - maximum_data_module
  - constituent_mass_module
calls: []
uses_variables:
  - basin_module.f90#bsn_cc
  - hru_module.f90#sol_plt_ini
  - input_file_module.f90#in_init
  - maximum_data_module.f90#db_mx
input_variables:
  - hru_module.f90#sol_plt_ini
reads:
  - in_init%soil_plant_ini
writes: []
purpose: ""
---

# soil_plant_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `soil_plant_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[input_file_module.f90#in_init]] - `input_init`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hru_module.f90#sol_plt_ini]]

## File I/O
- **Reads**:
  - [[soil_plant.ini]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

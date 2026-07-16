---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_cha_res_read.f90
note_file: pest_cha_res_read.f90
subroutine: pest_cha_res_read
module:
  - constituent_mass_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - hydrograph_module
  - sd_channel_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#pest_init_name
  - constituent_mass_module.f90#pest_water_ini
  - input_file_module.f90#in_init
  - maximum_data_module.f90#db_mx
input_variables:
  - constituent_mass_module.f90#pest_init_name
  - constituent_mass_module.f90#pest_water_ini
reads:
  - in_init%pest_water
writes: []
purpose: ""
---

# pest_cha_res_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_cha_res_read.f90`
- **Modules used**:
  - [[constituent_mass_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[organic_mineral_mass_module.f90]]
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
- [[constituent_mass_module.f90#pest_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#pest_water_ini]] - `cs_water_init_concentrations`
- [[input_file_module.f90#in_init]] - `input_init`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[constituent_mass_module.f90#pest_init_name]]
- [[constituent_mass_module.f90#pest_water_ini]]

## File I/O
- **Reads**:
  - [[pest_water.ini]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: om_water_init.f90
note_file: om_water_init.f90
subroutine: om_water_init
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - hydrograph_module
  - sd_channel_module
  - constituent_mass_module
calls: []
uses_variables:
  - hydrograph_module.f90#om_init_name
  - hydrograph_module.f90#om_init_water
  - input_file_module.f90#in_init
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrograph_module.f90#om_init_name
  - hydrograph_module.f90#om_init_water
reads:
  - in_init%om_water
writes: []
purpose: ""
---

# om_water_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `om_water_init.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
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
- [[hydrograph_module.f90#om_init_name]] - `character(len=16), dimension(:), allocatable`
- [[hydrograph_module.f90#om_init_water]] - `hyd_output`
- [[input_file_module.f90#in_init]] - `input_init`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrograph_module.f90#om_init_name]]
- [[hydrograph_module.f90#om_init_water]]

## File I/O
- **Reads**:
  - [[om_water.ini]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

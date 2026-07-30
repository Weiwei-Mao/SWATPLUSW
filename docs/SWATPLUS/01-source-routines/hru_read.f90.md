---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_read.f90
note_file: hru_read.f90
subroutine: hru_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - hydrology_data_module
  - topography_data_module
  - soil_data_module
  - input_file_module
  - hru_module
  - constituent_mass_module
calls:
  - allocate_parms
uses_variables:
  - constituent_mass_module.f90#cs_soil_ini
  - constituent_mass_module.f90#hmet_soil_ini
  - constituent_mass_module.f90#path_soil_ini
  - constituent_mass_module.f90#pest_soil_ini
  - constituent_mass_module.f90#salt_soil_ini
  - hru_module.f90#hru_db
  - hru_module.f90#ihru
  - hru_module.f90#isol
  - hru_module.f90#snodb
  - hru_module.f90#sol_plt_ini
  - hydrology_data_module.f90#hyd_db
  - input_file_module.f90#in_hru
  - landuse_data_module.f90#lum
  - maximum_data_module.f90#db_mx
  - soil_data_module.f90#soildb
  - soil_data_module.f90#solt_db
  - topography_data_module.f90#field_db
  - topography_data_module.f90#topo_db
input_variables:
  - hru_module.f90#hru_db
reads:
  - in_hru%hru_data
writes: []
purpose: ""
---

# hru_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_read.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[hydrology_data_module.f90]]
  - [[topography_data_module.f90]]
  - [[soil_data_module.f90]]
  - [[input_file_module.f90]]
  - [[hru_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[allocate_parms.f90]]

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_soil_ini]] - `cs_soil_init_concentrations`
- [[constituent_mass_module.f90#hmet_soil_ini]] - `cs_soil_init_concentrations`
- [[constituent_mass_module.f90#path_soil_ini]] - `cs_soil_init_concentrations`
- [[constituent_mass_module.f90#pest_soil_ini]] - `cs_soil_init_concentrations`
- [[constituent_mass_module.f90#salt_soil_ini]] - `cs_soil_init_concentrations`
- [[hru_module.f90#hru_db]] - `hydrologic_response_unit_db`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#isol]] - `integer`
- [[hru_module.f90#snodb]] - `snow_parameters`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[hydrology_data_module.f90#hyd_db]] - `hydrology_db`
- [[input_file_module.f90#in_hru]] - `input_hru`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[soil_data_module.f90#soildb]] - `soil_database`
- [[soil_data_module.f90#solt_db]] - `soiltest_db`
- [[topography_data_module.f90#field_db]] - `fields_db`
- [[topography_data_module.f90#topo_db]] - `topography_db`

**Populated by file reads:**

- [[hru_module.f90#hru_db]]

## File I/O
- **Reads**:
  - [[hru-data.hru]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 37, call [[allocate_parms.f90]], allocates array sizes
- Line 39, check [[input_file_module.f90#in_hru]] %hru_data, [[hru-data.hru]]
- Line 44-55, get imax
- Line 67, read [[hru_module.f90#hru_db]]
	- `hru_db(i)%dbsc` = text pointers from input file
	- `hru_db(i)%dbs` = resolved integer pointers used by the model
- Other part, initialization, and crosswalk input names to internal database indexes
- End

<!-- USER-NOTES-END -->

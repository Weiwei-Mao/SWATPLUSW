---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: aqu_read_init_cs.f90
note_file: aqu_read_init_cs.f90
subroutine: aqu_read_init_cs
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - aquifer_module
  - aqu_pesticide_module
  - hydrograph_module
  - constituent_mass_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - aquifer_module.f90#aqu_dat
  - aquifer_module.f90#aqu_init_dat_c_cs
  - aquifer_module.f90#aqudb
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_aqu_ini
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#path_init_name
  - constituent_mass_module.f90#path_soil_ini
  - constituent_mass_module.f90#pest_init_name
  - constituent_mass_module.f90#pest_water_ini
  - constituent_mass_module.f90#salt_aqu_ini
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
input_variables:
  - aquifer_module.f90#aqu_init_dat_c_cs
reads:
  - initial.aqu_cs
writes: []
purpose: ""
---

# aqu_read_init_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `aqu_read_init_cs.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[aquifer_module.f90]]
  - [[aqu_pesticide_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_aqu.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[aquifer_module.f90#aqu_dat]] - `aquifer_database`
- [[aquifer_module.f90#aqu_init_dat_c_cs]] - `aquifer_init_data_char_cs`
- [[aquifer_module.f90#aqudb]] - `aquifer_database`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_aqu_ini]] - `cs_aqu_init_concentrations`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#path_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#path_soil_ini]] - `cs_soil_init_concentrations`
- [[constituent_mass_module.f90#pest_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#pest_water_ini]] - `cs_water_init_concentrations`
- [[constituent_mass_module.f90#salt_aqu_ini]] - `salt_aqu_init_concentrations`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[aquifer_module.f90#aqu_init_dat_c_cs]]

## File I/O
- **Reads**:
  - [[initial.aqu_cs]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

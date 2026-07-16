---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: exco_read_salt.f90
note_file: exco_read_salt.f90
subroutine: exco_read_salt
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - maximum_data_module
  - exco_module
  - constituent_mass_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#exco_salt
  - constituent_mass_module.f90#obcs
  - exco_module.f90#exco_db
  - exco_module.f90#exco_salt_name
  - exco_module.f90#exco_salt_num
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_exco
  - maximum_data_module.f90#db_mx
input_variables:
  - exco_module.f90#exco_salt_name
reads:
  - in_exco%salt
writes: []
purpose: ""
---

# exco_read_salt

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `exco_read_salt.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[maximum_data_module.f90]]
  - [[exco_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[exco_db_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#exco_salt]] - `exco_salts`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[exco_module.f90#exco_db]] - `export_coefficient_datafiles`
- [[exco_module.f90#exco_salt_name]] - `character(len=16), dimension(:), allocatable`
- [[exco_module.f90#exco_salt_num]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_exco]] - `input_exco`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[exco_module.f90#exco_salt_name]]

## File I/O
- **Reads**:
  - [[exco_salt.exc]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

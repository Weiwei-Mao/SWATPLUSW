---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read.f90
note_file: res_read.f90
subroutine: res_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - conditional_module
  - hydrograph_module
  - constituent_mass_module
  - reservoir_module
  - pesticide_data_module
  - res_salt_module
  - res_cs_module
  - reservoir_conditions_module
calls: []
uses_variables:
  - conditional_module.f90#dtbl_res
  - constituent_mass_module.f90#path_init_name
  - constituent_mass_module.f90#pest_init_name
  - hydrograph_module.f90#om_init_name
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_res
  - maximum_data_module.f90#db_mx
  - reservoir_conditions_module.f90#ctbl
  - reservoir_conditions_module.f90#release
  - reservoir_data_module.f90#res_dat
  - reservoir_data_module.f90#res_dat_c
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_hyddb
  - reservoir_data_module.f90#res_init
  - reservoir_data_module.f90#res_init_dat_c
  - reservoir_data_module.f90#res_nut
  - reservoir_data_module.f90#res_prm
  - reservoir_data_module.f90#res_sed
  - reservoir_module.f90#res_ob
input_variables:
  - reservoir_data_module.f90#res_dat_c
reads:
  - in_res%res
writes: []
purpose: ""
---

# res_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[conditional_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[reservoir_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
  - [[reservoir_conditions_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_res.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[constituent_mass_module.f90#path_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#pest_init_name]] - `character(len=16), dimension(:), allocatable`
- [[hydrograph_module.f90#om_init_name]] - `character(len=16), dimension(:), allocatable`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_res]] - `input_res`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[reservoir_conditions_module.f90#ctbl]] - `reservoir_condition_tables`
- [[reservoir_conditions_module.f90#release]] - `real`
- [[reservoir_data_module.f90#res_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#res_dat_c]] - `reservoir_data_char_input`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_hyddb]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_init]] - `reservoir_init_data`
- [[reservoir_data_module.f90#res_init_dat_c]] - `reservoir_init_data_char`
- [[reservoir_data_module.f90#res_nut]] - `reservoir_nut_data`
- [[reservoir_data_module.f90#res_prm]] - `water_body_data_parameters`
- [[reservoir_data_module.f90#res_sed]] - `reservoir_sed_data`
- [[reservoir_module.f90#res_ob]] - `reservoir`

**Populated by file reads:**

- [[reservoir_data_module.f90#res_dat_c]]

## File I/O
- **Reads**:
  - [[reservoir.res]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wet_initial.f90
note_file: wet_initial.f90
subroutine: wet_initial
module:
  - reservoir_module
  - reservoir_data_module
  - hydrograph_module
  - hru_module
  - maximum_data_module
  - water_body_module
  - soil_module
  - conditional_module
  - constituent_mass_module
  - res_salt_module
  - res_cs_module
calls:
  - res_convert_mass
uses_variables:
  - conditional_module.f90#dtbl_res
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#path_init_name
  - constituent_mass_module.f90#pest_init_name
  - constituent_mass_module.f90#wet_water
  - hru_module.f90#hru
  - hydrograph_module.f90#om_init_name
  - hydrograph_module.f90#om_init_water
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_om_init
  - maximum_data_module.f90#db_mx
  - res_cs_module.f90#res_cs_data
  - res_salt_module.f90#res_salt_data
  - reservoir_data_module.f90#res_init
  - reservoir_data_module.f90#res_init_dat_c
  - reservoir_data_module.f90#res_nut
  - reservoir_data_module.f90#res_sed
  - reservoir_data_module.f90#res_weir
  - reservoir_data_module.f90#wet_dat
  - reservoir_data_module.f90#wet_dat_c
  - reservoir_data_module.f90#wet_hyd
  - reservoir_data_module.f90#wet_hyddb
  - reservoir_data_module.f90#wet_init
  - reservoir_data_module.f90#wet_prm
  - reservoir_module.f90#wet_ob
  - water_body_module.f90#wet_wat_d
input_variables: []
reads: []
writes: []
purpose: ""
---

# wet_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wet_initial.f90`
- **Modules used**:
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[maximum_data_module.f90]]
  - [[water_body_module.f90]]
  - [[soil_module.f90]]
  - [[conditional_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hydrograph_module.f90#res_convert_mass]]

**Called by:**

- [[actions.f90]]
- [[wet_all_initial.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#dtbl_res]] - `decision_table`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#path_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#pest_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#om_init_name]] - `character(len=16), dimension(:), allocatable`
- [[hydrograph_module.f90#om_init_water]] - `hyd_output`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_om_init]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[res_cs_module.f90#res_cs_data]] - `reservoir_cs_data`
- [[res_salt_module.f90#res_salt_data]] - `reservoir_salt_data`
- [[reservoir_data_module.f90#res_init]] - `reservoir_init_data`
- [[reservoir_data_module.f90#res_init_dat_c]] - `reservoir_init_data_char`
- [[reservoir_data_module.f90#res_nut]] - `reservoir_nut_data`
- [[reservoir_data_module.f90#res_sed]] - `reservoir_sed_data`
- [[reservoir_data_module.f90#res_weir]] - `reservoir_weir_outflow`
- [[reservoir_data_module.f90#wet_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#wet_dat_c]] - `reservoir_data_char_input`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_data_module.f90#wet_hyddb]] - `wetland_hyd_data`
- [[reservoir_data_module.f90#wet_init]] - `reservoir_init_data`
- [[reservoir_data_module.f90#wet_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[water_body_module.f90#wet_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

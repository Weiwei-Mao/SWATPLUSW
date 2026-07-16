---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_initial.f90
note_file: res_initial.f90
subroutine: res_initial
module:
  - reservoir_module
  - maximum_data_module
  - reservoir_data_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - water_body_module
  - res_salt_module
  - res_cs_module
calls:
  - res_convert_mass
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#path_water_ini
  - constituent_mass_module.f90#pest_water_ini
  - constituent_mass_module.f90#res_benthic
  - constituent_mass_module.f90#res_water
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#om_init_water
  - hydrograph_module.f90#res
  - hydrograph_module.f90#res_om_init
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - pesticide_data_module.f90#pestdb
  - res_cs_module.f90#res_cs_data
  - res_salt_module.f90#res_salt_data
  - reservoir_data_module.f90#res_dat
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_init
  - reservoir_data_module.f90#res_sed
  - reservoir_module.f90#res_ob
  - water_body_module.f90#res_wat_d
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_initial

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_initial.f90`
- **Modules used**:
  - [[reservoir_module.f90]]
  - [[maximum_data_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[water_body_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[hydrograph_module.f90#res_convert_mass]]

**Called by:**

- [[proc_res.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#path_water_ini]] - `cs_water_init_concentrations`
- [[constituent_mass_module.f90#pest_water_ini]] - `cs_water_init_concentrations`
- [[constituent_mass_module.f90#res_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#om_init_water]] - `hyd_output`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#res_om_init]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[res_cs_module.f90#res_cs_data]] - `reservoir_cs_data`
- [[res_salt_module.f90#res_salt_data]] - `reservoir_salt_data`
- [[reservoir_data_module.f90#res_dat]] - `reservoir_data`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_init]] - `reservoir_init_data`
- [[reservoir_data_module.f90#res_sed]] - `reservoir_sed_data`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[water_body_module.f90#res_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

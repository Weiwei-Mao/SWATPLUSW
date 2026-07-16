---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_allo.f90
note_file: res_allo.f90
subroutine: res_allo
module:
  - reservoir_module
  - reservoir_data_module
  - res_pesticide_module
  - res_salt_module
  - res_cs_module
  - hydrograph_module
  - constituent_mass_module
  - water_body_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#res_benthic
  - constituent_mass_module.f90#res_water
  - hydrograph_module.f90#res
  - hydrograph_module.f90#res_in_a
  - hydrograph_module.f90#res_in_d
  - hydrograph_module.f90#res_in_m
  - hydrograph_module.f90#res_in_y
  - hydrograph_module.f90#res_om_init
  - hydrograph_module.f90#res_out_a
  - hydrograph_module.f90#res_out_d
  - hydrograph_module.f90#res_out_m
  - hydrograph_module.f90#res_out_y
  - hydrograph_module.f90#res_trap
  - hydrograph_module.f90#sp_ob
  - res_cs_module.f90#rescs_a
  - res_cs_module.f90#rescs_d
  - res_cs_module.f90#rescs_m
  - res_cs_module.f90#rescs_y
  - res_pesticide_module.f90#brespst_a
  - res_pesticide_module.f90#brespst_d
  - res_pesticide_module.f90#brespst_m
  - res_pesticide_module.f90#brespst_y
  - res_pesticide_module.f90#respst_a
  - res_pesticide_module.f90#respst_d
  - res_pesticide_module.f90#respst_m
  - res_pesticide_module.f90#respst_y
  - res_salt_module.f90#ressalt_a
  - res_salt_module.f90#ressalt_d
  - res_salt_module.f90#ressalt_m
  - res_salt_module.f90#ressalt_y
  - reservoir_data_module.f90#res_hyd
  - reservoir_data_module.f90#res_prm
  - reservoir_module.f90#res_ob
  - water_body_module.f90#res_wat_a
  - water_body_module.f90#res_wat_d
  - water_body_module.f90#res_wat_m
  - water_body_module.f90#res_wat_y
input_variables: []
reads: []
writes: []
purpose: ""
---

# res_allo

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_allo.f90`
- **Modules used**:
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[res_pesticide_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#res_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#res_in_a]] - `hyd_output`
- [[hydrograph_module.f90#res_in_d]] - `hyd_output`
- [[hydrograph_module.f90#res_in_m]] - `hyd_output`
- [[hydrograph_module.f90#res_in_y]] - `hyd_output`
- [[hydrograph_module.f90#res_om_init]] - `hyd_output`
- [[hydrograph_module.f90#res_out_a]] - `hyd_output`
- [[hydrograph_module.f90#res_out_d]] - `hyd_output`
- [[hydrograph_module.f90#res_out_m]] - `hyd_output`
- [[hydrograph_module.f90#res_out_y]] - `hyd_output`
- [[hydrograph_module.f90#res_trap]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[res_cs_module.f90#rescs_a]] - `res_cs_output`
- [[res_cs_module.f90#rescs_d]] - `res_cs_output`
- [[res_cs_module.f90#rescs_m]] - `res_cs_output`
- [[res_cs_module.f90#rescs_y]] - `res_cs_output`
- [[res_pesticide_module.f90#brespst_a]] - `res_pesticide_output`
- [[res_pesticide_module.f90#brespst_d]] - `res_pesticide_output`
- [[res_pesticide_module.f90#brespst_m]] - `res_pesticide_output`
- [[res_pesticide_module.f90#brespst_y]] - `res_pesticide_output`
- [[res_pesticide_module.f90#respst_a]] - `res_pesticide_output`
- [[res_pesticide_module.f90#respst_d]] - `res_pesticide_output`
- [[res_pesticide_module.f90#respst_m]] - `res_pesticide_output`
- [[res_pesticide_module.f90#respst_y]] - `res_pesticide_output`
- [[res_salt_module.f90#ressalt_a]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_d]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_m]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_y]] - `res_salt_output`
- [[reservoir_data_module.f90#res_hyd]] - `reservoir_hyd_data`
- [[reservoir_data_module.f90#res_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[water_body_module.f90#res_wat_a]] - `water_body`
- [[water_body_module.f90#res_wat_d]] - `water_body`
- [[water_body_module.f90#res_wat_m]] - `water_body`
- [[water_body_module.f90#res_wat_y]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

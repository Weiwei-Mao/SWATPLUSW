---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_allo.f90
note_file: hru_allo.f90
subroutine: hru_allo
module:
  - hru_module
  - hydrograph_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - reservoir_module
  - reservoir_data_module
  - carbon_module
  - plant_module
  - soil_module
  - water_body_module
  - channel_velocity_module
  - res_salt_module
  - res_cs_module
calls: []
uses_variables:
  - channel_velocity_module.f90#grwway_vel
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_irr
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#wet_water
  - hru_module.f90#hru
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#wet
  - hydrograph_module.f90#wet_in_a
  - hydrograph_module.f90#wet_in_d
  - hydrograph_module.f90#wet_in_m
  - hydrograph_module.f90#wet_in_y
  - hydrograph_module.f90#wet_om_init
  - hydrograph_module.f90#wet_out_a
  - hydrograph_module.f90#wet_out_d
  - hydrograph_module.f90#wet_out_m
  - hydrograph_module.f90#wet_out_y
  - hydrograph_module.f90#wet_seep_day
  - organic_mineral_mass_module.f90#pl_mass
  - organic_mineral_mass_module.f90#soil1
  - organic_mineral_mass_module.f90#soil1_init
  - plant_module.f90#pcom
  - res_cs_module.f90#wetcs_a
  - res_cs_module.f90#wetcs_d
  - res_cs_module.f90#wetcs_m
  - res_cs_module.f90#wetcs_y
  - res_salt_module.f90#wetsalt_a
  - res_salt_module.f90#wetsalt_d
  - res_salt_module.f90#wetsalt_m
  - res_salt_module.f90#wetsalt_y
  - reservoir_data_module.f90#wet_hyd
  - reservoir_data_module.f90#wet_prm
  - reservoir_module.f90#wet_ob
  - soil_module.f90#soil
  - water_body_module.f90#wet_wat_a
  - water_body_module.f90#wet_wat_d
  - water_body_module.f90#wet_wat_m
  - water_body_module.f90#wet_wat_y
input_variables: []
reads: []
writes: []
purpose: ""
---

# hru_allo

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_allo.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[reservoir_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[carbon_module.f90]]
  - [[plant_module.f90]]
  - [[soil_module.f90]]
  - [[water_body_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_velocity_module.f90#grwway_vel]] - `channel_velocity_parameters`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_irr]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_pl]] - `plant_constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_a]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_m]] - `hyd_output`
- [[hydrograph_module.f90#wet_in_y]] - `hyd_output`
- [[hydrograph_module.f90#wet_om_init]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_a]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_d]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_m]] - `hyd_output`
- [[hydrograph_module.f90#wet_out_y]] - `hyd_output`
- [[hydrograph_module.f90#wet_seep_day]] - `hyd_output`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[organic_mineral_mass_module.f90#soil1_init]] - `soil_profile_mass`
- [[plant_module.f90#pcom]] - `plant_community`
- [[res_cs_module.f90#wetcs_a]] - `res_cs_output`
- [[res_cs_module.f90#wetcs_d]] - `res_cs_output`
- [[res_cs_module.f90#wetcs_m]] - `res_cs_output`
- [[res_cs_module.f90#wetcs_y]] - `res_cs_output`
- [[res_salt_module.f90#wetsalt_a]] - `res_salt_output`
- [[res_salt_module.f90#wetsalt_d]] - `res_salt_output`
- [[res_salt_module.f90#wetsalt_m]] - `res_salt_output`
- [[res_salt_module.f90#wetsalt_y]] - `res_salt_output`
- [[reservoir_data_module.f90#wet_hyd]] - `wetland_hyd_data`
- [[reservoir_data_module.f90#wet_prm]] - `water_body_data_parameters`
- [[reservoir_module.f90#wet_ob]] - `wetland`
- [[soil_module.f90#soil]] - `soil_profile`
- [[water_body_module.f90#wet_wat_a]] - `water_body`
- [[water_body_module.f90#wet_wat_d]] - `water_body`
- [[water_body_module.f90#wet_wat_m]] - `water_body`
- [[water_body_module.f90#wet_wat_y]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: salt_irrig.f90
note_file: salt_irrig.f90
subroutine: salt_irrig
module:
  - water_allocation_module
  - water_body_module
  - aquifer_module
  - reservoir_data_module
  - hydrograph_module
  - hru_module
  - salt_module
  - salt_aquifer
  - ch_salt_module
  - res_salt_module
  - basin_module
  - constituent_mass_module
calls: []
uses_variables:
  - aquifer_module.f90#aqu_d
  - basin_module.f90#bsn_cc
  - ch_salt_module.f90#chsalt_d
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_irr
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#res_water
  - constituent_mass_module.f90#wet_water
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#sp_ob1
  - res_salt_module.f90#ressalt_d
  - res_salt_module.f90#wetsalt_d
  - salt_aquifer.f90#asaltb_d
  - salt_module.f90#hsaltb_d
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#wallod_out
input_variables: []
reads: []
writes: []
purpose: "this subroutine adds salt mass from irrigation water into the soil profile, and removes salt mass; from the source object"
---

# salt_irrig

> [!info] Summary
> this subroutine adds salt mass from irrigation water into the soil profile, and removes salt mass; from the source object

## Basic Information
- **Type**: `subroutine`
- **Source file**: `salt_irrig.f90`
- **Modules used**:
  - [[water_allocation_module.f90]]
  - [[water_body_module.f90]]
  - [[aquifer_module.f90]]
  - [[reservoir_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[salt_module.f90]]
  - [[salt_aquifer.f90]]
  - [[ch_salt_module.f90]]
  - [[res_salt_module.f90]]
  - [[basin_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wallo_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[aquifer_module.f90#aqu_d]] - `aquifer_dynamic`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[ch_salt_module.f90#chsalt_d]] - `ch_salt_output`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_irr]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#res_water]] - `constituent_mass`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[res_salt_module.f90#ressalt_d]] - `res_salt_output`
- [[res_salt_module.f90#wetsalt_d]] - `res_salt_output`
- [[salt_aquifer.f90#asaltb_d]] - `object_salt_balance_aqu`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#wallod_out]] - `water_allocation_output`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cs_balance.f90
note_file: cs_balance.f90
subroutine: cs_balance
module:
  - hydrograph_module
  - organic_mineral_mass_module
  - output_landscape_module
  - aquifer_module
  - hru_module
  - soil_module
  - time_module
  - constituent_mass_module
  - cs_module
  - cs_aquifer
  - res_cs_module
  - ch_cs_module
  - gwflow_module
calls: []
uses_variables:
  - ch_cs_module.f90#chcs_d
  - constituent_mass_module.f90#cs_aqu
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#reccsb_d
  - constituent_mass_module.f90#recoutcsb_d
  - cs_aquifer.f90#acsb_d
  - cs_module.f90#cs_basin_aa
  - cs_module.f90#cs_basin_mo
  - cs_module.f90#cs_basin_yr
  - cs_module.f90#hcsb_d
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#ncell
  - hru_module.f90#hru
  - hru_module.f90#latq
  - hru_module.f90#mo
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - organic_mineral_mass_module.f90#fert
  - res_cs_module.f90#rescs_d
  - res_cs_module.f90#wetcs_d
  - soil_module.f90#soil
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates total constituent mass in system and writes out data to perform; a system-wide constituent mass balance"
---

# cs_balance

> [!info] Summary
> this subroutine calculates total constituent mass in system and writes out data to perform; a system-wide constituent mass balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cs_balance.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[output_landscape_module.f90]]
  - [[aquifer_module.f90]]
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[cs_module.f90]]
  - [[cs_aquifer.f90]]
  - [[res_cs_module.f90]]
  - [[ch_cs_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[ch_cs_module.f90#chcs_d]] - `ch_cs_output`
- [[constituent_mass_module.f90#cs_aqu]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#reccsb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutcsb_d]] - `constituent_mass`
- [[cs_aquifer.f90#acsb_d]] - `object_cs_balance_aqu`
- [[cs_module.f90#cs_basin_aa]] - `real`
- [[cs_module.f90#cs_basin_mo]] - `real`
- [[cs_module.f90#cs_basin_yr]] - `real`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#ncell]] - `integer`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[organic_mineral_mass_module.f90#fert]] - `fertilizer_mass`
- [[res_cs_module.f90#rescs_d]] - `res_cs_output`
- [[res_cs_module.f90#wetcs_d]] - `res_cs_output`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_pump_allo.f90
note_file: gwflow_pump_allo.f90
subroutine: gwflow_pump_allo
module:
  - gwflow_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
  - soil_module
  - constituent_mass_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#wet_water
  - cs_module.f90#hcsb_d
  - gwflow_module.f90#cell_id_list
  - gwflow_module.f90#grid_type
  - gwflow_module.f90#gw_cp
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_rho
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#gwsol_cons
  - gwflow_module.f90#gwsol_salt
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#hru_cells
  - gwflow_module.f90#hru_num_cells
  - hru_module.f90#hru
  - hru_module.f90#irrn
  - hru_module.f90#irrp
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#wet
  - organic_mineral_mass_module.f90#soil1
  - res_cs_module.f90#wetcs_d
  - res_salt_module.f90#wetsalt_d
  - salt_module.f90#hsaltb_d
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is extracted; from gwflow grid cells; (pumping volume are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_pump_allo

> [!info] Summary
> this subroutine determines the volume of groundwater that is extracted; from gwflow grid cells; (pumping volume are used in gwflow_simulate, in groundwater balance equations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_pump_allo.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[hru_module.f90]]
  - [[hydrograph_module.f90]]
  - [[soil_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[res_salt_module.f90]]
  - [[res_cs_module.f90]]
  - [[salt_module.f90]]
  - [[cs_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[wallo_withdraw.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#wet_water]] - `constituent_mass`
- [[cs_module.f90#hcsb_d]] - `object_cs_balance`
- [[gwflow_module.f90#cell_id_list]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#grid_type]] - `character*15`
- [[gwflow_module.f90#gw_cp]] - `real`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_rho]] - `real`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#gwsol_cons]] - `integer`
- [[gwflow_module.f90#gwsol_salt]] - `integer`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#hru_cells]] - `integer, dimension (:,:), allocatable`
- [[gwflow_module.f90#hru_num_cells]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#irrn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#irrp]] - `real, dimension (:), allocatable`
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#wet]] - `hyd_output`
- [[organic_mineral_mass_module.f90#soil1]] - `soil_profile_mass`
- [[res_cs_module.f90#wetcs_d]] - `res_cs_output`
- [[res_salt_module.f90#wetsalt_d]] - `res_salt_output`
- [[salt_module.f90#hsaltb_d]] - `object_salt_balance`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

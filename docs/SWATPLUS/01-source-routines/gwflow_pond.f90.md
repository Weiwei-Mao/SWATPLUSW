---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_pond.f90
note_file: gwflow_pond.f90
subroutine: gwflow_pond
module:
  - gwflow_module
  - hydrograph_module
  - time_module
  - constituent_mass_module
  - water_allocation_module
  - climate_module
calls: []
uses_variables:
  - climate_module.f90#wst
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_db
  - gwflow_module.f90#div_conc_cs
  - gwflow_module.f90#div_conc_salt
  - gwflow_module.f90#gw_canl_div_info
  - gwflow_module.f90#gw_daycount
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_npond
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_pond_div_flag
  - gwflow_module.f90#gw_pond_flag
  - gwflow_module.f90#gw_pond_info
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gwflag_flux
  - gwflow_module.f90#gwsol_cons
  - gwflow_module.f90#gwsol_nm
  - gwflow_module.f90#gwsol_salt
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#in_ponds
  - gwflow_module.f90#ncell
  - gwflow_module.f90#out_pond_bal
  - gwflow_module.f90#out_pond_conc
  - gwflow_module.f90#out_pond_mass
  - gwflow_module.f90#out_pond_sol
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#iwst
  - time_module.f90#time
  - water_allocation_module.f90#canal
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates the volume of seepage from recharge ponds;; removes water from source channel or canal diversion;; writes out recharge pond water balance"
---

# gwflow_pond

> [!info] Summary
> this subroutine calculates the volume of seepage from recharge ponds;; removes water from source channel or canal diversion;; writes out recharge pond water balance

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_pond.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[water_allocation_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[gwflow_simulate.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[gwflow_module.f90#div_conc_cs]] - `real, allocatable`
- [[gwflow_module.f90#div_conc_salt]] - `real, allocatable`
- [[gwflow_module.f90#gw_canl_div_info]] - `canal_info`
- [[gwflow_module.f90#gw_daycount]] - `integer`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_npond]] - `integer`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_pond_div_flag]] - `integer`
- [[gwflow_module.f90#gw_pond_flag]] - `integer`
- [[gwflow_module.f90#gw_pond_info]] - `cell_pond_info`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gwflag_flux]] - `integer`
- [[gwflow_module.f90#gwsol_cons]] - `integer`
- [[gwflow_module.f90#gwsol_nm]] - `character (len=16), allocatable`
- [[gwflow_module.f90#gwsol_salt]] - `integer`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#in_ponds]] - `integer`
- [[gwflow_module.f90#ncell]] - `integer`
- [[gwflow_module.f90#out_pond_bal]] - `integer`
- [[gwflow_module.f90#out_pond_conc]] - `integer`
- [[gwflow_module.f90#out_pond_mass]] - `integer`
- [[gwflow_module.f90#out_pond_sol]] - `integer`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#canal]] - `water_canal_data`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

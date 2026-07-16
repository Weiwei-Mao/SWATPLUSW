---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_biomass_gro.f90
note_file: pl_biomass_gro.f90
subroutine: pl_biomass_gro
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - climate_module
  - hydrograph_module
  - constituent_mass_module
  - salt_module
  - salt_data_module
  - output_landscape_module
calls:
  - pl_tstr
  - pl_nup
  - pl_pup
  - salt_uptake
  - cs_uptake
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_prm
  - carbon_module.f90#hpc_d
  - climate_module.f90#co2y
  - climate_module.f90#wgn
  - climate_module.f90#wst
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#bioday
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#par
  - hru_module.f90#rto_no3
  - hru_module.f90#rto_solp
  - hru_module.f90#sum_no3
  - hru_module.f90#sum_solp
  - hru_module.f90#uapd
  - hru_module.f90#uapd_tot
  - hru_module.f90#uno3d
  - hru_module.f90#uno3d_tot
  - hru_module.f90#vpd
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ob
  - organic_mineral_mass_module.f90#pl_mass_up
  - output_landscape_module.f90#hpw_d
  - plant_data_module.f90#plcp
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - salt_data_module.f90#salt_effect
  - salt_module.f90#salt_uptake_on
input_variables: []
reads: []
writes: []
purpose: ""
---

# pl_biomass_gro

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_biomass_gro.f90`
- **Modules used**:
  - [[plant_data_module.f90]]
  - [[basin_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[carbon_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[climate_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[salt_module.f90]]
  - [[salt_data_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 5 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[pl_tstr.f90]]
- [[pl_nup.f90]]
- [[pl_pup.f90]]
- [[salt_uptake.f90]]
- [[cs_uptake.f90]]

**Called by:**

- [[pl_grow.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[carbon_module.f90#hpc_d]] - `carbon_plant_gain_losses`
- [[climate_module.f90#co2y]] - `real, dimension(:), allocatable`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#bioday]] - `real`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#par]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rto_no3]] - `real`
- [[hru_module.f90#rto_solp]] - `real`
- [[hru_module.f90#sum_no3]] - `real`
- [[hru_module.f90#sum_solp]] - `real`
- [[hru_module.f90#uapd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uapd_tot]] - `real`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d_tot]] - `real`
- [[hru_module.f90#vpd]] - `real`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[organic_mineral_mass_module.f90#pl_mass_up]] - `organic_mass`
- [[output_landscape_module.f90#hpw_d]] - `output_plantweather`
- [[plant_data_module.f90#plcp]] - `plant_cp`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[salt_data_module.f90#salt_effect]] - `integer`
- [[salt_module.f90#salt_uptake_on]] - `integer`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

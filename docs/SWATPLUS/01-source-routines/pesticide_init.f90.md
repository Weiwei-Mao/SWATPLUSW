---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pesticide_init.f90
note_file: pesticide_init.f90
subroutine: pesticide_init
module:
  - hru_module
  - soil_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - hydrograph_module
  - plant_module
  - pesticide_data_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_irr
  - constituent_mass_module.f90#cs_pl
  - constituent_mass_module.f90#cs_soil
  - constituent_mass_module.f90#pest_soil_ini
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#sol_plt_ini
  - hydrograph_module.f90#sp_ob
  - output_ls_pesticide_module.f90#hpestb_d
  - plant_module.f90#pcom
  - soil_module.f90#soil
input_variables: []
reads: []
writes: []
purpose: "this subroutine calls subroutines which read input data for the; databases and the HRUs"
---

# pesticide_init

> [!info] Summary
> this subroutine calls subroutines which read input data for the; databases and the HRUs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pesticide_init.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[soil_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[hydrograph_module.f90]]
  - [[plant_module.f90]]
  - [[pesticide_data_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_irr]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_pl]] - `plant_constituent_mass`
- [[constituent_mass_module.f90#cs_soil]] - `soil_constituent_mass`
- [[constituent_mass_module.f90#pest_soil_ini]] - `cs_soil_init_concentrations`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#sol_plt_ini]] - `soil_plant_initialize`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[output_ls_pesticide_module.f90#hpestb_d]] - `object_pesticide_balance`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

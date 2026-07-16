---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_carbon_output.f90
note_file: hru_carbon_output.f90
subroutine: hru_carbon_output
module:
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - hydrograph_module
  - organic_mineral_mass_module
  - soil_module
  - carbon_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - carbon_module.f90#hpc_a
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hpc_m
  - carbon_module.f90#hpc_y
  - carbon_module.f90#hpcz
  - carbon_module.f90#hrc_a
  - carbon_module.f90#hrc_d
  - carbon_module.f90#hrc_m
  - carbon_module.f90#hrc_y
  - carbon_module.f90#hrcz
  - carbon_module.f90#hsc_a
  - carbon_module.f90#hsc_d
  - carbon_module.f90#hsc_m
  - carbon_module.f90#hsc_y
  - carbon_module.f90#hscf_a
  - carbon_module.f90#hscf_d
  - carbon_module.f90#hscf_m
  - carbon_module.f90#hscf_y
  - carbon_module.f90#hscfz
  - carbon_module.f90#hscz
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# hru_carbon_output

> [!info] Summary
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_carbon_output.f90`
- **Modules used**:
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[output_landscape_module.f90]]
  - [[hydrograph_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[soil_module.f90]]
  - [[carbon_module.f90]]
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
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[carbon_module.f90#hpc_a]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_m]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpc_y]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpcz]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hrc_a]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_m]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrc_y]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrcz]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hsc_a]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_m]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hsc_y]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hscf_a]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_d]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_m]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscf_y]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscfz]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscz]] - `carbon_soil_gain_losses`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

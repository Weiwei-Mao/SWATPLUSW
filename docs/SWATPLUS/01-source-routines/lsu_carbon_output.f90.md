---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsu_carbon_output.f90
note_file: lsu_carbon_output.f90
subroutine: lsu_carbon_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - carbon_module
  - plant_module
  - organic_mineral_mass_module
  - output_landscape_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - carbon_module.f90#hpc_d
  - carbon_module.f90#hpcz
  - carbon_module.f90#hrc_d
  - carbon_module.f90#hrcz
  - carbon_module.f90#hsc_d
  - carbon_module.f90#hscf_d
  - carbon_module.f90#hscfz
  - carbon_module.f90#hscz
  - carbon_module.f90#lpc_a
  - carbon_module.f90#lpc_d
  - carbon_module.f90#lpc_m
  - carbon_module.f90#lpc_y
  - carbon_module.f90#lrc_a
  - carbon_module.f90#lrc_d
  - carbon_module.f90#lrc_m
  - carbon_module.f90#lrc_y
  - carbon_module.f90#lsc_a
  - carbon_module.f90#lsc_d
  - carbon_module.f90#lsc_m
  - carbon_module.f90#lsc_y
  - carbon_module.f90#lscf_a
  - carbon_module.f90#lscf_d
  - carbon_module.f90#lscf_m
  - carbon_module.f90#lscf_y
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - organic_mineral_mass_module.f90#pl_mass
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "area-weighted LSU aggregations of three HRU-level carbon families:; lsu_carb_gl_* (gain/loss; soil + residue + plant flux); lsu_scf_* (HRU C transformations)"
---

# lsu_carbon_output

> [!info] Summary
> area-weighted LSU aggregations of three HRU-level carbon families:; lsu_carb_gl_*    (gain/loss; soil + residue + plant flux); lsu_scf_*        (HRU C transformations)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsu_carbon_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[carbon_module.f90]]
  - [[plant_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[output_landscape_module.f90]]
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
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[carbon_module.f90#hpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hpcz]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#hrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hrcz]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#hsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#hscf_d]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscfz]] - `carbon_soil_transformations`
- [[carbon_module.f90#hscz]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lpc_a]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_d]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_m]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lpc_y]] - `carbon_plant_gain_losses`
- [[carbon_module.f90#lrc_a]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_d]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_m]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lrc_y]] - `carbon_residue_gain_losses`
- [[carbon_module.f90#lsc_a]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_d]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_m]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lsc_y]] - `carbon_soil_gain_losses`
- [[carbon_module.f90#lscf_a]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_d]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_m]] - `carbon_soil_transformations`
- [[carbon_module.f90#lscf_y]] - `carbon_soil_transformations`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_pathogen_output.f90
note_file: hru_pathogen_output.f90
subroutine: hru_pathogen_output
module:
  - output_ls_pathogen_module
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - constituent_mass_module
  - hydrograph_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_db
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - output_ls_pathogen_module.f90#hpath_bal
  - output_ls_pathogen_module.f90#hpathb_a
  - output_ls_pathogen_module.f90#hpathb_m
  - output_ls_pathogen_module.f90#hpathb_y
  - output_ls_pathogen_module.f90#pathbz
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# hru_pathogen_output

> [!info] Summary
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_pathogen_output.f90`
- **Modules used**:
  - [[output_ls_pathogen_module.f90]]
  - [[plant_module.f90]]
  - [[plant_data_module.f90]]
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[output_landscape_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[output_ls_pathogen_module.f90#hpath_bal]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_a]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_m]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#hpathb_y]] - `object_pathogen_balance`
- [[output_ls_pathogen_module.f90#pathbz]] - `pathogen_balance`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

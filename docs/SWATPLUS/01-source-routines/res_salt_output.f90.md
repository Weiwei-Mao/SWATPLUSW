---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_salt_output.f90
note_file: res_salt_output.f90
subroutine: res_salt_output
module:
  - output_ls_pesticide_module
  - res_pesticide_module
  - res_salt_module
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
  - hydrograph_module.f90#irrig
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob1
  - res_salt_module.f90#ressalt_a
  - res_salt_module.f90#ressalt_d
  - res_salt_module.f90#ressalt_m
  - res_salt_module.f90#ressalt_y
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs salt mass in reservoirs"
---

# res_salt_output

> [!info] Summary
> this subroutine outputs salt mass in reservoirs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_salt_output.f90`
- **Modules used**:
  - [[output_ls_pesticide_module.f90]]
  - [[res_pesticide_module.f90]]
  - [[res_salt_module.f90]]
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
- [[hydrograph_module.f90#irrig]] - `irrigation_water_transfer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[res_salt_module.f90#ressalt_a]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_d]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_m]] - `res_salt_output`
- [[res_salt_module.f90#ressalt_y]] - `res_salt_output`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

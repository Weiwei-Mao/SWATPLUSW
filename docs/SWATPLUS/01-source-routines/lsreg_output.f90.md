---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsreg_output.f90
note_file: lsreg_output.f90
subroutine: lsreg_output
module:
  - time_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - plant_data_module
  - landuse_data_module
  - hru_module
  - plant_module
  - output_landscape_module
  - organic_mineral_mass_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - calibration_data_module.f90#lsu_out
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mo
  - landuse_data_module.f90#cn
  - landuse_data_module.f90#lum
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwb_a
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwb_m
  - output_landscape_module.f90#hwb_y
  - output_landscape_module.f90#hwbz
  - output_landscape_module.f90#rls_a
  - output_landscape_module.f90#rls_d
  - output_landscape_module.f90#rls_m
  - output_landscape_module.f90#rls_y
  - output_landscape_module.f90#rnb_a
  - output_landscape_module.f90#rnb_d
  - output_landscape_module.f90#rnb_m
  - output_landscape_module.f90#rnb_y
  - output_landscape_module.f90#rpw_a
  - output_landscape_module.f90#rpw_d
  - output_landscape_module.f90#rpw_m
  - output_landscape_module.f90#rpw_y
  - output_landscape_module.f90#rwb_a
  - output_landscape_module.f90#rwb_d
  - output_landscape_module.f90#rwb_m
  - output_landscape_module.f90#rwb_y
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "! PRINT CODES: \"avann\" = average annual (always print); \"year\" = yearly; \"mon\" = monthly"
---

# lsreg_output

> [!info] Summary
> !    PRINT CODES: "avann" = average annual (always print); "year"  = yearly; "mon"   = monthly

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsreg_output.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[output_landscape_module.f90]]
  - [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[landuse_data_module.f90#cn]] - `curvenumber_table`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[output_landscape_module.f90#rls_a]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_d]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_m]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_y]] - `regional_output_losses`
- [[output_landscape_module.f90#rnb_a]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_d]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_m]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_y]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rpw_a]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_d]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_m]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_y]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rwb_a]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_d]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_m]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_y]] - `regional_output_waterbal`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

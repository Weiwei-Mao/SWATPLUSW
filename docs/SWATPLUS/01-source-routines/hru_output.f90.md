---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_output.f90
note_file: hru_output.f90
subroutine: hru_output
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
  - hru_module
  - landuse_data_module
calls:
  - soil_nutcarb_write
  - soil_nutcarb_write_legacy
uses_variables:
  - basin_module.f90#pco
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ilu
  - hru_module.f90#ipl
  - hru_module.f90#latq
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#nplnt
  - hru_module.f90#percn
  - hru_module.f90#pplnt
  - hru_module.f90#qtile
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob1
  - landuse_data_module.f90#lum
  - organic_mineral_mass_module.f90#pl_mass
  - output_landscape_module.f90#hls_a
  - output_landscape_module.f90#hls_d
  - output_landscape_module.f90#hls_m
  - output_landscape_module.f90#hls_y
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hnb_a
  - output_landscape_module.f90#hnb_d
  - output_landscape_module.f90#hnb_m
  - output_landscape_module.f90#hnb_y
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpw_a
  - output_landscape_module.f90#hpw_d
  - output_landscape_module.f90#hpw_m
  - output_landscape_module.f90#hpw_y
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwb_a
  - output_landscape_module.f90#hwb_d
  - output_landscape_module.f90#hwb_m
  - output_landscape_module.f90#hwb_y
  - output_landscape_module.f90#hwbz
  - plant_data_module.f90#pldb
  - plant_module.f90#pcom
  - soil_module.f90#soil
  - time_module.f90#ndays
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# hru_output

> [!info] Summary
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_output.f90`
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
  - [[hru_module.f90]]
  - [[landuse_data_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[soil_nutcarb_write.f90]]
- [[soil_nutcarb_write_legacy.f90]]

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ilu]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#nplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#percn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#pplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qtile]] - `real`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[organic_mineral_mass_module.f90#pl_mass]] - `plant_community_mass`
- [[output_landscape_module.f90#hls_a]] - `output_losses`
- [[output_landscape_module.f90#hls_d]] - `output_losses`
- [[output_landscape_module.f90#hls_m]] - `output_losses`
- [[output_landscape_module.f90#hls_y]] - `output_losses`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hnb_a]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_d]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_m]] - `output_nutbal`
- [[output_landscape_module.f90#hnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpw_a]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_d]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_m]] - `output_plantweather`
- [[output_landscape_module.f90#hpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_module.f90#pcom]] - `plant_community`
- [[soil_module.f90#soil]] - `soil_profile`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

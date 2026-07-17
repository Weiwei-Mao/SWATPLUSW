---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_read.f90
note_file: sd_channel_read.f90
subroutine: sd_channel_read
module:
  - basin_module
  - input_file_module
  - maximum_data_module
  - channel_data_module
  - channel_velocity_module
  - ch_pesticide_module
  - ch_salt_module
  - ch_cs_module
  - sd_channel_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
  - pathogen_data_module
  - water_body_module
calls: []
uses_variables:
  - ch_cs_module.f90#chcs_a
  - ch_cs_module.f90#chcs_d
  - ch_cs_module.f90#chcs_m
  - ch_cs_module.f90#chcs_y
  - ch_pesticide_module.f90#bchpst_a
  - ch_pesticide_module.f90#bchpst_d
  - ch_pesticide_module.f90#bchpst_m
  - ch_pesticide_module.f90#bchpst_y
  - ch_pesticide_module.f90#chpst
  - ch_pesticide_module.f90#chpst_a
  - ch_pesticide_module.f90#chpst_d
  - ch_pesticide_module.f90#chpst_m
  - ch_pesticide_module.f90#chpst_y
  - ch_pesticide_module.f90#chpstz
  - ch_salt_module.f90#chsalt_a
  - ch_salt_module.f90#chsalt_d
  - ch_salt_module.f90#chsalt_m
  - ch_salt_module.f90#chsalt_y
  - channel_data_module.f90#ch_init
  - channel_data_module.f90#ch_init_cs
  - channel_data_module.f90#ch_nut
  - channel_velocity_module.f90#sd_ch_vel
  - constituent_mass_module.f90#ch_benthic
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_cha_ini
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#path_init_name
  - constituent_mass_module.f90#pest_init_name
  - constituent_mass_module.f90#salt_cha_ini
  - hydrograph_module.f90#ch_fp_wb
  - hydrograph_module.f90#ch_in_a
  - hydrograph_module.f90#ch_in_d
  - hydrograph_module.f90#ch_in_m
  - hydrograph_module.f90#ch_in_y
  - hydrograph_module.f90#ch_om_water_init
  - hydrograph_module.f90#ch_out_a
  - hydrograph_module.f90#ch_out_d
  - hydrograph_module.f90#ch_out_m
  - hydrograph_module.f90#ch_out_y
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#ch_stor_a
  - hydrograph_module.f90#ch_stor_hdsep
  - hydrograph_module.f90#ch_stor_m
  - hydrograph_module.f90#ch_stor_y
  - hydrograph_module.f90#fp_om_water_init
  - hydrograph_module.f90#fp_stor
  - hydrograph_module.f90#hyd_sep_array
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#om_init_name
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#tot_stor
  - hydrograph_module.f90#wet_stor
  - input_file_module.f90#in_cha
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#ch_morph
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#ch_sed_bud
  - sd_channel_module.f90#ch_sed_bud_a
  - sd_channel_module.f90#ch_sed_bud_m
  - sd_channel_module.f90#ch_sed_bud_y
  - sd_channel_module.f90#chsd_a
  - sd_channel_module.f90#chsd_d
  - sd_channel_module.f90#chsd_m
  - sd_channel_module.f90#chsd_y
  - sd_channel_module.f90#gully
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_chd
  - sd_channel_module.f90#sd_chd1
  - sd_channel_module.f90#sd_dat
  - sd_channel_module.f90#sd_init
  - water_body_module.f90#ch_wat_a
  - water_body_module.f90#ch_wat_d
  - water_body_module.f90#ch_wat_m
  - water_body_module.f90#ch_wat_y
input_variables:
  - sd_channel_module.f90#sd_dat
reads:
  - in_cha%chan_ez
writes: []
purpose: ""
---

# sd_channel_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_read.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[channel_data_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[ch_pesticide_module.f90]]
  - [[ch_salt_module.f90]]
  - [[ch_cs_module.f90]]
  - [[sd_channel_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[pathogen_data_module.f90]]
  - [[water_body_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_cha.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[ch_cs_module.f90#chcs_a]] - `ch_cs_output`
- [[ch_cs_module.f90#chcs_d]] - `ch_cs_output`
- [[ch_cs_module.f90#chcs_m]] - `ch_cs_output`
- [[ch_cs_module.f90#chcs_y]] - `ch_cs_output`
- [[ch_pesticide_module.f90#bchpst_a]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#bchpst_d]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#bchpst_m]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#bchpst_y]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_a]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_d]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_m]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_y]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpstz]] - `ch_pesticide_output`
- [[ch_salt_module.f90#chsalt_a]] - `ch_salt_output`
- [[ch_salt_module.f90#chsalt_d]] - `ch_salt_output`
- [[ch_salt_module.f90#chsalt_m]] - `ch_salt_output`
- [[ch_salt_module.f90#chsalt_y]] - `ch_salt_output`
- [[channel_data_module.f90#ch_init]] - `channel_init_datafiles`
- [[channel_data_module.f90#ch_init_cs]] - `channel_init_datafiles_cs`
- [[channel_data_module.f90#ch_nut]] - `channel_nut_data`
- [[channel_velocity_module.f90#sd_ch_vel]] - `channel_velocity_parameters`
- [[constituent_mass_module.f90#ch_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_cha_ini]] - `cs_cha_init_concentrations`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#path_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#pest_init_name]] - `character(len=16), dimension(:), allocatable`
- [[constituent_mass_module.f90#salt_cha_ini]] - `salt_cha_init_concentrations`
- [[hydrograph_module.f90#ch_fp_wb]] - `channel_floodplain_water_balance`
- [[hydrograph_module.f90#ch_in_a]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_m]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_a]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_m]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor_a]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor_hdsep]] - `hyd_sep`
- [[hydrograph_module.f90#ch_stor_m]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor_y]] - `hyd_output`
- [[hydrograph_module.f90#fp_om_water_init]] - `hyd_output`
- [[hydrograph_module.f90#fp_stor]] - `hyd_output`
- [[hydrograph_module.f90#hyd_sep_array]] - `real, dimension(:,:),allocatable`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#om_init_name]] - `character(len=16), dimension(:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#tot_stor]] - `hyd_output`
- [[hydrograph_module.f90#wet_stor]] - `hyd_output`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#ch_morph]] - `channel_morphology_output`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#ch_sed_bud]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_a]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_m]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_bud_y]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#chsd_a]] - `sd_ch_output`
- [[sd_channel_module.f90#chsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#chsd_m]] - `sd_ch_output`
- [[sd_channel_module.f90#chsd_y]] - `sd_ch_output`
- [[sd_channel_module.f90#gully]] - `gully_data`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_chd]] - `swatdeg_hydsed_data`
- [[sd_channel_module.f90#sd_chd1]] - `swatdeg_sednut_data`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[sd_channel_module.f90#sd_init]] - `swatdeg_init_datafiles`
- [[water_body_module.f90#ch_wat_a]] - `water_body`
- [[water_body_module.f90#ch_wat_d]] - `water_body`
- [[water_body_module.f90#ch_wat_m]] - `water_body`
- [[water_body_module.f90#ch_wat_y]] - `water_body`

**Populated by file reads:**

- [[sd_channel_module.f90#sd_dat]]

## File I/O
- **Reads**:
  - [[channel-lte.cha]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Beginning-187, allocation and initiation
- line 189, check [[input_file_module.f90#in_cha]], file [[channel_lte.cha]]
- read into [[sd_channel_module.f90#sd_dat]]
	- name
	- initc, initial
	- hydc, hydrology
	- sedc, sediment
	- nutc, nutrient
- Then initialize 









<!-- USER-NOTES-END -->

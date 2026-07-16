---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sd_channel_control3.f90
note_file: sd_channel_control3.f90
subroutine: sd_channel_control3
module:
  - sd_channel_module
  - channel_velocity_module
  - basin_module
  - hydrograph_module
  - constituent_mass_module
  - conditional_module
  - channel_data_module
  - channel_module
  - ch_pesticide_module
  - climate_module
  - water_body_module
  - time_module
  - ch_salt_module
  - ch_cs_module
  - gwflow_module
  - water_allocation_module
  - maximum_data_module
calls:
  - cli_lapse
  - gwflow_channel_exch
  - gwflow_canal
  - gwflow_tile
  - gwflow_satexcess
  - sd_channel_sediment3
  - ch_rtmusk
  - ch_rtpest
  - ch_rtpath
  - rcurv_interp_flo
  - ch_watqual4
  - wallo_control
  - ch_temp
uses_variables:
  - basin_module.f90#bsn_cc
  - ch_cs_module.f90#chcs_d
  - ch_pesticide_module.f90#chpst
  - ch_pesticide_module.f90#chpst_d
  - ch_pesticide_module.f90#frsol
  - ch_pesticide_module.f90#frsrb
  - ch_salt_module.f90#chsalt_d
  - channel_module.f90#ben_area
  - channel_module.f90#ch
  - channel_module.f90#jnut
  - channel_module.f90#peakr
  - channel_module.f90#rttime
  - channel_velocity_module.f90#sd_ch_vel
  - climate_module.f90#w
  - climate_module.f90#wst
  - constituent_mass_module.f90#aq_chcs
  - constituent_mass_module.f90#ch_benthic
  - constituent_mass_module.f90#ch_water
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#hcs2
  - constituent_mass_module.f90#hcs3
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - hydrograph_module.f90#aq_ch
  - hydrograph_module.f90#bank_ero
  - hydrograph_module.f90#bed_ero
  - hydrograph_module.f90#ch_dep
  - hydrograph_module.f90#ch_in_d
  - hydrograph_module.f90#ch_out_d
  - hydrograph_module.f90#ch_stor
  - hydrograph_module.f90#ch_stor_hdsep
  - hydrograph_module.f90#ch_trans
  - hydrograph_module.f90#fp_dep
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hdsep1
  - hydrograph_module.f90#hdsep2
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#ht2
  - hydrograph_module.f90#ht3
  - hydrograph_module.f90#hyd_sep_array
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#ch_rcurv
  - sd_channel_module.f90#ch_sed_bud
  - sd_channel_module.f90#ch_sed_budz
  - sd_channel_module.f90#chsd_d
  - sd_channel_module.f90#peakrate
  - sd_channel_module.f90#rcurv
  - sd_channel_module.f90#sd_ch
  - sd_channel_module.f90#sd_dat
  - sd_channel_module.f90#wtemp
  - time_module.f90#time
  - water_allocation_module.f90#trn_m3
  - water_allocation_module.f90#wallo
  - water_body_module.f90#ch_wat_d
input_variables: []
reads: []
writes: []
purpose: ""
---

# sd_channel_control3

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sd_channel_control3.f90`
- **Modules used**:
  - [[sd_channel_module.f90]]
  - [[channel_velocity_module.f90]]
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[conditional_module.f90]]
  - [[channel_data_module.f90]]
  - [[channel_module.f90]]
  - [[ch_pesticide_module.f90]]
  - [[climate_module.f90]]
  - [[water_body_module.f90]]
  - [[time_module.f90]]
  - [[ch_salt_module.f90]]
  - [[ch_cs_module.f90]]
  - [[gwflow_module.f90]]
  - [[water_allocation_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 13 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cli_lapse.f90]]
- [[gwflow_channel_exch.f90]]
- [[gwflow_canal.f90]]
- [[gwflow_tile.f90]]
- [[gwflow_satexcess.f90]]
- [[sd_channel_sediment3.f90]]
- [[ch_rtmusk.f90]]
- [[ch_rtpest.f90]]
- [[ch_rtpath.f90]]
- [[rcurv_interp_flo.f90]]
- [[ch_watqual4.f90]]
- [[wallo_control.f90]]
- [[ch_temp.f90]]

**Called by:**

- [[command.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[ch_cs_module.f90#chcs_d]] - `ch_cs_output`
- [[ch_pesticide_module.f90#chpst]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#chpst_d]] - `ch_pesticide_output`
- [[ch_pesticide_module.f90#frsol]] - `real`
- [[ch_pesticide_module.f90#frsrb]] - `real`
- [[ch_salt_module.f90#chsalt_d]] - `ch_salt_output`
- [[channel_module.f90#ben_area]] - `real`
- [[channel_module.f90#ch]] - `channel`
- [[channel_module.f90#jnut]] - `integer`
- [[channel_module.f90#peakr]] - `real`
- [[channel_module.f90#rttime]] - `real`
- [[channel_velocity_module.f90#sd_ch_vel]] - `channel_velocity_parameters`
- [[climate_module.f90#w]] - `weather_daily`
- [[climate_module.f90#wst]] - `weather_station`
- [[constituent_mass_module.f90#aq_chcs]] - `gw_load_hydrograph`
- [[constituent_mass_module.f90#ch_benthic]] - `constituent_mass`
- [[constituent_mass_module.f90#ch_water]] - `constituent_mass`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs3]] - `constituent_mass`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#aq_ch]] - `channel_aquifer_elements`
- [[hydrograph_module.f90#bank_ero]] - `hyd_output`
- [[hydrograph_module.f90#bed_ero]] - `hyd_output`
- [[hydrograph_module.f90#ch_dep]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor_hdsep]] - `hyd_sep`
- [[hydrograph_module.f90#ch_trans]] - `hyd_output`
- [[hydrograph_module.f90#fp_dep]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hdsep1]] - `hyd_sep`
- [[hydrograph_module.f90#hdsep2]] - `hyd_sep`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#ht2]] - `hyd_output`
- [[hydrograph_module.f90#ht3]] - `hyd_output`
- [[hydrograph_module.f90#hyd_sep_array]] - `real, dimension(:,:),allocatable`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#ch_rcurv]] - `channel_rating_curve`
- [[sd_channel_module.f90#ch_sed_bud]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#ch_sed_budz]] - `channel_sediment_budget_output`
- [[sd_channel_module.f90#chsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#peakrate]] - `real`
- [[sd_channel_module.f90#rcurv]] - `channel_rating_curve_parameters`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[sd_channel_module.f90#sd_dat]] - `swatdeg_datafiles`
- [[sd_channel_module.f90#wtemp]] - `real`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#trn_m3]] - `real`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_body_module.f90#ch_wat_d]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

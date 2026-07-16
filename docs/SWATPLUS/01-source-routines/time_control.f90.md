---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: time_control.f90
note_file: time_control.f90
subroutine: time_control
module:
  - maximum_data_module
  - calibration_data_module
  - plant_data_module
  - mgt_operations_module
  - hru_module
  - plant_module
  - soil_module
  - time_module
  - climate_module
  - basin_module
  - sd_channel_module
  - hru_lte_module
  - hydrograph_module
  - output_landscape_module
  - conditional_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - water_body_module
  - water_allocation_module
calls:
  - xmon
  - cli_precip_control
  - basin_sw_init
  - aqu_pest_output_init
  - date_and_time
  - sim_initday
  - climate_control
  - cli_atmodep_time_control
  - conditions
  - actions
  - mallo_control
  - command
  - calsoft_sum_output
  - mgt_newtillmix_cswat0
  - calsoft_ave_output
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#bsn_cc
  - basin_module.f90#bsn_sedbud
  - basin_module.f90#pco
  - calibration_data_module.f90#upd_cond
  - conditional_module.f90#d_tbl
  - conditional_module.f90#dtbl_scen
  - constituent_mass_module.f90#cs_db
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hru_module.f90#mgt_ops
  - hru_module.f90#mo
  - hru_module.f90#phubase
  - hru_module.f90#sedyld
  - hru_module.f90#yr_skip
  - hydrograph_module.f90#ch_in_y
  - hydrograph_module.f90#ch_out_y
  - hydrograph_module.f90#ch_stor_y
  - hydrograph_module.f90#chaz
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#res
  - hydrograph_module.f90#res_in_a
  - hydrograph_module.f90#res_out_a
  - hydrograph_module.f90#res_trap
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - hydrograph_module.f90#wtp_om_out
  - hydrograph_module.f90#wuse_om_out
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#sched
  - output_landscape_module.f90#bls_a
  - output_landscape_module.f90#hls_y
  - output_landscape_module.f90#hlsz
  - output_landscape_module.f90#hltls_y
  - output_landscape_module.f90#hltnb_y
  - output_landscape_module.f90#hltpw_y
  - output_landscape_module.f90#hltwb_y
  - output_landscape_module.f90#hnb_y
  - output_landscape_module.f90#hnbz
  - output_landscape_module.f90#hpw_y
  - output_landscape_module.f90#hpwz
  - output_landscape_module.f90#hwb_y
  - output_landscape_module.f90#hwbz
  - output_ls_pesticide_module.f90#hpestb_y
  - output_ls_pesticide_module.f90#pestbz
  - plant_data_module.f90#pldb
  - plant_data_module.f90#plts_bsn
  - plant_module.f90#basin_plants
  - plant_module.f90#bsn_crop_yld
  - plant_module.f90#bsn_crop_yld_aa
  - plant_module.f90#bsn_crop_yld_z
  - plant_module.f90#pcom
  - sd_channel_module.f90#ch_morph
  - sd_channel_module.f90#ch_morph_ord
  - sd_channel_module.f90#chsd_y
  - sd_channel_module.f90#chsdz
  - sd_channel_module.f90#sd_ch
  - time_module.f90#cal_sim
  - time_module.f90#ndays
  - time_module.f90#ndays_leap
  - time_module.f90#ndays_noleap
  - time_module.f90#ndmo
  - time_module.f90#time
  - time_module.f90#time_init
  - time_module.f90#yrs_print
  - water_allocation_module.f90#wallo
  - water_allocation_module.f90#walloz
  - water_body_module.f90#ch_wat_y
  - water_body_module.f90#wbodz
input_variables: []
reads: []
writes: []
purpose: "this subroutine contains the loops governing the modeling of processes; in the watershed"
---

# time_control

> [!info] Summary
> this subroutine contains the loops governing the modeling of processes; in the watershed

## Basic Information
- **Type**: `subroutine`
- **Source file**: `time_control.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[hru_module.f90]]
  - [[plant_module.f90]]
  - [[soil_module.f90]]
  - [[time_module.f90]]
  - [[climate_module.f90]]
  - [[basin_module.f90]]
  - [[sd_channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
  - [[conditional_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_ls_pesticide_module.f90]]
  - [[water_body_module.f90]]
  - [[water_allocation_module.f90]]
- **Subroutine calls**: 15 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]
- [[cli_precip_control.f90]]
- [[basin_sw_init.f90]]
- [[aqu_pest_output_init.f90]]
- `date_and_time`
- [[sim_initday.f90]]
- [[climate_control.f90]]
- [[cli_atmodep_time_control.f90]]
- [[conditions.f90]]
- [[actions.f90]]
- [[mallo_control.f90]]
- [[command.f90]]
- [[calsoft_sum_output.f90]]
- [[mgt_newtillmix_cswat0.f90]]
- [[calsoft_ave_output.f90]]

**Called by:**

- [[calhard_control.f90]]
- [[calsoft_hyd.f90]]
- [[calsoft_hyd_bfr_et.f90]]
- [[calsoft_hyd_bfr_latq.f90]]
- [[calsoft_hyd_bfr_perc.f90]]
- [[calsoft_hyd_bfr_pet.f90]]
- [[calsoft_hyd_bfr_surq.f90]]
- [[calsoft_plant.f90]]
- [[calsoft_sed.f90]]
- [[caltsoft_hyd.f90]]
- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#bsn_sedbud]] - `basin_sediment_budget`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[calibration_data_module.f90#upd_cond]] - `update_conditional`
- [[conditional_module.f90#d_tbl]] - `decision_table`
- [[conditional_module.f90#dtbl_scen]] - `decision_table`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hru_module.f90#mgt_ops]] - `integer, dimension (:,:), allocatable`
- [[hru_module.f90#mo]] - `integer`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#yr_skip]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#ch_in_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_y]] - `hyd_output`
- [[hydrograph_module.f90#ch_stor_y]] - `hyd_output`
- [[hydrograph_module.f90#chaz]] - `hyd_output`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#res_in_a]] - `hyd_output`
- [[hydrograph_module.f90#res_out_a]] - `hyd_output`
- [[hydrograph_module.f90#res_trap]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[hydrograph_module.f90#wtp_om_out]] - `hyd_output`
- [[hydrograph_module.f90#wuse_om_out]] - `hyd_output`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[output_landscape_module.f90#bls_a]] - `output_losses`
- [[output_landscape_module.f90#hls_y]] - `output_losses`
- [[output_landscape_module.f90#hlsz]] - `output_losses`
- [[output_landscape_module.f90#hltls_y]] - `output_losses`
- [[output_landscape_module.f90#hltnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hltpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hltwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hnb_y]] - `output_nutbal`
- [[output_landscape_module.f90#hnbz]] - `output_nutbal`
- [[output_landscape_module.f90#hpw_y]] - `output_plantweather`
- [[output_landscape_module.f90#hpwz]] - `output_plantweather`
- [[output_landscape_module.f90#hwb_y]] - `output_waterbal`
- [[output_landscape_module.f90#hwbz]] - `output_waterbal`
- [[output_ls_pesticide_module.f90#hpestb_y]] - `object_pesticide_balance`
- [[output_ls_pesticide_module.f90#pestbz]] - `pesticide_balance`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_data_module.f90#plts_bsn]] - `character(len=40), dimension (:), allocatable`
- [[plant_module.f90#basin_plants]] - `integer`
- [[plant_module.f90#bsn_crop_yld]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_aa]] - `basin_crop_yields`
- [[plant_module.f90#bsn_crop_yld_z]] - `basin_crop_yields`
- [[plant_module.f90#pcom]] - `plant_community`
- [[sd_channel_module.f90#ch_morph]] - `channel_morphology_output`
- [[sd_channel_module.f90#ch_morph_ord]] - `channel_morphology_output`
- [[sd_channel_module.f90#chsd_y]] - `sd_ch_output`
- [[sd_channel_module.f90#chsdz]] - `sd_ch_output`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[time_module.f90#cal_sim]] - `character (len=29)`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#ndays_leap]] - `integer, dimension (13)`
- [[time_module.f90#ndays_noleap]] - `integer, dimension (13)`
- [[time_module.f90#ndmo]] - `integer, dimension (12)`
- [[time_module.f90#time]] - `time_current`
- [[time_module.f90#time_init]] - `time_current`
- [[time_module.f90#yrs_print]] - `real`
- [[water_allocation_module.f90#wallo]] - `water_allocation`
- [[water_allocation_module.f90#walloz]] - `source_output`
- [[water_body_module.f90#ch_wat_y]] - `water_body`
- [[water_body_module.f90#wbodz]] - `water_body`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

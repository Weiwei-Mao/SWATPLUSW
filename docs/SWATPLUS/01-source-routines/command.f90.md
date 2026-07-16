---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: command.f90
note_file: command.f90
subroutine: command
module:
  - time_module
  - hydrograph_module
  - ru_module
  - channel_module
  - hru_lte_module
  - aquifer_module
  - sd_channel_module
  - reservoir_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - hru_module
  - basin_module
  - maximum_data_module
  - gwflow_module
  - soil_module
  - recall_module
  - water_allocation_module
calls:
  - wallo_control
  - hru_control
  - hyddep_output
  - hru_lte_control
  - ru_control
  - gwflow_simulate
  - aqu_1d_control
  - res_control
  - recall_nut
  - recall_salt
  - recall_cs
  - constit_hyd_mult
  - sd_channel_control3
  - flow_dur_curve
  - hydout_output
  - obj_output
  - wallo_allo_output
  - wallo_trn_output
  - wallo_treat_output
  - wallo_use_output
  - manure_source_output
  - manure_demand_output
  - hru_lte_output
  - hru_output
  - hru_carbon_output
  - wetland_output
  - wet_salt_output
  - wet_cs_output
  - hru_pesticide_output
  - hru_pathogen_output
  - hru_salt_output
  - hru_cs_output
  - soil_nutcarb_write
  - soil_carbvar_write
  - soil_nutcarb_write_legacy
  - soil_carbvar_write_legacy
  - aquifer_output
  - aqu_salt_output
  - aqu_cs_output
  - aqu_pesticide_output
  - channel_output
  - sd_chanmorph_output
  - sd_chanbud_output
  - sd_channel_output
  - cha_pesticide_output
  - ch_salt_output
  - ch_cs_output
  - cs_str_output
  - reservoir_output
  - res_pesticide_output
  - res_salt_output
  - res_cs_output
  - ru_output
  - ru_salt_output
  - ru_cs_output
  - recall_output
  - hydin_output
  - basin_ch_pest_output
  - basin_res_pest_output
  - basin_ls_pest_output
  - basin_aqu_pest_output
  - basin_output
  - lsu_output
  - lsu_carbon_output
  - basin_aquifer_output
  - basin_reservoir_output
  - basin_channel_output
  - basin_chanmorph_output
  - basin_chanbud_output
  - basin_sdchannel_output
  - basin_recall_output
  - salt_balance
  - cs_balance
uses_variables:
  - basin_module.f90#bsn_cc
  - basin_module.f90#pco
  - channel_module.f90#peakr
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#hcs2
  - constituent_mass_module.f90#hcs3
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - constituent_mass_module.f90#obcs_alloc
  - gwflow_module.f90#gw_daycount
  - gwflow_module.f90#hydsep_flag
  - gwflow_module.f90#out_hyd_sep
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#mo
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#ch_in_d
  - hydrograph_module.f90#ch_out_d
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#hd
  - hydrograph_module.f90#hdsep1
  - hydrograph_module.f90#ht1
  - hydrograph_module.f90#hyd_sep_array
  - hydrograph_module.f90#hz
  - hydrograph_module.f90#icmd
  - hydrograph_module.f90#isd_chsur
  - hydrograph_module.f90#isdch
  - hydrograph_module.f90#jrch
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#rec_d
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - maximum_data_module.f90#db_mx
  - recall_module.f90#recall_db
  - reservoir_module.f90#res_ob
  - ru_module.f90#iru
  - ru_module.f90#ru
  - sd_channel_module.f90#chsd_d
  - sd_channel_module.f90#peakrate
  - sd_channel_module.f90#sd_ch
  - time_module.f90#time
  - water_allocation_module.f90#wallo
input_variables: []
reads: []
writes: []
purpose: "for every day of simulation, this subroutine steps through the command; lines in the watershed configuration (.fig) file. Depending on the; command code on the .fig file line, a command loop is accessed"
---

# command

> [!info] Summary
> for every day of simulation, this subroutine steps through the command; lines in the watershed configuration (.fig) file. Depending on the; command code on the .fig file line, a command loop is accessed

## Basic Information
- **Type**: `subroutine`
- **Source file**: `command.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[ru_module.f90]]
  - [[channel_module.f90]]
  - [[hru_lte_module.f90]]
  - [[aquifer_module.f90]]
  - [[sd_channel_module.f90]]
  - [[reservoir_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[hru_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[gwflow_module.f90]]
  - [[soil_module.f90]]
  - [[recall_module.f90]]
  - [[water_allocation_module.f90]]
- **Subroutine calls**: 73 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[wallo_control.f90]]
- [[hru_control.f90]]
- [[hyddep_output.f90]]
- [[hru_lte_control.f90]]
- [[ru_control.f90]]
- [[gwflow_simulate.f90]]
- [[aqu_1d_control.f90]]
- [[res_control.f90]]
- [[recall_nut.f90]]
- [[recall_salt.f90]]
- [[recall_cs.f90]]
- [[constit_hyd_mult.f90]]
- [[sd_channel_control3.f90]]
- [[flow_dur_curve.f90]]
- [[hydout_output.f90]]
- [[obj_output.f90]]
- [[wallo_allo_output.f90]]
- [[wallo_trn_output.f90]]
- [[wallo_treat_output.f90]]
- [[wallo_use_output.f90]]
- [[manure_source_output.f90]]
- [[manure_demand_output.f90]]
- [[hru_lte_output.f90]]
- [[hru_output.f90]]
- [[hru_carbon_output.f90]]
- [[wetland_output.f90]]
- [[wet_salt_output.f90]]
- [[wet_cs_output.f90]]
- [[hru_pesticide_output.f90]]
- [[hru_pathogen_output.f90]]
- [[hru_salt_output.f90]]
- [[hru_cs_output.f90]]
- [[soil_nutcarb_write.f90]]
- [[soil_carbvar_write.f90]]
- [[soil_nutcarb_write_legacy.f90]]
- [[soil_carbvar_write_legacy.f90]]
- [[aquifer_output.f90]]
- [[aqu_salt_output.f90]]
- [[aqu_cs_output.f90]]
- [[aqu_pesticide_output.f90]]
- [[channel_output.f90]]
- [[sd_chanmorph_output.f90]]
- [[sd_chanbud_output.f90]]
- [[sd_channel_output.f90]]
- [[cha_pesticide_output.f90]]
- [[ch_salt_output.f90]]
- [[ch_cs_output.f90]]
- [[cs_str_output.f90]]
- [[reservoir_output.f90]]
- [[res_pesticide_output.f90]]
- [[res_salt_output.f90]]
- [[res_cs_output.f90]]
- [[ru_output.f90]]
- [[ru_salt_output.f90]]
- [[ru_cs_output.f90]]
- [[recall_output.f90]]
- [[hydin_output.f90]]
- [[basin_ch_pest_output.f90]]
- [[basin_res_pest_output.f90]]
- [[basin_ls_pest_output.f90]]
- [[basin_aqu_pest_output.f90]]
- [[basin_output.f90]]
- [[lsu_output.f90]]
- [[lsu_carbon_output.f90]]
- [[basin_aquifer_output.f90]]
- [[basin_reservoir_output.f90]]
- [[basin_channel_output.f90]]
- [[basin_chanmorph_output.f90]]
- [[basin_chanbud_output.f90]]
- [[basin_sdchannel_output.f90]]
- [[basin_recall_output.f90]]
- [[salt_balance.f90]]
- [[cs_balance.f90]]

**Called by:**

- [[main.f90]]
- [[time_control.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_cc]] - `basin_control_codes`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[channel_module.f90#peakr]] - `real`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs3]] - `constituent_mass`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[constituent_mass_module.f90#obcs_alloc]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_daycount]] - `integer`
- [[gwflow_module.f90#hydsep_flag]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#out_hyd_sep]] - `integer`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#mo]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#ch_in_d]] - `hyd_output`
- [[hydrograph_module.f90#ch_out_d]] - `hyd_output`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#hd]] - `hyd_output`
- [[hydrograph_module.f90#hdsep1]] - `hyd_sep`
- [[hydrograph_module.f90#ht1]] - `hyd_output`
- [[hydrograph_module.f90#hyd_sep_array]] - `real, dimension(:,:),allocatable`
- [[hydrograph_module.f90#hz]] - `hyd_output`
- [[hydrograph_module.f90#icmd]] - `integer`
- [[hydrograph_module.f90#isd_chsur]] - `integer`
- [[hydrograph_module.f90#isdch]] - `integer`
- [[hydrograph_module.f90#jrch]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#rec_d]] - `hyd_output`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[recall_module.f90#recall_db]] - `recall_databases`
- [[reservoir_module.f90#res_ob]] - `reservoir`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`
- [[sd_channel_module.f90#chsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#peakrate]] - `real`
- [[sd_channel_module.f90#sd_ch]] - `swatdeg_channel_dynamic`
- [[time_module.f90#time]] - `time_current`
- [[water_allocation_module.f90#wallo]] - `water_allocation`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

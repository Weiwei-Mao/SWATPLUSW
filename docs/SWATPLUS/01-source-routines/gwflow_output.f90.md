---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_output.f90
note_file: gwflow_output.f90
subroutine: gwflow_output_init
module:
  - gwflow_module
  - hydrograph_module
  - sd_channel_module
  - time_module
  - constituent_mass_module
  - basin_module
calls:
  - gwflow_write_celldef
  - gwflow_write_cell_array
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - constituent_mass_module.f90#cs_db
  - gwflow_module.f90#cell_col
  - gwflow_module.f90#cell_gis_id
  - gwflow_module.f90#cell_id_list
  - gwflow_module.f90#cell_name
  - gwflow_module.f90#cell_row
  - gwflow_module.f90#grid_type
  - gwflow_module.f90#gw_cell_chan_time
  - gwflow_module.f90#gw_cell_tile_time
  - gwflow_module.f90#gw_group_flag
  - gwflow_module.f90#gw_head_sum_aa
  - gwflow_module.f90#gw_heat_flag
  - gwflow_module.f90#gw_heat_grid_aa
  - gwflow_module.f90#gw_heat_grid_yr
  - gwflow_module.f90#gw_heat_ss
  - gwflow_module.f90#gw_heat_ss_yr
  - gwflow_module.f90#gw_hyd_grid_aa
  - gwflow_module.f90#gw_hyd_grid_mo
  - gwflow_module.f90#gw_hyd_grid_yr
  - gwflow_module.f90#gw_hyd_ss
  - gwflow_module.f90#gw_hyd_ss_aa
  - gwflow_module.f90#gw_hyd_ss_mo
  - gwflow_module.f90#gw_hyd_ss_yr
  - gwflow_module.f90#gw_nsolute
  - gwflow_module.f90#gw_num_obs_wells
  - gwflow_module.f90#gw_obs_cells
  - gwflow_module.f90#gw_obs_head
  - gwflow_module.f90#gw_obs_sol_aa
  - gwflow_module.f90#gw_obs_solute
  - gwflow_module.f90#gw_obs_temp
  - gwflow_module.f90#gw_obs_temp_aa
  - gwflow_module.f90#gw_solute_flag
  - gwflow_module.f90#gw_state
  - gwflow_module.f90#gw_time_step
  - gwflow_module.f90#gw_ttime
  - gwflow_module.f90#gw_wb_grp_cells
  - gwflow_module.f90#gw_wb_grp_ncell
  - gwflow_module.f90#gw_wb_grp_num
  - gwflow_module.f90#gwflag_aa
  - gwflow_module.f90#gwflag_day
  - gwflow_module.f90#gwflag_flux
  - gwflow_module.f90#gwflag_heat
  - gwflow_module.f90#gwflag_mon
  - gwflow_module.f90#gwflag_obs
  - gwflow_module.f90#gwflag_pump
  - gwflow_module.f90#gwflag_solute
  - gwflow_module.f90#gwflag_yr
  - gwflow_module.f90#gwheat_state
  - gwflow_module.f90#gwsol_nm
  - gwflow_module.f90#gwsol_ss
  - gwflow_module.f90#gwsol_ss_sum
  - gwflow_module.f90#gwsol_ss_sum_mo
  - gwflow_module.f90#gwsol_state
  - gwflow_module.f90#heat_haft_grid
  - gwflow_module.f90#heat_hbef_grid
  - gwflow_module.f90#ncell
  - gwflow_module.f90#num_active
  - gwflow_module.f90#out_gw
  - gwflow_module.f90#out_gw_celldef
  - gwflow_module.f90#out_gw_transit_chan
  - gwflow_module.f90#out_gw_transit_tile
  - gwflow_module.f90#out_gwbal
  - gwflow_module.f90#out_gwbal_aa
  - gwflow_module.f90#out_gwbal_grp
  - gwflow_module.f90#out_gwbal_mon
  - gwflow_module.f90#out_gwbal_yr
  - gwflow_module.f90#out_gwcell_aa
  - gwflow_module.f90#out_gwcell_day
  - gwflow_module.f90#out_gwcell_mon
  - gwflow_module.f90#out_gwcell_yr
  - gwflow_module.f90#out_gwobs
  - gwflow_module.f90#out_gwobs_aa
  - gwflow_module.f90#out_gwobs_mon
  - gwflow_module.f90#out_gwobs_yr
  - gwflow_module.f90#out_heatbal_aa
  - gwflow_module.f90#out_heatbal_dy
  - gwflow_module.f90#out_heatbal_yr
  - gwflow_module.f90#out_hru_pump_aa
  - gwflow_module.f90#out_hru_pump_day
  - gwflow_module.f90#out_hru_pump_mo
  - gwflow_module.f90#out_hru_pump_yr
  - gwflow_module.f90#out_solbal_aa
  - gwflow_module.f90#out_solbal_dy
  - gwflow_module.f90#out_solbal_mo
  - gwflow_module.f90#out_solbal_yr
  - gwflow_module.f90#sim_month
  - gwflow_module.f90#sol_grid_advn_tt
  - gwflow_module.f90#sol_grid_advn_yr
  - gwflow_module.f90#sol_grid_canl_tt
  - gwflow_module.f90#sol_grid_canl_yr
  - gwflow_module.f90#sol_grid_chng_mo
  - gwflow_module.f90#sol_grid_chng_tt
  - gwflow_module.f90#sol_grid_chng_yr
  - gwflow_module.f90#sol_grid_disp_tt
  - gwflow_module.f90#sol_grid_disp_yr
  - gwflow_module.f90#sol_grid_fpln_tt
  - gwflow_module.f90#sol_grid_fpln_yr
  - gwflow_module.f90#sol_grid_gwsw_mo
  - gwflow_module.f90#sol_grid_gwsw_tt
  - gwflow_module.f90#sol_grid_gwsw_yr
  - gwflow_module.f90#sol_grid_maft
  - gwflow_module.f90#sol_grid_mbef
  - gwflow_module.f90#sol_grid_minl_tt
  - gwflow_module.f90#sol_grid_minl_yr
  - gwflow_module.f90#sol_grid_pond_tt
  - gwflow_module.f90#sol_grid_pond_yr
  - gwflow_module.f90#sol_grid_ppag_tt
  - gwflow_module.f90#sol_grid_ppag_yr
  - gwflow_module.f90#sol_grid_ppex_tt
  - gwflow_module.f90#sol_grid_ppex_yr
  - gwflow_module.f90#sol_grid_rcti_tt
  - gwflow_module.f90#sol_grid_rcti_yr
  - gwflow_module.f90#sol_grid_rcto_tt
  - gwflow_module.f90#sol_grid_rcto_yr
  - gwflow_module.f90#sol_grid_rech_mo
  - gwflow_module.f90#sol_grid_rech_tt
  - gwflow_module.f90#sol_grid_rech_yr
  - gwflow_module.f90#sol_grid_resv_tt
  - gwflow_module.f90#sol_grid_resv_yr
  - gwflow_module.f90#sol_grid_satx_tt
  - gwflow_module.f90#sol_grid_satx_yr
  - gwflow_module.f90#sol_grid_soil_tt
  - gwflow_module.f90#sol_grid_soil_yr
  - gwflow_module.f90#sol_grid_sorb_tt
  - gwflow_module.f90#sol_grid_sorb_yr
  - gwflow_module.f90#sol_grid_swgw_mo
  - gwflow_module.f90#sol_grid_swgw_tt
  - gwflow_module.f90#sol_grid_swgw_yr
  - gwflow_module.f90#sol_grid_tile_tt
  - gwflow_module.f90#sol_grid_tile_yr
  - gwflow_module.f90#sol_grid_wetl_tt
  - gwflow_module.f90#sol_grid_wetl_yr
  - gwflow_module.f90#vaft_grid
  - gwflow_module.f90#vbef_grid
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - time_module.f90#time
input_variables:
  - gwflow_module.f90#gw_wb_grp_ncell
  - gwflow_module.f90#gw_wb_grp_num
reads:
  - gwflow.wbgroups
  - file_name_scalar
  - file_name(n
  - file_name(n
  - file_name(n
  - file_name(n
writes:
  - gwflow_basin_wb_day.txt
  - gwflow_basin_wb_mon.txt
  - gwflow_basin_wb_yr.txt
  - gwflow_basin_wb_aa.txt
  - gwflow_basin_heat_day.txt
  - gwflow_basin_heat_yr.txt
  - gwflow_basin_heat_aa.txt
  - gwflow_cell_wb_day.txt
  - gwflow_cell_wb_mon.txt
  - gwflow_cell_wb_yr.txt
  - gwflow_cell_wb_aa.txt
  - gwflow_cell_definition.txt
purpose: "this subroutine opens all gwflow output files and writes headers; (extracted from gwflow_read)"
---

# gwflow_output_init

> [!info] Summary
> this subroutine opens all gwflow output files and writes headers; (extracted from gwflow_read)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_output.f90`
- **Modules used**:
  - [[gwflow_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
  - [[time_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 6 | **Files written**: 12

## Call Relationships
**This routine calls:**

- `gwflow_write_celldef`
- `gwflow_write_cell_array`

**Called by:**

- [[gwflow_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[gwflow_module.f90#cell_col]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#cell_gis_id]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#cell_id_list]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#cell_name]] - `character(len=16), dimension (:), allocatable`
- [[gwflow_module.f90#cell_row]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#grid_type]] - `character*15`
- [[gwflow_module.f90#gw_cell_chan_time]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_cell_tile_time]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_group_flag]] - `integer`
- [[gwflow_module.f90#gw_head_sum_aa]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_heat_flag]] - `integer`
- [[gwflow_module.f90#gw_heat_grid_aa]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_grid_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_heat_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_grid_aa]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_grid_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_grid_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_aa]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_mo]] - `groundwater_ss`
- [[gwflow_module.f90#gw_hyd_ss_yr]] - `groundwater_ss`
- [[gwflow_module.f90#gw_nsolute]] - `integer`
- [[gwflow_module.f90#gw_num_obs_wells]] - `integer`
- [[gwflow_module.f90#gw_obs_cells]] - `integer, dimension (:), allocatable`
- [[gwflow_module.f90#gw_obs_head]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_obs_sol_aa]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#gw_obs_solute]] - `real, dimension (:,:), allocatable`
- [[gwflow_module.f90#gw_obs_temp]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_obs_temp_aa]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#gw_solute_flag]] - `integer`
- [[gwflow_module.f90#gw_state]] - `groundwater_state`
- [[gwflow_module.f90#gw_time_step]] - `real`
- [[gwflow_module.f90#gw_ttime]] - `integer`
- [[gwflow_module.f90#gw_wb_grp_cells]] - `integer, allocatable`
- [[gwflow_module.f90#gw_wb_grp_ncell]] - `integer, allocatable`
- [[gwflow_module.f90#gw_wb_grp_num]] - `integer`
- [[gwflow_module.f90#gwflag_aa]] - `integer`
- [[gwflow_module.f90#gwflag_day]] - `integer`
- [[gwflow_module.f90#gwflag_flux]] - `integer`
- [[gwflow_module.f90#gwflag_heat]] - `integer`
- [[gwflow_module.f90#gwflag_mon]] - `integer`
- [[gwflow_module.f90#gwflag_obs]] - `integer`
- [[gwflow_module.f90#gwflag_pump]] - `integer`
- [[gwflow_module.f90#gwflag_solute]] - `integer`
- [[gwflow_module.f90#gwflag_yr]] - `integer`
- [[gwflow_module.f90#gwheat_state]] - `groundwater_heat_state`
- [[gwflow_module.f90#gwsol_nm]] - `character (len=16), allocatable`
- [[gwflow_module.f90#gwsol_ss]] - `object_solute_ss`
- [[gwflow_module.f90#gwsol_ss_sum]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_ss_sum_mo]] - `object_solute_ss_sum`
- [[gwflow_module.f90#gwsol_state]] - `object_solute_state`
- [[gwflow_module.f90#heat_haft_grid]] - `real*8`
- [[gwflow_module.f90#heat_hbef_grid]] - `real*8`
- [[gwflow_module.f90#ncell]] - `integer`
- [[gwflow_module.f90#num_active]] - `integer`
- [[gwflow_module.f90#out_gw]] - `integer`
- [[gwflow_module.f90#out_gw_celldef]] - `integer`
- [[gwflow_module.f90#out_gw_transit_chan]] - `integer`
- [[gwflow_module.f90#out_gw_transit_tile]] - `integer`
- [[gwflow_module.f90#out_gwbal]] - `integer`
- [[gwflow_module.f90#out_gwbal_aa]] - `integer`
- [[gwflow_module.f90#out_gwbal_grp]] - `integer`
- [[gwflow_module.f90#out_gwbal_mon]] - `integer`
- [[gwflow_module.f90#out_gwbal_yr]] - `integer`
- [[gwflow_module.f90#out_gwcell_aa]] - `integer`
- [[gwflow_module.f90#out_gwcell_day]] - `integer`
- [[gwflow_module.f90#out_gwcell_mon]] - `integer`
- [[gwflow_module.f90#out_gwcell_yr]] - `integer`
- [[gwflow_module.f90#out_gwobs]] - `integer`
- [[gwflow_module.f90#out_gwobs_aa]] - `integer`
- [[gwflow_module.f90#out_gwobs_mon]] - `integer`
- [[gwflow_module.f90#out_gwobs_yr]] - `integer`
- [[gwflow_module.f90#out_heatbal_aa]] - `integer`
- [[gwflow_module.f90#out_heatbal_dy]] - `integer`
- [[gwflow_module.f90#out_heatbal_yr]] - `integer`
- [[gwflow_module.f90#out_hru_pump_aa]] - `integer`
- [[gwflow_module.f90#out_hru_pump_day]] - `integer`
- [[gwflow_module.f90#out_hru_pump_mo]] - `integer`
- [[gwflow_module.f90#out_hru_pump_yr]] - `integer`
- [[gwflow_module.f90#out_solbal_aa]] - `integer`
- [[gwflow_module.f90#out_solbal_dy]] - `integer`
- [[gwflow_module.f90#out_solbal_mo]] - `integer`
- [[gwflow_module.f90#out_solbal_yr]] - `integer`
- [[gwflow_module.f90#sim_month]] - `integer`
- [[gwflow_module.f90#sol_grid_advn_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_advn_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_canl_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_canl_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_chng_mo]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_chng_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_chng_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_disp_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_disp_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_fpln_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_fpln_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_gwsw_mo]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_gwsw_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_gwsw_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_maft]] - `real`
- [[gwflow_module.f90#sol_grid_mbef]] - `real`
- [[gwflow_module.f90#sol_grid_minl_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_minl_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_pond_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_pond_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_ppag_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_ppag_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_ppex_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_ppex_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rcti_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rcti_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rcto_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rcto_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rech_mo]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rech_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_rech_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_resv_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_resv_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_satx_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_satx_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_soil_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_soil_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_sorb_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_sorb_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_swgw_mo]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_swgw_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_swgw_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_tile_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_tile_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_wetl_tt]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#sol_grid_wetl_yr]] - `real, dimension (:), allocatable`
- [[gwflow_module.f90#vaft_grid]] - `real*8`
- [[gwflow_module.f90#vbef_grid]] - `real*8`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[gwflow_module.f90#gw_wb_grp_ncell]]
- [[gwflow_module.f90#gw_wb_grp_num]]

## File I/O
- **Writes**:
  - [[gwflow_basin_wb_day.txt]]
  - [[gwflow_basin_wb_mon.txt]]
  - [[gwflow_basin_wb_yr.txt]]
  - [[gwflow_basin_wb_aa.txt]]
  - [[gwflow_basin_heat_day.txt]]
  - [[gwflow_basin_heat_yr.txt]]
  - [[gwflow_basin_heat_aa.txt]]
  - [[gwflow_cell_wb_day.txt]]
  - [[gwflow_cell_wb_mon.txt]]
  - [[gwflow_cell_wb_yr.txt]]
  - [[gwflow_cell_wb_aa.txt]]
  - [[gwflow_cell_definition.txt]]
- **Reads**:
  - [[gwflow.wbgroups]]
  - `file_name_scalar` _(variable; see [[file.cio]])_
  - `file_name(n` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

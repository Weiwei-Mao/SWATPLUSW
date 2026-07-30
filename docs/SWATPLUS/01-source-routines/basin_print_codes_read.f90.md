---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_print_codes_read.f90
note_file: basin_print_codes_read.f90
subroutine: basin_print_codes_read
module:
  - input_file_module
  - basin_module
  - time_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - input_file_module.f90#in_sim
  - time_module.f90#time
input_variables:
  - basin_module.f90#pco
reads:
  - in_sim%prt
writes: []
purpose: ""
---

# basin_print_codes_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_print_codes_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[basin_module.f90#pco]]

## File I/O
- **Reads**:
  - [[print.prt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation.

- Line 17-783, Read input file [[print.prt]], from variable *[[input_file_module.f90#in_sim]]* to get the file name
	- File line 3, 6 parameters
		- nyskip, number of year at the beginning of the simulation to not print output
		- day_start: Julian day to start printing output, for daily only
		- yrc_start, calendar year to start printing output
		- day_end, Julian day to stop printing output, for daily only
		- yrc_end, calendar year to stop printing output
		- interval, print interval within the period
	- For line 5
		- aa_int_cnt, Number of print intervals for average annual output
	- For line 7
		- csvout, csv format
		- dbout, DB format
		- cdfout, NetCDF format
	- For line 9
		- crop_yld, yearly and average annual crop yield
		- mgtout, management output
		- hydcon, hydrograph connection output
		- fdcout, flow duration curve output
	- Then the output-control rows are read as `name daily monthly yearly avann`
		- `y` prints that time scale, `n` suppresses it. Some legacy carbon rows also use `l` for extra legacy diagnostics.
		- If `use_obj_labels = n`, SWAT+ ignores the text label and reads rows in fixed order. If `use_obj_labels` is not `n`, the label must match one of the table rows.
		- The table lists the `.txt` outputs. If `csvout = y`, SWAT+ also writes matching `.csv` files for the active outputs.

		| Group | `print.prt` row | Meaning | Main output files |
		|---|---|---|---|
		| Basin | `basin_wb` | Basin water balance. | - `basin_wb_day.txt`<br>- `basin_wb_mon.txt`<br>- `basin_wb_yr.txt`<br>- `basin_wb_aa.txt` |
		| Basin | `basin_nb` | Basin nutrient balance. | - `basin_nb_day.txt`<br>- `basin_nb_mon.txt`<br>- `basin_nb_yr.txt`<br>- `basin_nb_aa.txt` |
		| Basin | `basin_ls` | Basin losses. | - `basin_ls_day.txt`<br>- `basin_ls_mon.txt`<br>- `basin_ls_yr.txt`<br>- `basin_ls_aa.txt` |
		| Basin | `basin_pw` | Basin plant/weather summary. | - `basin_pw_day.txt`<br>- `basin_pw_mon.txt`<br>- `basin_pw_yr.txt`<br>- `basin_pw_aa.txt` |
		| Basin | `basin_aqu` | Basin aquifer summary. | - `basin_aqu_day.txt`<br>- `basin_aqu_mon.txt`<br>- `basin_aqu_yr.txt`<br>- `basin_aqu_aa.txt` |
		| Basin | `basin_res` | Basin reservoir/wetland summary. | - `basin_res_day.txt`<br>- `basin_res_mon.txt`<br>- `basin_res_yr.txt`<br>- `basin_res_aa.txt` |
		| Basin | `basin_cha` | Basin channel summary. | - `basin_cha_day.txt`<br>- `basin_cha_mon.txt`<br>- `basin_cha_yr.txt`<br>- `basin_cha_aa.txt` |
		| Basin | `basin_sd_cha` | Basin channel sediment and morphology summary. | - `basin_sd_cha_day.txt`<br>- `basin_sd_cha_mon.txt`<br>- `basin_sd_cha_yr.txt`<br>- `basin_sd_cha_aa.txt`<br>- `basin_sd_chamorph_day.txt`<br>- `basin_sd_chamorph_mon.txt`<br>- `basin_sd_chamorph_yr.txt`<br>- `basin_sd_chamorph_aa.txt`<br>- `basin_sd_chanbud_day.txt`<br>- `basin_sd_chanbud_mon.txt`<br>- `basin_sd_chanbud_yr.txt`<br>- `basin_sd_chanbud_aa.txt` |
		| Basin | `basin_psc` | Basin point-source summary; internally stored in `pco%recall_bsn`. | - `basin_psc_day.txt`<br>- `basin_psc_mon.txt`<br>- `basin_psc_yr.txt`<br>- `basin_psc_aa.txt` |
		| Region | `region_wb` | Region water balance flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_nb` | Region nutrient balance flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_ls` | Region losses flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_pw` | Region plant/weather flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_aqu` | Region aquifer flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_res` | Region reservoir flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_sd_cha` | Region channel sediment/morphology flag. | - Reader flag exists, but active region output calls are commented out in the current source. |
		| Region | `region_psc` | Region point-source flag; internally stored in `pco%recall_reg`. | - Reader flag exists, but active region recall output is commented out in the current source. |
		| Water allocation | `water_allo` | Water allocation output. | - `water_allo_day.txt`<br>- `water_allo_mon.txt`<br>- `water_allo_yr.txt`<br>- `water_allo_aa.txt` |
		| LSU | `lsunit_wb` | Landscape unit water balance. | - `lsunit_wb_day.txt`<br>- `lsunit_wb_mon.txt`<br>- `lsunit_wb_yr.txt`<br>- `lsunit_wb_aa.txt` |
		| LSU | `lsunit_nb` | Landscape unit nutrient balance. | - `lsunit_nb_day.txt`<br>- `lsunit_nb_mon.txt`<br>- `lsunit_nb_yr.txt`<br>- `lsunit_nb_aa.txt` |
		| LSU | `lsunit_ls` | Landscape unit losses. | - `lsunit_ls_day.txt`<br>- `lsunit_ls_mon.txt`<br>- `lsunit_ls_yr.txt`<br>- `lsunit_ls_aa.txt` |
		| LSU | `lsunit_pw` | Landscape unit plant/weather summary. | - `lsunit_pw_day.txt`<br>- `lsunit_pw_mon.txt`<br>- `lsunit_pw_yr.txt`<br>- `lsunit_pw_aa.txt` |
		| LSU carbon | `lsu_cb_gl` | LSU carbon gain/loss summary. | - `lsu_carb_gl_day.txt`<br>- `lsu_carb_gl_mon.txt`<br>- `lsu_carb_gl_yr.txt`<br>- `lsu_carb_gl_aa.txt` |
		| LSU carbon | `lsu_cb_trf` | LSU soil carbon transformation summary. | - `lsu_scf_day.txt`<br>- `lsu_scf_mon.txt`<br>- `lsu_scf_yr.txt`<br>- `lsu_scf_aa.txt` |
		| LSU carbon | `lsu_cb_plt` | LSU plant carbon state. | - `lsu_plc_stat_day.txt`<br>- `lsu_plc_stat_mon.txt`<br>- `lsu_plc_stat_yr.txt`<br>- `lsu_plc_stat_aa.txt` |
		| HRU | `hru_wb` | HRU water balance. | - `hru_wb_day.txt`<br>- `hru_wb_mon.txt`<br>- `hru_wb_yr.txt`<br>- `hru_wb_aa.txt` |
		| HRU | `hru_nb` | HRU nutrient balance. | - `hru_nb_day.txt`<br>- `hru_nb_mon.txt`<br>- `hru_nb_yr.txt`<br>- `hru_nb_aa.txt`<br>- `hru_ncycle_day.txt`<br>- `hru_ncycle_mon.txt`<br>- `hru_ncycle_yr.txt`<br>- `hru_ncycle_aa.txt` |
		| HRU | `hru_ls` | HRU losses. | - `hru_ls_day.txt`<br>- `hru_ls_mon.txt`<br>- `hru_ls_yr.txt`<br>- `hru_ls_aa.txt` |
		| HRU | `hru_pw` | HRU plant/weather summary. | - `hru_pw_day.txt`<br>- `hru_pw_mon.txt`<br>- `hru_pw_yr.txt`<br>- `hru_pw_aa.txt` |
		| HRU carbon | `hru_cb` | Legacy HRU carbon output switch. | - `hru_cbn_lyr.txt`<br>- `hru_seq_lyr.txt`<br>- `hru_n_p_pool_stat.txt`<br>- `basin_carbon_all.txt`<br>- With `l`: `hru_begsim_soil_prop.txt`<br>- With `l`: `hru_endsim_soil_prop.txt`<br>- With `l` and `cswat == 2`: `hru_plc_stat.txt`<br>- With `l` and `cswat == 2`: `hru_cflux_stat.txt`<br>- With `l` and `cswat == 2`: `hru_cpool_stat.txt` |
		| HRU carbon | `hru_cb_vars` | Legacy HRU carbon variable diagnostics; requires `cswat == 2`. | - `hru_carbvars.txt`<br>- `hru_org_allo_vars.txt`<br>- `hru_org_ratio_vars.txt`<br>- `hru_org_trans_vars.txt` |
		| HRU carbon | `hru_cb_gl` | New HRU carbon gain/loss summary. | - `hru_carb_gl_day.txt`<br>- `hru_carb_gl_mon.txt`<br>- `hru_carb_gl_yr.txt`<br>- `hru_carb_gl_aa.txt` |
		| HRU carbon | `hru_cb_trf` | New HRU soil carbon transformation summary. | - `hru_scf_day.txt`<br>- `hru_scf_mon.txt`<br>- `hru_scf_yr.txt`<br>- `hru_scf_aa.txt` |
		| HRU carbon | `hru_cb_lyr` | New per-layer total soil carbon and sequestered carbon; written by `soil_nutcarb_write`. | - `hru_cbn_lyr_day.txt`<br>- `hru_cbn_lyr_mon.txt`<br>- `hru_cbn_lyr_yr.txt`<br>- `hru_cbn_lyr_aa.txt` |
		| HRU carbon | `hru_cb_cpool` | New per-layer carbon pools; requires `cswat == 2`; written by `soil_nutcarb_write`. | - `hru_cpool_stat_day.txt`<br>- `hru_cpool_stat_mon.txt`<br>- `hru_cpool_stat_yr.txt`<br>- `hru_cpool_stat_aa.txt` |
		| HRU carbon | `hru_cb_npool` | New per-layer organic N/P pools; not mineral `NO3`/`NH4`; written by `soil_nutcarb_write`. | - `hru_n_p_pool_stat_day.txt`<br>- `hru_n_p_pool_stat_mon.txt`<br>- `hru_n_p_pool_stat_yr.txt`<br>- `hru_n_p_pool_stat_aa.txt` |
		| HRU carbon | `hru_cb_plt` | New HRU plant carbon state; written by `soil_nutcarb_write`. | - `hru_plc_stat_day.txt`<br>- `hru_plc_stat_mon.txt`<br>- `hru_plc_stat_yr.txt`<br>- `hru_plc_stat_aa.txt` |
		| HRU carbon | `hru_cb_flux` | New per-layer C and N transformation flux diagnostics; requires `cswat == 2`; written by `soil_nutcarb_write`. | - `hru_cflux_stat_day.txt`<br>- `hru_cflux_stat_mon.txt`<br>- `hru_cflux_stat_yr.txt`<br>- `hru_cflux_stat_aa.txt` |
		| HRU carbon | `hru_cb_drv` | New per-layer carbon driver diagnostics; requires `cswat == 2`; includes diagnostic `no3` and `nh4`; written by `soil_carbvar_write`. | - `hru_carb_drv_day.txt`<br>- `hru_carb_drv_mon.txt`<br>- `hru_carb_drv_yr.txt`<br>- `hru_carb_drv_aa.txt` |
		| HRU carbon | `hru_cb_dyn` | New per-layer carbon dynamic variables; requires `cswat == 2`; written by `soil_carbvar_write`. | - `hru_carb_dyn_day.txt`<br>- `hru_carb_dyn_mon.txt`<br>- `hru_carb_dyn_yr.txt`<br>- `hru_carb_dyn_aa.txt` |
		| HRU carbon | `hru_cb_snap` | New per-layer soil property snapshot. | - `hru_soil_snap_day.txt`<br>- `hru_soil_snap_mon.txt`<br>- `hru_soil_snap_yr.txt`<br>- `hru_soil_snap_tot.txt` |
		| HRU-LTE | `hru-lte_wb` | HRU-LTE water balance. | - `hru-lte_wb_day.txt`<br>- `hru-lte_wb_mon.txt`<br>- `hru-lte_wb_yr.txt`<br>- `hru-lte_wb_aa.txt` |
		| HRU-LTE | `hru-lte_nb` | HRU-LTE nutrient balance flag. | - Reader flag exists, but active standard output files are not opened in the current source. |
		| HRU-LTE | `hru-lte_ls` | HRU-LTE losses. | - `hru-lte_ls_day.txt`<br>- `hru-lte_ls_mon.txt`<br>- `hru-lte_ls_yr.txt`<br>- `hru-lte_ls_aa.txt` |
		| HRU-LTE | `hru-lte_pw` | HRU-LTE plant/weather summary. | - `hru-lte_pw_day.txt`<br>- `hru-lte_pw_mon.txt`<br>- `hru-lte_pw_yr.txt`<br>- `hru-lte_pw_aa.txt` |
		| Channel | `channel` | Channel hydrology/water-quality output. | - `channel_day.txt`<br>- `channel_mon.txt`<br>- `channel_yr.txt`<br>- `channel_aa.txt` |
		| Channel | `channel_sd` | Channel sediment and morphology output. | - `channel_sd_day.txt`<br>- `channel_sd_mon.txt`<br>- `channel_sd_yr.txt`<br>- `channel_sd_aa.txt`<br>- `channel_sdmorph_day.txt`<br>- `channel_sdmorph_mon.txt`<br>- `channel_sdmorph_yr.txt`<br>- `channel_sdmorph_aa.txt` |
		| Aquifer | `aquifer` | Aquifer output. | - `aquifer_day.txt`<br>- `aquifer_mon.txt`<br>- `aquifer_yr.txt`<br>- `aquifer_aa.txt` |
		| Reservoir | `reservoir` | Reservoir and wetland output; both use `pco%res`. | - `reservoir_day.txt`<br>- `reservoir_mon.txt`<br>- `reservoir_yr.txt`<br>- `reservoir_aa.txt`<br>- `wetland_day.txt`<br>- `wetland_mon.txt`<br>- `wetland_yr.txt`<br>- `wetland_aa.txt` |
		| Recall | `recall` | Recall object output. | - `recall_day.txt`<br>- `recall_mon.txt`<br>- `recall_yr.txt`<br>- `recall_aa.txt` |
		| HYD | `hyd` | Hydrology routing input/output hydrographs and hydrograph deposition. | - `hydin_day.txt`<br>- `hydin_mon.txt`<br>- `hydin_yr.txt`<br>- `hydin_aa.txt`<br>- `hydout_day.txt`<br>- `hydout_mon.txt`<br>- `hydout_yr.txt`<br>- `hydout_aa.txt`<br>- `deposition_day.txt`<br>- `deposition_mon.txt`<br>- `deposition_yr.txt`<br>- `deposition_aa.txt` |
		| RU | `ru` | Routing unit output. | - `ru_day.txt`<br>- `ru_mon.txt`<br>- `ru_yr.txt`<br>- `ru_aa.txt` |
		| PEST | `pest` | Pesticide output families. | - `hru_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `channel_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `reservoir_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `aquifer_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `basin_aqu_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `basin_ch_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `basin_res_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `basin_ls_pest_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt` |
		| Salt | `basin_salt` | Basin salt output. | - `basin_salt_day.txt`<br>- `basin_salt_mon.txt`<br>- `basin_salt_yr.txt`<br>- `basin_salt_aa.txt` |
		| Salt | `hru_salt` | HRU salt output. | - `hru_salt_day.txt`<br>- `hru_salt_mon.txt`<br>- `hru_salt_yr.txt`<br>- `hru_salt_aa.txt` |
		| Salt | `ru_salt` | Routing unit salt output. | - `rout_unit_salt_day.txt`<br>- `rout_unit_salt_mon.txt`<br>- `rout_unit_salt_yr.txt`<br>- `rout_unit_salt_aa.txt` |
		| Salt | `aqu_salt` | Aquifer salt output. | - `aquifer_salt_day.txt`<br>- `aquifer_salt_mon.txt`<br>- `aquifer_salt_yr.txt`<br>- `aquifer_salt_aa.txt` |
		| Salt | `channel_salt` | Channel salt output. | - `channel_salt_day.txt`<br>- `channel_salt_mon.txt`<br>- `channel_salt_yr.txt`<br>- `channel_salt_aa.txt` |
		| Salt | `res_salt` | Reservoir salt output. | - `reservoir_salt_day.txt`<br>- `reservoir_salt_mon.txt`<br>- `reservoir_salt_yr.txt`<br>- `reservoir_salt_aa.txt` |
		| Salt | `wetland_salt` | Wetland salt output. | - `wetland_salt_day.txt`<br>- `wetland_salt_mon.txt`<br>- `wetland_salt_yr.txt`<br>- `wetland_salt_aa.txt` |
		| CS | `basin_cs` | Basin constituent/salt module output. | - `basin_cs_day.txt`<br>- `basin_cs_mon.txt`<br>- `basin_cs_yr.txt`<br>- `basin_cs_aa.txt` |
		| CS | `hru_cs` | HRU constituent/salt module output. | - `hru_cs_day.txt`<br>- `hru_cs_mon.txt`<br>- `hru_cs_yr.txt`<br>- `hru_cs_aa.txt` |
		| CS | `ru_cs` | Routing unit constituent/salt module output. | - `rout_unit_cs_day.txt`<br>- `rout_unit_cs_mon.txt`<br>- `rout_unit_cs_yr.txt`<br>- `rout_unit_cs_aa.txt` |
		| CS | `aqu_cs` | Aquifer constituent/salt module output. | - `aquifer_cs_day.txt`<br>- `aquifer_cs_mon.txt`<br>- `aquifer_cs_yr.txt`<br>- `aquifer_cs_aa.txt` |
		| CS | `channel_cs` | Channel constituent/salt module output. | - `channel_cs_day.txt`<br>- `channel_cs_mon.txt`<br>- `channel_cs_yr.txt`<br>- `channel_cs_aa.txt` |
		| CS | `res_cs` | Reservoir constituent/salt module output. | - `reservoir_cs_day.txt`<br>- `reservoir_cs_mon.txt`<br>- `reservoir_cs_yr.txt`<br>- `reservoir_cs_aa.txt` |
		| CS | `wetland_cs` | Wetland constituent/salt module output. | - `wetland_cs_day.txt`<br>- `wetland_cs_mon.txt`<br>- `wetland_cs_yr.txt`<br>- `wetland_cs_aa.txt` |
		| Gwflow | `gwflow_wb` | Groundwater flow basin and cell water balance. | - `gwflow_basin_wb_day.txt`<br>- `gwflow_basin_wb_mon.txt`<br>- `gwflow_basin_wb_yr.txt`<br>- `gwflow_basin_wb_aa.txt`<br>- `gwflow_cell_wb_day.txt`<br>- `gwflow_cell_wb_mon.txt`<br>- `gwflow_cell_wb_yr.txt`<br>- `gwflow_cell_wb_aa.txt` |
		| Gwflow | `gwflow_flux` | Groundwater exchange-flux diagnostics. | - `gwflow_tile_group_day.txt`<br>- `gwflow_canal_wb_day.txt`<br>- `gwflow_canal_sol_day.txt`<br>- `gwflow_pond_wb_day.txt`<br>- `gwflow_pond_sol_day.txt`<br>- `gwflow_pond_mass_day.txt`<br>- `gwflow_pond_conc_day.txt`<br>- `gwflow_gwsw_group_day.txt` |
		| Gwflow | `gwflow_heat` | Groundwater basin heat output. | - `gwflow_basin_heat_day.txt`<br>- `gwflow_basin_heat_yr.txt`<br>- `gwflow_basin_heat_aa.txt` |
		| Gwflow | `gwflow_solute` | Groundwater basin solute output. | - `gwflow_basin_sol_no3_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- `gwflow_basin_sol_p_day.txt` / `_mon.txt` / `_yr.txt` / `_aa.txt`<br>- Optional salt/constituent solutes: `gwflow_basin_sol_<solute>_<time>.txt` |
		| Gwflow | `gwflow_obs` | Groundwater observation output. | - `gwflow_obs_day.txt`<br>- `gwflow_obs_mon.txt`<br>- `gwflow_obs_yr.txt`<br>- `gwflow_obs_aa.txt`<br>- `gwflow_chan_obs_flow_day.txt`<br>- `gwflow_chan_obs_no3_day.txt` |
		| Gwflow | `gwflow_pump` | Groundwater HRU pumping output. | - `gwflow_hru_pump_day.txt`<br>- `gwflow_hru_pump_mon.txt`<br>- `gwflow_hru_pump_yr.txt`<br>- `gwflow_hru_pump_aa.txt`<br>- `gwflow_cell_wb_ppag_obs_day.txt` |
- Line 785-790, reset input data of line 3
	- if <= 0, set to default time or date from [[time_module.f90#time]]
- End
<!-- USER-NOTES-END -->

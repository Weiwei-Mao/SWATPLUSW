---
type: module
tags:
  - swat/module
  - swat/to-read
file: gwflow_module.f90
note_file: gwflow_module.f90
module_name: gwflow_module
defines_types:
  - groundwater_state
  - groundwater_transit
  - groundwater_ss
  - cell_channel_info
  - satx_channel_info
  - cell_connections
  - tile_channel_info
  - cell_reservoir_info
  - cell_floodplain_info
  - canal_chan_info
  - cell_canal_info
  - cell_canal_out_info
  - cell_canal_div_info
  - canal_info
  - cell_pond_info
  - groundwater_heat_state
  - solute_state
  - object_solute_state
  - minl_state
  - solute_chem
  - solute_ss
  - object_solute_ss
  - solute_ss_sum
  - object_solute_ss_sum
defines_vars:
  - ncell
  - num_active
  - gw_time_step
  - gwflag_day
  - gwflag_mon
  - gwflag_yr
  - gwflag_aa
  - gwflag_obs
  - gwflag_pump
  - gwflag_heat
  - gwflag_solute
  - gwflag_flux
  - bc_type
  - conn_type
  - gw_daycount
  - gwflow_area
  - bc_type_array
  - grid_type
  - grid_nrow
  - grid_ncol
  - cell_id_usg
  - cell_id_list
  - grid_status
  - grid_int
  - grid_val
  - cell_row
  - cell_col
  - cell_gis_id
  - cell_name
  - out_gw_celldef
  - gw_state
  - gw_ttime
  - gw_transit_num
  - gw_transit_cells
  - gw_cell_chan_flag
  - gw_cell_chan_time
  - gw_cell_tile_time
  - gw_transit
  - hru_cells_link
  - hru_num_cells
  - hru_cells
  - hru_cells_fract
  - cells_fract
  - hrus_connected
  - lsu_cells_link
  - in_lsu_cell
  - lsu_num_cells
  - lsu_cells
  - lsu_cells_fract
  - lsus_connected
  - gw_hyd_ss
  - gw_hyd_ss_mo
  - gw_hyd_ss_yr
  - gw_hyd_ss_aa
  - gw_head_sum_aa
  - gw_hyd_grid_mo
  - gw_hyd_grid_yr
  - gw_hyd_grid_aa
  - vbef_grid
  - vaft_grid
  - heat_hbef_grid
  - heat_haft_grid
  - sol_grid_mbef
  - sol_grid_maft
  - sim_month
  - gw_heat_ss
  - gw_heat_ss_mo
  - gw_heat_ss_yr
  - gw_heat_grid_mo
  - gw_heat_grid_yr
  - gw_heat_grid_aa
  - gw_bound_near
  - gw_bound_dist
  - gwflow_perc
  - gw_delay
  - gw_rech
  - delay
  - gw_et_flag
  - etremain
  - num_chancells
  - gw_chan_id
  - gw_chan_cell
  - gw_chan_chan
  - gw_chan_zone
  - gw_chan_ncell
  - gw_chan_len
  - gw_chan_elev
  - gw_chan_K
  - gw_chan_thick
  - gw_bed_change
  - gw_chan_dpzn
  - gw_chan_obs
  - gw_chan_dep_flag
  - gw_chan_ndpzn
  - gw_chan_dep
  - gw_canl_out_info
  - gw_canal_ncells_out
  - canal_out_info
  - canal_out_conc
  - div_conc_salt
  - div_conc_cs
  - gw_canl_div_cell
  - gw_canal_ncells_div
  - gw_canl_div_info
  - gw_pond_flag
  - gw_pond_div_flag
  - gw_npond
  - in_ponds
  - gw_pond_info
  - gw_phyt_flag
  - gw_phyt_ncells
  - gw_phyt_npts
  - gw_phyt_ids
  - gw_phyt_area
  - gw_phyt_dep
  - gw_phyt_rate
  - gw_tvh_flag
  - gw_ntvh
  - gw_tvh_ids
  - gw_tvh_vals
  - gw_group_flag
  - gw_wb_grp_num
  - gw_wb_grp_ncell
  - gw_wb_grp_cells
  - cell_channel
  - gw_num_output
  - gw_output_index
  - gw_output_yr
  - gw_output_day
  - gw_num_obs_wells
  - gw_obs_cells
  - gw_obs_head
  - gw_cell_obs_ss
  - gw_cell_obs_ss_vals
  - chan_hyd_sep
  - hydsep_flag
  - gw_heat_flag
  - gw_rho
  - gw_cp
  - gw_rechheat
  - gw_obs_temp
  - gw_obs_temp_aa
  - gw_obs_sol_aa
  - heat_cell
  - gwheat_state
  - gw_solute_flag
  - gw_nsolute
  - num_ts_transport
  - gw_long_disp
  - gwsol_salt
  - gwsol_cons
  - gwsol_minl
  - gw_nminl
  - gwsol_nm
  - gwsol_rctn
  - gwsol_sorb
  - gwsol_state
  - mass_min
  - gwsol_minl_state
  - cell_int
  - mass_rct
  - gwsol_chem
  - gwsol_ss
  - gwsol_ss_sum
  - gwsol_ss_sum_mo
  - gwflow_percsol
  - gw_rechsol
  - sol_grid_chng_mo
  - sol_grid_rech_mo
  - sol_grid_gwsw_mo
  - sol_grid_swgw_mo
  - sol_grid_chng_yr
  - sol_grid_rech_yr
  - sol_grid_gwsw_yr
  - sol_grid_swgw_yr
  - sol_grid_satx_yr
  - sol_grid_advn_yr
  - sol_grid_disp_yr
  - sol_grid_rcti_yr
  - sol_grid_rcto_yr
  - sol_grid_minl_yr
  - sol_grid_sorb_yr
  - sol_grid_ppag_yr
  - sol_grid_ppex_yr
  - sol_grid_tile_yr
  - sol_grid_soil_yr
  - sol_grid_resv_yr
  - sol_grid_wetl_yr
  - sol_grid_canl_yr
  - sol_grid_fpln_yr
  - sol_grid_pond_yr
  - sol_grid_chng_tt
  - sol_grid_rech_tt
  - sol_grid_gwsw_tt
  - sol_grid_swgw_tt
  - sol_grid_satx_tt
  - sol_grid_advn_tt
  - sol_grid_disp_tt
  - sol_grid_rcti_tt
  - sol_grid_rcto_tt
  - sol_grid_minl_tt
  - sol_grid_sorb_tt
  - sol_grid_ppag_tt
  - sol_grid_ppex_tt
  - sol_grid_tile_tt
  - sol_grid_soil_tt
  - sol_grid_resv_tt
  - sol_grid_wetl_tt
  - sol_grid_canl_tt
  - sol_grid_fpln_tt
  - sol_grid_pond_tt
  - gw_obs_solute
  - out_gw
  - in_wet_cell
  - out_gwobs
  - out_gwobs_mon
  - out_gwobs_yr
  - out_gwobs_aa
  - out_gwconnect
  - out_gwheads
  - out_gwbal
  - out_gwsw_chan
  - out_gw_chan
  - out_gw_rech
  - out_gw_et
  - out_gw_grid
  - out_gw_satex
  - out_gwsw
  - out_lateral
  - out_gw_etact
  - out_gw_tile
  - out_gwbal_mon
  - out_gwbal_yr
  - out_gwbal_aa
  - out_gwbal_grp
  - out_hyd_sep
  - out_tile_cells
  - out_gwconc
  - out_gwtile_hru
  - out_gwobs_ss
  - out_gw_soil
  - out_gw_res
  - out_gw_wet
  - out_gw_pumpag
  - out_gw_pumpex
  - out_gw_pumpdef
  - out_gw_canal
  - out_gw_fp
  - out_gw_chem
  - out_gw_gwet
  - out_gw_gwsw
  - out_gw_satx
  - out_gw_ppag
  - out_gw_ppex
  - out_gw_resv
  - out_gw_wetl
  - out_gw_fpln
  - out_gw_canl
  - out_gw_pond
  - out_gw_phyt
  - out_canal_bal
  - out_canal_sol
  - out_pond_bal
  - out_pond_sol
  - out_pond_mass
  - out_pond_conc
  - out_gwtemps
  - out_gw_transit
  - out_gw_transit_chan
  - out_gw_transit_tile
  - out_gwsw_groups
  - out_gwsw_chanobs_flow
  - out_gwsw_chanobs_no3
  - out_hru_pump_day
  - out_hru_pump_mo
  - out_hru_pump_yr
  - out_hru_pump_aa
  - out_hru_pump_obs
  - out_head_mo
  - out_head_yr
  - out_conc_mo
  - out_conc_yr
  - out_sol_rech
  - out_sol_gwsw
  - out_sol_soil
  - out_sol_satx
  - out_sol_ppag
  - out_sol_ppex
  - out_sol_tile
  - out_sol_resv
  - out_sol_fpln
  - out_sol_canl
  - out_sol_wetl
  - out_sol_rcti
  - out_sol_rcto
  - out_sol_minl
  - out_sol_sorb
  - out_sol_pond
  - out_sol_rech_mo
  - out_sol_gwsw_mo
  - out_sol_soil_mo
  - out_sol_satx_mo
  - out_sol_ppag_mo
  - out_sol_ppex_mo
  - out_sol_tile_mo
  - out_sol_resv_mo
  - out_sol_fpln_mo
  - out_sol_canl_mo
  - out_sol_wetl_mo
  - out_sol_rcti_mo
  - out_sol_rcto_mo
  - out_sol_minl_mo
  - out_sol_sorb_mo
  - out_sol_pond_mo
  - out_solbal_dy
  - out_solbal_mo
  - out_solbal_yr
  - out_solbal_aa
  - out_gwobs_sol
  - out_gw_rech_mo
  - out_gw_gwet_mo
  - out_gw_gwsw_mo
  - out_gw_soil_mo
  - out_gw_satx_mo
  - out_gw_ppag_mo
  - out_gw_ppex_mo
  - out_gw_tile_mo
  - out_gw_resv_mo
  - out_gw_wetl_mo
  - out_gw_fpln_mo
  - out_gw_canl_mo
  - out_gw_pond_mo
  - out_gw_phyt_mo
  - out_heatbal_dy
  - out_heatbal_yr
  - out_heatbal_aa
  - out_temp_mo
  - out_temp_yr
  - out_gwobs_temp
  - out_heat_rech
  - out_heat_gwet
  - out_heat_gwsw
  - out_heat_satx
  - out_heat_soil
  - out_heat_tile
  - out_heat_ppag
  - out_heat_ppex
  - out_heat_resv
  - out_heat_wetl
  - out_heat_fpln
  - out_heat_canl
  - out_heat_pond
  - out_gwcell_day
  - out_gwcell_mon
  - out_gwcell_yr
  - out_gwcell_aa
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# gwflow_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### groundwater_state

- **Defined in source**: `gwflow_module.f90:40`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `elev` | `real` | 41 | m \|ground surface elevation |
| `thck` | `real` | 42 | m \|aquifer thickness |
| `botm` | `real` | 43 | m \|bottom (bedrock) elevation |
| `xcrd` | `real` | 44 | m \|x coordinate of cell centroid |
| `ycrd` | `real` | 45 | m \|y coordinate of cell centroid |
| `area` | `real` | 46 | m2 \|surface area |
| `init` | `real` | 47 | m \|initial groundwater head (beginning of simulation) |
| `head` | `real` | 48 | m \|current simulated groundwater head |
| `hydc` | `real` | 49 | m/day \|aquifer hydraulic conductivity |
| `spyd` | `real` | 50 | m3/m3 \|aquifer specific yield |
| `exdp` | `real` | 51 | m \|groundwater ET extinction depth |
| `stat` | `integer` | 52 | \|status (0=inactive; 1=active; 2=boundary) |
| `zone` | `integer` | 53 | \|aquifer zone |
| `ncon` | `integer` | 54 | \|number of connected cells |
| `tile` | `integer` | 55 | \|tile drainage flag (0=no tile; 1=tile is present) |
| `hnew` | `real` | 56 | m \|new groundwater head (at end of day) |
| `hold` | `real` | 57 | m \|old groundwater head (at beginning of day) |
| `stor` | `real` | 58 | m3 \|currently available groundwater storage |
| `vbef` | `real` | 59 | m3 \|groundwater volume at beginning of day |
| `vaft` | `real` | 60 | m3 \|groundwater volume at end of day |
| `hdmo` | `real` | 61 | m \|monthly average groundwater head |
| `hdyr` | `real` | 62 | m \|annual average groundwater head |
| `delx` | `real` | 63 | m \|change in groundwater position (x direction) for current time step |
| `dely` | `real` | 64 | m \|change in groundwater position (y direction) for current time step |

### groundwater_transit

- **Defined in source**: `gwflow_module.f90:76`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `x` | `real*8` | 77 | m \|x coordinate |
| `y` | `real*8` | 78 | m \|y coordinate |
| `cell` | `integer` | 79 | \|current cell where groundwater is located |
| `t` | `real` | 80 | d \|cumulative groundwater travel time from recharge area |
| `t_chan` | `real` | 81 | d \|time for groundwater to reach a channel |
| `t_tile` | `real` | 82 | d \|time for groundwater to reach a tile drain |
| `t_well` | `real` | 83 | d \|time for groundwater to reach pumping well |

### groundwater_ss

- **Defined in source**: `gwflow_module.f90:108`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `chng` | `real` | 109 | \|change in storage (grid summaries only) |
| `rech` | `real` | 110 | \|recharge |
| `gwet` | `real` | 111 | \|groundwater ET |
| `gwsw` | `real` | 112 | \|groundwater discharge to channels |
| `swgw` | `real` | 113 | \|channel seepage to groundwater |
| `satx` | `real` | 114 | \|saturation excess flow |
| `soil` | `real` | 115 | \|groundwater added to soil profile |
| `latl` | `real` | 116 | \|lateral flow between cells |
| `disp` | `real` | 117 | \|dispersion (heat/solute transport) |
| `bndr` | `real` | 118 | \|boundary exchange |
| `ppag` | `real` | 119 | \|allocation-driven pumping (irrigation) |
| `ppdf` | `real` | 120 | \|pumping deficit (unmet demand) |
| `ppex` | `real` | 121 | \|external pumping |
| `tile` | `real` | 122 | \|tile drainage outflow |
| `resv` | `real` | 123 | \|reservoir exchange |
| `wetl` | `real` | 124 | \|wetland exchange |
| `fpln` | `real` | 125 | \|floodplain exchange |
| `canl` | `real` | 126 | \|canal exchange |
| `pond` | `real` | 127 | \|recharge pond seepage |
| `phyt` | `real` | 128 | \|phreatophyte transpiration |
| `totl` | `real` | 129 | \|sum of inputs and outputs |

### cell_channel_info

- **Defined in source**: `gwflow_module.f90:193`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 194 | \|number of cells connected to the channel |
| `cells` | `integer, allocatable` | 195 | \|cells connected to the channel |
| `leng` | `real, allocatable` | 196 | m \|length of channel in the cell |
| `elev` | `real, allocatable` | 197 | m \|elevation of channel bed in the cell |
| `hydc` | `real, allocatable` | 198 | m \|hydraulic conductivity of channel bed in the cell |
| `thck` | `real, allocatable` | 199 | m \|thickness of channel bed in the cell |
| `dpzn` | `integer, allocatable` | 200 | \|channel depth zone (optional) |
| `gw_chan_info` | `cell_channel_info` | 202 | groundwater-channel cell groups --------------------------------------------------------- |
| `gw_gwsw_group_flag` | `integer` | 205 | \|flag for channel cell grouping |
| `gw_gwsw_ngroup` | `integer` | 206 | \|number of groups |
| `gw_gwsw_max` | `integer` | 207 | \|max cells per group |
| `gw_gwsw_ncell` | `integer, dimension (:), allocatable` | 208 | \|number of cells per group |
| `gw_gwsw_group` | `integer, dimension (:,:), allocatable` | 209 | \|cell IDs in each group channel observation cells --------------------------------------------------------------- |
| `gw_chan_obs_flag` | `integer` | 212 | \|flag for observation cells |
| `gw_chan_nobs` | `integer` | 213 | \|number of observation cells |
| `gw_chan_obs_cell` | `integer, dimension (:), allocatable` | 214 | \|cell IDs for observations satx: variables for saturated excess flow -------------------------------------------------- |
| `gw_satx_flag` | `integer` | 217 | \| |
| `satx_count` | `integer` | 218 | \|for each day: number of cells that are saturated |

### satx_channel_info

- **Defined in source**: `gwflow_module.f90:219`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 220 | \|number of cells connected to the channel |
| `cells` | `integer, allocatable` | 221 | \|cells connected to the channel |
| `gw_satx_info` | `satx_channel_info` | 223 | soil: variables for gw-->soil exchange ----------------------------------------------------- |
| `gw_soil_flag` | `integer` | 226 | \| |
| `hru_soil` | `real, dimension (:,:,:), allocatable` | 227 | \| latl: variables for groundwater lateral flow ----------------------------------------------- |

### cell_connections

- **Defined in source**: `gwflow_module.f90:230`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cell_id` | `integer, allocatable` | 231 | \|cells connected to the cell |
| `latl` | `real, allocatable` | 232 | m3 \|groundwater flow to/from connected cell |
| `sat` | `real, allocatable` | 233 | m \|saturated thickness of connected cell |
| `cell_con` | `cell_connections` | 235 | ppag: variables for irrigation pumping ----------------------------------------------------- |
| `hru_pump` | `real, dimension (:), allocatable` | 238 | m3/day \|daily pumping per HRU |
| `hru_pump_mo` | `real, dimension (:), allocatable` | 239 | m3 \|monthly accumulator |
| `hru_pump_yr` | `real, dimension (:), allocatable` | 240 | m3 \|yearly accumulator |
| `hru_pump_aa` | `real, dimension (:), allocatable` | 241 | m3 \|average annual accumulator (sum of yearly totals) |
| `hru_pump_flag` | `integer` | 243 |  |
| `in_hru_pump_obs` | `integer` | 244 | \| |
| `num_hru_pump_obs` | `integer` | 245 | \| |
| `hru_pump_ids` | `integer, dimension (:), allocatable` | 246 | \| |
| `hru_pump_obs` | `real, dimension (:), allocatable` | 247 | \| ppex: variables for specified groundwater pumping ------------------------------------------ |
| `gw_pumpex_flag` | `integer` | 250 | \| |
| `gw_npumpex` | `integer` | 251 | \| |
| `gw_pumpex_cell` | `integer, dimension (:), allocatable` | 252 | \| |
| `gw_pumpex_nperiods` | `integer, dimension (:), allocatable` | 253 | \| |
| `gw_pumpex_dates` | `integer, dimension (:,:,:), allocatable` | 254 | \| |
| `gw_pumpex_rates` | `real, dimension (:,:), allocatable` | 255 | \| tile: variables for tile drainage outflow -------------------------------------------------- |
| `gw_tile_flag` | `integer` | 258 | \| |
| `gw_tile_group_flag` | `integer` | 259 | \| |
| `gw_tile_num_group` | `integer` | 260 | \| |
| `num_tile_cells` | `integer` | 261 | \| |
| `gw_tile_depth` | `real, dimension (:), allocatable` | 262 | m \|tile drain depth per cell |
| `gw_tile_drain_area` | `real, dimension (:), allocatable` | 263 | m2 \|drainage area per cell |
| `gw_tile_K` | `real, dimension (:), allocatable` | 264 | m/day \|tile hydraulic conductivity per cell |
| `gw_cell_tile` | `integer, dimension (:,:), allocatable` | 265 | \| |
| `gw_tilecell_chancell` | `integer, dimension (:), allocatable` | 266 | \| |
| `gw_tile_groups` | `integer, dimension (:,:), allocatable` | 267 | \| channel-tile connection |

### tile_channel_info

- **Defined in source**: `gwflow_module.f90:269`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 270 | \|number of cells connected to the channel |
| `cells` | `integer, allocatable` | 271 | \|cells connected to the channel |
| `gw_tile_info` | `tile_channel_info` | 273 | resv: variables for groundwater-reservoir exchange ----------------------------------------- |
| `gw_res_flag` | `integer` | 276 | \| |
| `res_thick` | `real` | 277 | \| |
| `res_K` | `real` | 278 | \| |
| `num_res_cells` | `integer` | 279 | \| cell-reservoir connection |

### cell_reservoir_info

- **Defined in source**: `gwflow_module.f90:281`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 282 | \|number of cells connected to the channel |
| `cells` | `integer, allocatable` | 283 | \|cells connected to the channel |
| `elev` | `real, allocatable` | 284 | m \|elevation of channel bed in the cell |
| `hydc` | `real, allocatable` | 285 | m \|hydraulic conductivity of channel bed in the cell |
| `thck` | `real, allocatable` | 286 | m \|thickness of channel bed in the cell |
| `gw_resv_info` | `cell_reservoir_info` | 288 | wetl: variables for groundwater-wetland exchange ------------------------------------------- |
| `gw_wet_flag` | `integer` | 291 | \| |
| `wet_thick` | `real, dimension (:), allocatable` | 292 | \| fpln: variables for groundwater-floodplain exchange ---------------------------------------- |
| `gw_fp_flag` | `integer` | 295 | \| |
| `in_fp_cell` | `integer` | 296 | \| |
| `gw_fp_ncells` | `integer` | 297 | \| |
| `gw_fp_cellid` | `integer, dimension (:), allocatable` | 298 | \| |
| `gw_fp_chanid` | `integer, dimension (:), allocatable` | 299 | \| |
| `gw_fp_K` | `real, dimension (:), allocatable` | 300 | \| |
| `gw_fp_area` | `real, dimension (:), allocatable` | 301 | \| |
| `flood_freq` | `integer, dimension (:), allocatable` | 302 | \| channel-cell connection |

### cell_floodplain_info

- **Defined in source**: `gwflow_module.f90:304`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 305 | \|number of cells connected to the channel |
| `cells` | `integer, allocatable` | 306 | \|cells connected to the channel |
| `hydc` | `real, allocatable` | 307 | m \|hydraulic conductivity of floodplain bottom in the cell |
| `area` | `real, allocatable` | 308 | m \|floodplain area in connection with cell |
| `mtch` | `integer, allocatable` | 309 | \|matching channel cell |
| `gw_fpln_info` | `cell_floodplain_info` | 311 | canl: variables for groundwater-canal exchange --------------------------------------------- |
| `gw_canal_flag` | `integer` | 314 | \| |
| `gw_ncanal` | `integer` | 315 | \| |
| `gw_canal_ncells` | `integer` | 316 | \| |
| `num_canalK_zones` | `integer` | 317 | \| |
| `canalK_zones` | `real, dimension (:), allocatable` | 318 | \| canal-channel connection |

### canal_chan_info

- **Defined in source**: `gwflow_module.f90:320`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncanal` | `integer` | 321 | \|number of canals connected to the channel |
| `canals` | `integer, allocatable` | 322 | \|canals connected to the channel |
| `wdth` | `real, allocatable` | 323 | m \|canal width |
| `dpth` | `real, allocatable` | 324 | m \|canal depth |
| `thck` | `real, allocatable` | 325 | m \|canal thickness |
| `hydc` | `real, allocatable` | 326 | m/d \|hydraulic conductivity of canal bed sediments |
| `dayb` | `integer, allocatable` | 327 | \|beginning day of active canal |
| `daye` | `integer, allocatable` | 328 | \|ending day of active canal |
| `gw_chan_canl_info` | `canal_chan_info` | 330 | canal-cell connection |

### cell_canal_info

- **Defined in source**: `gwflow_module.f90:332`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ncon` | `integer` | 333 | \|number of cells connected to the canal |
| `cells` | `integer, allocatable` | 334 | \|cells connected to the canal |
| `leng` | `real, allocatable` | 335 | m \|length of canal in the cell |
| `elev` | `real, allocatable` | 336 | m \|stage of canal in the cell |
| `hydc` | `real, allocatable` | 337 | m \|hydraulic conductivity of canal bed in the cell |
| `gw_canl_info` | `cell_canal_info` | 339 | canal-cell connection for canals that receive water outside of the model domain |

### cell_canal_out_info

- **Defined in source**: `gwflow_module.f90:341`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cell_id` | `integer` | 342 |  |
| `wdth` | `real` | 343 |  |
| `dpth` | `real` | 344 |  |
| `thck` | `real` | 345 |  |
| `leng` | `real` | 346 |  |
| `elev` | `real` | 347 |  |
| `hydc` | `real` | 348 |  |
| `dayb` | `integer` | 349 |  |
| `daye` | `integer` | 350 |  |

### cell_canal_div_info

- **Defined in source**: `gwflow_module.f90:360`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cell_id` | `integer` | 361 |  |
| `canal_id` | `integer` | 362 |  |
| `leng` | `real` | 363 |  |
| `elev` | `real` | 364 |  |

### canal_info

- **Defined in source**: `gwflow_module.f90:369`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `canal_id` | `integer` | 370 |  |
| `divr` | `integer` | 371 | \|recall diversion ID (0 = no recall) |
| `width` | `real` | 372 | m \|canal width |
| `depth` | `real` | 373 | m \|canal water depth |
| `thick` | `real` | 374 | m \|canal bed thickness |
| `bed_K` | `real` | 375 | m/day\|canal bed hydraulic conductivity |
| `div` | `real` | 376 | m3 \|volume of water diverted from channel source |
| `stor` | `real` | 377 | m3 \|current volume of canal water |
| `out_seep` | `real` | 378 | m3 \|volume of canal water seeped to aquifer |
| `out_pond` | `real` | 379 | m3 \|volume of canal water routed to recharge pond |

### cell_pond_info

- **Defined in source**: `gwflow_module.f90:389`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `id` | `integer` | 390 | \|recharge pond id |
| `chan` | `integer` | 391 | \|channel which provides water to the recharge pond |
| `canal` | `integer` | 392 | \|canal which provides water to the recharge pond |
| `unl` | `integer` | 393 | \|flag for outside source (1 = outside source) |
| `ncell` | `integer` | 394 | \|number of cells connected to the recharge pond |
| `wsta` | `integer` | 395 | \|weather station id |
| `area` | `real` | 396 | m2 \|recharge pond surface area |
| `bed_k` | `real` | 397 | m/d \|hydraulic conductivity of the pond bed sediments |
| `evap_co` | `real` | 398 | \|pond evaporation coefficient |
| `stor` | `real` | 399 | m3 \|current daily volume of the recharge pond |
| `seep` | `real` | 400 | m3 \|current daily seepage from the pond to the aquifer |
| `div` | `real` | 401 | m3 \|current daily specified diversion volume |
| `div_uns` | `real` | 402 | m3 \|unsatisfied diversion volume |
| `evap` | `real` | 403 | m3 \|current daily volume of evaporation from the recharge pond |
| `dy_start` | `integer` | 404 | \|year when recharge pond begins operation |
| `cells` | `integer, allocatable` | 405 | \|cells connected to the recharge pond |
| `conn_area` | `real, allocatable` | 406 | m2 \|connection area between recharge pond and cell |
| `sol_mass` | `real, allocatable` | 407 | kg \|solute mass in the pond water |
| `sol_conc` | `real, allocatable` | 408 | g/m3 \|solute concentration in the pond water |
| `unl_conc` | `real, allocatable` | 409 | g/m3 \|solute concentrations for an outside water source |

### groundwater_heat_state

- **Defined in source**: `gwflow_module.f90:467`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `stor` | `real` | 468 | Joule \|current heat stored in groundwater |
| `thmc` | `real` | 469 | J/(d m K) \|thermal conductivity |
| `temp` | `real` | 470 | C \|current groundwater temperature |
| `tnew` | `real` | 471 | C \|new groundwater temperature (at end of day) |
| `told` | `real` | 472 | C \|old groundwater temperature (at beginning of day) |
| `hbef` | `real` | 473 | Joule \|groundwater heat at beginning of day |
| `haft` | `real` | 474 | Joule \|groundwater heat at end of day |
| `tpmo` | `real` | 475 | C \|monthly average groundwater temperature |
| `tpyr` | `real` | 476 | C \|annual average groundwater temperature |

### solute_state

- **Defined in source**: `gwflow_module.f90:502`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `mass` | `real` | 503 | g \|solute mass in groundwater |
| `init` | `real` | 504 | g/m3 \|solute concentration in groundwater at beginning of simulation |
| `conc` | `real` | 505 | g/m3 \|solute concentration in groundwater |
| `cnew` | `real` | 506 | g/m3 \|new concentrations at end of time step |
| `mbef` | `real` | 507 | g \|solute mass at beginning of time step |
| `maft` | `real` | 508 | g \|solute mass at end of time step |
| `cnmo` | `real` | 509 | g/m3 \|monthly average concentration |
| `cnyr` | `real` | 510 | g/m3 \|annual average concentration |

### object_solute_state

- **Defined in source**: `gwflow_module.f90:512`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `solute` | `solute_state` | 513 |  |

### minl_state

- **Defined in source**: `gwflow_module.f90:519`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `fract` | `real, dimension (:), allocatable` | 520 | \|fraction of cell that is the salt mineral |

### solute_chem

- **Defined in source**: `gwflow_module.f90:527`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ino3` | `real` | 528 | \|selenium reduction inhibition factor |
| `oxyg` | `real` | 529 | g/m3 \|oxygen concentration in groundwater |
| `kd_seo4` | `real` | 530 | \|seo4 sorption partitioning coefficient |
| `kd_seo3` | `real` | 531 | \|seo3 sorption partitioning coefficient |
| `kd_boron` | `real` | 532 | \|boron sorption partitioning coefficient |
| `kseo4` | `real` | 533 | 1/day \|seo4 microbial reduction rate |
| `kseo3` | `real` | 534 | 1/day \|seo3 microbial reduction rate |
| `nshale` | `integer` | 535 | \|number of shale formations |
| `shale` | `integer, dimension (:), allocatable` | 536 | \|presence of shale in cell |
| `shale_sseratio` | `real, dimension (:), allocatable` | 537 | \|sulfur:se ratio in shale |
| `shale_o2a` | `real, dimension (:), allocatable` | 538 | 1/day \|o2 oxidation rate in presence of shale |
| `shale_no3a` | `real, dimension (:), allocatable` | 539 | 1/day \|no3 oxidation rate in presence of shale |
| `bed_flag` | `integer` | 540 | \|flag (0,1) for presence of shale in bedrock |
| `bed_sse` | `real` | 541 | \|sulfur:se ratio in bedrock shale |
| `bed_o2a` | `real` | 542 | 1/day \|o2 oxidation rate in presence of bedrock shale |
| `bed_no3a` | `real` | 543 | 1/day \|no3 oxidation rate in presence of bedrock shale |
| `ripar` | `integer` | 544 | \|flag: 1=cell in riparian area; 0=not |

### solute_ss

- **Defined in source**: `gwflow_module.f90:549`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `rech` | `real` | 550 | g \|solute mass entering cell via recharge water |
| `gwsw` | `real` | 551 | g \|solute mass leaving cell via groundwater discharging to channels |
| `swgw` | `real` | 552 | g \|solute mass entering cell via channel water seeping to groundwater |
| `soil` | `real` | 553 | g \|solute mass leaving cell via gw-->soil transfer |
| `satx` | `real` | 554 | g \|solute mass leaving cell via saturation excess flow |
| `ppag` | `real` | 555 | g \|solute mass leaving cell via pumping (for agriculture) |
| `ppex` | `real` | 556 | g \|solute mass leaving cell via pumping (external demand) |
| `tile` | `real` | 557 | g \|solute mass leaving cell via tile drainage outflow |
| `resv` | `real` | 558 | g \|solute mass exchanged with reservoir |
| `wetl` | `real` | 559 | g \|solute mass exchanged with wetland |
| `fpln` | `real` | 560 | g \|solute mass exchanged with channel in floodplain |
| `canl` | `real` | 561 | g \|solute mass exchanged with irrigation canal |
| `pond` | `real` | 562 | g \|solute mass in recharge pond seepage water |
| `advn` | `real` | 563 | g \|solute mass advected to/from cell |
| `disp` | `real` | 564 | g \|solute mass dispersed to/from cell |
| `rcti` | `real` | 565 | g \|solute mass of chemical reaction (input) |
| `rcto` | `real` | 566 | g \|solute mass of chemical reaction (output) |
| `minl` | `real` | 567 | g \|solute mass added (dissolution) or removed (precipitation) via salt mineral interactions |
| `sorb` | `real` | 568 | g \|solute mass of sorption |
| `totl` | `real` | 569 | g \|sum of mass inputs and outputs |

### object_solute_ss

- **Defined in source**: `gwflow_module.f90:571`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `solute` | `solute_ss` | 572 |  |

### solute_ss_sum

- **Defined in source**: `gwflow_module.f90:577`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `rech` | `real` | 578 | g \|solute mass entering cell via recharge water |
| `gwsw` | `real` | 579 | g \|solute mass leaving cell via groundwater discharging to channels |
| `swgw` | `real` | 580 | g \|solute mass entering cell via channel water seeping to groundwater |
| `soil` | `real` | 581 | g \|solute mass leaving cell via gw-->soil transfer |
| `satx` | `real` | 582 | g \|solute mass leaving cell via saturation excess flow |
| `ppag` | `real` | 583 | g \|solute mass leaving cell via pumping (for agriculture) |
| `ppex` | `real` | 584 | g \|solute mass leaving cell via pumping (external demand) |
| `tile` | `real` | 585 | g \|solute mass leaving cell via tile drainage outflow |
| `resv` | `real` | 586 | g \|solute mass exchanged with reservoir |
| `wetl` | `real` | 587 | g \|solute mass exchanged with wetland |
| `fpln` | `real` | 588 | g \|solute mass exchanged with channel in floodplain |
| `canl` | `real` | 589 | g \|solute mass exchanged with irrigation canal |
| `pond` | `real` | 590 | g \|solute mass in recharge pond seepage water |
| `advn` | `real` | 591 | g \|solute mass advected to/from cell |
| `disp` | `real` | 592 | g \|solute mass dispersed to/from cell |
| `rcti` | `real` | 593 | g \|solute mass produced by chemical reaction |
| `rcto` | `real` | 594 | g \|solute mass consumed by chemical reaction |
| `minl` | `real` | 595 | g \|solute mass produced by salt mineral dissolution |
| `sorb` | `real` | 596 | g \|solute mass of sorption |

### object_solute_ss_sum

- **Defined in source**: `gwflow_module.f90:598`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `solute` | `solute_ss_sum` | 599 |  |

## Variables Defined
### ncell

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:6`
- **Source note**: !number of gwflow cells

### num_active

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:7`
- **Source note**: !number of active cells

### gw_time_step

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:8`
- **Source note**: days           !flow solution time step

### gwflag_day

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:9`
- **Source note**: !flag for writing daily mass balance file

### gwflag_mon

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:10`
- **Source note**: !flag for writing monthly mass balance file

### gwflag_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:11`
- **Source note**: !flag for writing yearly mass balance file

### gwflag_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:12`
- **Source note**: !flag for writing average annual mass balance file

### gwflag_obs

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:13`
- **Source note**: !flag for writing observation well output (default on)

### gwflag_pump

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:14`
- **Source note**: !flag for writing HRU pumping output (default on)

### gwflag_heat

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:15`
- **Source note**: !flag for writing heat balance output (default on if heat active)

### gwflag_solute

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:16`
- **Source note**: !flag for writing solute balance output (default on if solute active)

### gwflag_flux

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:17`
- **Source note**: !flag for writing specialty diagnostic output (default on)

### bc_type

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:18`
- **Source note**: !boundary conditions (1=constant head; 2=no-flow)

### conn_type

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:19`
- **Source note**: !recharge/ET connections (1=HRU; 2=LSU)

### gw_daycount

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:20`
- **Source note**: !simulation day counter (for pumping time series)

### gwflow_area

- **Type**: `real*8`
- **Defined in source**: `gwflow_module.f90:21`
- **Source note**: m2             !area of the watershed occupied by active gwflow cells

### bc_type_array

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:22`
- **Source note**: generic array for reading in values for structured grid

### grid_type

- **Type**: `character*15`
- **Defined in source**: `gwflow_module.f90:25`
- **Source note**: "structured" or "unstructured" (usg)

### grid_nrow

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:26`
- **Source note**: number of rows in structured grid

### grid_ncol

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:27`
- **Source note**: number of columns in structured grid

### cell_id_usg

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:28`
- **Source note**: usg cell number, for cell in structured grid (array)

### cell_id_list

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:29`
- **Source note**: usg cell number, for cell in structured grid (list)

### grid_status

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:30`
- **Source note**: cell status for structured grid

### grid_int

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:31`
- **Source note**: generic array for reading in values for structured grid

### grid_val

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:32`
- **Source note**: generic array for reading in values for structured grid

### cell_row

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:33`
- **Source note**: structured grid row for each cell (for cell definition output)

### cell_col

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:34`
- **Source note**: structured grid column for each cell (for cell definition output)

### cell_gis_id

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:35`
- **Source note**: authoritative gis_id per cell (gwflowcells.shp id), from gwflow.cells col 22

### cell_name

- **Type**: `character(len=16), dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:36`
- **Source note**: authoritative cell name (cellNNNN), from gwflow.cells col 2

### out_gw_celldef

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:37`
- **Source note**: file unit for cell definition output

### gw_state

- **Type**: `groundwater_state`
- **Defined in source**: `gwflow_module.f90:66`

### gw_ttime

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:70`

### gw_transit_num

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:71`

### gw_transit_cells

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:72`

### gw_cell_chan_flag

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:73`

### gw_cell_chan_time

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:74`

### gw_cell_tile_time

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:75`

### gw_transit

- **Type**: `groundwater_transit`
- **Defined in source**: `gwflow_module.f90:85`

### hru_cells_link

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:89`
- **Source note**: |

### hru_num_cells

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:90`
- **Source note**: |

### hru_cells

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:91`
- **Source note**: |

### hru_cells_fract

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:92`
- **Source note**: |

### cells_fract

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:93`
- **Source note**: |

### hrus_connected

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:94`
- **Source note**: |flag: which HRUs are connected to cells

### lsu_cells_link

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:96`
- **Source note**: |

### in_lsu_cell

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:97`
- **Source note**: |

### lsu_num_cells

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:98`
- **Source note**: |

### lsu_cells

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:99`
- **Source note**: |

### lsu_cells_fract

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:100`
- **Source note**: |

### lsus_connected

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:101`
- **Source note**: |

### gw_hyd_ss

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:133`
- **Source note**: daily

### gw_hyd_ss_mo

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:134`
- **Source note**: monthly sums

### gw_hyd_ss_yr

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:135`
- **Source note**: yearly sums

### gw_hyd_ss_aa

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:136`
- **Source note**: average annual sums

### gw_head_sum_aa

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:137`
- **Source note**: head sum across all years for AA avg

### gw_hyd_grid_mo

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:140`
- **Source note**: monthly grid total

### gw_hyd_grid_yr

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:141`
- **Source note**: yearly grid total

### gw_hyd_grid_aa

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:142`
- **Source note**: accumulates simulation total; divided by nbyr at end

### vbef_grid

- **Type**: `real*8`
- **Defined in source**: `gwflow_module.f90:145`
- **Source note**: m3 total GW volume at start of day

### vaft_grid

- **Type**: `real*8`
- **Defined in source**: `gwflow_module.f90:146`
- **Source note**: m3 total GW volume at end of day

### heat_hbef_grid

- **Type**: `real*8`
- **Defined in source**: `gwflow_module.f90:147`
- **Source note**: J total heat at start of day

### heat_haft_grid

- **Type**: `real*8`
- **Defined in source**: `gwflow_module.f90:148`
- **Source note**: J total heat at end of day

### sol_grid_mbef

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:149`
- **Source note**: kg total solute mass at start of day

### sol_grid_maft

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:150`
- **Source note**: kg total solute mass at end of day

### sim_month

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:151`
- **Source note**: month counter for simulation

### gw_heat_ss

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:154`
- **Source note**: daily

### gw_heat_ss_mo

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:155`
- **Source note**: monthly sums

### gw_heat_ss_yr

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:156`
- **Source note**: yearly sums

### gw_heat_grid_mo

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:159`
- **Source note**: monthly grid total

### gw_heat_grid_yr

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:160`
- **Source note**: yearly grid total

### gw_heat_grid_aa

- **Type**: `groundwater_ss`
- **Defined in source**: `gwflow_module.f90:161`
- **Source note**: accumulates simulation total; divided by nbyr at end

### gw_bound_near

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:164`
- **Source note**: |nearest active cell to each boundary cell

### gw_bound_dist

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:165`
- **Source note**: m          |distance of nearest active cell to each boundary cell

### gwflow_perc

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:166`
- **Source note**: |

### gw_delay

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:167`
- **Source note**: |

### gw_rech

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:168`
- **Source note**: |

### delay

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:169`
- **Source note**: |

### gw_et_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:172`
- **Source note**: |

### etremain

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:173`
- **Source note**: |

### num_chancells

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:176`
- **Source note**: |

### gw_chan_id

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:177`
- **Source note**: |

### gw_chan_cell

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:178`
- **Source note**: |

### gw_chan_chan

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:179`
- **Source note**: |

### gw_chan_zone

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:180`
- **Source note**: |

### gw_chan_ncell

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:181`
- **Source note**: |number of cells connected to each channel

### gw_chan_len

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:182`
- **Source note**: |

### gw_chan_elev

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:183`
- **Source note**: |

### gw_chan_K

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:184`
- **Source note**: |

### gw_chan_thick

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:185`
- **Source note**: |

### gw_bed_change

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:186`
- **Source note**: |

### gw_chan_dpzn

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:187`
- **Source note**: |depth zone per channel-cell connection

### gw_chan_obs

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:188`
- **Source note**: |obs flag (0/1) per channel-cell connection (from chancell.gw)

### gw_chan_dep_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:189`
- **Source note**: |flag for channel depth zones

### gw_chan_ndpzn

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:190`
- **Source note**: |number of channel depth zones

### gw_chan_dep

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:191`
- **Source note**: m          |specified daily channel depths

### gw_canl_out_info

- **Type**: `cell_canal_out_info`
- **Defined in source**: `gwflow_module.f90:352`

### gw_canal_ncells_out

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:353`
- **Source note**: |number of cells connected to canals that receive outside water

### canal_out_info

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:354`
- **Source note**: |characteristics for canals that receive outside water

### canal_out_conc

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:355`
- **Source note**: |solute concentration in canals that receive outside water

### div_conc_salt

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:357`
- **Source note**: g/m3 |salt ion concentration in diverted water

### div_conc_cs

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:358`
- **Source note**: g/m3 |constituent concentration in diverted water

### gw_canl_div_cell

- **Type**: `cell_canal_div_info`
- **Defined in source**: `gwflow_module.f90:366`

### gw_canal_ncells_div

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:367`
- **Source note**: |number of cells connected to canals that receive from diversions

### gw_canl_div_info

- **Type**: `canal_info`
- **Defined in source**: `gwflow_module.f90:381`

### gw_pond_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:384`
- **Source note**: |flag = 0 (off) or 1 (on)

### gw_pond_div_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:385`
- **Source note**: |flag: daily pond diversion series present (pond_div.gw)

### gw_npond

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:386`
- **Source note**: |number of recharge ponds in the model domain

### in_ponds

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:387`
- **Source note**: |input file unit for ponds

### gw_pond_info

- **Type**: `cell_pond_info`
- **Defined in source**: `gwflow_module.f90:411`

### gw_phyt_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:414`
- **Source note**: |flag = 0 (off) or 1 (on)

### gw_phyt_ncells

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:415`
- **Source note**: |number of cells with phreatophytes

### gw_phyt_npts

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:416`
- **Source note**: |number of depth-rate points

### gw_phyt_ids

- **Type**: `integer, allocatable`
- **Defined in source**: `gwflow_module.f90:417`
- **Source note**: |ids of cells with phreatophytes

### gw_phyt_area

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:418`
- **Source note**: m2   |area of each cell that contains phreatophytes

### gw_phyt_dep

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:419`
- **Source note**: m    |depth below ground surface for ET-rate relationship

### gw_phyt_rate

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:420`
- **Source note**: m/day|rate of transpiration at corresponding depth

### gw_tvh_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:423`
- **Source note**: |flag = 0 (off) or 1 (on)

### gw_ntvh

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:424`
- **Source note**: |number of time-varying boundary cells

### gw_tvh_ids

- **Type**: `integer, allocatable`
- **Defined in source**: `gwflow_module.f90:425`
- **Source note**: |boundary cell IDs

### gw_tvh_vals

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:426`
- **Source note**: |boundary cell head values for each year

### gw_group_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:429`
- **Source note**: |flag to make active

### gw_wb_grp_num

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:430`
- **Source note**: |number of water balance groups

### gw_wb_grp_ncell

- **Type**: `integer, allocatable`
- **Defined in source**: `gwflow_module.f90:431`
- **Source note**: |number of cells in each group

### gw_wb_grp_cells

- **Type**: `integer, allocatable`
- **Defined in source**: `gwflow_module.f90:432`
- **Source note**: |cell IDs in each water balance group

### cell_channel

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:435`
- **Source note**: |nearest channel for each grid cell

### gw_num_output

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:439`
- **Source note**: |

### gw_output_index

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:440`
- **Source note**: |

### gw_output_yr

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:441`
- **Source note**: |

### gw_output_day

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:442`
- **Source note**: |

### gw_num_obs_wells

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:446`
- **Source note**: |

### gw_obs_cells

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:447`
- **Source note**: |

### gw_obs_head

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:448`
- **Source note**: |

### gw_cell_obs_ss

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:449`
- **Source note**: |

### gw_cell_obs_ss_vals

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:450`
- **Source note**: |

### chan_hyd_sep

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:454`

### hydsep_flag

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:455`

### gw_heat_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:459`
- **Source note**: |flag (0 or 1) 1 = heat transport is simulated

### gw_rho

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:460`
- **Source note**: kg/m3        |density of groundwater

### gw_cp

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:461`
- **Source note**: J/(kg C)     |specific heat of groundwater

### gw_rechheat

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:462`
- **Source note**: J            |heat in daily recharge (reaching water table)

### gw_obs_temp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:463`
- **Source note**: deg C        |temperature in observation cells

### gw_obs_temp_aa

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:464`
- **Source note**: deg C       |AA temperature accumulator for obs wells

### gw_obs_sol_aa

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:465`
- **Source note**: mg/L      |AA solute conc accumulator for obs wells

### heat_cell

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:466`
- **Source note**: J            |heat storage for current day (before heat change loop)

### gwheat_state

- **Type**: `groundwater_heat_state`
- **Defined in source**: `gwflow_module.f90:478`

### gw_solute_flag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:487`
- **Source note**: |main flag

### gw_nsolute

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:488`
- **Source note**: |number of solutes

### num_ts_transport

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:489`
- **Source note**: |number of transport time steps per day

### gw_long_disp

- **Type**: `real`
- **Defined in source**: `gwflow_module.f90:490`
- **Source note**: m   |aquifer longitudinal dispersivity

### gwsol_salt

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:491`
- **Source note**: |flag for simulating salt ion groundwater transport (so4,ca,mg,na,k,cl,co3,hco3)

### gwsol_cons

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:492`
- **Source note**: |flag for simulating constituent groundwater transport (seo4,seo3,boron)

### gwsol_minl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:493`
- **Source note**: |flag for simulating salt mineral precipitation-dissolution

### gw_nminl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:494`
- **Source note**: |number of salt minerals (set to 5)

### gwsol_nm

- **Type**: `character (len=16), allocatable`
- **Defined in source**: `gwflow_module.f90:497`

### gwsol_rctn

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:498`

### gwsol_sorb

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:499`

### gwsol_state

- **Type**: `object_solute_state`
- **Defined in source**: `gwflow_module.f90:515`

### mass_min

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:518`
- **Source note**: g       |solute mass added/removed from cell via precipitation-dissolution

### gwsol_minl_state

- **Type**: `minl_state`
- **Defined in source**: `gwflow_module.f90:522`

### cell_int

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:525`

### mass_rct

- **Type**: `real, allocatable`
- **Defined in source**: `gwflow_module.f90:526`
- **Source note**: g            |solute mass added/removed from cell via chemical reaction (allocated in gwflow_read)

### gwsol_chem

- **Type**: `solute_chem`
- **Defined in source**: `gwflow_module.f90:546`

### gwsol_ss

- **Type**: `object_solute_ss`
- **Defined in source**: `gwflow_module.f90:574`

### gwsol_ss_sum

- **Type**: `object_solute_ss_sum`
- **Defined in source**: `gwflow_module.f90:601`

### gwsol_ss_sum_mo

- **Type**: `object_solute_ss_sum`
- **Defined in source**: `gwflow_module.f90:602`

### gwflow_percsol

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:605`
- **Source note**: kg/ha    |solute mass leaving the soil profile

### gw_rechsol

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:606`
- **Source note**: kg/ha    |solute mass in daily recharge (reaching water table)

### sol_grid_chng_mo

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:609`

### sol_grid_rech_mo

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:609`

### sol_grid_gwsw_mo

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:609`

### sol_grid_swgw_mo

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:609`

### sol_grid_chng_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:615`

### sol_grid_rech_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:616`

### sol_grid_gwsw_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:617`

### sol_grid_swgw_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:618`

### sol_grid_satx_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:619`

### sol_grid_advn_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:620`

### sol_grid_disp_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:621`

### sol_grid_rcti_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:622`

### sol_grid_rcto_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:623`

### sol_grid_minl_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:624`

### sol_grid_sorb_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:625`

### sol_grid_ppag_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:626`

### sol_grid_ppex_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:627`

### sol_grid_tile_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:628`

### sol_grid_soil_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:629`

### sol_grid_resv_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:630`

### sol_grid_wetl_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:631`

### sol_grid_canl_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:632`

### sol_grid_fpln_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:633`

### sol_grid_pond_yr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:634`

### sol_grid_chng_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:635`

### sol_grid_rech_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:636`

### sol_grid_gwsw_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:637`

### sol_grid_swgw_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:638`

### sol_grid_satx_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:639`

### sol_grid_advn_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:640`

### sol_grid_disp_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:641`

### sol_grid_rcti_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:642`

### sol_grid_rcto_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:643`

### sol_grid_minl_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:644`

### sol_grid_sorb_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:645`

### sol_grid_ppag_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:646`

### sol_grid_ppex_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:647`

### sol_grid_tile_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:648`

### sol_grid_soil_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:649`

### sol_grid_resv_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:650`

### sol_grid_wetl_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:651`

### sol_grid_canl_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:652`

### sol_grid_fpln_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:653`

### sol_grid_pond_tt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `gwflow_module.f90:654`

### gw_obs_solute

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `gwflow_module.f90:657`
- **Source note**: |

### out_gw

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:661`

### in_wet_cell

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:662`

### out_gwobs

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:663`
- **Source note**: merged obs well long-format file (day)

### out_gwobs_mon

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:664`

### out_gwobs_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:665`

### out_gwobs_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:666`

### out_gwconnect

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:667`

### out_gwheads

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:668`

### out_gwbal

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:669`

### out_gwsw_chan

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:670`

### out_gw_chan

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:671`

### out_gw_rech

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:672`

### out_gw_et

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:673`

### out_gw_grid

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:674`

### out_gw_satex

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:675`

### out_gwsw

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:676`

### out_lateral

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:677`

### out_gw_etact

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:678`

### out_gw_tile

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:679`

### out_gwbal_mon

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:680`

### out_gwbal_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:681`

### out_gwbal_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:682`

### out_gwbal_grp

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:683`

### out_hyd_sep

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:684`

### out_tile_cells

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:685`

### out_gwconc

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:686`

### out_gwtile_hru

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:687`

### out_gwobs_ss

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:688`

### out_gw_soil

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:689`

### out_gw_res

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:690`

### out_gw_wet

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:691`

### out_gw_pumpag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:692`

### out_gw_pumpex

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:693`

### out_gw_pumpdef

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:694`

### out_gw_canal

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:695`

### out_gw_fp

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:696`

### out_gw_chem

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:697`

### out_gw_gwet

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:699`

### out_gw_gwsw

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:700`

### out_gw_satx

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:701`

### out_gw_ppag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:702`

### out_gw_ppex

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:703`

### out_gw_resv

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:704`

### out_gw_wetl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:705`

### out_gw_fpln

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:706`

### out_gw_canl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:707`

### out_gw_pond

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:708`

### out_gw_phyt

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:709`

### out_canal_bal

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:711`

### out_canal_sol

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:712`

### out_pond_bal

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:713`

### out_pond_sol

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:714`

### out_pond_mass

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:715`

### out_pond_conc

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:716`

### out_gwtemps

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:718`

### out_gw_transit

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:720`

### out_gw_transit_chan

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:721`

### out_gw_transit_tile

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:722`

### out_gwsw_groups

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:724`

### out_gwsw_chanobs_flow

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:725`

### out_gwsw_chanobs_no3

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:726`

### out_hru_pump_day

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:727`

### out_hru_pump_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:728`

### out_hru_pump_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:729`

### out_hru_pump_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:730`

### out_hru_pump_obs

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:731`

### out_head_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:732`

### out_head_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:733`

### out_conc_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:734`

### out_conc_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:735`

### out_sol_rech

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:737`

### out_sol_gwsw

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:738`

### out_sol_soil

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:739`

### out_sol_satx

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:740`

### out_sol_ppag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:741`

### out_sol_ppex

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:742`

### out_sol_tile

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:743`

### out_sol_resv

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:744`

### out_sol_fpln

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:745`

### out_sol_canl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:746`

### out_sol_wetl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:747`

### out_sol_rcti

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:748`

### out_sol_rcto

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:749`

### out_sol_minl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:750`

### out_sol_sorb

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:751`

### out_sol_pond

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:752`

### out_sol_rech_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:754`

### out_sol_gwsw_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:755`

### out_sol_soil_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:756`

### out_sol_satx_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:757`

### out_sol_ppag_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:758`

### out_sol_ppex_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:759`

### out_sol_tile_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:760`

### out_sol_resv_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:761`

### out_sol_fpln_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:762`

### out_sol_canl_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:763`

### out_sol_wetl_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:764`

### out_sol_rcti_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:765`

### out_sol_rcto_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:766`

### out_sol_minl_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:767`

### out_sol_sorb_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:768`

### out_sol_pond_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:769`

### out_solbal_dy

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:771`

### out_solbal_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:772`

### out_solbal_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:773`

### out_solbal_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:774`

### out_gwobs_sol

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:776`

### out_gw_rech_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:778`

### out_gw_gwet_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:779`

### out_gw_gwsw_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:780`

### out_gw_soil_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:781`

### out_gw_satx_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:782`

### out_gw_ppag_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:783`

### out_gw_ppex_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:784`

### out_gw_tile_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:785`

### out_gw_resv_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:786`

### out_gw_wetl_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:787`

### out_gw_fpln_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:788`

### out_gw_canl_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:789`

### out_gw_pond_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:790`

### out_gw_phyt_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:791`

### out_heatbal_dy

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:793`

### out_heatbal_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:794`

### out_heatbal_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:795`

### out_temp_mo

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:796`

### out_temp_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:797`

### out_gwobs_temp

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:798`

### out_heat_rech

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:800`

### out_heat_gwet

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:801`

### out_heat_gwsw

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:802`

### out_heat_satx

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:803`

### out_heat_soil

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:804`

### out_heat_tile

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:805`

### out_heat_ppag

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:806`

### out_heat_ppex

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:807`

### out_heat_resv

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:808`

### out_heat_wetl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:809`

### out_heat_fpln

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:810`

### out_heat_canl

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:811`

### out_heat_pond

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:812`

### out_gwcell_day

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:815`

### out_gwcell_mon

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:816`

### out_gwcell_yr

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:817`

### out_gwcell_aa

- **Type**: `integer`
- **Defined in source**: `gwflow_module.f90:818`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

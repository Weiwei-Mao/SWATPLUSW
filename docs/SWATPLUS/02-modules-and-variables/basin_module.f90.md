---
type: module
tags:
  - swat/module
  - swat/to-read
file: basin_module.f90
note_file: basin_module.f90
module_name: basin_module
defines_types:
  - basin_inputs
  - basin_control_codes
  - basin_parms
  - print_interval
  - basin_print_codes
  - basin_sediment_budget
  - mgt_header
  - mgt_header_unit1
  - basin_yld_header
defines_vars:
  - prog
  - ban_precip_aa
  - bsn
  - bsn_cc
  - bsn_prm
  - pco
  - pco_init
  - bsn_sedbud
  - mgt_hdr
  - mgt_hdr_unt1
  - bsn_yld_hdr
defines_subroutines: []
defines_functions:
  - print_prt_error
defines_procedures:
  - print_prt_error
purpose: ""
---

# basin_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### basin_inputs

- **Defined in source**: `basin_module.f90:9`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 10 |  |
| `area_ls_ha` | `real` | 11 |  |
| `area_tot_ha` | `real` | 12 |  |

### basin_control_codes

- **Defined in source**: `basin_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `petfile` | `character(len=16)` | 18 | potential et filename |
| `wwqfile` | `character(len=16)` | 19 | watershed stream water quality filename |
| `pet` | `integer` | 20 | potential ET method code 0 = Priestley-Taylor 1 = Penman-Monteith 2 = Hargreaves method |
| `nam1` | `integer` | 24 | not used |
| `crk` | `integer` | 25 | crack flow code 1 = compute flow in cracks |
| `swift_out` | `integer` | 27 | write to SWIFT input file 0 = do not write 1 = write to swift_hru.inp |
| `sed_det` | `integer` | 30 | peak rate method 0 = NRCS dimensionless hydrograph with PRF 1 = half hour rainfall intensity method |
| `rte` | `integer` | 33 | water routing method 0 variable storage method 1 Muskingum method |
| `deg` | `integer` | 36 | not used |
| `wq` | `integer` | 37 | not used |
| `nostress` | `integer` | 38 | redefined to the sequence number -- changed to no nutrient stress 0 = all stresses applied 1 = turn off all plant stress 2 = turn off nutrient plant stress only |
| `cn` | `integer` | 42 | not used |
| `cfac` | `integer` | 43 | not used |
| `cswat` | `integer` | 44 | carbon code: 0 = off (static), 1 = C-FARM (reserved, not implemented), 2 = dynamic CENTURY/SWAT-C model. numbering aligned with legacy SWAT as directed by Srinivasan. = 0 Static soil carbon (old mineralization routines) = 1 C-FARM one carbon pool model = 2 Century model |
| `lapse` | `integer` | 50 | precip and temperature lapse rate control 0 = do not adjust for elevation 1 = adjust for elevation |
| `uhyd` | `integer` | 53 | Unit hydrograph method: 0 = triangular UH 1 = gamma function UH |
| `sed_ch` | `integer` | 56 | not used |
| `tdrn` | `integer` | 57 | tile drainage eq code 0 = tile flow using drawdown days equation 1 = tile flow using drainmod equations |
| `wtdn` | `integer` | 60 | shallow water table depth algorithms code 0 = depth using orig water table depth routine - fill to upper limit 1 = depth using drainmod water table depth routine |
| `sol_p_model` | `integer` | 63 | 0 = original soil P model in SWAT documentation 1 = new soil P model in Vadas and White (2010) |
| `gampt` | `integer` | 65 | 0 = curve number; 1 = Green and Ampt |
| `atmo` | `character(len=1)` | 66 | not used |
| `smax` | `integer` | 67 | not used |
| `qual2e` | `integer` | 68 | 0 = instream nutrient routing using QUAL2E 1 = instream nutrient routing using QUAL2E - with simplified nutrient transformations |
| `gwflow` | `integer` | 70 | 0 = gwflow module not active; 1 = gwflow module active |
| `idc_till` | `integer` | 71 | 1 = Use dssat tillage method to use if cswat = 2 2 = Use epic tillage method to use if cswat = 2 3 = Use Kemanian tillage method to use if cswat = 2 4 = Use dndc tillage method to use if cswat = 2 |

### basin_parms

- **Defined in source**: `basin_module.f90:79`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `evlai` | `real` | 80 | none \|leaf area index at which no evap occurs |
| `ffcb` | `real` | 81 | none \|initial soil water cont expressed as a fraction of fc |
| `surlag` | `real` | 82 | days \|surface runoff lag time (days) |
| `adj_pkr` | `real` | 83 | none \|peak rate adjustment factor in the subbasin |
| `prf` | `real` | 84 | peak rate factor for peak rate equation |
| `spcon` | `real` | 85 | not used |
| `spexp` | `real` | 86 | not used |
| `cmn` | `real` | 87 | rate factor for mineralization on active org N - 0.0003 -> 0.003 |
| `n_updis` | `real` | 88 | nitrogen uptake dist parm |
| `p_updis` | `real` | 89 | phosphorus uptake dist parm |
| `nperco` | `real` | 90 | nitrate perc coeff (0-1) 0 = conc of nitrate in surface runoff is zero 1 = perc has same conc of nitrate as surf runoff |
| `pperco` | `real` | 93 | phos perc coeff (0-1) 0 = conc of sol P in surf runoff is zero 1 = percolate has some conc of sol P as surf runoff |
| `phoskd` | `real` | 96 | phos soil partitioning coef |
| `psp` | `real` | 97 | phos availability index |
| `rsdco` | `real` | 98 | residue decomposition coeff |
| `percop` | `real` | 99 | pestcide perc coeff (0-1) |
| `msk_co1` | `real` | 100 | calibration coeff to control impact of the storage time constant for the reach at bankfull depth |
| `msk_co2` | `real` | 102 | calibration coefficient used to control impact of the storage time constant for low flow (where low flow is when river is at 0.1 bankfull depth) upon the Km value calculated for the reach |
| `msk_x` | `real` | 106 | weighting factor control relative importance of inflow rate and outflow rate in determining storage on reach |
| `nperco_lchtile` | `real` | 108 | n concentration coeff for tile flow and leach from bottom layer |
| `evrch` | `real` | 109 | reach evaporation adjustment factor |
| `scoef` | `real` | 110 | channel storage coefficient (0-1) |
| `cdn` | `real` | 111 | denitrification exponential rate coefficient |
| `sdnco` | `real` | 112 | denitrification threshold frac of field cap |
| `bact_swf` | `real` | 113 | frac of manure containing active colony forming units |
| `tb_adj` | `real` | 114 | adjustment factor for subdaily unit hydrograph basetime |
| `cn_froz` | `real` | 115 | parameter for frozen soil adjustment on infiltraion/runoff |
| `dorm_hr` | `real` | 116 | time threshold used to define dormant (hrs) |
| `plaps` | `real` | 117 | mm/km \|precipitation lapse rate: mm per km of elevation difference |
| `tlaps` | `real` | 118 | deg C/km \|temperature lapse rate: deg C per km of elevation difference |
| `nfixmx` | `real` | 119 | max daily n-fixation (kg/ha) |
| `decr_min` | `real` | 120 | minimum daily residue decay |
| `rsd_covco` | `real` | 121 | residue cover factor for computing frac of cover |
| `urb_init_abst` | `real` | 122 | maximum initial abstraction for urban areas when using Green and Ampt |
| `petco_pmpt` | `real` | 123 | PET adjustment (%) for Penman-Montieth and Preiestly-Taylor methods |
| `uhalpha` | `real` | 124 | alpha coeff for est unit hydrograph using gamma func |
| `eros_spl` | `real` | 125 | coeff of splash erosion varying 0.9-3.1 |
| `rill_mult` | `real` | 126 | rill erosion coefficient |
| `eros_expo` | `real` | 127 | exponential coefficient for overland flow |
| `c_factor` | `real` | 128 | scaling parameter for cover and management factor for overland flow erosion |
| `ch_d50` | `real` | 130 | median particle diameter of main channel (mm) |
| `co2` | `real` | 131 | co2 concentration at start of simulation (ppm) |
| `day_lag_mx` | `integer` | 132 | max days to lag hydrographs for hru, ru and channels non-draining soils |
| `igen` | `integer` | 134 | random generator code: 0 = use default numbers 1 = generate new numbers in every simulation |

### print_interval

- **Defined in source**: `basin_module.f90:140`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `d` | `character(len=1)` | 141 |  |
| `m` | `character(len=1)` | 142 |  |
| `y` | `character(len=1)` | 143 |  |
| `a` | `character(len=1)` | 144 |  |
| `already_read_in` | `logical` | 145 |  |

### basin_print_codes

- **Defined in source**: `basin_module.f90:148`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day_print` | `character (len=1)` | 154 |  |
| `day_print_over` | `character (len=1)` | 155 |  |
| `nyskip` | `integer` | 156 | number of years to skip output summarization |
| `sw_init` | `character (len=1)` | 157 | n=sw not initialized, y=sw initialized for output (when hit nyskip) DAILY START/END AND INTERVAL |
| `day_start` | `integer` | 159 | julian day to start printing output |
| `day_end` | `integer` | 160 | julian day to end printing output |
| `yrc_start` | `integer` | 161 | calendar year to start printing output |
| `yrc_end` | `integer` | 162 | calendar year to end printing output |
| `int_day` | `integer` | 163 | interval between daily printing |
| `int_day_cur` | `integer` | 164 | current day since last print AVE ANNUAL END YEARS |
| `aa_numint` | `integer` | 166 | number of print intervals for ave annual output |
| `aa_yrs` | `integer, dimension(:), allocatable` | 167 | end years for ave annual output SPECIAL OUTPUTS |
| `csvout` | `character(len=1)` | 169 | code to print .csv files n=no print; y=print; code to print carbon output; d = end of day; m = end of month; y = end of year; a = end of simulation; |
| `use_obj_labels` | `character(len=1)` | 171 | code to read in the print.prt print objects respecting the label of in the row (1st column) to identify name of the print object |
| `cdfout` | `character(len=1)` | 174 | code to print netcdf (cdf) files n=no print; y=print; OTHER OUTPUTS |
| `crop_yld` | `character(len=1)` | 177 | crop yields - a=average annual; y=yearly; b=both annual and yearly; n=no print |
| `mgtout` | `character(len=1)` | 178 | management output file (mgt.out) (default ave annual-d,m,y,a input) |
| `hydcon` | `character(len=1)` | 179 | hydrograph connect output file (hydcon.out) |
| `fdcout` | `character(len=1)` | 180 | flow duration curve output n=no print; avann=print; NOT ACTIVE BASIN |
| `wb_bsn` | `print_interval` | 182 | water balance BASIN output |
| `nb_bsn` | `print_interval` | 183 | nutrient balance BASIN output |
| `ls_bsn` | `print_interval` | 184 | losses BASIN output |
| `pw_bsn` | `print_interval` | 185 | plant weather BASIN output |
| `aqu_bsn` | `print_interval` | 186 |  |
| `res_bsn` | `print_interval` | 187 |  |
| `chan_bsn` | `print_interval` | 188 |  |
| `sd_chan_bsn` | `print_interval` | 189 |  |
| `recall_bsn` | `print_interval` | 190 | REGION |
| `wb_reg` | `print_interval` | 192 | water balance REGION output |
| `nb_reg` | `print_interval` | 193 | nutrient balance REGION output |
| `ls_reg` | `print_interval` | 194 | losses REGION output |
| `pw_reg` | `print_interval` | 195 | plant weather REGION output |
| `aqu_reg` | `print_interval` | 196 |  |
| `res_reg` | `print_interval` | 197 |  |
| `sd_chan_reg` | `print_interval` | 198 |  |
| `recall_reg` | `print_interval` | 199 |  |
| `water_allo` | `print_interval` | 200 | LSU |
| `wb_lsu` | `print_interval` | 202 | water balance LSU output |
| `nb_lsu` | `print_interval` | 203 | nutrient balance LSU output |
| `ls_lsu` | `print_interval` | 204 | losses LSU output |
| `pw_lsu` | `print_interval` | 205 | plant weather LSU output HRU |
| `wb_hru` | `print_interval` | 207 | water balance HRU output |
| `nb_hru` | `print_interval` | 208 | nutrient balance HRU output |
| `ls_hru` | `print_interval` | 209 | losses HRU output |
| `pw_hru` | `print_interval` | 210 | plant weather HRU output |
| `cb_hru` | `print_interval` | 211 | legacy carbon flag (kept for backward compat with print.prt readers; no longer referenced by writers) |
| `cb_vars_hru` | `print_interval` | 212 | legacy carbon variable flag (same) per-family carbon output flags (10 rows) |
| `cb_gl_hru` | `print_interval` | 214 | hru_carb_gl_* HRU C gain/loss |
| `cb_trf_hru` | `print_interval` | 215 | hru_scf_* HRU C transformations |
| `cb_lyr_hru` | `print_interval` | 216 | hru_cbn_lyr_* per-layer SOC totals + sequestered |
| `cb_cpool_hru` | `print_interval` | 217 | hru_cpool_stat_* per-layer C pools |
| `cb_npool_hru` | `print_interval` | 218 | hru_n_p_pool_stat_* per-layer N+P pools |
| `cb_plt_hru` | `print_interval` | 219 | hru_plc_stat_* plant C state |
| `cb_flux_hru` | `print_interval` | 220 | hru_cflux_stat_* per-layer flux diagnostic |
| `cb_drv_hru` | `print_interval` | 221 | hru_carb_drv_* per-layer drivers diagnostic |
| `cb_dyn_hru` | `print_interval` | 222 | hru_carb_dyn_* per-layer dynamics diagnostic |
| `cb_snap_hru` | `print_interval` | 223 | hru_soil_snap_* soil property snapshot LSU-level area-weighted aggregations (Option 1: HRU-aggregated families only) |
| `cb_gl_lsu` | `print_interval` | 225 | lsu_carb_gl_* LSU-area-weighted C gain/loss |
| `cb_trf_lsu` | `print_interval` | 226 | lsu_scf_* LSU-area-weighted C transformations |
| `cb_plt_lsu` | `print_interval` | 227 | lsu_plc_stat_* LSU-area-weighted plant C state HRU-LTE |
| `wb_sd` | `print_interval` | 229 | water balance SWAT-DEG output |
| `nb_sd` | `print_interval` | 230 | nutrient balance SWAT-DEG output |
| `ls_sd` | `print_interval` | 231 | losses SWAT-DEG output |
| `pw_sd` | `print_interval` | 232 | plant weather SWAT-DEG output CHANNEL |
| `chan` | `print_interval` | 234 | channel output CHANNEL_LTE |
| `sd_chan` | `print_interval` | 236 | swat deg (lte) channel output AQUIFER |
| `aqu` | `print_interval` | 238 | aqufier output RESERVOIR |
| `res` | `print_interval` | 240 | reservoir output RECALL |
| `recall` | `print_interval` | 242 | recall output HYDIN AND HYDOUT |
| `hyd` | `print_interval` | 244 | hydin_output and hydout_output |
| `ru` | `print_interval` | 245 |  |
| `pest` | `print_interval` | 246 | all constituents pesticide output files (hru, chan, res, basin_chan, basin_res, basin_ls SALT (rtb salt) |
| `salt_basin` | `print_interval` | 249 | salt output for the basin |
| `salt_hru` | `print_interval` | 250 | salt output for HRUs |
| `salt_ru` | `print_interval` | 251 | salt output for routing units |
| `salt_aqu` | `print_interval` | 252 | salt output for aquifers |
| `salt_chn` | `print_interval` | 253 | salt output for channels |
| `salt_res` | `print_interval` | 254 | salt output for reservoirs |
| `salt_wet` | `print_interval` | 255 | salt output for reservoirs CONSTITUENTS (rtb cs) |
| `cs_basin` | `print_interval` | 257 | constituent output for the basin |
| `cs_hru` | `print_interval` | 258 | constituent output for HRUs |
| `cs_ru` | `print_interval` | 259 | constituent output for routing units |
| `cs_aqu` | `print_interval` | 260 | constituent output for aquifers |
| `cs_chn` | `print_interval` | 261 | constituent output for channels |
| `cs_res` | `print_interval` | 262 | constituent output for reservoirs |
| `cs_wet` | `print_interval` | 263 | constituent output for reservoirs |
| `gwflow_wb` | `print_interval` | 264 | gwflow cell + basin water balance (day/mon/yr/aa) |
| `gwflow_flux` | `print_interval` | 265 | gwflow canal, pond, tile, gwsw, chan obs diagnostic output |
| `gwflow_heat` | `print_interval` | 266 | gwflow basin heat balance output |
| `gwflow_solute` | `print_interval` | 267 | gwflow basin solute balance output |
| `gwflow_obs` | `print_interval` | 268 | gwflow observation well output |
| `gwflow_pump` | `print_interval` | 269 | gwflow HRU pumping output |

### basin_sediment_budget

- **Defined in source**: `basin_module.f90:275`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `upland_t` | `real` | 276 | total upland sediment yield - all land uses - tons |
| `ch_ebank_t` | `real` | 277 | total bank erosion - all stream orders - tons |
| `up_ch_rto` | `real` | 278 | upland/channel ratio |
| `ch_w_yr` | `real` | 279 | basin average widths per year |
| `fp_dep_t` | `real` | 280 | total flood plain deposition - stream orders - tons |
| `fp_dep_mm` | `real` | 281 | basin flood plain deposition - mm/year |
| `res_dep_t` | `real` | 282 | total reservoir deposition - all reservoirs - tons |
| `res_trap_eff` | `real` | 283 | average reservoir trap efficiency - all reservoirs |

### mgt_header

- **Defined in source**: `basin_module.f90:287`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru` | `character (len=12)` | 288 |  |
| `year` | `character (len=12)` | 289 |  |
| `mon` | `character (len=12)` | 290 |  |
| `day` | `character (len=11)` | 291 |  |
| `crop` | `character (len=15)` | 292 |  |
| `oper` | `character (len=12)` | 293 |  |
| `phub` | `character (len=12)` | 294 |  |
| `phua` | `character (len=11)` | 295 |  |
| `sw` | `character (len=12)` | 296 |  |
| `bio` | `character (len=17)` | 297 |  |
| `rsd` | `character (len=11)` | 298 |  |
| `solno3` | `character (len=15)` | 299 |  |
| `solp` | `character (len=15)` | 300 |  |
| `op_var` | `character (len=15)` | 301 |  |
| `var1` | `character (len=15)` | 302 |  |
| `var2` | `character (len=14)` | 303 |  |
| `var3` | `character (len=17)` | 304 |  |
| `var4` | `character (len=17)` | 305 |  |
| `var5` | `character (len=16)` | 306 |  |
| `var6` | `character (len=16)` | 307 |  |
| `var7` | `character (len=16)` | 308 |  |

### mgt_header_unit1

- **Defined in source**: `basin_module.f90:312`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru` | `character (len=12)` | 313 |  |
| `year` | `character (len=12)` | 314 |  |
| `mon` | `character (len=12)` | 315 |  |
| `day` | `character (len=12)` | 316 |  |
| `crop` | `character (len=11)` | 317 |  |
| `oper` | `character (len=13)` | 318 |  |
| `phub` | `character (len=9)` | 319 |  |
| `phua` | `character (len=16)` | 320 |  |
| `sw` | `character (len=12)` | 321 |  |
| `bio` | `character (len=17)` | 322 |  |
| `rsd` | `character (len=11)` | 323 |  |
| `solno3` | `character (len=15)` | 324 |  |
| `solp` | `character (len=15)` | 325 |  |
| `op_var` | `character (len=15)` | 326 |  |
| `var1` | `character (len=16)` | 327 |  |
| `var2` | `character (len=15)` | 328 |  |
| `var3` | `character (len=16)` | 329 |  |
| `var4` | `character (len=16)` | 330 |  |
| `var5` | `character (len=16)` | 331 |  |
| `var6` | `character (len=16)` | 332 |  |
| `var7` | `character (len=15)` | 333 |  |

### basin_yld_header

- **Defined in source**: `basin_module.f90:430`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `year` | `character (len=11)` | 431 |  |
| `plant_no` | `character (len=16)` | 432 |  |
| `plant_name` | `character (len=16)` | 433 |  |
| `area_ha` | `character (len=17)` | 434 |  |
| `yield_t` | `character (len=17)` | 435 |  |
| `yield_tha` | `character (len=16)` | 436 |  |

## Variables Defined
### prog

- **Type**: `character(len=80)`
- **Defined in source**: `basin_module.f90:5`

### ban_precip_aa

- **Type**: `real`
- **Defined in source**: `basin_module.f90:7`

### bsn

- **Type**: `basin_inputs`
- **Defined in source**: `basin_module.f90:14`

### bsn_cc

- **Type**: `basin_control_codes`
- **Defined in source**: `basin_module.f90:77`

### bsn_prm

- **Type**: `basin_parms`
- **Defined in source**: `basin_module.f90:138`

### pco

- **Type**: `basin_print_codes`
- **Defined in source**: `basin_module.f90:271`

### pco_init

- **Type**: `basin_print_codes`
- **Defined in source**: `basin_module.f90:272`

### bsn_sedbud

- **Type**: `basin_sediment_budget`
- **Defined in source**: `basin_module.f90:285`

### mgt_hdr

- **Type**: `mgt_header`
- **Defined in source**: `basin_module.f90:310`

### mgt_hdr_unt1

- **Type**: `mgt_header_unit1`
- **Defined in source**: `basin_module.f90:335`

### bsn_yld_hdr

- **Type**: `basin_yld_header`
- **Defined in source**: `basin_module.f90:438`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### print_prt_error

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/module
  - swat/to-read
file: calibration_data_module.f90
note_file: calibration_data_module.f90
module_name: calibration_data_module
defines_types:
  - calibration_parameters
  - calibration_conditions
  - update_parameters
  - update_conditional
  - soft_calibration_codes
  - soft_calib_parms
  - soft_calib_ls_adjust
  - soft_calib_ls_processes
  - ls_calib_regions
  - soft_data_calib_landscape
  - pl_parms_cal
  - pl_parm_region
  - cataloging_units
  - landscape_units
  - landscape_region_elements
  - landscape_elements
  - soft_calib_pl_adjust
  - soft_calib_pl_processes
  - pl_calib_regions
  - soft_data_calib_plant
  - soft_calib_chan_adjust
  - soft_calib_chan_processes
  - chan_calib_regions
  - soft_data_calib_channel
defines_vars:
  - cal_parms
  - cal_upd
  - chg
  - upd_cond
  - cal_codes
  - cal_soft
  - cal_hard
  - ls_prms
  - ch_prms
  - lscal_z
  - lscal
  - lscalt
  - pl_prms
  - region
  - ccu_cal
  - acu_cal
  - rcu_cal
  - pcu_cal
  - lsu_out
  - lsu_reg
  - acu_out
  - acu_reg
  - ccu_out
  - ccu_reg
  - rcu_out
  - rcu_reg
  - pcu_out
  - pcu_reg
  - reg_elem
  - lsu_elem
  - ccu_elem
  - acu_elem
  - rcu_elem
  - pcu_elem
  - plcal_z
  - plcal
  - chcal_z
  - chcal
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# calibration_data_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### calibration_parameters

- **Defined in source**: `calibration_data_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 6 | \|cn2, esco, awc, etc. |
| `ob_typ` | `character(len=25)` | 7 | \|object type the parameter is associated with (hru, chan, res, basin, etc) |
| `absmin` | `real` | 8 | \|minimum range for variable |
| `absmax` | `real` | 9 | \|maximum change for variable |
| `units` | `character(len=25)` | 10 | \|units used for each parameter |

### calibration_conditions

- **Defined in source**: `calibration_data_module.f90:14`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `var` | `character(len=25)` | 15 |  |
| `alt` | `character(len=25)` | 16 |  |
| `targ` | `real` | 17 |  |
| `targc` | `character(len=25)` | 18 |  |

### update_parameters

- **Defined in source**: `calibration_data_module.f90:21`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 22 | cn2, terrace, land use, mgt, etc. |
| `num_db` | `integer` | 23 | crosswalk number of parameter, structure or land use to get database array number |
| `chg_typ` | `character(len=16)` | 24 | type of change (absval,abschg,pctchg) |
| `val` | `real` | 25 | value of change |
| `val1` | `real` | 26 | lower bound of numerical condition |
| `val2` | `real` | 27 | upper bound of numerical condition |
| `conds` | `integer` | 28 | number of conditions |
| `lyr1` | `integer` | 29 | first layer in range for soil variables (0 assumes all layers are modified) |
| `lyr2` | `integer` | 30 | last layer in range for soil variables (0 assumes through last layer) |
| `year1` | `integer` | 31 | first year for precip and temp |
| `year2` | `integer` | 32 | last year for precip and temp |
| `day1` | `integer` | 33 | first day in range for precip and temp |
| `day2` | `integer` | 34 | last day in range for precip and temp |
| `num_tot` | `integer` | 35 | total number of integers read in |
| `num_elem` | `integer` | 36 | total number of elements modified (ie - 1 -5 18; num_tot=3 and num_elem=6) |
| `num` | `integer, dimension(:), allocatable` | 37 |  |
| `num_cond` | `integer` | 38 |  |
| `cond` | `calibration_conditions` | 39 |  |

### update_conditional

- **Defined in source**: `calibration_data_module.f90:45`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `max_hits` | `integer` | 46 | maximum number of times the table will be executed |
| `num_hits` | `integer` | 47 | current number of times the table will be executed |
| `typ` | `character(len=25)` | 48 | type of table- "lu_change" checks all hru; "hru_fr_change" sets all hru fractions |
| `dtbl` | `character(len=25)` | 49 | points to ruleset in conditional.ctl for scheduling the update |
| `cond_num` | `integer` | 50 | integer pointer to d_table in conditional.ctl |

### soft_calibration_codes

- **Defined in source**: `calibration_data_module.f90:54`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hyd_hru` | `character (len=1)` | 55 | if a, calibrate all hydrologic balance processes for hru by land use in each region if b, calibrate baseflow and total runoff for hru by land use in each region if y, defaults to b for existing NAM simulations |
| `hyd_hrul` | `character (len=1)` | 58 | if y, calibrate hydrologic balance for hru_lte by land use in each region |
| `plt` | `character (len=1)` | 59 | if y, calibrate plant growth by land use (by plant) in each region |
| `sed` | `character (len=1)` | 60 | if y, calibrate sediment yield by land use in each region |
| `nut` | `character (len=1)` | 61 | if y, calibrate nutrient balance by land use in each region |
| `chsed` | `character (len=1)` | 62 | if y, calibrate channel widening and bank accretion by stream order |
| `chnut` | `character (len=1)` | 63 | if y, calibrate channel nutrient balance by stream order |
| `res` | `character (len=1)` | 64 | if y, calibrate reservoir budgets by reservoir |

### soft_calib_parms

- **Defined in source**: `calibration_data_module.f90:70`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 71 | cn2, terrace, land use, mgt, etc. |
| `num_db` | `integer` | 72 | crosswalk number of parameter, structure or land use to get database array number |
| `chg_typ` | `character(len=16)` | 73 | type of change (absval,abschg,pctchg) |
| `neg` | `real` | 74 | negative limit of change |
| `pos` | `real` | 75 | positive limit of change |
| `lo` | `real` | 76 | lower limit of parameter |
| `up` | `real` | 77 | upper limit of parameter |

### soft_calib_ls_adjust

- **Defined in source**: `calibration_data_module.f90:82`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cn` | `real` | 83 | +/- or 0/1 \|cn2 adjustment or at limit |
| `esco` | `real` | 84 | +/- or 0/1 \|esco adjustment or at limit |
| `lat_len` | `real` | 85 | +/- or 0/1 \|lateral flow soil length adjustment or at limit |
| `petco` | `real` | 86 | +/- or 0/1 \|k (lowest layer) adjustment or at limit |
| `slope` | `real` | 87 | +/- or 0/1 \|slope adjustment or at limit |
| `tconc` | `real` | 88 | +/- or 0/1 \|time of concentration adjustment or at limit |
| `etco` | `real` | 89 | +/- or 0/1 \|etco adjustment or at limit |
| `perco` | `real` | 90 | +/- or 0/1 \|percolation coefficient adjustment or at limit |
| `revapc` | `real` | 91 | +/- or 0/1 \|slope adjustment or at limit |
| `cn3_swf` | `real` | 92 | +/- or 0/1 \|cn3_swf adjustment or at limit |

### soft_calib_ls_processes

- **Defined in source**: `calibration_data_module.f90:95`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 97 | srr + lfr + pcr + etr + tfr = 1 |
| `srr` | `real` | 99 | - or m3 \|surface runoff ratio - surface runoff/precip |
| `lfr` | `real` | 100 | - or m3 \|lateral flow ratio - soil lat flow/precip |
| `pcr` | `real` | 101 | - or m3 \|percolation ratio - perc/precip |
| `etr` | `real` | 102 | - or m3 \|et ratio - et/precip |
| `tfr` | `real` | 103 | - or m3 \|tile flow ratio - tile flow/total runoff |
| `pet` | `real` | 104 | - or m3 \|ave annual potential et |
| `sed` | `real` | 105 | t/ha or t \|sediment yield |
| `wyr` | `real` | 107 | - or m3 \|water yield ratio - total water yield/precip |
| `bfr` | `real` | 108 | - or m3 \|base flow ratio - base flow/precip - lat+prec+tile |
| `solp` | `real` | 109 | kg/ha or kg \|soluble p yield |

### ls_calib_regions

- **Defined in source**: `calibration_data_module.f90:113`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 114 |  |
| `lum_no` | `integer` | 115 | xwalk lum()%name with lscal()%lum()%name |
| `ha` | `real` | 116 | ha of each land use |
| `nbyr` | `integer` | 117 | number of years the land use occurred |
| `meas` | `soft_calib_ls_processes` | 118 | input soft calibration parms of each land use - ratio,t/ha,kg/ha |
| `precip` | `real` | 119 | model precip for each land use to determine ratios |
| `precip_aa` | `real` | 120 | model ave annual precip for each land use to determine ratios |
| `precip_aa_sav` | `real` | 121 | model ave annual precip for each land use to determine ratios for final output |
| `pet` | `real` | 122 | model precip for each land use to determine ratios |
| `pet_aa` | `real` | 123 | model ave annual precip for each land use to determine ratios |
| `petco` | `real` | 124 | potential et coefficient - linear adjustment, no iterating |
| `sim` | `soft_calib_ls_processes` | 125 | simulated sum of soft calibration parms of each land use - m3,t,kg |
| `aa` | `soft_calib_ls_processes` | 126 | average annual soft calibration parms of each land use - mm,t/ha,kg/ha |
| `prev` | `soft_calib_ls_processes` | 127 | simulated sum of soft calibration parms of previous run - m3,t,kg |
| `prm` | `soft_calib_ls_adjust` | 128 | parameter adjustments used in landscape calibration |
| `prm_prev` | `soft_calib_ls_adjust` | 129 | parameter adjustments used in landscape calibration |
| `prm_lim` | `soft_calib_ls_adjust` | 130 | code if parameters are at limits |
| `pcur` | `soft_calib_ls_adjust` | 131 | current parameter |
| `phi` | `soft_calib_ls_adjust` | 132 | high parameter |
| `plo` | `soft_calib_ls_adjust` | 133 | low parameter |
| `scur` | `soft_calib_ls_processes` | 134 | simulated sum of soft calibration parms of each land use - m3,t,kg |
| `shi` | `soft_calib_ls_processes` | 135 | average annual soft calibration parms of each land use - mm,t/ha,kg/ha |
| `slo` | `soft_calib_ls_processes` | 136 | simulated sum of soft calibration parms of previous run - m3,t,kg |

### soft_data_calib_landscape

- **Defined in source**: `calibration_data_module.f90:140`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 141 | name of region - (number of regions = db_mx%lsu_reg) |
| `lum_num` | `integer` | 142 | number of land uses in each region |
| `num_tot` | `integer` | 143 | number of hru"s in each region |
| `num` | `integer, dimension(:), allocatable` | 144 | hru"s that are included in the region |
| `num_reg` | `integer` | 145 | number of regions the soft data applies to |
| `reg` | `character(len=16), dimension(:), allocatable` | 146 | name of regions the soft data applies to |
| `ireg` | `integer, dimension(:), allocatable` | 147 | name of regions the soft data applies to |
| `lum` | `ls_calib_regions` | 148 | dimension for land uses within a region |

### pl_parms_cal

- **Defined in source**: `calibration_data_module.f90:153`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `var` | `character(len=16)` | 154 |  |
| `name` | `character(len=16)` | 155 |  |
| `init_val` | `real` | 156 | xwalk lum()%name with lscal()%lum()%name |
| `chg_typ` | `character(len=16)` | 157 | type of change (absval,abschg,pctchg) |
| `neg` | `real` | 158 | negative limit per iteration |
| `pos` | `real` | 159 | positive limit per iteration |
| `lo` | `real` | 160 | ultimate lower limit of parameter |
| `up` | `real` | 161 | ultimate upper limit of parameter |

### pl_parm_region

- **Defined in source**: `calibration_data_module.f90:164`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 165 | name of region - (number of regions = db_mx%lsu_reg) |
| `lum_num` | `integer` | 166 | number of land uses in each region |
| `parms` | `integer` | 167 | number of plant parameters used in calibration |
| `num_tot` | `integer` | 168 | number of hru"s in each region |
| `num` | `integer, dimension(:), allocatable` | 169 | hru"s that are included in the region |
| `prm` | `pl_parms_cal` | 170 | dimension for land uses within a region |

### cataloging_units

- **Defined in source**: `calibration_data_module.f90:174`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 175 | name of region - (number of regions = db_mx%lsu_reg) |
| `area_ha` | `real` | 176 | area of landscape cataloging unit -hectares |
| `num_tot` | `integer` | 177 | number of hru"s in each region |
| `num` | `integer, dimension(:), allocatable` | 178 | hru"s that are included in the region |
| `nlum` | `integer` | 179 | number of land use and mgt in the region |
| `lumc` | `character(len=16), dimension(:), allocatable` | 180 | land use groups |
| `lum_num` | `integer, dimension(:), allocatable` | 181 | db number of land use in the region - dimensioned by lum in the region |
| `lum_num_tot` | `integer, dimension(:), allocatable` | 182 | db number of land use in the region each year- dimensioned by lum in database |
| `lum_ha` | `real, dimension(:), allocatable` | 183 | area (ha) of land use in the region - dimensioned by lum in the region |
| `lum_ha_tot` | `real, dimension(:), allocatable` | 184 | sum of area (ha) of land use in the region each year- dimensioned by lum in database |
| `hru_ha` | `real, dimension(:), allocatable` | 185 | area (ha) of hrus in the region |

### landscape_units

- **Defined in source**: `calibration_data_module.f90:193`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 194 | name of region - (number of regions = db_mx%lsu_out) |
| `area_ha` | `real` | 195 | area of landscape cataloging unit -hectares |
| `num_tot` | `integer` | 196 | number of hru"s in each region |
| `num` | `integer, dimension(:), allocatable` | 197 | hru"s that are included in the region |

### landscape_region_elements

- **Defined in source**: `calibration_data_module.f90:210`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 211 |  |
| `ha` | `real` | 212 | area of region element -hectares |
| `obj` | `integer` | 213 | object number |
| `obtyp` | `character (len=3)` | 214 | object type- hru, hru_lte, lsu, etc |
| `obtypno` | `integer` | 215 | 2-number of hru_lte"s or 1st hru_lte command |

### landscape_elements

- **Defined in source**: `calibration_data_module.f90:219`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 220 |  |
| `obj` | `integer` | 221 | object number |
| `obtyp` | `character (len=3)` | 222 | object type- 1=hru, 2=hru_lte, 11=export coef, etc |
| `obtypno` | `integer` | 223 | 2-number of hru_lte"s or 1st hru_lte command |
| `bsn_frac` | `real` | 224 | fraction of element in basin (expansion factor) |
| `ru_frac` | `real` | 225 | fraction of element in ru (expansion factor) |
| `reg_frac` | `real` | 226 | fraction of element in calibration region (expansion factor) |

### soft_calib_pl_adjust

- **Defined in source**: `calibration_data_module.f90:234`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `epco` | `real` | 235 | +/- or 0/1 \|\|plant water uptake compensation factor (0-1) |
| `pest_stress` | `real` | 236 | +/- or 0/1 \|pest stress - insect/disease |
| `harv_idx` | `real` | 237 | +/- or 0/1 \|harvest index |
| `lai_pot` | `real` | 238 | +/- or 0/1 \|potential leaf area index |

### soft_calib_pl_processes

- **Defined in source**: `calibration_data_module.f90:241`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 243 |  |
| `yield` | `real` | 244 | t/ha or t \|crop yield |
| `npp` | `real` | 245 | t/ha or t \|net primary productivity (biomass) dry weight |
| `lai_mx` | `real` | 246 | \|maximum leaf area index |
| `wstress` | `real` | 247 | \|sum of water (drought) stress |
| `astress` | `real` | 248 | \|sum of water (aeration) stress |
| `tstress` | `real` | 249 | \|sum of temperature stress |

### pl_calib_regions

- **Defined in source**: `calibration_data_module.f90:253`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 254 |  |
| `plant_no` | `integer` | 255 | xwalk lum()%name with lscal()%lum()%name |
| `ha` | `real` | 256 | ha of each land use |
| `nbyr` | `integer` | 257 | number of years the land use occurred |
| `meas` | `soft_calib_pl_processes` | 258 | input soft calibration parms of each land use - ratio,t/ha,kg/ha |
| `precip` | `real` | 259 | model precip for each land use to determine ratios |
| `precip_aa` | `real` | 260 | model ave annual precip for each land use to determine ratios |
| `precip_aa_sav` | `real` | 261 | model ave annual precip for each land use to determine ratios for final output |
| `sim` | `soft_calib_pl_processes` | 262 | simulated sum of soft calibration parms of each land use - m3,t,kg |
| `aa` | `soft_calib_pl_processes` | 263 | average annual soft calibration parms of each land use - mm,t/ha,kg/ha |
| `prev` | `soft_calib_pl_processes` | 264 | simulated sum of soft calibration parms of previous run - m3,t,kg |
| `prm` | `soft_calib_pl_adjust` | 265 | parameter adjustments used in landscape calibration |
| `prm_prev` | `soft_calib_pl_adjust` | 266 | parameter adjustments used in landscape calibration |
| `prm_lim` | `soft_calib_pl_adjust` | 267 | code if parameters are at limits |
| `prm_uplim` | `soft_calib_pl_adjust` | 268 | parameter adjustments used in landscape calibration |
| `prm_lowlim` | `soft_calib_pl_adjust` | 269 | code if parameters are at limits |

### soft_data_calib_plant

- **Defined in source**: `calibration_data_module.f90:272`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 273 | name of region - (number of regions = db_mx%lsu_reg) |
| `lum_num` | `integer` | 274 | number of land uses in each region |
| `num_tot` | `integer` | 275 | number of hru"s in each region |
| `num` | `integer, dimension(:), allocatable` | 276 | hru"s that are included in the region |
| `lum` | `pl_calib_regions` | 277 | dimension for land uses within a region |

### soft_calib_chan_adjust

- **Defined in source**: `calibration_data_module.f90:281`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cov` | `real` | 282 | +/- or 0/1 \|cover adjustment or at limit |
| `erod` | `real` | 283 | +/- or 0/1 \|channel erodibility adjustment or at limit |
| `shear_bnk` | `real` | 284 | +/- or 0/1 \|bank shear coefficient adjustment or at limit |
| `hc_erod` | `real` | 285 | +/- or 0/1 \|head cut erodibility adjustment or at limit |

### soft_calib_chan_processes

- **Defined in source**: `calibration_data_module.f90:288`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 290 |  |
| `chw` | `real` | 291 | mm/yr \|channel widening |
| `chd` | `real` | 292 | mm/yr \|channel downcutting or accretion |
| `hc` | `real` | 293 | m/yr \|head cut advance |
| `fpd` | `real` | 294 | mm/yr \|flood plain accretion |

### chan_calib_regions

- **Defined in source**: `calibration_data_module.f90:298`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 299 |  |
| `length` | `real` | 300 | ha of each land use |
| `nbyr` | `integer` | 301 | number of years the land use occurred |
| `meas` | `soft_calib_chan_processes` | 302 | input soft calibration parms of each land use - ratio,t/ha,kg/ha |
| `sim` | `soft_calib_chan_processes` | 303 | simulated sum of soft calibration parms of each land use - m3,t,kg |
| `aa` | `soft_calib_chan_processes` | 304 | average annual soft calibration parms of each land use - mm,t/ha,kg/ha |
| `prev` | `soft_calib_chan_processes` | 305 | simulated sum of soft calibration parms of previous run - m3,t,kg |
| `prm` | `soft_calib_chan_adjust` | 306 | parameter adjustments used in landscape calibration |
| `prm_prev` | `soft_calib_chan_adjust` | 307 | parameter adjustments used in landscape calibration |
| `prm_lim` | `soft_calib_chan_adjust` | 308 | code if parameters are at limits |

### soft_data_calib_channel

- **Defined in source**: `calibration_data_module.f90:311`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 312 | name of region - (number of regions = db_mx%lsu_reg) |
| `ord_num` | `integer` | 313 | number of stream orders in each region |
| `num_tot` | `integer` | 314 | number of channels in each region |
| `num` | `integer, dimension(:), allocatable` | 315 | channels that are included in the region |
| `ord` | `chan_calib_regions` | 316 | dimension for stream order within a region |

## Variables Defined
### cal_parms

- **Type**: `calibration_parameters`
- **Defined in source**: `calibration_data_module.f90:12`
- **Source note**: dimensioned to db_mx%cal_parms_tot

### cal_upd

- **Type**: `update_parameters`
- **Defined in source**: `calibration_data_module.f90:42`
- **Source note**: dimensioned to db_mx%cal_parms

### chg

- **Type**: `update_parameters`
- **Defined in source**: `calibration_data_module.f90:43`

### upd_cond

- **Type**: `update_conditional`
- **Defined in source**: `calibration_data_module.f90:52`

### cal_codes

- **Type**: `soft_calibration_codes`
- **Defined in source**: `calibration_data_module.f90:66`

### cal_soft

- **Type**: `character (len=1)`
- **Defined in source**: `calibration_data_module.f90:67`
- **Source note**: if y, calibrate at least one balance

### cal_hard

- **Type**: `character (len=1)`
- **Defined in source**: `calibration_data_module.f90:68`
- **Source note**: if y, perform hard calibration

### ls_prms

- **Type**: `soft_calib_parms`
- **Defined in source**: `calibration_data_module.f90:79`

### ch_prms

- **Type**: `soft_calib_parms`
- **Defined in source**: `calibration_data_module.f90:80`

### lscal_z

- **Type**: `soft_calib_ls_processes`
- **Defined in source**: `calibration_data_module.f90:111`
- **Source note**: to zero values

### lscal

- **Type**: `soft_data_calib_landscape`
- **Defined in source**: `calibration_data_module.f90:150`
- **Source note**: dimension by region for hru"s

### lscalt

- **Type**: `soft_data_calib_landscape`
- **Defined in source**: `calibration_data_module.f90:151`
- **Source note**: dimension by region for hru_lte"s

### pl_prms

- **Type**: `pl_parm_region`
- **Defined in source**: `calibration_data_module.f90:172`
- **Source note**: dimension by region for hru"s

### region

- **Type**: `cataloging_units`
- **Defined in source**: `calibration_data_module.f90:187`
- **Source note**: dimension by region for hru"s

### ccu_cal

- **Type**: `cataloging_units`
- **Defined in source**: `calibration_data_module.f90:188`
- **Source note**: channel cataoging unit region

### acu_cal

- **Type**: `cataloging_units`
- **Defined in source**: `calibration_data_module.f90:189`
- **Source note**: aquifer cataoging unit region

### rcu_cal

- **Type**: `cataloging_units`
- **Defined in source**: `calibration_data_module.f90:190`
- **Source note**: reservoir cataoging unit region

### pcu_cal

- **Type**: `cataloging_units`
- **Defined in source**: `calibration_data_module.f90:191`
- **Source note**: point source cataoging unit region

### lsu_out

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:199`
- **Source note**: dimension by region for hrus

### lsu_reg

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:200`
- **Source note**: dimension by region for hrus

### acu_out

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:201`
- **Source note**: dimension by region for aquifers

### acu_reg

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:202`
- **Source note**: dimension by region for aquifers

### ccu_out

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:203`
- **Source note**: dimension by region for channels

### ccu_reg

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:204`
- **Source note**: dimension by region for channels

### rcu_out

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:205`
- **Source note**: dimension by region for reservoirs

### rcu_reg

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:206`
- **Source note**: dimension by region for reservoirs

### pcu_out

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:207`
- **Source note**: dimension by region for point sources

### pcu_reg

- **Type**: `landscape_units`
- **Defined in source**: `calibration_data_module.f90:208`
- **Source note**: dimension by region for point sources

### reg_elem

- **Type**: `landscape_region_elements`
- **Defined in source**: `calibration_data_module.f90:217`
- **Source note**: landscape region elements

### lsu_elem

- **Type**: `landscape_elements`
- **Defined in source**: `calibration_data_module.f90:228`
- **Source note**: landscape cataoging unit

### ccu_elem

- **Type**: `landscape_elements`
- **Defined in source**: `calibration_data_module.f90:229`
- **Source note**: channel cataoging unit

### acu_elem

- **Type**: `landscape_elements`
- **Defined in source**: `calibration_data_module.f90:230`
- **Source note**: aquifer cataoging unit

### rcu_elem

- **Type**: `landscape_elements`
- **Defined in source**: `calibration_data_module.f90:231`
- **Source note**: reservoir cataoging unit

### pcu_elem

- **Type**: `landscape_elements`
- **Defined in source**: `calibration_data_module.f90:232`
- **Source note**: point source cataoging unit

### plcal_z

- **Type**: `soft_calib_pl_processes`
- **Defined in source**: `calibration_data_module.f90:251`
- **Source note**: to zero values

### plcal

- **Type**: `soft_data_calib_plant`
- **Defined in source**: `calibration_data_module.f90:279`
- **Source note**: dimension by region for plants

### chcal_z

- **Type**: `soft_calib_chan_processes`
- **Defined in source**: `calibration_data_module.f90:296`
- **Source note**: to zero values

### chcal

- **Type**: `soft_data_calib_channel`
- **Defined in source**: `calibration_data_module.f90:318`
- **Source note**: dimension by region

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

---
type: module
tags:
  - swat/module
  - swat/to-read
file: sd_channel_module.f90
note_file: sd_channel_module.f90
module_name: sd_channel_module
defines_types:
  - swatdeg_hydsed_data
  - swatdeg_sednut_data
  - channel_sediment_budget_output
  - channel_morphology_output
  - gully_data
  - swatdeg_init_datafiles
  - swatdeg_datafiles
  - floodplain_parameters
  - muskingum_parameters
  - swatdeg_channel_dynamic
  - channel_rating_curve_parameters
  - channel_rating_curve
  - sd_ch_output
  - sdch_header
  - sdch_header_units
  - sdch_bud
  - sdch_bud_units
  - sdch_header_sub
  - sdch_header_units_sub
  - sd_chd_header
defines_vars:
  - maxint
  - wtemp
  - peakrate
  - sed_reduc_t
  - no3_reduc_kg
  - tp_reduc_kg
  - tp_reduc
  - srp_reduc_kg
  - hyd_rad
  - trav_time
  - flo_dep
  - timeint
  - sd_chd
  - sd_chd1
  - ch_sed_bud
  - ch_sed_bud_m
  - ch_sed_bud_y
  - ch_sed_bud_a
  - ch_sed_budz
  - bch_sed_bud_d
  - bch_sed_bud_m
  - bch_sed_bud_y
  - bch_sed_bud_a
  - ch_morph
  - ch_morph_ord
  - gully
  - sd_init
  - sd_dat
  - sd_ch
  - sdch_init
  - rcurv
  - rcz
  - ch_rcurv
  - chsd_d
  - chsd_m
  - chsd_y
  - chsd_a
  - schsd_d
  - schsd_m
  - schsd_y
  - schsd_a
  - bchsd_d
  - bchsd_m
  - bchsd_y
  - bchsd_a
  - chsdz
  - sdch_hdr
  - sdch_hdr_units
  - sdch_bud_hdr
  - sdch_bud_hdr_units
  - sdch_hdr_subday
  - sdch_hdr_units_sub
  - sd_chd_hdr
defines_subroutines:
  - chrc_interp
defines_functions:
  - chsednut_add
  - chsednut_div
  - chsd_add
  - chsd_div
  - chsd_ave
  - chsd_mult
  - chrc_mult
defines_procedures:
  - chrc_interp
  - chsednut_add
  - chsednut_div
  - chsd_add
  - chsd_div
  - chsd_ave
  - chsd_mult
  - chrc_mult
purpose: ""
---

# sd_channel_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### swatdeg_hydsed_data

- **Defined in source**: `sd_channel_module.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 19 |  |
| `order` | `integer` | 20 |  |
| `chw` | `real` | 21 | m \|channel width |
| `chd` | `real` | 22 | m \|channel depth |
| `chs` | `real` | 23 | m/m \|channel slope |
| `chl` | `real` | 24 | km \|channel length |
| `chn` | `real` | 25 | \|channel Manning's n |
| `chk` | `real` | 26 | mm/h \|channel bottom conductivity |
| `bank_exp` | `real` | 27 | \|bank erosion exponent |
| `cov` | `real` | 28 | 0-1 \|channel cover factor |
| `sinu` | `real` | 29 | none \|sinuousity - ratio of channel length and straight line length |
| `vcr_coef` | `real` | 30 | \|critical velocity coefficient |
| `d50` | `real` | 31 | mm \|channel median sediment size |
| `ch_clay` | `real` | 32 | % \|clay percent of bank and bed |
| `carbon` | `real` | 33 | % \|carbon percent of bank and bed |
| `ch_bd` | `real` | 34 | t/m3 \|dry bulk density |
| `chss` | `real` | 35 | \|channel side slope |
| `bankfull_flo` | `real` | 36 | \|bank full flow rate |
| `fps` | `real` | 37 | m/m \|flood plain slope |
| `fpn` | `real` | 38 | \|flood plain Manning's n |
| `n_conc` | `real` | 39 | mg/kg \|nitrogen concentration in channel bank |
| `p_conc` | `real` | 40 | mg/kg \|phosphorus concentration in channel bank |
| `p_bio` | `real` | 41 | frac \|fraction of p in bank that is bioavailable |

### swatdeg_sednut_data

- **Defined in source**: `sd_channel_module.f90:45`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 46 |  |
| `order` | `character(len=16)` | 47 |  |
| `pk_rto` | `real` | 48 | ratio \|ratio of peak to mean daily flow in channel |
| `fp_inun_days` | `real` | 49 | days \|number of days fllod plain is inundated after flood |
| `n_setl` | `real` | 50 | ratio \|ratio of amount of N settling and sediment settling |
| `p_setl` | `real` | 51 | ratio \|ratio of amount of P settling and sediment settling |
| `n_sol_part` | `real` | 52 | \|instream nitrogen soluble to particulate transformation coefficient |
| `p_sol_part` | `real` | 53 | \|instream phosphorus soluble to particulate transformation coefficient |
| `n_dep_enr` | `real` | 54 | \|enrichment of N in remaining water - deposition = 1/enrichment ratio |
| `p_dep_enr` | `real` | 55 | \|enrichment of P in remaining water - deposition = 1/enrichment ratio |
| `arc_len_fr` | `real` | 56 | frac \|fraction of arc length where bank erosion occurs |
| `bed_exp` | `real` | 57 | \|bed erosion exponential coefficient |
| `wash_bed_fr` | `real` | 58 | frac \|fraction of bank erosion that is washload |

### channel_sediment_budget_output

- **Defined in source**: `sd_channel_module.f90:63`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `in_sed` | `real` | 64 | t \|incoming sediment to channel |
| `out_sed` | `real` | 65 | t \|outgoing sediment from channel |
| `fp_dep` | `real` | 66 | t \|flood plain deposition |
| `ch_dep` | `real` | 67 | t \|channel deposition |
| `bank_ero` | `real` | 68 | t \|channel bank erosion |
| `bed_ero` | `real` | 69 | t \|channel bed erosion |
| `in_no3` | `real` | 70 | t \|incoming no3 to channel |
| `in_orgn` | `real` | 71 | t \|incoming organic n to channel |
| `out_no3` | `real` | 72 | t \|outgoing no3 from channel |
| `out_orgn` | `real` | 73 | t \|outgoing organic n from channel |
| `fp_no3` | `real` | 74 | t \|flood plain no3 lost |
| `bank_no3` | `real` | 75 | t \|bank no3 gain |
| `bed_no3` | `real` | 76 | t \|bed no3 gain |
| `fp_orgn` | `real` | 77 | t \|flood plain organic n deposited |
| `ch_orgn` | `real` | 78 | t \|channel organic n deposited |
| `bank_orgn` | `real` | 79 | t \|bank organic n gain from erosion |
| `bed_orgn` | `real` | 80 | t \|bed organic n gain from erosion |
| `in_solp` | `real` | 81 | t \|incoming soluble p to channel |
| `in_orgp` | `real` | 82 | t \|incoming organic p to channel |
| `out_solp` | `real` | 83 | t \|outgoing soluble p from channel |
| `out_orgp` | `real` | 84 | t \|outgoing organic p from channel |
| `fp_solp` | `real` | 85 | t \|flood plain soluble p lost |
| `bank_solp` | `real` | 86 | t \|bank no3 gain |
| `bed_solp` | `real` | 87 | t \|bed no3 gain |
| `fp_orgp` | `real` | 88 | t \|flood plain organic p deposited |
| `ch_orgp` | `real` | 89 | t \|channel organic p deposited |
| `bank_orgp` | `real` | 90 | t \|bank organic p gain from erosion |
| `bed_orgp` | `real` | 91 | t \|bed organic n gain from erosion |
| `no3_orgn` | `real` | 92 | t \|in channel transformation from no3 to organic n |
| `solp_orgp` | `real` | 93 | t \|in channel transformation from no3 to organic n |

### channel_morphology_output

- **Defined in source**: `sd_channel_module.f90:99`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num` | `integer` | 100 | \|number of channels in each order |
| `w_yr` | `real` | 101 | ratio \|bank cutting - widths per year |
| `d_yr` | `real` | 102 | ratio \|bed down cutting - depths per year |
| `fp_mm` | `real` | 103 | mm/yr \|flood plain deposition - uniform across the flood plain |
| `ebank_m` | `real` | 104 | tons \|bank cutting |
| `ebtm_m` | `real` | 105 | m \|bed down cutting |
| `ebank_t` | `real` | 106 | tons \|bank cutting |
| `ebtm_t` | `real` | 107 | tons \|bed down cutting |
| `fp_t` | `real` | 108 | mm/yr \|flood plain deposition |

### gully_data

- **Defined in source**: `sd_channel_module.f90:113`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 114 |  |
| `hc_kh` | `real` | 115 | \|headcut erodibility |
| `hc_hgt` | `real` | 116 | m \|headcut height |
| `hc_ini` | `real` | 117 | km \|initial channel length for gullies |

### swatdeg_init_datafiles

- **Defined in source**: `sd_channel_module.f90:121`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init` | `integer` | 122 | initial data-points to initial.cha |
| `org_min` | `integer` | 123 | points to initial organic-mineral input file |
| `pest` | `integer` | 124 | points to initial pesticide input file |
| `path` | `integer` | 125 | points to initial pathogen input file |
| `hmet` | `integer` | 126 | points to initial heavy metals input file |
| `salt` | `integer` | 127 | points to initial salt input file (salt_channel.ini) (rtb salt) |
| `cs` | `integer` | 128 | points to initial constituent input file (cs_channel.ini) (rtb cs) |

### swatdeg_datafiles

- **Defined in source**: `sd_channel_module.f90:132`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 133 |  |
| `initc` | `character(len=16)` | 134 |  |
| `hydc` | `character(len=16)` | 135 |  |
| `sedc` | `character(len=16)` | 136 |  |
| `nutc` | `character(len=16)` | 137 |  |
| `init` | `integer` | 138 |  |
| `hyd` | `integer` | 139 |  |
| `sed` | `integer` | 140 |  |
| `nut` | `integer` | 141 |  |
| `sednut` | `integer` | 142 |  |

### floodplain_parameters

- **Defined in source**: `sd_channel_module.f90:146`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 147 | \|name of flood plain |
| `obj_tot` | `integer` | 148 | \|number of objects (hru and/or ru) in the flood plain |
| `hru_tot` | `integer` | 149 | \|number of hru in the flood plain |
| `ha` | `real` | 150 | ha \|sum of area of all hru in flood plain |
| `obtyp` | `character (len=3), dimension(:), allocatable` | 151 | object type- 1=hru, 2=hru_lte, 11=export coef, etc |
| `obtypno` | `integer, dimension(:), allocatable` | 152 | 2-number of hru_lte"s or 1st hru_lte command |
| `hru` | `integer, dimension (:), allocatable` | 153 | \|flood plain hru number |
| `hru_fr` | `real, dimension (:), allocatable` | 154 | \|hru area fraction of the flood plain |

### muskingum_parameters

- **Defined in source**: `sd_channel_module.f90:157`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `nsteps` | `integer` | 158 | none \|number of daily time steps required for stability |
| `substeps` | `integer` | 159 | none \|number of time substeps required for stability |
| `c1` | `real` | 160 |  |
| `c2` | `real` | 161 |  |
| `c3` | `real` | 162 |  |

### swatdeg_channel_dynamic

- **Defined in source**: `sd_channel_module.f90:165`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=25)` | 166 |  |
| `props` | `integer` | 167 |  |
| `obj_no` | `integer` | 168 |  |
| `wallo` | `integer` | 169 | water allocation object number |
| `aqu_link` | `integer` | 170 | aquifer the channel is linked to |
| `aqu_link_ch` | `integer` | 171 | sequential channel number in the aquifer |
| `region` | `character(len=25)` | 172 |  |
| `order` | `integer` | 173 |  |
| `chw` | `real` | 174 | m \|channel width |
| `chd` | `real` | 175 | m \|channel depth |
| `chs` | `real` | 176 | m/m \|channel slope |
| `chl` | `real` | 177 | km \|channel length |
| `chn` | `real` | 178 | \|channel Manning's n |
| `chk` | `real` | 179 | mm/h \|channel bottom conductivity |
| `cov` | `real` | 180 | 0-1 \|channel cover factor |
| `sinu` | `real` | 181 | none \|sinuousity - ratio of channel length and straight line length |
| `vcr_coef` | `real` | 182 | m/m \|critical velocity coefficient |
| `d50` | `real` | 183 |  |
| `ch_clay` | `real` | 184 |  |
| `carbon` | `real` | 185 |  |
| `ch_bd` | `real` | 186 |  |
| `chss` | `real` | 187 |  |
| `bankfull_flo` | `real` | 188 |  |
| `fps` | `real` | 189 |  |
| `fpn` | `real` | 190 |  |
| `n_conc` | `real` | 191 | mg/kg \|nitrogen concentration in channel bank |
| `p_conc` | `real` | 192 | mg/kg \|phosphorus concentration in channel bank |
| `p_bio` | `real` | 193 | frac \|fraction of p in bank that is bioavailable |
| `pk_rto` | `real` | 194 | ratio \|ratio of peak to mean daily flow in channel |
| `fp_inun_days` | `real` | 195 | days \|number of days fllod plain is inundated after flood |
| `n_setl` | `real` | 196 | ratio \|ratio of amount of N settling and sediment settling |
| `p_setl` | `real` | 197 | ratio \|ratio of amount of P settling and sediment settling |
| `n_sol_part` | `real` | 198 | frac \|instream nitrogen soluble to particulate transformation coefficient |
| `p_sol_part` | `real` | 199 | frac \|instream phosphorus soluble to particulate transformation coefficient |
| `n_dep_enr` | `real` | 200 | \|enrichment of N in remaining water - deposition = 1/enrichment ratio |
| `p_dep_enr` | `real` | 201 | \|enrichment of P in remaining water - deposition = 1/enrichment ratio |
| `arc_len_fr` | `real` | 202 | frac \|fraction of arc length where bank erosion occurs |
| `bed_exp` | `real` | 203 | mm \|bed erosion exponent |
| `wash_bed_fr` | `real` | 204 | frac \|fraction of bank erosion that is washload |
| `hc_kh` | `real` | 205 |  |
| `hc_hgt` | `real` | 206 | m \|headcut height |
| `hc_ini` | `real` | 207 |  |
| `bank_exp` | `real` | 208 | \|bank erosion exponent |
| `shear_bnk` | `real` | 209 | 0-1 \|bank shear coefficient - fraction of bottom shear |
| `hc_erod` | `real` | 210 | \|headcut erodibility |
| `hc_co` | `real` | 211 | m/m \|proportionality coefficient for head cut |
| `hc_len` | `real` | 212 | m \|length of head cut |
| `in1_vol` | `real` | 213 | m3 \|inflow during previous time step for Muskingum |
| `out1_vol` | `real` | 214 | m3 \|outflow during previous time step for Muskingum |
| `stor_dis_01bf` | `real` | 215 | hr \|storage time constant at 0.1*bankfull |
| `stor_dis_bf` | `real` | 216 | hr \|storage time constant at bankfull |
| `msk` | `muskingum_parameters` | 217 |  |
| `fp` | `floodplain_parameters` | 218 |  |
| `kd` | `real, dimension (:), allocatable` | 219 | \|aquatic mixing velocity (diffusion/dispersion)-using mol_wt |
| `aq_mix` | `real, dimension (:), allocatable` | 220 | m/day \|aquatic mixing velocity (diffusion/dispersion)-using mol_wt |
| `overbank` | `character (len=2)` | 221 | \|"ib"=in bank; "ob"=overbank flood |

### channel_rating_curve_parameters

- **Defined in source**: `sd_channel_module.f90:226`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_rate` | `real` | 227 | m^3/s \|flow rate |
| `xsec_area` | `real` | 228 | m^2 \|cross sectional area of flow |
| `surf_area` | `real` | 229 | m^2 \|total surface area |
| `dep` | `real` | 230 | m \|depth of water |
| `top_wid` | `real` | 231 | m \|depth of water |
| `vol` | `real` | 232 | m^3 \|total volume of water in reach and flood plain |
| `vol_fp` | `real` | 233 | m^3 \|volume of water in flood plain |
| `vol_ch` | `real` | 234 | m^3 \|volume of water in and above channel |
| `wet_perim` | `real` | 235 | m \|wetted perimeter |
| `ttime` | `real` | 236 | hr \|travel time |

### channel_rating_curve

- **Defined in source**: `sd_channel_module.f90:241`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `npts` | `integer` | 242 | none \|number of points on the rating curve |
| `wid_btm` | `real` | 243 | m \|bottom width of main channel elev - 1=.1 bf dep; 2=bf dep; 3=1.2*bf dep; 4=2*bf dep |
| `in1` | `channel_rating_curve_parameters` | 245 | rating curve - inflow previous time step |
| `in2` | `channel_rating_curve_parameters` | 246 | rating curve - inflow current time step |
| `out1` | `channel_rating_curve_parameters` | 247 | rating curve - outflow previous time step |
| `out2` | `channel_rating_curve_parameters` | 248 | rating curve - outflow current time step |
| `elev` | `channel_rating_curve_parameters` | 249 | rating curve at each depth |

### sd_ch_output

- **Defined in source**: `sd_channel_module.f90:253`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `real` | 254 | (m^3/s) \|average daily inflow rate during time step |
| `aqu_in` | `real` | 255 | (m^3/s) \|geomorphic aquifer flow into channel/aquifer inflow using geomorphic baseflow method |
| `flo` | `real` | 256 | (m^3/s) \|average daily outflow rate during timestep |
| `peakr` | `real` | 257 | (m^3/s) \|average peak runoff rate during timestep |
| `sed_in` | `real` | 258 | (tons) \|sediment in |
| `sed_out` | `real` | 259 | (tons) \|sediment out |
| `washld` | `real` | 260 | (tons) \|wash load (suspended) out |
| `bedld` | `real` | 261 | (tons) \|bed load out |
| `dep` | `real` | 262 | (tons) \|deposition in channel and flood plain |
| `deg_btm` | `real` | 263 | (tons) \|erosion of channel bottom |
| `deg_bank` | `real` | 264 | (tons) \|erosion of channel bank |
| `hc_sed` | `real` | 265 | (tons) \|erosion from gully head cut |
| `width` | `real` | 266 | m \|channel bank full top width at end of time step |
| `depth` | `real` | 267 | m \|channel bank full depth at end of time step |
| `slope` | `real` | 268 | m/m \|channel slope |
| `deg_btm_m` | `real` | 269 | (m) !downcutting of channel bottom |
| `deg_bank_m` | `real` | 270 | (m) \|widening of channel banks |
| `hc_m` | `real` | 271 | (m) \|headcut retreat |
| `flo_in_mm` | `real` | 272 | (mm) \|inflow rate total sum for each time step |
| `aqu_in_mm` | `real` | 273 | (mm) \|aquifer inflow rate total sum for each time step |
| `flo_mm` | `real` | 274 | (mm) \|outflow rate total sum for each time step |
| `sed_stor` | `real` | 275 | (tons) \|sed storage at end of timestep |
| `n_tot` | `real` | 276 | (kg N) \|total nitrogen leaving the reach |
| `p_tot` | `real` | 277 | (kg N) \|total phosphorus leaving the reach |
| `dep_bf` | `real` | 278 | m \|depth of water when reach is at bankfull depth |
| `velav_bf` | `real` | 279 | m/s \|average velocity when reach is at bankfull depth |

### sdch_header

- **Defined in source**: `sd_channel_module.f90:296`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 297 |  |
| `mo` | `character (len=6)` | 298 |  |
| `day_mo` | `character (len=6)` | 299 |  |
| `yrc` | `character (len=6)` | 300 |  |
| `isd` | `character (len=8)` | 301 |  |
| `id` | `character (len=8)` | 302 |  |
| `name` | `character (len=16)` | 303 |  |
| `flo_in` | `character(len=16)` | 304 | (m^3/s) |
| `aqu_in` | `character(len=16)` | 305 | (m^3/s) |
| `flo` | `character(len=16)` | 306 | (m^3/s) |
| `peakr` | `character(len=15)` | 307 | (m^3/s) |
| `sed_in` | `character(len=15)` | 308 | (tons) |
| `sed_out` | `character(len=15)` | 309 | (tons) |
| `washld` | `character(len=15)` | 310 | (tons) |
| `bedld` | `character(len=15)` | 311 | (tons) |
| `dep` | `character(len=15)` | 312 | (tons) |
| `deg_btm` | `character(len=15)` | 313 | (tons) |
| `deg_bank` | `character(len=15)` | 314 | (tons) |
| `hc_sed` | `character(len=15)` | 315 | (tons) |
| `width` | `character(len=15)` | 316 | (m) |
| `depth` | `character(len=15)` | 317 | (m) |
| `slope` | `character(len=15)` | 318 | (m/m) |
| `deg_btm_m` | `character(len=15)` | 319 | (m) |
| `deg_bank_m` | `character(len=15)` | 320 | (m) |
| `hc_len` | `character(len=15)` | 321 | (m) |
| `flo_in_mm` | `character(len=16)` | 322 | (mm) |
| `aqu_in_mm` | `character(len=16)` | 323 | (mm) |
| `flo_mm` | `character(len=16)` | 324 | (mm) |
| `sed_stor` | `character(len=16)` | 325 | (tons) |
| `n_tot` | `character(len=16)` | 326 | (kg_N) |
| `p_tot` | `character(len=16)` | 327 | (kg_N) |
| `dep_bf` | `character(len=16)` | 328 | (m/s) |
| `velav_bf` | `character(len=16)` | 329 | (m/s) |

### sdch_header_units

- **Defined in source**: `sd_channel_module.f90:333`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 334 |  |
| `mo` | `character (len=6)` | 335 |  |
| `day_mo` | `character (len=6)` | 336 |  |
| `yrc` | `character (len=6)` | 337 |  |
| `isd` | `character (len=8)` | 338 |  |
| `id` | `character (len=8)` | 339 |  |
| `name` | `character (len=16)` | 340 |  |
| `flo_in` | `character(len=16)` | 341 | (m^3/s) |
| `aqu_in` | `character(len=16)` | 342 | (m^3/s) |
| `flo` | `character(len=16)` | 343 | (m^3/s) |
| `peakr` | `character(len=15)` | 344 | (m^3/s) |
| `sed_in` | `character(len=15)` | 345 | (tons) |
| `sed_out` | `character(len=15)` | 346 | (tons) |
| `washld` | `character(len=15)` | 347 | (tons) |
| `bedld` | `character(len=15)` | 348 | (tons) |
| `dep` | `character(len=15)` | 349 | (tons) |
| `deg_btm` | `character(len=15)` | 350 | (tons) |
| `deg_bank` | `character(len=15)` | 351 | (tons) |
| `hc_sed` | `character(len=15)` | 352 | (tons) |
| `width` | `character(len=15)` | 353 | (m) |
| `depth` | `character(len=15)` | 354 | (m) |
| `slope` | `character(len=15)` | 355 | (m/m) |
| `deg_btm_m` | `character(len=15)` | 356 | (m) |
| `deg_bank_m` | `character(len=15)` | 357 | (m) |
| `hc_len` | `character(len=15)` | 358 | (m) |
| `flo_in_mm` | `character(len=16)` | 359 | (mm) |
| `aqu_in_mm` | `character(len=16)` | 360 | (mm) |
| `flo_mm` | `character(len=16)` | 361 | (mm) |
| `sed_stor` | `character(len=16)` | 362 | (tons) |
| `n_tot` | `character(len=16)` | 363 | (kg_N) |
| `p_tot` | `character(len=16)` | 364 | (kg_P) |
| `dep_bf` | `character(len=16)` | 365 | (m/s) |
| `velav_bf` | `character(len=16)` | 366 | (m/s) |

### sdch_bud

- **Defined in source**: `sd_channel_module.f90:372`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 373 |  |
| `mo` | `character (len=6)` | 374 |  |
| `day_mo` | `character (len=6)` | 375 |  |
| `yrc` | `character (len=6)` | 376 |  |
| `isd` | `character (len=8)` | 377 |  |
| `id` | `character (len=8)` | 378 |  |
| `name` | `character (len=16)` | 379 |  |
| `in_sed` | `character(len=16)` | 380 | (tons) |
| `out_sed` | `character(len=16)` | 381 | (tons) |
| `fp_dep` | `character(len=16)` | 382 | (tons) |
| `ch_dep` | `character(len=16)` | 383 | (tons) |
| `bank_ero` | `character(len=16)` | 384 | (tons) |
| `bed_ero` | `character(len=16)` | 385 | (tons) |
| `in_no3` | `character(len=16)` | 386 | (tons) |
| `in_orgn` | `character(len=16)` | 387 | (tons) |
| `out_no3` | `character(len=15)` | 388 | (tons) |
| `out_orgn` | `character(len=16)` | 389 | (tons) |
| `fp_no3` | `character(len=15)` | 390 | (tons) |
| `bank_no3` | `character(len=15)` | 391 | (tons) |
| `bed_no3` | `character(len=15)` | 392 | (tons) |
| `fp_orgn` | `character(len=15)` | 393 | (tons) |
| `ch_orgn` | `character(len=15)` | 394 | (tons) |
| `bank_orgn` | `character(len=15)` | 395 | (tons) |
| `bed_orgn` | `character(len=15)` | 396 | (tons) |
| `in_solp` | `character(len=15)` | 397 | (tons) |
| `in_orgp` | `character(len=15)` | 398 | (tons) |
| `out_solp` | `character(len=15)` | 399 | (tons) |
| `out_orgp` | `character(len=15)` | 400 | (tons) |
| `fp_solp` | `character(len=15)` | 401 | (tons) |
| `bank_solp` | `character(len=15)` | 402 | (tons) |
| `bed_solp` | `character(len=15)` | 403 | (tons) |
| `fp_orgp` | `character(len=15)` | 404 | (tons) |
| `ch_orgp` | `character(len=15)` | 405 | (tons) |
| `bank_orgp` | `character(len=15)` | 406 | (tons) |
| `bed_orgp` | `character(len=15)` | 407 | (tons) |
| `no3_orgn` | `character(len=15)` | 408 | (tons) |
| `solp_orgp` | `character(len=15)` | 409 | (tons) |

### sdch_bud_units

- **Defined in source**: `sd_channel_module.f90:413`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 414 |  |
| `mo` | `character (len=6)` | 415 |  |
| `day_mo` | `character (len=6)` | 416 |  |
| `yrc` | `character (len=6)` | 417 |  |
| `isd` | `character (len=8)` | 418 |  |
| `id` | `character (len=8)` | 419 |  |
| `name` | `character (len=16)` | 420 |  |
| `in_sed` | `character(len=16)` | 421 | (tons) |
| `out_sed` | `character(len=16)` | 422 | (tons) |
| `fp_dep` | `character(len=16)` | 423 | (tons) |
| `ch_dep` | `character(len=16)` | 424 | (tons) |
| `bank_ero` | `character(len=16)` | 425 | (tons) |
| `bed_ero` | `character(len=16)` | 426 | (tons) |
| `in_no3` | `character(len=16)` | 427 | (tons) |
| `in_orgn` | `character(len=16)` | 428 | (tons) |
| `out_no3` | `character(len=15)` | 429 | (tons) |
| `out_orgn` | `character(len=16)` | 430 | (tons) |
| `fp_no3` | `character(len=15)` | 431 | (tons) |
| `bank_no3` | `character(len=15)` | 432 | (tons) |
| `bed_no3` | `character(len=15)` | 433 | (tons) |
| `fp_orgn` | `character(len=16)` | 434 | (tons) |
| `ch_orgn` | `character(len=15)` | 435 | (tons) |
| `bank_orgn` | `character(len=15)` | 436 | (tons) |
| `bed_orgn` | `character(len=15)` | 437 | (tons) |
| `in_solp` | `character(len=15)` | 438 | (tons) |
| `in_orgp` | `character(len=15)` | 439 | (tons) |
| `out_solp` | `character(len=15)` | 440 | (tons) |
| `out_orgp` | `character(len=15)` | 441 | (tons) |
| `fp_solp` | `character(len=15)` | 442 | (tons) |
| `bank_solp` | `character(len=15)` | 443 | (tons) |
| `bed_solp` | `character(len=15)` | 444 | (tons) |
| `fp_orgp` | `character(len=15)` | 445 | (tons) |
| `ch_orgp` | `character(len=15)` | 446 | (tons) |
| `bank_orgp` | `character(len=15)` | 447 | (tons) |
| `bed_orgp` | `character(len=15)` | 448 | (tons) |
| `no3_orgp` | `character(len=15)` | 449 | (tons) |
| `solp_orgp` | `character(len=15)` | 450 | (tons) |

### sdch_header_sub

- **Defined in source**: `sd_channel_module.f90:455`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 456 |  |
| `mo` | `character (len=6)` | 457 |  |
| `day_mo` | `character (len=6)` | 458 |  |
| `yrc` | `character (len=6)` | 459 |  |
| `isd` | `character (len=8)` | 460 |  |
| `id` | `character (len=8)` | 461 |  |
| `ii` | `character (len=8)` | 462 |  |
| `name` | `character (len=16)` | 463 |  |
| `hyd_flo` | `character(len=16)` | 464 | (m^3/s) |

### sdch_header_units_sub

- **Defined in source**: `sd_channel_module.f90:468`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 469 |  |
| `mo` | `character (len=6)` | 470 |  |
| `day_mo` | `character (len=6)` | 471 |  |
| `yrc` | `character (len=6)` | 472 |  |
| `isd` | `character (len=8)` | 473 |  |
| `id` | `character (len=8)` | 474 |  |
| `ii` | `character (len=8)` | 475 |  |
| `name` | `character (len=16)` | 476 |  |
| `hyd_flo` | `character (len=16)` | 477 | (m^3/s) |

### sd_chd_header

- **Defined in source**: `sd_channel_module.f90:481`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 482 |  |
| `order` | `character(len=16)` | 483 |  |
| `chw` | `character (len=16)` | 484 | m \|channel width |
| `chd` | `character (len=16)` | 485 | m \|channel depth |
| `chs` | `character (len=16)` | 486 | m/m \|channel slope |
| `chl` | `character (len=16)` | 487 | m \|channel length |
| `chn` | `character (len=16)` | 488 | \|channel Manning's n |
| `chk` | `character (len=16)` | 489 | mm/h \|channel bottom conductivity |
| `cherod` | `character (len=16)` | 490 | \|channel erodibility |
| `cov` | `character (len=16)` | 491 | 0-1 \|channel cover factor |
| `sinu` | `character (len=16)` | 492 | \|sinuousity - ratio of channel length and straight line length |
| `chseq` | `character (len=16)` | 493 | m/m \|equilibrium channel slope |
| `d50` | `character (len=16)` | 494 | \|median particle size |
| `ch_clay` | `character (len=16)` | 495 | % \|clay percent of bank and bed |
| `carbon` | `character (len=16)` | 496 | % \|carbon percent of bank and bed |
| `ch_bd` | `character (len=16)` | 497 | g/cm^3 \|channel bank density |
| `chss` | `character (len=16)` | 498 | \|channel sediment supply |
| `bankfull_flo` | `character (len=16)` | 499 | m^3/s \|bankfull flow |
| `fps` | `character (len=16)` | 500 | \|flood plain slope |
| `fpn` | `character (len=16)` | 501 | \|flood plain Manning's n |
| `n_conc` | `character (len=16)` | 502 | mg/kg \|nitrogen concentration in channel bank |
| `p_conc` | `character (len=16)` | 503 | mg/kg \|phosphorus concentration in channel bank |
| `p_bio` | `character (len=16)` | 504 | frac \|fraction of p in bank that is bioavailable |

## Variables Defined
### maxint

- **Type**: `integer`
- **Defined in source**: `sd_channel_module.f90:5`
- **Source note**: number of intervals in hydrograph for degradation

### wtemp

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:6`
- **Source note**: stream water temperature C

### peakrate

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:7`

### sed_reduc_t

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:8`

### no3_reduc_kg

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:9`

### tp_reduc_kg

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:10`

### tp_reduc

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:11`

### srp_reduc_kg

- **Type**: `real`
- **Defined in source**: `sd_channel_module.f90:12`

### hyd_rad

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `sd_channel_module.f90:13`
- **Source note**: m^2        |hydraulic radius for each hydrograph time step

### trav_time

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `sd_channel_module.f90:14`
- **Source note**: days       |time spent in each hydrograph time step

### flo_dep

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `sd_channel_module.f90:15`
- **Source note**: m^2        |hydraulic radius for each hydrograph time step

### timeint

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `sd_channel_module.f90:16`
- **Source note**: days       |time spent in each hydrograph time step

### sd_chd

- **Type**: `swatdeg_hydsed_data`
- **Defined in source**: `sd_channel_module.f90:43`

### sd_chd1

- **Type**: `swatdeg_sednut_data`
- **Defined in source**: `sd_channel_module.f90:60`

### ch_sed_bud

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:95`

### ch_sed_bud_m

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:96`

### ch_sed_bud_y

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:96`

### ch_sed_bud_a

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:96`

### ch_sed_budz

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:97`

### bch_sed_bud_d

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:97`

### bch_sed_bud_m

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:97`

### bch_sed_bud_y

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:97`

### bch_sed_bud_a

- **Type**: `channel_sediment_budget_output`
- **Defined in source**: `sd_channel_module.f90:97`

### ch_morph

- **Type**: `channel_morphology_output`
- **Defined in source**: `sd_channel_module.f90:110`

### ch_morph_ord

- **Type**: `channel_morphology_output`
- **Defined in source**: `sd_channel_module.f90:111`

### gully

- **Type**: `gully_data`
- **Defined in source**: `sd_channel_module.f90:119`

### sd_init

- **Type**: `swatdeg_init_datafiles`
- **Defined in source**: `sd_channel_module.f90:130`

### sd_dat

- **Type**: `swatdeg_datafiles`
- **Defined in source**: `sd_channel_module.f90:144`

### sd_ch

- **Type**: `swatdeg_channel_dynamic`
- **Defined in source**: `sd_channel_module.f90:223`

### sdch_init

- **Type**: `swatdeg_channel_dynamic`
- **Defined in source**: `sd_channel_module.f90:224`

### rcurv

- **Type**: `channel_rating_curve_parameters`
- **Defined in source**: `sd_channel_module.f90:238`
- **Source note**: rating curve at each time step

### rcz

- **Type**: `channel_rating_curve_parameters`
- **Defined in source**: `sd_channel_module.f90:239`
- **Source note**: zero rating curve

### ch_rcurv

- **Type**: `channel_rating_curve`
- **Defined in source**: `sd_channel_module.f90:251`

### chsd_d

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:282`

### chsd_m

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:283`

### chsd_y

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:284`

### chsd_a

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:285`

### schsd_d

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:286`

### schsd_m

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:287`

### schsd_y

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:288`

### schsd_a

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:289`

### bchsd_d

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:290`

### bchsd_m

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:291`

### bchsd_y

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:292`

### bchsd_a

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:293`

### chsdz

- **Type**: `sd_ch_output`
- **Defined in source**: `sd_channel_module.f90:294`

### sdch_hdr

- **Type**: `sdch_header`
- **Defined in source**: `sd_channel_module.f90:331`

### sdch_hdr_units

- **Type**: `sdch_header_units`
- **Defined in source**: `sd_channel_module.f90:368`

### sdch_bud_hdr

- **Type**: `sdch_bud`
- **Defined in source**: `sd_channel_module.f90:411`

### sdch_bud_hdr_units

- **Type**: `sdch_bud_units`
- **Defined in source**: `sd_channel_module.f90:452`

### sdch_hdr_subday

- **Type**: `sdch_header_sub`
- **Defined in source**: `sd_channel_module.f90:466`

### sdch_hdr_units_sub

- **Type**: `sdch_header_units`
- **Defined in source**: `sd_channel_module.f90:479`

### sd_chd_hdr

- **Type**: `sd_chd_header`
- **Defined in source**: `sd_channel_module.f90:506`

## Subroutines Defined
### chrc_interp

## Functions Defined
### chsednut_add

### chsednut_div

### chsd_add

### chsd_div

### chsd_ave

### chsd_mult

### chrc_mult

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

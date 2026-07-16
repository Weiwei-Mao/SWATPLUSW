---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_landscape_module.f90
note_file: output_landscape_module.f90
module_name: output_landscape_module
defines_types:
  - output_waterbal
  - regional_output_waterbal
  - output_nutbal
  - regional_output_nutbal
  - output_nutcarb_cycling
  - output_losses
  - regional_output_losses
  - output_plantweather
  - regional_output_plantweather
  - output_waterbal_header
  - output_waterbal_header_units
  - output_nutbal_header
  - output_nutbal_header_units
  - output_losses_header
  - output_losses_header_units
  - output_nutcarb_cycling_header
  - output_nutbal_header_units1
  - output_carbon_header
  - output_carbon_header_units1
  - output_carb_gl_header
  - output_carb_gl_header_units
  - output_hscf_header
  - output_hscf_header_units
  - output_losses_header1
  - output_losses_header_units1
  - output_plantweather_header
  - output_plantweather_header_units
defines_vars:
  - h
  - hwb_d
  - hwb_m
  - hwb_y
  - hwb_a
  - hwbz
  - hltwb_d
  - hltwb_m
  - hltwb_y
  - hltwb_a
  - lsu_wb_d
  - ruwb_d
  - ruwb_m
  - ruwb_y
  - ruwb_a
  - bwb_d
  - bwb_m
  - bwb_y
  - bwb_a
  - rwb_d
  - rwb_m
  - rwb_y
  - rwb_a
  - hnb_d
  - hnb_m
  - hnb_y
  - hnb_a
  - hnbz
  - hltnb_d
  - hltnb_m
  - hltnb_y
  - hltnb_a
  - runb_d
  - runb_m
  - runb_y
  - runb_a
  - bnb_d
  - bnb_m
  - bnb_y
  - bnb_a
  - rnb_d
  - rnb_m
  - rnb_y
  - rnb_a
  - hcyl_d
  - hcyl_m
  - hcyl_y
  - hcyl_a
  - hycl_z
  - hls_d
  - hls_m
  - hls_y
  - hls_a
  - hlsz
  - hltls_d
  - hltls_m
  - hltls_y
  - hltls_a
  - ruls_d
  - ruls_m
  - ruls_y
  - ruls_a
  - bls_d
  - bls_m
  - bls_y
  - bls_a
  - rls_d
  - rls_m
  - rls_y
  - rls_a
  - hpw_d
  - hpw_m
  - hpw_y
  - hpw_a
  - hpwz
  - hltpw_d
  - hltpw_m
  - hltpw_y
  - hltpw_a
  - rupw_d
  - rupw_m
  - rupw_y
  - rupw_a
  - bpw_d
  - bpw_m
  - bpw_y
  - bpw_a
  - rpw_d
  - rpw_m
  - rpw_y
  - rpw_a
  - wb_hdr
  - wb_hdr_units
  - nb_hdr
  - nb_hdr_units
  - ls_hdr
  - ls_hdr_units
  - nb_hdr1
  - nb_hdr_units1
  - carbon_hdr1
  - carbon_hdr_units1
  - carb_gl_hdr
  - carb_gl_hdr_units
  - hscf_hdr
  - hscf_hdr_units
  - ls_hdr1
  - ls_hdr_units1
  - pw_hdr
  - pw_hdr_units
defines_subroutines: []
defines_functions:
  - hruout_waterbal_add
  - hruout_nutbal_add
  - hruout_losses_add
  - hruout_nut_cycling_add
  - hruout_nut_cycling_mult
  - hruout_nut_cycling_div
  - hruout_plantweather_add
  - hruout_waterbal_div
  - hruout_waterbal_ave
  - hruout_waterbal_mult
  - hruout_nutbal_div
  - hruout_nutbal_mult
  - hruout_losses_div
  - hruout_losses_mult
  - hruout_plantweather_div
  - hruout_plantweather_ave
  - hruout_plantweather_mult
defines_procedures:
  - hruout_waterbal_add
  - hruout_nutbal_add
  - hruout_losses_add
  - hruout_nut_cycling_add
  - hruout_nut_cycling_mult
  - hruout_nut_cycling_div
  - hruout_plantweather_add
  - hruout_waterbal_div
  - hruout_waterbal_ave
  - hruout_waterbal_mult
  - hruout_nutbal_div
  - hruout_nutbal_mult
  - hruout_losses_div
  - hruout_losses_mult
  - hruout_plantweather_div
  - hruout_plantweather_ave
  - hruout_plantweather_mult
purpose: ""
---

# output_landscape_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### output_waterbal

- **Defined in source**: `output_landscape_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `precip` | `real` | 6 | mm H2O \|precipitation falling as rain and snow |
| `snofall` | `real` | 7 | mm H2O \|precipitation falling as snow, sleet or freezing rain |
| `snomlt` | `real` | 8 | mm H2O \|snow or melting ice |
| `surq_gen` | `real` | 9 | mm H2O \|surface runoff generated from the landscape |
| `latq` | `real` | 10 | mm H2O \|lateral soil flow |
| `wateryld` | `real` | 11 | mm H2O \|water yield - sum of surface runoff, lateral soil flow and tile flow |
| `perc` | `real` | 12 | mm H2O \|amt of water perc out of the soil profile & into the vadose zone |
| `et` | `real` | 13 | mm H2O \|actual evapotranspiration from the soil |
| `ecanopy` | `real` | 14 | mm H2O \|not reported |
| `eplant` | `real` | 15 | mm H2O \|plant transpiration |
| `esoil` | `real` | 16 | mm H2O \|soil evaporation |
| `surq_cont` | `real` | 17 | mm H2O \|surface runoff leaving the landscape |
| `cn` | `real` | 18 | none \|average curve number value for timestep |
| `sw_init` | `real` | 19 | mm H2O \|initial soil water content of soil profile at start of time step |
| `sw_final` | `real` | 20 | mm H2O \|final soil water content of soil profile at end of time step |
| `sw` | `real` | 21 | mm H2O \|average soil water content of soil profile |
| `sw_300` | `real` | 22 | mm H2O \|final soil water content of upper 300 mm at end of time step |
| `sno_init` | `real` | 23 | mm H2O \|initial soil water content of snow pack |
| `sno_final` | `real` | 24 | mm H2O \|final soil water content of snow pack |
| `snopack` | `real` | 25 | mm \|water equivalent in snow pack |
| `pet` | `real` | 26 | mm H2O \|potential evapotranspiration |
| `qtile` | `real` | 27 | mm H2O \|subsurface tile flow leaving the landscape |
| `irr` | `real` | 28 | mm H2O \|irrigation water applied |
| `surq_runon` | `real` | 29 | mm H2O \|surface runoff from upland landscape |
| `latq_runon` | `real` | 30 | mm H2O \|lateral soil flow from upland landscape |
| `overbank` | `real` | 31 | mm H2O \|overbank flooding from channels |
| `surq_cha` | `real` | 32 | mm H2O \|surface runoff flowing into channels |
| `surq_res` | `real` | 33 | mm H2O \|surface runoff flowing into reservoirs |
| `surq_ls` | `real` | 34 | mm H2O \|surface runoff flowing onto the landscape |
| `latq_cha` | `real` | 35 | mm H2O \|lateral soil flow into channels |
| `latq_res` | `real` | 36 | mm H2O \|lateral soil flow into reservoirs |
| `latq_ls` | `real` | 37 | mm H2O \|lateral soil flow into a landscape element |
| `gwsoil` | `real` | 38 | mm H2O \|groundwater transferred to soil profile (when water table is in soil profile) !rtb gwflow |
| `satex` | `real` | 39 | mm H2O \|saturation excess flow developed from high water table !rtb gwflow |
| `satex_chan` | `real` | 40 | mm H2O \|saturation excess flow reaching main channel !rtb gwflow |
| `delsw` | `real` | 41 | mm H2O \|change in soil water volume !rtb gwflow |
| `lagsurf` | `real` | 42 | mm H2O \|surface runoff in transit to channel |
| `laglatq` | `real` | 43 | mm H2O \|lateral flow in transit to channel |
| `lagsatex` | `real` | 44 | mm H2O \|saturation excess flow in transit to channel |
| `wet_evap` | `real` | 45 | mm H2O \|evaporation from wetland surface |
| `wet_out` | `real` | 46 | mm H2O \|outflow (spill) from wetland |
| `wet_stor` | `real` | 47 | mm H2O \|volume stored in wetland at end of time period |

### regional_output_waterbal

- **Defined in source**: `output_landscape_module.f90:73`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lum` | `output_waterbal` | 74 |  |

### output_nutbal

- **Defined in source**: `output_landscape_module.f90:82`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `grazn` | `real` | 83 | kg N/ha \|total nitrogen added to soil from grazing |
| `grazp` | `real` | 84 | kg P/ha \|total phophorous added to soil from grazing |
| `lab_min_p` | `real` | 85 | kg P/ha \|phosphoros moving from the labile mineral pool to the active mineral pool |
| `act_sta_p` | `real` | 86 | kg P/ha \|phosphorus moving from the active mineral pool to the stable mineral pool |
| `fertn` | `real` | 87 | kg N/ha \|total nitrogen applied to soil |
| `fertp` | `real` | 88 | kg P/ha \|total phosphorus applied to soil |
| `fixn` | `real` | 89 | kg N/ha \|nitrogen added to plant biomass via fixation |
| `denit` | `real` | 90 | kg N/ha \|nitrogen lost from nitrate pool by denitrification |
| `act_nit_n` | `real` | 91 | kg N/ha \|nitrogen moving from active organic pool to nitrate pool |
| `act_sta_n` | `real` | 92 | kg N/ha \|nitrogen moving from active organic pool to stable pool |
| `org_lab_p` | `real` | 93 | kg P/ha \|phosphorus moving from the organic pool to labile pool |
| `rsd_nitorg_n` | `real` | 94 | kg N/ha \|nitrogen moving from the fresh organic pool (residue) to the nitrate (80%) and active org (20%) pools |
| `rsd_laborg_p` | `real` | 96 | kg P/ha \|phosphorus moving from the fresh organic pool (residue) to the labile (80%) and org (20%) pools |
| `no3atmo` | `real` | 98 | kg N/ha \|nitrate added to the soil from atmospheric deposition |
| `nh4atmo` | `real` | 99 | kg N/ha \|ammonia added to the soil from atmospheric deposition |
| `nuptake` | `real` | 100 | kg N/ha \|plant nitrogen uptake |
| `puptake` | `real` | 101 | kg P/ha \|plant phosphorus uptake |
| `gwsoiln` | `real` | 102 | kg N/ha \|nitrate added to the soil from the aquifer (rtb gwflow) |
| `gwsoilp` | `real` | 103 | kg P/ha \|Phos added to the soil from the aquifer (rtb gwflow) |

### regional_output_nutbal

- **Defined in source**: `output_landscape_module.f90:127`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lum` | `output_nutbal` | 128 |  |

### output_nutcarb_cycling

- **Defined in source**: `output_landscape_module.f90:135`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lab_min_p` | `real` | 136 | kg P/ha \|phosphorus moving from the labile mineral pool to the active mineral pool |
| `act_sta_p` | `real` | 137 | kg P/ha \|phosphorus moving from the active mineral pool to the stable mineral pool |
| `act_nit_n` | `real` | 138 | kg N/ha \|nitrogen moving from active organic pool to nitrate pool |
| `act_sta_n` | `real` | 139 | kg N/ha \|nitrogen moving from active organic pool to stable pool |
| `org_lab_p` | `real` | 140 | kg P/ha \|phosphorus moving from the organic pool to labile pool |
| `rsd_hs_c` | `real` | 141 | kg C/ha \|amt of carbon moving from the fresh org (residue) to soil slow humus |
| `rsd_nitorg_n` | `real` | 142 | kg N/ha \|nitrogen moving from the fresh organic pool (residue) to nitrate |
| `rsd_laborg_p` | `real` | 143 | kg P/ha \|phosphorus moving from the fresh organic pool (residue) to the labile (80%) and org (20%) pools |

### output_losses

- **Defined in source**: `output_landscape_module.f90:152`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sedyld` | `real` | 153 | metric tons/ha \|sediment yield leaving the landscape caused by water erosion |
| `sedorgn` | `real` | 154 | kg N/ha \|organic nitrogen transported in surface runoff |
| `sedorgp` | `real` | 155 | kg P/ha \|organic phosphorus transported in surface runoff |
| `surqno3` | `real` | 156 | kg N/ha \|nitrate NO3-N transported in surface runoff |
| `latno3` | `real` | 157 | kg N/ha \|nitrate NO3-N transported in lateral runoff |
| `surqsolp` | `real` | 158 | kg P/ha \|soluble phosphorus transported in surface runoff |
| `usle` | `real` | 159 | metric tons/ha \|sediment erosion predicted with the USLE equation |
| `sedminp` | `real` | 160 | kg P/ha \|mineral phosphorus leaving the landscape transported in sediment |
| `tileno3` | `real` | 161 | kg N/ha \|nitrate NO3 in tile flow |
| `lchlabp` | `real` | 162 | kg P/ha \|soluble P (labile) leaching past bottom soil layer |
| `tilelabp` | `real` | 163 | kg P/ha \|soluble P (labile) in tile flow |
| `satexn` | `real` | 164 | kg N/ha \| amt of NO3-N in saturation excess surface runoff in HRU for the day |

### regional_output_losses

- **Defined in source**: `output_landscape_module.f90:188`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lum` | `output_losses` | 189 |  |

### output_plantweather

- **Defined in source**: `output_landscape_module.f90:196`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lai` | `real` | 197 | m**2/m**2 \|average leaf area index during timestep |
| `bioms` | `real` | 198 | kg/ha \|average total plant biomass during timestep |
| `yield` | `real` | 199 | kg/ha \|harvested biomass yield (dry weight) during timestep |
| `residue` | `real` | 200 | kg/ha \|average surface residue cover during timestep |
| `sol_tmp` | `real` | 201 | deg C \|average temperature of soil layer 2 during timestep |
| `strsw` | `real` | 202 | days \|limiting water (drought) stress |
| `strsa` | `real` | 203 | days \|excess water (aeration) stress |
| `strstmp` | `real` | 204 | days \|temperature stress |
| `strsn` | `real` | 205 | days \|nitrogen stress |
| `strsp` | `real` | 206 | days \|phosphorus stress |
| `strss` | `real` | 207 | days \|salinity stress |
| `nplnt` | `real` | 208 | kg N/ha \|plant uptake of nitrogen |
| `percn` | `real` | 209 | kg N/ha \|nitrate NO3-N leached from bottom of soil profile |
| `pplnt` | `real` | 210 | kg P/ha \|plant uptake of phosphorus |
| `tmx` | `real` | 211 | deg C \|average maximum temperature during timestep |
| `tmn` | `real` | 212 | deg C \|average minimum temperature during timestep |
| `tmpav` | `real` | 213 | deg C \|average of daily air temperature during timestep |
| `solrad` | `real` | 214 | MJ/m^2 \|average solar radiation during timestep |
| `wndspd` | `real` | 215 | m/s \|average windspeed during timestep |
| `rhum` | `real` | 216 | none \|average relative humidity during timestep |
| `phubase0` | `real` | 217 | deg c/deg c \|base zero potential heat units |
| `lai_max` | `real` | 218 | m**2/m**2 \|maximum leaf area index during timestep |
| `bm_max` | `real` | 219 | kg/ha \|maximum total plant biomass during timestep |
| `bm_grow` | `real` | 220 | kg/ha \|total plant biomass growth during timestep |
| `c_gro` | `real` | 221 | kg/ha \|total plant carbon growth during timestep |

### regional_output_plantweather

- **Defined in source**: `output_landscape_module.f90:245`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `lum` | `output_plantweather` | 246 |  |

### output_waterbal_header

- **Defined in source**: `output_landscape_module.f90:253`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 254 |  |
| `mo` | `character (len=6)` | 255 |  |
| `day_mo` | `character (len=6)` | 256 |  |
| `yrc` | `character (len=6)` | 257 |  |
| `isd` | `character (len=8)` | 258 |  |
| `id` | `character (len=8)` | 259 |  |
| `name` | `character (len=16)` | 260 |  |
| `precip` | `character (len=14)` | 261 |  |
| `snofall` | `character (len=12)` | 262 |  |
| `snomlt` | `character (len=12)` | 263 |  |
| `surq_gen` | `character (len=12)` | 264 |  |
| `latq` | `character (len=12)` | 265 |  |
| `wateryld` | `character (len=12)` | 266 |  |
| `perc` | `character (len=12)` | 267 |  |
| `et` | `character (len=12)` | 268 |  |
| `ecanopy` | `character (len=12)` | 269 |  |
| `eplant` | `character (len=12)` | 270 |  |
| `esoil` | `character (len=12)` | 271 |  |
| `surq_cont` | `character (len=12)` | 272 |  |
| `cn` | `character (len=12)` | 273 |  |
| `sw_init` | `character (len=12)` | 274 |  |
| `sw_final` | `character (len=12)` | 275 |  |
| `sw_ave` | `character (len=12)` | 276 |  |
| `sw_300` | `character (len=12)` | 277 |  |
| `sno_init` | `character (len=12)` | 278 |  |
| `sno_final` | `character (len=12)` | 279 |  |
| `snopack` | `character (len=12)` | 280 |  |
| `pet` | `character (len=12)` | 281 |  |
| `qtile` | `character (len=12)` | 282 |  |
| `irr` | `character (len=12)` | 283 |  |
| `surq_runon` | `character (len=12)` | 284 |  |
| `latq_runon` | `character (len=12)` | 285 |  |
| `overbank` | `character (len=12)` | 286 |  |
| `surq_cha` | `character (len=12)` | 287 |  |
| `surq_res` | `character (len=12)` | 288 |  |
| `surq_ls` | `character (len=12)` | 289 |  |
| `latq_cha` | `character (len=12)` | 290 |  |
| `latq_res` | `character (len=12)` | 291 |  |
| `latq_ls` | `character (len=12)` | 292 |  |
| `gwsoilq` | `character (len=12)` | 293 |  |
| `satex` | `character (len=12)` | 294 |  |
| `satex_chan` | `character (len=12)` | 295 |  |
| `sw_change` | `character (len=12)` | 296 |  |
| `lagsurf` | `character (len=12)` | 297 |  |
| `laglatq` | `character (len=12)` | 298 |  |
| `lagsatex` | `character (len=12)` | 299 |  |
| `wet_evap` | `character (len=12)` | 300 |  |
| `wet_oflo` | `character (len=12)` | 301 |  |
| `wet_stor` | `character (len=12)` | 302 |  |
| `plt_cov` | `character (len=16)` | 303 |  |
| `mgt_ops` | `character (len=30)` | 304 |  |

### output_waterbal_header_units

- **Defined in source**: `output_landscape_module.f90:308`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 309 |  |
| `mo` | `character (len=6)` | 310 |  |
| `day_mo` | `character (len=6)` | 311 |  |
| `yrc` | `character (len=6)` | 312 |  |
| `isd` | `character (len=8)` | 313 |  |
| `id` | `character (len=8)` | 314 |  |
| `name` | `character (len=16)` | 315 |  |
| `precip` | `character (len=14)` | 316 |  |
| `snofall` | `character (len=12)` | 317 |  |
| `snomlt` | `character (len=12)` | 318 |  |
| `surq_gen` | `character (len=12)` | 319 |  |
| `latq` | `character (len=12)` | 320 |  |
| `wateryld` | `character (len=12)` | 321 |  |
| `perc` | `character (len=12)` | 322 |  |
| `et` | `character (len=12)` | 323 |  |
| `ecanopy` | `character (len=12)` | 324 |  |
| `eplant` | `character (len=12)` | 325 |  |
| `esoil` | `character (len=12)` | 326 |  |
| `surq_cont` | `character (len=12)` | 327 |  |
| `cn` | `character (len=12)` | 328 |  |
| `sw_init` | `character (len=12)` | 329 |  |
| `sw_final` | `character (len=12)` | 330 |  |
| `sw_ave` | `character (len=12)` | 331 |  |
| `sw_300` | `character (len=12)` | 332 |  |
| `sno_init` | `character (len=12)` | 333 |  |
| `sno_final` | `character (len=12)` | 334 |  |
| `snopack` | `character (len=12)` | 335 |  |
| `pet` | `character (len=12)` | 336 |  |
| `qtile` | `character (len=12)` | 337 |  |
| `irr` | `character (len=12)` | 338 |  |
| `surq_runon` | `character (len=12)` | 339 |  |
| `latq_runon` | `character (len=12)` | 340 |  |
| `overbank` | `character (len=12)` | 341 |  |
| `surq_cha` | `character (len=12)` | 342 |  |
| `surq_res` | `character (len=12)` | 343 |  |
| `surq_ls` | `character (len=12)` | 344 |  |
| `latq_cha` | `character (len=12)` | 345 |  |
| `latq_res` | `character (len=12)` | 346 |  |
| `latq_ls` | `character (len=12)` | 347 |  |
| `gwsoilq` | `character (len=12)` | 348 |  |
| `satex` | `character (len=12)` | 349 |  |
| `satex_chan` | `character (len=12)` | 350 |  |
| `sw_change` | `character (len=12)` | 351 |  |
| `lagsurf` | `character (len=12)` | 352 |  |
| `laglatq` | `character (len=12)` | 353 |  |
| `lagsatex` | `character (len=12)` | 354 |  |
| `wet_evap` | `character (len=12)` | 355 |  |
| `wet_oflo` | `character (len=12)` | 356 |  |
| `wet_stor` | `character (len=12)` | 357 |  |

### output_nutbal_header

- **Defined in source**: `output_landscape_module.f90:361`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 362 |  |
| `mo` | `character (len=6)` | 363 |  |
| `day_mo` | `character (len=6)` | 364 |  |
| `yrc` | `character (len=6)` | 365 |  |
| `isd` | `character (len=9)` | 366 |  |
| `id` | `character (len=8)` | 367 |  |
| `name` | `character (len=16)` | 368 |  |
| `grazn` | `character(len=12)` | 369 |  |
| `grazp` | `character(len=12)` | 370 |  |
| `lab_min_p` | `character(len=12)` | 371 |  |
| `act_sta_p` | `character(len=12)` | 372 |  |
| `fertn` | `character(len=17)` | 373 |  |
| `fertp` | `character(len=17)` | 374 |  |
| `fixn` | `character(len=17)` | 375 |  |
| `denit` | `character(len=17)` | 376 |  |
| `act_nit_n` | `character(len=17)` | 377 |  |
| `act_sta_n` | `character(len=17)` | 378 |  |
| `org_lab_p` | `character(len=17)` | 379 |  |
| `rsd_nitorg_n` | `character(len=17)` | 380 |  |
| `rsd_laborg_p` | `character(len=17)` | 381 |  |
| `no3atmo` | `character(len=17)` | 382 |  |
| `nh4atmo` | `character(len=17)` | 383 |  |
| `nuptake` | `character(len=17)` | 384 |  |
| `puptake` | `character(len=17)` | 385 |  |
| `gwsoiln` | `character(len=17)` | 386 |  |
| `gwsoilp` | `character(len=17)` | 387 |  |
| `plt_cov` | `character (len=16)` | 388 |  |
| `mgt_ops` | `character (len=30)` | 389 |  |

### output_nutbal_header_units

- **Defined in source**: `output_landscape_module.f90:393`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 394 |  |
| `mo` | `character (len=6)` | 395 |  |
| `day_mo` | `character (len=6)` | 396 |  |
| `yrc` | `character (len=6)` | 397 |  |
| `isd` | `character (len=9)` | 398 |  |
| `id` | `character (len=8)` | 399 |  |
| `name` | `character (len=16)` | 400 |  |
| `grazn` | `character(len=12)` | 401 |  |
| `grazp` | `character(len=12)` | 402 |  |
| `lab_min_p` | `character(len=12)` | 403 |  |
| `act_sta_p` | `character(len=12)` | 404 |  |
| `fertn` | `character(len=17)` | 405 |  |
| `fertp` | `character(len=17)` | 406 |  |
| `fixn` | `character(len=17)` | 407 |  |
| `denit` | `character(len=17)` | 408 |  |
| `act_nit_n` | `character(len=17)` | 409 |  |
| `act_sta_n` | `character(len=17)` | 410 |  |
| `org_lab_p` | `character(len=17)` | 411 |  |
| `rsd_nitorg_n` | `character(len=17)` | 412 |  |
| `rsd_laborg_p` | `character(len=17)` | 413 |  |
| `no3atmo` | `character(len=17)` | 414 |  |
| `nh4atmo` | `character(len=17)` | 415 |  |
| `nuptake` | `character(len=17)` | 416 |  |
| `puptake` | `character(len=17)` | 417 |  |
| `gwsoiln` | `character(len=17)` | 418 |  |
| `gwsoilp` | `character(len=17)` | 419 |  |

### output_losses_header

- **Defined in source**: `output_landscape_module.f90:423`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 424 |  |
| `mo` | `character (len=6)` | 425 |  |
| `day_mo` | `character (len=6)` | 426 |  |
| `yrc` | `character (len=6)` | 427 |  |
| `isd` | `character (len=8)` | 428 |  |
| `id` | `character (len=8)` | 429 |  |
| `name` | `character (len=16)` | 430 |  |
| `sedyld` | `character (len=17)` | 431 |  |
| `sedorgn` | `character (len=17)` | 432 |  |
| `sedorgp` | `character (len=17)` | 433 |  |
| `surqno3` | `character (len=17)` | 434 |  |
| `latno3` | `character (len=17)` | 435 |  |
| `surqsolp` | `character (len=17)` | 436 |  |
| `usle` | `character (len=17)` | 437 |  |
| `sedminp` | `character (len=17)` | 438 |  |
| `tileno3` | `character (len=17)` | 439 |  |
| `lchlabp` | `character (len=17)` | 440 |  |
| `tilelabp` | `character (len=17)` | 441 |  |
| `satexn` | `character (len=17)` | 442 |  |
| `plt_cov` | `character (len=16)` | 443 |  |
| `mgt_ops` | `character (len=30)` | 444 |  |
| `percn` | `character (len=12)` | 445 |  |

### output_losses_header_units

- **Defined in source**: `output_landscape_module.f90:449`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 450 |  |
| `mo` | `character (len=6)` | 451 |  |
| `day_mo` | `character (len=6)` | 452 |  |
| `yrc` | `character (len=6)` | 453 |  |
| `isd` | `character (len=8)` | 454 |  |
| `id` | `character (len=8)` | 455 |  |
| `name` | `character (len=16)` | 456 |  |
| `sedyld` | `character (len=17)` | 457 |  |
| `sedorgn` | `character (len=17)` | 458 |  |
| `sedorgp` | `character (len=17)` | 459 |  |
| `surqno3` | `character (len=17)` | 460 |  |
| `latno3` | `character (len=17)` | 461 |  |
| `surqsolp` | `character (len=17)` | 462 |  |
| `usle` | `character (len=17)` | 463 |  |
| `sedmin` | `character (len=17)` | 464 |  |
| `tileno3` | `character (len=17)` | 465 |  |
| `lchlabp` | `character (len=17)` | 466 |  |
| `tilelabp` | `character (len=17)` | 467 |  |
| `satexn` | `character (len=17)` | 468 |  |
| `plt_cov` | `character (len=16)` | 469 |  |
| `mgt_ops` | `character (len=30)` | 470 |  |
| `percn` | `character (len=12)` | 471 |  |

### output_nutcarb_cycling_header

- **Defined in source**: `output_landscape_module.f90:475`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 476 |  |
| `mo` | `character (len=6)` | 477 |  |
| `day_mo` | `character (len=6)` | 478 |  |
| `yrc` | `character (len=6)` | 479 |  |
| `isd` | `character (len=9)` | 480 |  |
| `id` | `character (len=8)` | 481 |  |
| `name` | `character (len=9)` | 482 |  |
| `lab_min_p` | `character(len=17)` | 483 |  |
| `act_sta_p` | `character(len=17)` | 484 |  |
| `act_nit_n` | `character(len=17)` | 485 |  |
| `act_sta_n` | `character(len=17)` | 486 |  |
| `org_lab_p` | `character(len=17)` | 487 |  |
| `rsd_hs_c` | `character(len=17)` | 488 |  |
| `rsd_nitorg_n` | `character(len=17)` | 489 |  |
| `rsd_laborg_p` | `character(len=17)` | 490 |  |

### output_nutbal_header_units1

- **Defined in source**: `output_landscape_module.f90:494`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 495 |  |
| `mo` | `character (len=6)` | 496 |  |
| `day_mo` | `character (len=6)` | 497 |  |
| `yrc` | `character (len=6)` | 498 |  |
| `isd` | `character (len=9)` | 499 |  |
| `id` | `character (len=8)` | 500 |  |
| `name` | `character (len=9)` | 501 |  |
| `lab_min_p` | `character(len=17)` | 502 |  |
| `act_sta_p` | `character(len=17)` | 503 |  |
| `act_nit_n` | `character(len=17)` | 504 |  |
| `act_sta_n` | `character(len=17)` | 505 |  |
| `org_lab_p` | `character(len=17)` | 506 |  |
| `rsd_hs_c` | `character(len=17)` | 507 |  |
| `rsd_nitorg_n` | `character(len=17)` | 508 |  |
| `rsd_laborg_p` | `character(len=17)` | 509 |  |

### output_carbon_header

- **Defined in source**: `output_landscape_module.f90:514`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 515 |  |
| `mo` | `character (len=6)` | 516 |  |
| `day_mo` | `character (len=6)` | 517 |  |
| `yrc` | `character (len=6)` | 518 |  |
| `isd` | `character (len=9)` | 519 |  |
| `id` | `character (len=8)` | 520 |  |
| `name` | `character (len=9)` | 521 |  |
| `sed_c` | `character(len=17)` | 522 |  |
| `surq_c` | `character(len=17)` | 523 |  |
| `surq_doc` | `character(len=17)` | 524 |  |
| `surq_dic` | `character(len=17)` | 525 |  |
| `latq_c` | `character(len=17)` | 526 |  |
| `latq_doc` | `character(len=17)` | 527 |  |
| `latq_dic` | `character(len=17)` | 528 |  |
| `perc_c` | `character(len=17)` | 529 |  |
| `perc_doc` | `character(len=17)` | 530 |  |
| `perc_dic` | `character(len=17)` | 531 |  |
| `npp_c` | `character(len=17)` | 532 |  |
| `rsd_c` | `character(len=17)` | 533 |  |
| `grain_c` | `character(len=17)` | 534 |  |
| `stover_c` | `character(len=17)` | 535 |  |
| `rsp_c` | `character(len=17)` | 536 |  |
| `emit_c` | `character(len=17)` | 537 |  |

### output_carbon_header_units1

- **Defined in source**: `output_landscape_module.f90:541`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=5)` | 542 |  |
| `mo` | `character (len=6)` | 543 |  |
| `day_mo` | `character (len=6)` | 544 |  |
| `yrc` | `character (len=6)` | 545 |  |
| `isd` | `character (len=9)` | 546 |  |
| `id` | `character (len=8)` | 547 |  |
| `name` | `character (len=9)` | 548 |  |
| `sed_c` | `character(len=17)` | 549 |  |
| `surq_c` | `character(len=17)` | 550 |  |
| `surq_doc` | `character(len=17)` | 551 |  |
| `surq_dic` | `character(len=17)` | 552 |  |
| `latq_c` | `character(len=17)` | 553 |  |
| `latq_doc` | `character(len=17)` | 554 |  |
| `latq_dic` | `character(len=17)` | 555 |  |
| `perc_c` | `character(len=17)` | 556 |  |
| `perc_doc` | `character(len=17)` | 557 |  |
| `perc_dic` | `character(len=17)` | 558 |  |
| `npp_c` | `character(len=17)` | 559 |  |
| `rsd_c` | `character(len=17)` | 560 |  |
| `grain_c` | `character(len=17)` | 561 |  |
| `stover_c` | `character(len=17)` | 562 |  |
| `rsp_c` | `character(len=17)` | 563 |  |
| `emit_c` | `character(len=17)` | 564 |  |

### output_carb_gl_header

- **Defined in source**: `output_landscape_module.f90:572`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 573 |  |
| `mo` | `character (len=11)` | 574 |  |
| `day_mo` | `character (len=11)` | 575 |  |
| `yrc` | `character (len=11)` | 576 |  |
| `isd` | `character (len=16)` | 577 |  |
| `id` | `character (len=21)` | 578 |  |
| `name` | `character (len=16)` | 579 |  |
| `sed_c` | `character (len=16)` | 580 |  |
| `surq_c` | `character (len=16)` | 581 |  |
| `latq_c` | `character (len=16)` | 582 |  |
| `perc_c` | `character (len=16)` | 583 |  |
| `res_decay` | `character (len=16)` | 584 |  |
| `man_app_c` | `character (len=16)` | 585 |  |
| `man_graze_c` | `character (len=16)` | 586 |  |
| `rsp_c` | `character (len=16)` | 587 |  |
| `soil_emit_c` | `character (len=16)` | 588 |  |
| `plant_surf_c` | `character (len=16)` | 589 |  |
| `plant_root_c` | `character (len=16)` | 590 |  |
| `rsd_surfdecay_c` | `character (len=16)` | 591 |  |
| `rsd_rootdecay_c` | `character (len=16)` | 592 |  |
| `harv_stov_c` | `character (len=16)` | 593 |  |
| `rsd_emit_c` | `character (len=16)` | 594 |  |
| `npp_c` | `character (len=16)` | 595 |  |
| `harv_abgr_c` | `character (len=16)` | 596 |  |
| `harv_root_c` | `character (len=16)` | 597 |  |
| `drop_c` | `character (len=16)` | 598 |  |
| `grazeat_c` | `character (len=16)` | 599 |  |
| `plant_emit_c` | `character (len=16)` | 600 |  |

### output_carb_gl_header_units

- **Defined in source**: `output_landscape_module.f90:604`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 605 |  |
| `mo` | `character (len=11)` | 606 |  |
| `day_mo` | `character (len=11)` | 607 |  |
| `yrc` | `character (len=11)` | 608 |  |
| `isd` | `character (len=16)` | 609 |  |
| `id` | `character (len=21)` | 610 |  |
| `name` | `character (len=16)` | 611 |  |
| `sed_c` | `character (len=16)` | 612 |  |
| `surq_c` | `character (len=16)` | 613 |  |
| `latq_c` | `character (len=16)` | 614 |  |
| `perc_c` | `character (len=16)` | 615 |  |
| `res_decay` | `character (len=16)` | 616 |  |
| `man_app_c` | `character (len=16)` | 617 |  |
| `man_graze_c` | `character (len=16)` | 618 |  |
| `rsp_c` | `character (len=16)` | 619 |  |
| `soil_emit_c` | `character (len=16)` | 620 |  |
| `plant_surf_c` | `character (len=16)` | 621 |  |
| `plant_root_c` | `character (len=16)` | 622 |  |
| `rsd_surfdecay_c` | `character (len=16)` | 623 |  |
| `rsd_rootdecay_c` | `character (len=16)` | 624 |  |
| `harv_stov_c` | `character (len=16)` | 625 |  |
| `rsd_emit_c` | `character (len=16)` | 626 |  |
| `npp_c` | `character (len=16)` | 627 |  |
| `harv_abgr_c` | `character (len=16)` | 628 |  |
| `harv_root_c` | `character (len=16)` | 629 |  |
| `drop_c` | `character (len=16)` | 630 |  |
| `grazeat_c` | `character (len=16)` | 631 |  |
| `plant_emit_c` | `character (len=16)` | 632 |  |

### output_hscf_header

- **Defined in source**: `output_landscape_module.f90:639`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 640 |  |
| `mo` | `character (len=11)` | 641 |  |
| `day_mo` | `character (len=11)` | 642 |  |
| `yrc` | `character (len=11)` | 643 |  |
| `isd` | `character (len=16)` | 644 |  |
| `id` | `character (len=21)` | 645 |  |
| `name` | `character (len=16)` | 646 |  |
| `meta_micr` | `character(len=15)` | 647 |  |
| `str_micr` | `character(len=15)` | 648 |  |
| `str_hs` | `character(len=15)` | 649 |  |
| `co2_meta` | `character(len=15)` | 650 |  |
| `co2_str` | `character(len=15)` | 651 |  |
| `micr_hs` | `character(len=15)` | 652 |  |
| `micr_hp` | `character(len=15)` | 653 |  |
| `hs_micr` | `character(len=15)` | 654 |  |
| `hs_hp` | `character(len=15)` | 655 |  |
| `hp_micr` | `character(len=15)` | 656 |  |
| `co2_micr` | `character(len=15)` | 657 |  |
| `co2_hs` | `character(len=15)` | 658 |  |
| `co2_hp` | `character(len=15)` | 659 |  |

### output_hscf_header_units

- **Defined in source**: `output_landscape_module.f90:663`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 664 |  |
| `mo` | `character (len=11)` | 665 |  |
| `day_mo` | `character (len=11)` | 666 |  |
| `yrc` | `character (len=11)` | 667 |  |
| `isd` | `character (len=16)` | 668 |  |
| `id` | `character (len=21)` | 669 |  |
| `name` | `character (len=16)` | 670 |  |
| `meta_micr` | `character(len=15)` | 671 |  |
| `str_micr` | `character(len=15)` | 672 |  |
| `str_hs` | `character(len=15)` | 673 |  |
| `co2_meta` | `character(len=15)` | 674 |  |
| `co2_str` | `character(len=15)` | 675 |  |
| `micr_hs` | `character(len=15)` | 676 |  |
| `micr_hp` | `character(len=15)` | 677 |  |
| `hs_micr` | `character(len=15)` | 678 |  |
| `hs_hp` | `character(len=15)` | 679 |  |
| `hp_micr` | `character(len=15)` | 680 |  |
| `co2_micr` | `character(len=15)` | 681 |  |
| `co2_hs` | `character(len=15)` | 682 |  |
| `co2_hp` | `character(len=15)` | 683 |  |

### output_losses_header1

- **Defined in source**: `output_landscape_module.f90:703`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 704 |  |
| `mo` | `character (len=6)` | 705 |  |
| `day_mo` | `character (len=6)` | 706 |  |
| `yrc` | `character (len=6)` | 707 |  |
| `isd` | `character (len=9)` | 708 |  |
| `id` | `character (len=8)` | 709 |  |
| `name` | `character (len=9)` | 710 |  |
| `sedyld` | `character (len=17)` | 711 |  |
| `usle` | `character (len=17)` | 712 |  |
| `sedorgc` | `character (len=17)` | 713 |  |
| `sedorgn` | `character (len=17)` | 714 |  |
| `sedorgp` | `character (len=17)` | 715 |  |
| `surqno3` | `character (len=17)` | 716 |  |
| `latno3` | `character (len=17)` | 717 |  |
| `surqsolp` | `character (len=17)` | 718 |  |
| `sedminp` | `character (len=17)` | 719 |  |
| `tileno3` | `character (len=17)` | 720 |  |
| `no3atmo` | `character (len=17)` | 721 |  |
| `nh4atmo` | `character (len=17)` | 722 |  |
| `manurec` | `character (len=17)` | 723 |  |
| `manuren` | `character (len=17)` | 724 |  |
| `manurep` | `character (len=17)` | 725 |  |
| `fertc` | `character (len=17)` | 726 |  |
| `fertn` | `character (len=17)` | 727 |  |
| `fertp` | `character (len=17)` | 728 |  |
| `grazc_eat` | `character (len=17)` | 729 |  |
| `gracn_eat` | `character (len=17)` | 730 |  |
| `gracp_eat` | `character (len=17)` | 731 |  |
| `grazc_man` | `character (len=17)` | 732 |  |
| `gracn_man` | `character (len=17)` | 733 |  |
| `gracp_man` | `character (len=17)` | 734 |  |
| `fixn` | `character (len=17)` | 735 |  |
| `denit` | `character (len=17)` | 736 |  |
| `yieldc` | `character (len=17)` | 737 |  |
| `yieldn` | `character (len=17)` | 738 |  |
| `yieldp` | `character (len=17)` | 739 |  |

### output_losses_header_units1

- **Defined in source**: `output_landscape_module.f90:743`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 744 |  |
| `mo` | `character (len=6)` | 745 |  |
| `day_mo` | `character (len=6)` | 746 |  |
| `yrc` | `character (len=6)` | 747 |  |
| `isd` | `character (len=9)` | 748 |  |
| `id` | `character (len=8)` | 749 |  |
| `name` | `character (len=9)` | 750 |  |
| `sedyld` | `character (len=17)` | 751 |  |
| `usle` | `character (len=17)` | 752 |  |
| `sedorgc` | `character (len=17)` | 753 |  |
| `sedorgn` | `character (len=17)` | 754 |  |
| `sedorgp` | `character (len=17)` | 755 |  |
| `surqno3` | `character (len=17)` | 756 |  |
| `latno3` | `character (len=17)` | 757 |  |
| `surqsolp` | `character (len=17)` | 758 |  |
| `sedmin` | `character (len=17)` | 759 |  |
| `tileno3` | `character (len=17)` | 760 |  |
| `no3atmo` | `character (len=17)` | 761 |  |
| `nh4atmo` | `character (len=17)` | 762 |  |
| `manurec` | `character (len=17)` | 763 |  |
| `manuren` | `character (len=17)` | 764 |  |
| `manurep` | `character (len=17)` | 765 |  |
| `fertc` | `character (len=17)` | 766 |  |
| `fertn` | `character (len=17)` | 767 |  |
| `fertp` | `character (len=17)` | 768 |  |
| `grazc_eat` | `character (len=17)` | 769 |  |
| `gracn_eat` | `character (len=17)` | 770 |  |
| `gracp_eat` | `character (len=17)` | 771 |  |
| `grazc_man` | `character (len=17)` | 772 |  |
| `gracn_man` | `character (len=17)` | 773 |  |
| `gracp_man` | `character (len=17)` | 774 |  |
| `fixn` | `character (len=17)` | 775 |  |
| `denit` | `character (len=17)` | 776 |  |
| `yieldc` | `character (len=17)` | 777 |  |
| `yieldn` | `character (len=17)` | 778 |  |
| `yieldp` | `character (len=17)` | 779 |  |

### output_plantweather_header

- **Defined in source**: `output_landscape_module.f90:783`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 784 |  |
| `mo` | `character (len=6)` | 785 |  |
| `day_mo` | `character (len=6)` | 786 |  |
| `yrc` | `character (len=6)` | 787 |  |
| `isd` | `character (len=8)` | 788 |  |
| `id` | `character (len=8)` | 789 |  |
| `name` | `character (len=16)` | 790 |  |
| `lai` | `character (len=13)` | 791 |  |
| `bioms` | `character (len=12)` | 792 |  |
| `yield` | `character (len=12)` | 793 |  |
| `residue` | `character (len=12)` | 794 |  |
| `sol_tmp` | `character (len=12)` | 795 |  |
| `strsw` | `character (len=12)` | 796 |  |
| `strsa` | `character (len=12)` | 797 |  |
| `strstmp` | `character (len=12)` | 798 |  |
| `strsn` | `character (len=12)` | 799 |  |
| `strsp` | `character (len=12)` | 800 |  |
| `strss` | `character (len=12)` | 801 |  |
| `nplnt` | `character (len=12)` | 802 |  |
| `percn` | `character (len=12)` | 803 |  |
| `pplnt` | `character (len=12)` | 804 |  |
| `tmx` | `character (len=12)` | 805 |  |
| `tmn` | `character (len=12)` | 806 |  |
| `tmpav` | `character (len=12)` | 807 |  |
| `solrad` | `character (len=12)` | 808 |  |
| `wndspd` | `character (len=12)` | 809 |  |
| `rhum` | `character (len=12)` | 810 |  |
| `phubase0` | `character (len=12)` | 811 |  |
| `lai_max` | `character (len=12)` | 812 |  |
| `bm_max` | `character (len=12)` | 813 |  |
| `bm_grow` | `character (len=12)` | 814 |  |
| `c_gro` | `character (len=12)` | 815 |  |
| `plt_cov` | `character (len=16)` | 816 |  |
| `mgt_ops` | `character (len=30)` | 817 |  |

### output_plantweather_header_units

- **Defined in source**: `output_landscape_module.f90:821`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 822 |  |
| `mo` | `character (len=6)` | 823 |  |
| `day_mo` | `character (len=6)` | 824 |  |
| `yrc` | `character (len=6)` | 825 |  |
| `isd` | `character (len=8)` | 826 |  |
| `id` | `character (len=8)` | 827 |  |
| `name` | `character (len=16)` | 828 |  |
| `lai` | `character (len=13)` | 829 |  |
| `bioms` | `character (len=12)` | 830 |  |
| `yield` | `character (len=12)` | 831 |  |
| `residue` | `character (len=12)` | 832 |  |
| `sol_tmp` | `character (len=12)` | 833 |  |
| `strsw` | `character (len=12)` | 834 |  |
| `strsa` | `character (len=12)` | 835 |  |
| `strstmp` | `character (len=12)` | 836 |  |
| `strsn` | `character (len=12)` | 837 |  |
| `strsp` | `character (len=12)` | 838 |  |
| `strss` | `character (len=12)` | 839 |  |
| `nplnt` | `character (len=12)` | 840 |  |
| `percn` | `character (len=12)` | 841 |  |
| `pplnt` | `character (len=12)` | 842 |  |
| `tmx` | `character (len=12)` | 843 |  |
| `tmn` | `character (len=12)` | 844 |  |
| `tmpav` | `character (len=12)` | 845 |  |
| `solrad` | `character (len=12)` | 846 |  |
| `wndspd` | `character (len=12)` | 847 |  |
| `rhum` | `character (len=12)` | 848 |  |
| `phubase0` | `character (len=12)` | 849 |  |
| `lai_max` | `character (len=12)` | 850 |  |
| `bm_max` | `character (len=12)` | 851 |  |
| `bm_grow` | `character (len=12)` | 852 |  |
| `c_gro` | `character (len=12)` | 853 |  |

## Variables Defined
### h

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:50`

### hwb_d

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:51`

### hwb_m

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:52`

### hwb_y

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:53`

### hwb_a

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:54`

### hwbz

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:55`

### hltwb_d

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:57`

### hltwb_m

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:58`

### hltwb_y

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:59`

### hltwb_a

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:60`

### lsu_wb_d

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:62`
- **Source note**: output for using components of lsus in ch_temp

### ruwb_d

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:63`

### ruwb_m

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:64`

### ruwb_y

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:65`

### ruwb_a

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:66`

### bwb_d

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:68`

### bwb_m

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:69`

### bwb_y

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:70`

### bwb_a

- **Type**: `output_waterbal`
- **Defined in source**: `output_landscape_module.f90:71`

### rwb_d

- **Type**: `regional_output_waterbal`
- **Defined in source**: `output_landscape_module.f90:76`

### rwb_m

- **Type**: `regional_output_waterbal`
- **Defined in source**: `output_landscape_module.f90:77`

### rwb_y

- **Type**: `regional_output_waterbal`
- **Defined in source**: `output_landscape_module.f90:78`

### rwb_a

- **Type**: `regional_output_waterbal`
- **Defined in source**: `output_landscape_module.f90:79`

### hnb_d

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:106`

### hnb_m

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:107`

### hnb_y

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:108`

### hnb_a

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:109`

### hnbz

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:110`

### hltnb_d

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:112`

### hltnb_m

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:113`

### hltnb_y

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:114`

### hltnb_a

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:115`

### runb_d

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:117`

### runb_m

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:118`

### runb_y

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:119`

### runb_a

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:120`

### bnb_d

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:122`

### bnb_m

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:123`

### bnb_y

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:124`

### bnb_a

- **Type**: `output_nutbal`
- **Defined in source**: `output_landscape_module.f90:125`

### rnb_d

- **Type**: `regional_output_nutbal`
- **Defined in source**: `output_landscape_module.f90:130`

### rnb_m

- **Type**: `regional_output_nutbal`
- **Defined in source**: `output_landscape_module.f90:131`

### rnb_y

- **Type**: `regional_output_nutbal`
- **Defined in source**: `output_landscape_module.f90:132`

### rnb_a

- **Type**: `regional_output_nutbal`
- **Defined in source**: `output_landscape_module.f90:133`

### hcyl_d

- **Type**: `output_nutcarb_cycling`
- **Defined in source**: `output_landscape_module.f90:146`

### hcyl_m

- **Type**: `output_nutcarb_cycling`
- **Defined in source**: `output_landscape_module.f90:147`

### hcyl_y

- **Type**: `output_nutcarb_cycling`
- **Defined in source**: `output_landscape_module.f90:148`

### hcyl_a

- **Type**: `output_nutcarb_cycling`
- **Defined in source**: `output_landscape_module.f90:149`

### hycl_z

- **Type**: `output_nutcarb_cycling`
- **Defined in source**: `output_landscape_module.f90:150`

### hls_d

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:167`

### hls_m

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:168`

### hls_y

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:169`

### hls_a

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:170`

### hlsz

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:171`

### hltls_d

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:173`

### hltls_m

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:174`

### hltls_y

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:175`

### hltls_a

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:176`

### ruls_d

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:178`

### ruls_m

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:179`

### ruls_y

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:180`

### ruls_a

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:181`

### bls_d

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:183`

### bls_m

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:184`

### bls_y

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:185`

### bls_a

- **Type**: `output_losses`
- **Defined in source**: `output_landscape_module.f90:186`

### rls_d

- **Type**: `regional_output_losses`
- **Defined in source**: `output_landscape_module.f90:191`

### rls_m

- **Type**: `regional_output_losses`
- **Defined in source**: `output_landscape_module.f90:192`

### rls_y

- **Type**: `regional_output_losses`
- **Defined in source**: `output_landscape_module.f90:193`

### rls_a

- **Type**: `regional_output_losses`
- **Defined in source**: `output_landscape_module.f90:194`

### hpw_d

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:224`

### hpw_m

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:225`

### hpw_y

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:226`

### hpw_a

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:227`

### hpwz

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:228`

### hltpw_d

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:230`

### hltpw_m

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:231`

### hltpw_y

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:232`

### hltpw_a

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:233`

### rupw_d

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:235`

### rupw_m

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:236`

### rupw_y

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:237`

### rupw_a

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:238`

### bpw_d

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:240`

### bpw_m

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:241`

### bpw_y

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:242`

### bpw_a

- **Type**: `output_plantweather`
- **Defined in source**: `output_landscape_module.f90:243`

### rpw_d

- **Type**: `regional_output_plantweather`
- **Defined in source**: `output_landscape_module.f90:248`

### rpw_m

- **Type**: `regional_output_plantweather`
- **Defined in source**: `output_landscape_module.f90:249`

### rpw_y

- **Type**: `regional_output_plantweather`
- **Defined in source**: `output_landscape_module.f90:250`

### rpw_a

- **Type**: `regional_output_plantweather`
- **Defined in source**: `output_landscape_module.f90:251`

### wb_hdr

- **Type**: `output_waterbal_header`
- **Defined in source**: `output_landscape_module.f90:306`

### wb_hdr_units

- **Type**: `output_waterbal_header_units`
- **Defined in source**: `output_landscape_module.f90:359`

### nb_hdr

- **Type**: `output_nutbal_header`
- **Defined in source**: `output_landscape_module.f90:391`

### nb_hdr_units

- **Type**: `output_nutbal_header_units`
- **Defined in source**: `output_landscape_module.f90:421`

### ls_hdr

- **Type**: `output_losses_header`
- **Defined in source**: `output_landscape_module.f90:447`

### ls_hdr_units

- **Type**: `output_losses_header_units`
- **Defined in source**: `output_landscape_module.f90:473`

### nb_hdr1

- **Type**: `output_nutcarb_cycling_header`
- **Defined in source**: `output_landscape_module.f90:492`

### nb_hdr_units1

- **Type**: `output_nutbal_header_units1`
- **Defined in source**: `output_landscape_module.f90:511`

### carbon_hdr1

- **Type**: `output_carbon_header`
- **Defined in source**: `output_landscape_module.f90:539`

### carbon_hdr_units1

- **Type**: `output_carbon_header_units1`
- **Defined in source**: `output_landscape_module.f90:566`

### carb_gl_hdr

- **Type**: `output_carb_gl_header`
- **Defined in source**: `output_landscape_module.f90:602`

### carb_gl_hdr_units

- **Type**: `output_carb_gl_header_units`
- **Defined in source**: `output_landscape_module.f90:634`

### hscf_hdr

- **Type**: `output_hscf_header`
- **Defined in source**: `output_landscape_module.f90:661`

### hscf_hdr_units

- **Type**: `output_hscf_header_units`
- **Defined in source**: `output_landscape_module.f90:685`

### ls_hdr1

- **Type**: `output_losses_header1`
- **Defined in source**: `output_landscape_module.f90:741`

### ls_hdr_units1

- **Type**: `output_losses_header_units1`
- **Defined in source**: `output_landscape_module.f90:781`

### pw_hdr

- **Type**: `output_plantweather_header`
- **Defined in source**: `output_landscape_module.f90:819`

### pw_hdr_units

- **Type**: `output_plantweather_header_units`
- **Defined in source**: `output_landscape_module.f90:855`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### hruout_waterbal_add

### hruout_nutbal_add

### hruout_losses_add

### hruout_nut_cycling_add

### hruout_nut_cycling_mult

### hruout_nut_cycling_div

### hruout_plantweather_add

### hruout_waterbal_div

### hruout_waterbal_ave

### hruout_waterbal_mult

### hruout_nutbal_div

### hruout_nutbal_mult

### hruout_losses_div

### hruout_losses_mult

### hruout_plantweather_div

### hruout_plantweather_ave

### hruout_plantweather_mult

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

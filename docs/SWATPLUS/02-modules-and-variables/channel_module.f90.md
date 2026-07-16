---
type: module
tags:
  - swat/module
  - swat/to-read
file: channel_module.f90
note_file: channel_module.f90
module_name: channel_module
defines_types:
  - channel
  - ch_output
  - regional_output_channel
  - ch_header
  - ch_header_units
defines_vars:
  - jhyd
  - jsed
  - jnut
  - rttime
  - ben_area
  - rchdep
  - rtevp
  - rttlc
  - pet_ch
  - hrtwtr
  - hharea
  - hdepth
  - rhy
  - hsdti
  - hhtime
  - hrttlc
  - hrtevp
  - hhstor
  - hrchwtr
  - halgae
  - hbactlp
  - hbactp
  - hbod
  - hchla
  - hdisox
  - hnh4
  - hno2
  - hno3
  - horgn
  - horgp
  - hsedst
  - hsedyld
  - hsolp
  - hsolpst
  - hsorpst
  - rchsep
  - peakr
  - rcharea
  - sdti
  - bnkrte
  - degrte
  - sedrch
  - rch_san
  - rch_sil
  - rch_cla
  - rch_sag
  - rtwtr_d
  - rt_delt
  - rch_lag
  - rch_gra
  - rtwtr
  - wtrin
  - sed_ch
  - ch
  - rch_d
  - rch_m
  - rch_y
  - rch_a
  - ch_d
  - ch_m
  - ch_y
  - ch_a
  - bch_d
  - bch_m
  - bch_y
  - bch_a
  - chz
  - ch_hdr
  - ch_hdr_units
defines_subroutines: []
defines_functions:
  - ch_add
  - ch_div
  - ch_mult
defines_procedures:
  - ch_add
  - ch_div
  - ch_mult
purpose: ""
---

# channel_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### channel

- **Defined in source**: `channel_module.f90:61`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `algae` | `real` | 62 | mg alg/L \|algal biomass concentration in reach |
| `ammonian` | `real` | 63 | mg N/L \|ammonia concentration in reach |
| `bankst` | `real` | 64 | m^3 H2O \|bank storage |
| `li` | `real` | 65 | km \|initial length of main channel |
| `orgn` | `real` | 66 | \|organic nitrogen contribution from channel erosion |
| `orgp` | `real` | 67 | \|organic phosphorus contribution from channel erosion |
| `si` | `real` | 68 | (m/n) \|slope of main channel |
| `wi` | `real` | 69 | (m) \|width of main channel at top of bank |
| `di` | `real` | 70 | (m) \|depth of main channel from top of bank to bottom |
| `chlora` | `real` | 71 | mg chl-a/L \|chlorophyll-a concentration in reach |
| `pst_conc` | `real` | 72 | mg/(m**3) \|initial pesticide concentration in reach |
| `dep_chan` | `real` | 73 | m \|average daily water depth in channel |
| `disolvp` | `real` | 74 | mg P/L \|dissolved P concentration in reach |
| `drift` | `real` | 75 | kg \|amount of pesticide drifting onto main channel in subbasin |
| `flwin` | `real` | 76 | m^3 H2O \|flow into reach on previous day |
| `flwout` | `real` | 77 | m^3 H2O \|flow out of reach on previous day |
| `nitraten` | `real` | 78 | mg N/L \|nitrate concentration in reach |
| `nitriten` | `real` | 79 | mg N/L \|nitrite concentration in reach |
| `organicn` | `real` | 80 | mg N/L \|organic nitrogen concentration in reach |
| `organicp` | `real` | 81 | mg P/L \|organic phosphorus concentration in reach |
| `rch_bactlp` | `real` | 82 | # cfu/100ml \|less persistent bacteria stored in reach |
| `rch_bactp` | `real` | 83 | # cfu/100ml \|persistent bacteria stored in reach |
| `rch_cbod` | `real` | 84 | mg O2/L \|carbonaceous biochemical oxygen demand in reach |
| `rch_dox` | `real` | 85 | mg O2/L \|dissolved oxygen concentration in reach |
| `rchstor` | `real` | 86 | m^3 H2O \|water stored in reach |
| `sedst` | `real` | 87 | metric tons \|amount of sediment stored in reach |
| `vel_chan` | `real` | 88 | m/s \|average flow velocity in channel |
| `bed_san` | `real` | 89 |  |
| `bed_sil` | `real` | 90 |  |
| `bed_cla` | `real` | 91 |  |
| `bed_gra` | `real` | 92 |  |
| `bnk_san` | `real` | 93 |  |
| `bnk_sil` | `real` | 94 |  |
| `bnk_cla` | `real` | 95 |  |
| `bnk_gra` | `real` | 96 |  |
| `depfp` | `real` | 97 |  |
| `depprfp` | `real` | 98 |  |
| `depsilfp` | `real` | 99 |  |
| `depclafp` | `real` | 100 |  |
| `depch` | `real` | 101 |  |
| `depprch` | `real` | 102 |  |
| `depsanch` | `real` | 103 |  |
| `depsilch` | `real` | 104 |  |
| `depclach` | `real` | 105 |  |
| `depsagch` | `real` | 106 |  |
| `deplagch` | `real` | 107 |  |
| `depgrach` | `real` | 108 |  |
| `sanst` | `real` | 109 |  |
| `silst` | `real` | 110 |  |
| `clast` | `real` | 111 |  |
| `sagst` | `real` | 112 |  |
| `lagst` | `real` | 113 |  |
| `grast` | `real` | 114 |  |
| `wattemp` | `real` | 115 |  |
| `bactp` | `real` | 116 |  |
| `chfloodvol` | `real` | 117 |  |
| `bactlp` | `real` | 118 |  |

### ch_output

- **Defined in source**: `channel_module.f90:122`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `real` | 123 | (ha-m) \|streamflow into reach during time step |
| `flo_out` | `real` | 124 | (ha-m) \|streamflow out of reach during time step |
| `evap` | `real` | 125 | (m^3/s) \|daily rate of water loss from reach by evaporation |
| `tloss` | `real` | 126 | (m^3/s) \|rate of water loss from reach by transmission through the streambed |
| `sed_in` | `real` | 127 | (tons) \|sediment transported with water into reach |
| `sed_out` | `real` | 128 | (tons) \|sediment transported with water out of reach |
| `sed_conc` | `real` | 129 | (mg/L) \|concentration of sediment in reach |
| `orgn_in` | `real` | 130 | (kg N) \|organic nitrogen transported with water into reach |
| `orgn_out` | `real` | 131 | (kg N) \|organic nitrogen transported with water out of reach |
| `orgp_in` | `real` | 132 | (kg P) \|organic phosphorus transported with water into reach |
| `orgp_out` | `real` | 133 | (kg P) \|organic phosphorus transported with water out of reach |
| `no3_in` | `real` | 134 | (kg N) \|nitrate transported with water into reach |
| `no3_out` | `real` | 135 | (kg N) \|nitrate transported with water out of reach |
| `nh4_in` | `real` | 136 | (kg) \|ammonium transported with water into reach |
| `nh4_out` | `real` | 137 | (kg) \|ammonium transported with water out of reach |
| `no2_in` | `real` | 138 | (kg) \|nitrite transported with water into reach |
| `no2_out` | `real` | 139 | (kg) \|nitrite transported with water out of reach |
| `solp_in` | `real` | 140 | (kg P) \|soluble pesticide transported with water into reach |
| `solp_out` | `real` | 141 | (kg P) \|soluble pesticide transported with water out of reach |
| `chla_in` | `real` | 142 | (kg) \|amount of chlorophyll a transported into reach |
| `chla_out` | `real` | 143 | (kg) \|amount of chlorophyll a transported out of reach |
| `cbod_in` | `real` | 144 | (kg) \|carbonaceous biochemical oxygen demand of material transported into reach |
| `cbod_out` | `real` | 145 | (kg) \|carbonaceous biochemical oxygen demand of material transported out of reach |
| `dis_in` | `real` | 146 | (kg) \|amount of dissolved oxygen transported into reach |
| `dis_out` | `real` | 147 | (kg) \|amount of dissolved oxygen transported out of reach |
| `solpst_in` | `real` | 148 | (mg pst) \|soluble pesticide transported with water into reach |
| `solpst_out` | `real` | 149 | (mg pst) \|soluble pesticide transported with water out of reach |
| `sorbpst_in` | `real` | 150 | (mg pst) \|pesticide sorbed to sediment transported with water into reach |
| `sorbpst_out` | `real` | 151 | (mg pst) \|pesticide sorbed to sediment transported with water out of reach |
| `react` | `real` | 152 | (mg pst) \|loss of pesticide from water from reaction |
| `volat` | `real` | 153 | (mg) \|loss of pesticide from water by volatilization |
| `setlpst` | `real` | 154 | (mg pst) \|transfer of pesticide from water to river bed sediment by settling |
| `resuspst` | `real` | 155 | (mg) \|transfer of pesticide from river bed sediment to water by resuspension |
| `difus` | `real` | 156 | mg \|transfer of pesticide from water to river bed sediment by diffusion |
| `reactb` | `real` | 157 | (mg) \|loss of pesticide from river bed sediment by reaction |
| `bury` | `real` | 158 | (mg) \|loss of pesticide from river bed sediment by burial |
| `sedpest` | `real` | 159 | mg \|pesticide in river bed sediment |
| `bacp` | `real` | 160 | # cfu/100mL \|number of persistent bacteria transported out of reach |
| `baclp` | `real` | 161 | # cfu/100mL \|number of less persistent bacteria transported out of reach |
| `met1` | `real` | 162 | kg \|conservative metal #1 transported out of reach |
| `met2` | `real` | 163 | kg \|conservative metal #2 transported out of reach |
| `met3` | `real` | 164 | kg \|conservative metal #3 transported out of reach |
| `sand_in` | `real` | 165 | tons \|sand in |
| `sand_out` | `real` | 166 | tons \|sand out |
| `silt_in` | `real` | 167 | tons \|silt_in |
| `silt_out` | `real` | 168 | tons \|silt_out |
| `clay_in` | `real` | 169 | tons \|clay_in |
| `clay_out` | `real` | 170 | tons \|clay_out |
| `smag_in` | `real` | 171 | tons \|small aggregates transported into reach |
| `smag_out` | `real` | 172 | tons \|small aggregates transported out of reach |
| `lag_in` | `real` | 173 | tons \|large aggregates transported into reachlg ag in |
| `lag_out` | `real` | 174 | tons \|large aggregates transported out of reach |
| `grvl_in` | `real` | 175 | tons \|gravel in |
| `grvl_out` | `real` | 176 | tons \|gravel out |
| `bnk_ero` | `real` | 177 | tons \|bank erosion |
| `ch_deg` | `real` | 178 | tons \|channel degradation |
| `ch_dep` | `real` | 179 | tons \|channel deposition |
| `fp_dep` | `real` | 180 | tons \|flood deposition |
| `tot_ssed` | `real` | 181 | mg/L \|total suspended sediments |

### regional_output_channel

- **Defined in source**: `channel_module.f90:184`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ord` | `ch_output` | 185 |  |

### ch_header

- **Defined in source**: `channel_module.f90:202`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 203 |  |
| `mo` | `character (len=6)` | 204 |  |
| `day_mo` | `character (len=6)` | 205 |  |
| `yrc` | `character (len=5)` | 206 |  |
| `isd` | `character (len=9)` | 207 |  |
| `id` | `character (len=8)` | 208 |  |
| `name` | `character (len=16)` | 209 |  |
| `flo_in` | `character(len=16)` | 210 | (ha-m) |
| `flo_out` | `character(len=15)` | 211 | (ha-m) |
| `evap` | `character(len=15)` | 212 | (ha-m) |
| `tloss` | `character(len=15)` | 213 | (ha-m) |
| `sed_in` | `character(len=15)` | 214 | (tons) |
| `sed_out` | `character(len=15)` | 215 | (tons) |
| `sed_conc` | `character(len=15)` | 216 | (mg/L) |
| `orgn_in` | `character(len=15)` | 217 | (kg N) |
| `orgn_out` | `character(len=15)` | 218 | (kg N) |
| `orgp_in` | `character(len=15)` | 219 | (kg P) |
| `orgp_out` | `character(len=15)` | 220 | (kg P) |
| `no3_in` | `character(len=15)` | 221 | (kg N) |
| `no3_out` | `character(len=15)` | 222 | (kg N) |
| `nh4_in` | `character(len=15)` | 223 | (kg) |
| `nh4_out` | `character(len=15)` | 224 | (kg) |
| `no2_in` | `character(len=15)` | 225 | (kg) |
| `no2_out` | `character(len=15)` | 226 | (kg) |
| `solp_in` | `character(len=15)` | 227 | (kg P) |
| `solp_out` | `character(len=15)` | 228 | (kg P) |
| `chla_in` | `character(len=15)` | 229 | (kg) |
| `chla_out` | `character(len=15)` | 230 | (kg) |
| `cbod_in` | `character(len=15)` | 231 | (kg) |
| `cbod_out` | `character(len=15)` | 232 | (kg) |
| `dis_in` | `character(len=15)` | 233 | (kg) |
| `dis_out` | `character(len=15)` | 234 | (kg) |
| `solpst_in` | `character(len=15)` | 235 | (mg pst) |
| `solpst_out` | `character(len=15)` | 236 | (mg pst) |
| `sorbpst_in` | `character(len=15)` | 237 | (mg pst) |
| `sorbpst_out` | `character(len=15)` | 238 | (mg pst) |
| `react` | `character(len=15)` | 239 | (mg pst) |
| `volat` | `character(len=15)` | 240 | (mg) |
| `setlpst` | `character(len=15)` | 241 | (mg pst) |
| `resuspst` | `character(len=15)` | 242 | (mg) |
| `difus` | `character(len=15)` | 243 | (mg pst) |
| `reactb` | `character(len=15)` | 244 | pst/sed (mg) |
| `bury` | `character(len=15)` | 245 | pst bury (mg) |
| `sedpest` | `character(len=15)` | 246 | pst in rivbed sed mg |
| `bacp` | `character(len=15)` | 247 | persistent bact out |
| `baclp` | `character(len=15)` | 248 | lpersistent bact out |
| `met1` | `character(len=15)` | 249 | cmetal #1 |
| `met2` | `character(len=15)` | 250 | cmetal #2 |
| `met3` | `character(len=15)` | 251 | cmetal #3 |
| `sand_in` | `character(len=15)` | 252 | sand in |
| `sand_out` | `character(len=15)` | 253 | sand out |
| `silt_in` | `character(len=15)` | 254 | silt_in |
| `silt_out` | `character(len=15)` | 255 | silt_out |
| `clay_in` | `character(len=15)` | 256 | clay_in |
| `clay_out` | `character(len=15)` | 257 | clay_out |
| `smag_in` | `character(len=15)` | 258 | sm ag in |
| `smag_out` | `character(len=15)` | 259 | sm ag out |
| `lag_in` | `character(len=15)` | 260 | lg ag in |
| `lag_out` | `character(len=15)` | 261 | lg ag out |
| `grvl_in` | `character(len=15)` | 262 | gravel in |
| `grvl_out` | `character(len=15)` | 263 | gravel out |
| `bnk_ero` | `character(len=15)` | 264 | bank erosion |
| `ch_deg` | `character(len=15)` | 265 | channel degradation |
| `ch_dep` | `character(len=15)` | 266 | channel deposition |
| `fp_dep` | `character(len=15)` | 267 | flood deposition |
| `tot_ssed` | `character(len=15)` | 268 | total suspended sediments |

### ch_header_units

- **Defined in source**: `channel_module.f90:272`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 273 |  |
| `mo` | `character (len=6)` | 274 |  |
| `day_mo` | `character (len=6)` | 275 |  |
| `yrc` | `character (len=5)` | 276 |  |
| `isd` | `character (len=9)` | 277 |  |
| `id` | `character (len=8)` | 278 |  |
| `name` | `character (len=16)` | 279 |  |
| `flo_in` | `character(len=16)` | 280 | (ha-m) |
| `flo_out` | `character(len=15)` | 281 | (ha-m) |
| `evap` | `character(len=15)` | 282 | (ha-m) |
| `tloss` | `character(len=15)` | 283 | (ha-m) |
| `sed_in` | `character(len=15)` | 284 | (tons) |
| `sed_out` | `character(len=15)` | 285 | (tons) |
| `sed_conc` | `character(len=15)` | 286 | (mg/L) |
| `orgn_in` | `character(len=15)` | 287 | (kg N) |
| `orgn_out` | `character(len=15)` | 288 | (kg N) |
| `orgp_in` | `character(len=15)` | 289 | (kg P) |
| `orgp_out` | `character(len=15)` | 290 | (kg P) |
| `no3_in` | `character(len=15)` | 291 | (kg N) |
| `no3_out` | `character(len=15)` | 292 | (kg N) |
| `nh4_in` | `character(len=15)` | 293 | (kg) |
| `nh4_out` | `character(len=15)` | 294 | (kg) |
| `no2_in` | `character(len=15)` | 295 | (kg) |
| `no2_out` | `character(len=15)` | 296 | (kg) |
| `solp_in` | `character(len=15)` | 297 | (kg P) |
| `solp_out` | `character(len=15)` | 298 | (kg P) |
| `chla_in` | `character(len=15)` | 299 | (kg) |
| `chla_out` | `character(len=15)` | 300 | (kg) |
| `cbod_in` | `character(len=15)` | 301 | (kg) |
| `cbod_out` | `character(len=15)` | 302 | (kg) |
| `dis_in` | `character(len=15)` | 303 | (kg) |
| `dis_out` | `character(len=15)` | 304 | (kg) |
| `solpst_in` | `character(len=15)` | 305 | (mg pst) |
| `solpst_out` | `character(len=15)` | 306 | (mg pst) |
| `sorbpst_in` | `character(len=15)` | 307 | (mg pst) |
| `sorbpst_out` | `character(len=15)` | 308 | (mg pst) |
| `react` | `character(len=15)` | 309 | (mg pst) |
| `volat` | `character(len=15)` | 310 | (mg) |
| `setlpst` | `character(len=15)` | 311 | (mg pst) |
| `resuspst` | `character(len=15)` | 312 | (mg) |
| `difus` | `character(len=15)` | 313 | (mg pst) |
| `reactb` | `character(len=15)` | 314 | pst/sed (mg) |
| `bury` | `character(len=15)` | 315 | pst bury (mg) |
| `sedpest` | `character(len=15)` | 316 | pst in rivbed sed mg |
| `bacp` | `character(len=15)` | 317 | persistent bact out |
| `baclp` | `character(len=15)` | 318 | lpersistent bact out |
| `met1` | `character(len=15)` | 319 | cmetal #1 |
| `met2` | `character(len=15)` | 320 | cmetal #2 |
| `met3` | `character(len=15)` | 321 | cmetal #3 |
| `sand_in` | `character(len=15)` | 322 | sand in |
| `sand_out` | `character(len=15)` | 323 | sand out |
| `silt_in` | `character(len=15)` | 324 | silt_in |
| `silt_out` | `character(len=15)` | 325 | silt_out |
| `clay_in` | `character(len=15)` | 326 | clay_in |
| `clay_out` | `character(len=15)` | 327 | clay_out |
| `smag_in` | `character(len=15)` | 328 | sm ag in |
| `smag_out` | `character(len=15)` | 329 | sm ag out |
| `lag_in` | `character(len=15)` | 330 | lg ag in |
| `lag_out` | `character(len=15)` | 331 | lg ag out |
| `grvl_in` | `character(len=15)` | 332 | gravel in |
| `grvl_out` | `character(len=15)` | 333 | gravel out |
| `bnk_ero` | `character(len=15)` | 334 | bank erosion |
| `ch_deg` | `character(len=15)` | 335 | channel degradation |
| `ch_dep` | `character(len=15)` | 336 | channel deposition |
| `fp_dep` | `character(len=15)` | 337 | flood deposition |
| `tot_ssed` | `character(len=15)` | 338 | total suspended sediments |

## Variables Defined
### jhyd

- **Type**: `integer`
- **Defined in source**: `channel_module.f90:5`
- **Source note**: units         |description

### jsed

- **Type**: `integer`
- **Defined in source**: `channel_module.f90:6`
- **Source note**: units         |description

### jnut

- **Type**: `integer`
- **Defined in source**: `channel_module.f90:7`
- **Source note**: units         |description

### rttime

- **Type**: `real`
- **Defined in source**: `channel_module.f90:8`
- **Source note**: hr            |reach travel time

### ben_area

- **Type**: `real`
- **Defined in source**: `channel_module.f90:9`
- **Source note**: m2            |benthic area (bottom sediments)

### rchdep

- **Type**: `real`
- **Defined in source**: `channel_module.f90:10`
- **Source note**: m             |depth of flow on day

### rtevp

- **Type**: `real`
- **Defined in source**: `channel_module.f90:11`
- **Source note**: m^3 H2O       |evaporation from reach on day

### rttlc

- **Type**: `real`
- **Defined in source**: `channel_module.f90:12`
- **Source note**: m^3 H2O       |transmission losses from reach on day

### pet_ch

- **Type**: `real`
- **Defined in source**: `channel_module.f90:13`
- **Source note**: mm           |potential evaporation from reach on day

### hrtwtr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:14`
- **Source note**: m^3 H2O       |water leaving reach

### hharea

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:15`
- **Source note**: m^2           |cross-sectional area of flow

### hdepth

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:16`
- **Source note**: m             |depth of flow

### rhy

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:17`
- **Source note**: m H2O         |main channel hydraulic radius

### hsdti

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:18`
- **Source note**: m^3/s         |flow rate in reach for hour

### hhtime

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:19`
- **Source note**: hr            |flow travel time for hour

### hrttlc

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:20`
- **Source note**: m^3 H2O       |transmission losses from reach during time step

### hrtevp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:21`
- **Source note**: m^3 H2O       |evaporation from reach during time step

### hhstor

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:22`
- **Source note**: m^3 H2O       |water stored in reach at end of hour

### hrchwtr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:23`
- **Source note**: m^3 H2O       |water stored at beginning of day

### halgae

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:24`
- **Source note**: mg alg/L      |algal biomass concentration in reach

### hbactlp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:25`
- **Source note**: # cfu/100mL   |less persistent bacteria in reach/outflow during hour

### hbactp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:26`
- **Source note**: # cfu/100mL   |persistent bacteria in reach/outflow during hour

### hbod

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:27`
- **Source note**: mg O2/L       |carbonaceous biochemical oxygen demand inreach at end of hour

### hchla

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:28`
- **Source note**: mg chl-a/L    |chlorophyll-a concentration in reach at end of hour

### hdisox

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:29`
- **Source note**: mg O2/L       |dissolved oxygen concentration in reach at end of hour

### hnh4

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:30`
- **Source note**: mg N/L        |ammonia concentration in reach at end of hour

### hno2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:31`
- **Source note**: mg N/L        |nitrite concentration in reach at end of hour

### hno3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:32`
- **Source note**: mg N/L        |nitrate concentration in reach at end of hour

### horgn

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:33`
- **Source note**: mg N/L        |organic nitrogen concentration in reach at end of hour

### horgp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:34`
- **Source note**: mg P/L        |organic phosphorus concentration in reach at end of hour

### hsedst

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:35`
- **Source note**: metric tons   |amount of sediment stored in reach at the end of hour

### hsedyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:36`
- **Source note**: metric tons   |sediment transported out of reach during hour

### hsolp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:37`
- **Source note**: mg P/L        |dissolved phosphorus concentration in reach at end of hour

### hsolpst

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:38`
- **Source note**: mg pst/m^3    |soluble pesticide concentration in outflow on day

### hsorpst

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:39`
- **Source note**: mg pst/m^3    |sorbed pesticide concentration in outflow on day

### rchsep

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `channel_module.f90:40`

### peakr

- **Type**: `real`
- **Defined in source**: `channel_module.f90:42`

### rcharea

- **Type**: `real`
- **Defined in source**: `channel_module.f90:43`

### sdti

- **Type**: `real`
- **Defined in source**: `channel_module.f90:44`

### bnkrte

- **Type**: `real`
- **Defined in source**: `channel_module.f90:45`

### degrte

- **Type**: `real`
- **Defined in source**: `channel_module.f90:46`

### sedrch

- **Type**: `real`
- **Defined in source**: `channel_module.f90:47`
- **Source note**: metric tons       |sediment transported out of reach on day

### rch_san

- **Type**: `real`
- **Defined in source**: `channel_module.f90:48`

### rch_sil

- **Type**: `real`
- **Defined in source**: `channel_module.f90:49`

### rch_cla

- **Type**: `real`
- **Defined in source**: `channel_module.f90:50`

### rch_sag

- **Type**: `real`
- **Defined in source**: `channel_module.f90:51`

### rtwtr_d

- **Type**: `real`
- **Defined in source**: `channel_module.f90:52`
- **Source note**: m^3 H2O           |water leaving reach during day

### rt_delt

- **Type**: `real`
- **Defined in source**: `channel_module.f90:53`
- **Source note**: calculation time step in days

### rch_lag

- **Type**: `real`
- **Defined in source**: `channel_module.f90:54`

### rch_gra

- **Type**: `real`
- **Defined in source**: `channel_module.f90:55`

### rtwtr

- **Type**: `real`
- **Defined in source**: `channel_module.f90:56`
- **Source note**: m^3 H2O           |water leaving reach on day

### wtrin

- **Type**: `real`
- **Defined in source**: `channel_module.f90:57`
- **Source note**: m^3               |water entering reach during day

### sed_ch

- **Type**: `integer`
- **Defined in source**: `channel_module.f90:58`

### ch

- **Type**: `channel`
- **Defined in source**: `channel_module.f90:120`

### rch_d

- **Type**: `regional_output_channel`
- **Defined in source**: `channel_module.f90:187`

### rch_m

- **Type**: `regional_output_channel`
- **Defined in source**: `channel_module.f90:188`

### rch_y

- **Type**: `regional_output_channel`
- **Defined in source**: `channel_module.f90:189`

### rch_a

- **Type**: `regional_output_channel`
- **Defined in source**: `channel_module.f90:190`

### ch_d

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:192`

### ch_m

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:193`

### ch_y

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:194`

### ch_a

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:195`

### bch_d

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:196`

### bch_m

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:197`

### bch_y

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:198`

### bch_a

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:199`

### chz

- **Type**: `ch_output`
- **Defined in source**: `channel_module.f90:200`

### ch_hdr

- **Type**: `ch_header`
- **Defined in source**: `channel_module.f90:270`

### ch_hdr_units

- **Type**: `ch_header_units`
- **Defined in source**: `channel_module.f90:340`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### ch_add

### ch_div

### ch_mult

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

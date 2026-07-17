---
type: module
tags:
  - swat/module
  - swat/to-read
file: hru_module.f90
note_file: hru_module.f90
module_name: hru_module
defines_types:
  - uptake_parameters
  - irrigation_sources
  - topography
  - field
  - hydrology
  - snow_parameters
  - subsurface_drainage_parameters
  - saturated_buffer_parameters
  - saturated_buffer
  - landuse
  - soil_plant_initialize
  - hru_databases
  - hru_databases_char
  - hydrologic_response_unit_db
  - land_use_mgt_variables
  - nutrient_parameters
  - hydrologic_response_unit
defines_vars:
  - isep
  - ilu
  - ulu
  - iwgen
  - timest
  - uptake
  - snodb
  - sdr
  - satbuff_db
  - luse
  - sol_plt_ini
  - hru_db
  - hru
  - hru_init
  - precip_eff
  - qday
  - satexq_chan
  - ipl
  - isol
  - strsa_av
  - strsn_av
  - strsp_av
  - strstmp_av
  - rto_no3
  - rto_solp
  - uno3d_tot
  - uapd_tot
  - sum_no3
  - sum_solp
  - epmax
  - cvm_com
  - translt
  - uno3d
  - uapd
  - par
  - htfac
  - un2
  - up2
  - iseptic
  - qp_cms
  - sw_excess
  - albday
  - wt_shall
  - sq_rto
  - snomlt
  - snofall
  - fixn
  - qtile
  - latlyr
  - inflpcp
  - fertn
  - sepday
  - bioday
  - sepcrk
  - sepcrktot
  - fertno3
  - fertnh3
  - fertorgn
  - fertsolp
  - fertorgp
  - fertp
  - grazn
  - grazp
  - sdti
  - voltot
  - volcrmin
  - canev
  - usle
  - rcn
  - enratio
  - vpd
  - pet_day
  - ep_day
  - snoev
  - es_day
  - ls_overq
  - latqrunon
  - tilerunon
  - ep_max
  - bsprev
  - usle_ei
  - snocov1
  - snocov2
  - lyrtile
  - etday
  - mo
  - ihru
  - nd_30
  - mpst
  - mlyr
  - date
  - isep_ly
  - qstemm
  - bio_bod
  - biom
  - rbiom
  - fcoli
  - bz_perc
  - plqm
  - i_sep
  - sep_tsincefail
  - sol_sumno3
  - sol_sumsolp
  - sanyld
  - silyld
  - clayld
  - sagyld
  - lagyld
  - grayld
  - itb
  - wnan
  - phusw
  - yr_skip
  - isweep
  - sweepeff
  - ranrns_hru
  - itill
  - tc_gwat
  - wfsh
  - sed_con
  - orgn_con
  - orgp_con
  - soln_con
  - solp_con
  - filterw
  - cn2
  - smx
  - cnday
  - tconc
  - usle_cfac
  - usle_eifac
  - t_ov
  - canstor
  - ovrlnd
  - cumei
  - cumeira
  - cumrt
  - cumrai
  - sstmaxd
  - stmaxd
  - surqsolp
  - cklsp
  - pplnt
  - brt
  - twash
  - doxq
  - percn
  - cbodu
  - chl_a
  - qdr
  - latno3
  - latq
  - nplnt
  - tileno3
  - sedminpa
  - sedminps
  - sedorgn
  - sedorgp
  - sedyld
  - sepbtm
  - surfq
  - surqno3
  - surqsalt
  - latqsalt
  - tilesalt
  - percsalt
  - gwupsalt
  - urbqsalt
  - irswsalt
  - irgwsalt
  - wetqsalt
  - wtspsalt
  - surqcs
  - latqcs
  - tilecs
  - perccs
  - gwupcs
  - urbqcs
  - sedmcs
  - irswcs
  - irgwcs
  - wetqcs
  - wtspcs
  - phubase
  - dormhr
  - wrt
  - bss
  - surf_bs
  - swtrg
  - rateinf_prev
  - urb_abstinit
  - grz_days
  - igrz
  - ndeat
  - gwsoilq
  - satexq
  - bss_ex
  - gwsoiln
  - gwsoilp
  - satexn
  - irrn
  - irrp
  - mgt_ops
  - hhqday
  - ubnrunoff
  - ubntss
  - ovrlnd_dt
  - hhsurfq
  - hhsurf_bs
  - hhsedy
  - init_abstrc
  - tillage_switch
  - tillage_depth
  - tillage_days
  - tillage_factor
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# hru_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### uptake_parameters

- **Defined in source**: `hru_module.f90:11`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `water_dis` | `real` | 12 | \|the uptake distribution for water is hardwired |
| `water_norm` | `real` | 13 | none \|water uptake normalization parameter |
| `n_norm` | `real` | 14 | none \|nitrogen uptake normalization parameter |
| `p_norm` | `real` | 15 | none \|phosphorus uptake normalization parameter |

### irrigation_sources

- **Defined in source**: `hru_module.f90:19`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flag` | `integer` | 20 | 0= don't irrigate, 1=irrigate |
| `chan` | `integer, dimension(:), allocatable` | 21 |  |
| `res` | `integer, dimension(:), allocatable` | 22 |  |
| `pond` | `integer, dimension(:), allocatable` | 23 |  |
| `shal` | `integer, dimension(:), allocatable` | 24 |  |
| `deep` | `integer, dimension(:), allocatable` | 25 |  |

### topography

- **Defined in source**: `hru_module.f90:28`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 29 |  |
| `elev` | `real` | 30 | \|m \|elevation of HRU |
| `slope` | `real` | 31 | hru_slp(:) \|m/m \|average slope steepness in HRU |
| `slope_len` | `real` | 32 | slsubbsn(:) \|m \|average slope length for erosion |
| `dr_den` | `real` | 33 | \|km/km2 \|drainage density |
| `lat_len` | `real` | 34 | slsoil(:) \|m \|slope length for lateral subsurface flow |
| `dis_stream` | `real` | 35 | dis_stream(:) \| m \|average distance to stream |
| `dep_co` | `real` | 36 | \| \|deposition coefficient |
| `field_db` | `integer` | 37 | \| \|pointer to field.fld |
| `channel_db` | `integer` | 38 | \| \|pointer to channel.dat |

### field

- **Defined in source**: `hru_module.f90:41`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 42 |  |
| `length` | `real` | 43 | \|m \|field length for wind erosion |
| `wid` | `real` | 44 | \|m \|field width for wind erosion |
| `ang` | `real` | 45 | \|deg \|field angle for wind erosion |

### hydrology

- **Defined in source**: `hru_module.f90:48`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 49 |  |
| `lat_ttime` | `real` | 50 | lat_ttime(:) \|days \|days of lateral soil flow across the hillslope |
| `lat_sed` | `real` | 51 | lat_sed(:) \|g/L \|sediment concentration in lateral flow |
| `canmx` | `real` | 52 | canmx(:) \|mm H2O \|maximum canopy storage |
| `esco` | `real` | 53 | esco(:) \|none \|soil evaporation compensation factor |
| `epco` | `real` | 54 | epco(:) \|none \|plant water uptake compensation factor (0-1) |
| `erorgn` | `real` | 55 | erorgn(:) \|none \|organic N enrichment ratio, if left blank the model will calculate for every event |
| `erorgp` | `real` | 57 | erorgp(:) \|none \|organic P enrichment ratio, if left blank the model will calculate for every event |
| `cn3_swf` | `real` | 59 | \|none \|curve number adjustment factor - sw at cn3 |
| `biomix` | `real` | 60 | biomix(:) \|none \|biological mixing efficiency. Mixing of soil due to activity of earthworms and other soil biota. Mixing is performed at the end of every calendar year. |
| `perco` | `real` | 64 | \|0-1 \|percolation coefficient - linear adjustment to daily perc |
| `lat_orgn` | `real` | 65 |  |
| `lat_orgp` | `real` | 66 |  |
| `pet_co` | `real` | 67 |  |
| `latq_co` | `real` | 68 | \| \|lateral soil flow coefficient - linear adjustment to daily lat flow |
| `perco_lim` | `real` | 69 | \| \|percolation coefficient-limits perc from bottom layer |

### snow_parameters

- **Defined in source**: `hru_module.f90:72`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 73 |  |
| `falltmp` | `real` | 74 | deg C \|snowfall temp |
| `melttmp` | `real` | 75 | deg C \|snow melt base temp |
| `meltmx` | `real` | 76 | mm/deg C/day \|Max melt rate for snow during year (June 21) |
| `meltmn` | `real` | 77 | mm/deg C/day \|Min melt rate for snow during year (Dec 21) |
| `timp` | `real` | 78 | none \|snow pack temp lag factor (0-1) |
| `covmx` | `real` | 79 | mm H20 \|snow water content at full ground cover |
| `cov50` | `real` | 80 | none \|frac of covmx at 50% snow cover |
| `init_mm` | `real` | 81 | mm H20 \|initial snow water content at start of simulation |

### subsurface_drainage_parameters

- **Defined in source**: `hru_module.f90:85`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 86 |  |
| `depth` | `real` | 87 | \|mm \|depth of drain tube from the soil surface |
| `time` | `real` | 88 | \|hrs \|time to drain soil to field capacity |
| `lag` | `real` | 89 | \|hours \|drain tile lag time |
| `radius` | `real` | 90 | \|mm \|effective radius of drains |
| `dist` | `real` | 91 | \|mm \|distance between two drain tubes or tiles |
| `drain_co` | `real` | 92 | \|mm/day \|drainage coefficient |
| `pumpcap` | `real` | 93 | \|mm/hr \|pump capacity |
| `latksat` | `real` | 94 | !na \|multiplication factor to determine lat sat hyd conductivity for profile |

### saturated_buffer_parameters

- **Defined in source**: `hru_module.f90:98`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 99 |  |
| `hru_src` | `integer` | 100 | \|source of tile inflow |
| `frac_src` | `real` | 101 | \|fration of source hru contributing to tile flow |
| `flocon_dtbl` | `character(len=40)` | 102 | \|decision table to control flow into buffer hru |
| `hru_rcv` | `integer` | 103 | \|receiving (buffer) hru |
| `lyr` | `integer` | 104 | \|soil layer for incoming tile flow (0 = surface) |

### saturated_buffer

- **Defined in source**: `hru_module.f90:108`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sb_db` | `saturated_buffer_parameters` | 109 |  |
| `dtbl` | `integer` | 110 |  |
| `inflo` | `real` | 111 |  |
| `no3` | `real` | 112 |  |

### landuse

- **Defined in source**: `hru_module.f90:115`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 116 |  |
| `cn_lu` | `integer` | 117 |  |
| `cons_prac` | `integer` | 118 |  |
| `usle_p` | `real` | 119 | none \| USLE equation support practice (P) factor daily |
| `urb_ro` | `character (len=40)` | 120 | none \| urban runoff model "usgs_reg", simulate using USGS regression eqs "buildup_washoff", simulate using build up/wash off alg |
| `urb_lu` | `integer` | 123 | none \| urban land type identification number |
| `ovn` | `real` | 124 | none \| Manning's "n" value for overland flow |

### soil_plant_initialize

- **Defined in source**: `hru_module.f90:128`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 129 |  |
| `sw_frac` | `real` | 130 |  |
| `nutc` | `character(len=40)` | 131 |  |
| `pestc` | `character(len=40)` | 132 |  |
| `pathc` | `character(len=40)` | 133 |  |
| `saltc` | `character(len=40)` | 134 |  |
| `hmetc` | `character(len=40)` | 135 |  |
| `csc` | `character(len=40)` | 136 | rtb cs |
| `nut` | `integer` | 137 |  |
| `pest` | `integer` | 138 |  |
| `path` | `integer` | 139 |  |
| `salt` | `integer` | 140 |  |
| `hmet` | `integer` | 141 |  |
| `cs` | `integer` | 142 | rtb cs |

### hru_databases

- **Defined in source**: `hru_module.f90:146`

Integer database pointers for an HRU database record. Most fields are resolved
from the matching text names in `hru_databases_char` while reading
[[hru-data.hru]]. These integer values are what the simulation uses after the
crosswalk.

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 147 | HRU database record name. |
| `topo` | `integer` | 148 | Pointer to topography data from [[topography.hyd]]. |
| `hyd` | `integer` | 149 | Pointer to hydrology data from [[hydrology.hyd]]. |
| `soil` | `integer` | 150 | Pointer to soil data from [[soils.sol]]. |
| `land_use_mgt` | `integer` | 151 | Pointer to land-use/management data from [[landuse.lum]]. |
| `soil_plant_init` | `integer` | 152 | Pointer to soil/plant initialization data loaded into `sol_plt_ini`. |
| `surf_stor` | `integer` | 153 | Pointer to HRU surface-storage/wetland data from [[wetland.wet]]; `0` means none. |
| `snow` | `integer` | 154 | Pointer to snow data from [[snow.sno]]. |
| `field` | `integer` | 155 | Pointer to field data from [[field.fld]]; `0` means none. |

### hru_databases_char

- **Defined in source**: `hru_module.f90:158`

Text database names read from [[hru-data.hru]]. The reader stores the input row
directly in `hru_db(id)%dbsc` using list-directed Fortran input, so values are
consumed in the declaration order shown below. `hru_read.f90` then crosswalks
these names to integer pointers in `hru_db(id)%dbs`, and `hrudb_init.f90`
copies both `dbsc` and `dbs` into each active `hru()` object.

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 159 | HRU database record name from [[hru-data.hru]]. |
| `topo` | `character(len=40)` | 160 | Name matched to `topo_db(:)%name` from [[topography.hyd]]. |
| `hyd` | `character(len=40)` | 161 | Name matched to `hyd_db(:)%name` from [[hydrology.hyd]]. |
| `soil` | `character(len=40)` | 162 | Soil name matched to `soildb(:)%s%snam` from [[soils.sol]]. |
| `land_use_mgt` | `character(len=40)` | 163 | Land-use/management name matched to `lum(:)%name` from [[landuse.lum]]. |
| `soil_plant_init` | `character(len=40)` | 164 | Soil/plant initialization name matched to `sol_plt_ini(:)%name`. |
| `surf_stor` | `character(len=40)` | 165 | Surface-storage/wetland name from [[wetland.wet]], or `null`. This is resolved later in `wet_initial.f90`. |
| `snow` | `character(len=40)` | 166 | Snow parameter name matched to `snodb(:)%name` from [[snow.sno]], or `null`. |
| `field` | `character(len=40)` | 167 | Field data name matched to `field_db(:)%name` from [[field.fld]], or `null`. |

### hydrologic_response_unit_db

- **Defined in source**: `hru_module.f90:170`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 171 |  |
| `dbs` | `hru_databases` | 172 |  |
| `dbsc` | `hru_databases_char` | 173 |  |

### land_use_mgt_variables

- **Defined in source**: `hru_module.f90:177`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `usle_p` | `real` | 178 | \|none \|USLE equation comservation practice (P) factor |
| `usle_ls` | `real` | 179 | \|none \|USLE equation length slope (LS) factor |
| `usle_mult` | `real` | 180 | \|none \|product of USLE K,P,LS,exp(rock) |
| `sdr_dep` | `real` | 181 | \| |
| `ldrain` | `integer` | 182 | \|none \|soil layer where drainage tile is located |
| `tile_ttime` | `real` | 183 | \|none \|Exponential of the tile flow travel time |
| `vfsi` | `integer` | 184 | \|none \|on/off flag for vegetative filter strip |
| `vfsratio` | `real` | 185 | \|none \|contouring USLE P factor |
| `vfscon` | `real` | 186 | \|none \|fraction of the total runoff from the entire field |
| `vfsch` | `real` | 187 | \|none \|fraction of flow entering the most concentrated 10% of the VFS. which is fully channelized |
| `ngrwat` | `integer` | 189 |  |
| `grwat_i` | `integer` | 190 | \|none \|On/off Flag for waterway simulation |
| `grwat_n` | `real` | 191 | \|none \|Mannings's n for grassed waterway |
| `grwat_spcon` | `real` | 192 | \|none \|sediment transport coefficant defined by user |
| `grwat_d` | `real` | 193 | \|m \|depth of Grassed waterway |
| `grwat_w` | `real` | 194 | \|none \|Width of grass waterway |
| `grwat_l` | `real` | 195 | \|km \|length of Grass Waterway |
| `grwat_s` | `real` | 196 | \|m/m \|slope of grass waterway |
| `bmp_flag` | `integer` | 197 | \|none \|On/off Flag for user defeined bmp efficiency |
| `bmp_sed` | `real` | 198 | \|% \| Sediment removal by BMP |
| `bmp_pp` | `real` | 199 | \|% \| Particulate P removal by BMP |
| `bmp_sp` | `real` | 200 | \|% \| Soluble P removal by BMP |
| `bmp_pn` | `real` | 201 | \|% \| Particulate N removal by BMP |
| `bmp_sn` | `real` | 202 | \|% \| Soluble N removal by BMP |
| `bmp_bac` | `real` | 203 | \|% \| Bacteria removal by BMP |

### nutrient_parameters

- **Defined in source**: `hru_module.f90:206`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `phoskd` | `real` | 207 | \|kg/m3 \| |
| `pperco` | `real` | 208 | \|kg/m3 \| |
| `psp` | `real` | 209 | \|kg/m3 \| |
| `nperco` | `real` | 210 | \|kg/m3 \| |
| `cmn` | `real` | 211 | \|kg/m3 \| |
| `nperco_lchtile` | `real` | 212 | \|kg/m3 \| |

### hydrologic_response_unit

- **Defined in source**: `hru_module.f90:214`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 215 |  |
| `obj_no` | `integer` | 216 |  |
| `area_ha` | `real` | 217 |  |
| `km` | `real` | 218 |  |
| `surf_stor` | `integer` | 219 | points to res() for surface storage |
| `dbs` | `hru_databases` | 220 | database pointers |
| `dbsc` | `hru_databases_char` | 221 | database pointers |
| `land_use_mgt` | `integer` | 222 |  |
| `land_use_mgt_c` | `character(len=40)` | 223 |  |
| `lum_group` | `integer` | 224 |  |
| `lum_group_c` | `character(len=40)` | 225 | land use group for soft cal and output |
| `cal_group` | `character(len=40)` | 226 |  |
| `plant_cov` | `integer` | 227 |  |
| `mgt_ops` | `integer` | 228 |  |
| `tiledrain` | `integer` | 229 |  |
| `septic` | `integer` | 230 |  |
| `fstrip` | `integer` | 231 |  |
| `grassww` | `integer` | 232 |  |
| `bmpuser` | `integer` | 233 |  |
| `crop_reg` | `integer` | 234 |  |
| `paddy_irr` | `integer` | 235 | Jaehak 2022 other data |
| `topo` | `topography` | 238 |  |
| `field` | `field` | 239 |  |
| `hyd` | `hydrology` | 240 |  |
| `hydcal` | `hydrology` | 241 |  |
| `luse` | `landuse` | 242 |  |
| `lumv` | `land_use_mgt_variables` | 243 |  |
| `sdr` | `subsurface_drainage_parameters` | 244 |  |
| `sno` | `snow_parameters` | 245 |  |
| `nut` | `nutrient_parameters` | 246 |  |
| `sb` | `saturated_buffer` | 247 |  |
| `snocov1` | `real` | 248 |  |
| `snocov2` | `real` | 249 |  |
| `cur_op` | `integer` | 250 |  |
| `irr` | `integer` | 251 | none \|set to 1 if irrigated during simulation - for wb soft cal |
| `man_trn_dtbl` | `integer` | 252 |  |
| `irr_trn_iauto` | `integer` | 253 |  |
| `man_trn_iauto` | `integer` | 254 |  |
| `wet_db` | `integer` | 255 | none \|pointer to wetland data - saved so turn on/off |
| `wet_hc` | `real` | 256 | mm/h \|hydraulic conductivity of upper layer - wetlands |
| `sno_mm` | `real` | 257 | mm H2O \|amount of water in snow on current day |
| `water_seep` | `real` | 258 |  |
| `water_evap` | `real` | 259 |  |
| `wet_obank_in` | `real` | 260 | mm \|inflow from overbank into wetlands |
| `precip_aa` | `real` | 261 |  |
| `irr_yr` | `real` | 262 | mm \|irrigation for year - used as dtbl condition jga6-25 |
| `wet_fp` | `character(len=1)` | 263 |  |
| `irr_src` | `character(len=40)` | 264 | \|irrigation source, Jaehak 2022 |
| `strsa` | `real` | 265 |  |
| `irr_hmax` | `real` | 266 | mm H2O \|target ponding depth during paddy irrigation Jaehak 2022 |
| `irr_hmin` | `real` | 267 | mm H2O \|threshold ponding depth to trigger paddy irrigation |
| `irr_isc` | `real` | 268 | mm H2O \|ID of the source cha/res/aqu for paddy irrigation |
| `flow` | `real, dimension(5)` | 269 | mm H2O \|average annual flow (1=wyld,2=perc,3=surface,4=lateral,5=tile) |

## Variables Defined
### isep

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:5`
- **Source note**: |

### ilu

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:6`
- **Source note**: |

### ulu

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:7`
- **Source note**: |

### iwgen

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:8`
- **Source note**: |

### timest

- **Type**: `character (len=1)`
- **Defined in source**: `hru_module.f90:9`
- **Source note**: |

### uptake

- **Type**: `uptake_parameters`
- **Defined in source**: `hru_module.f90:17`

### snodb

- **Type**: `snow_parameters`
- **Defined in source**: `hru_module.f90:83`

### sdr

- **Type**: `subsurface_drainage_parameters`
- **Defined in source**: `hru_module.f90:96`

### satbuff_db

- **Type**: `saturated_buffer_parameters`
- **Defined in source**: `hru_module.f90:106`

### luse

- **Type**: `landuse`
- **Defined in source**: `hru_module.f90:126`

### sol_plt_ini

- **Type**: `soil_plant_initialize`
- **Defined in source**: `hru_module.f90:144`

### hru_db

- **Type**: `hydrologic_response_unit_db`
- **Defined in source**: `hru_module.f90:175`

### hru

- **Type**: `hydrologic_response_unit`
- **Defined in source**: `hru_module.f90:271`

### hru_init

- **Type**: `hydrologic_response_unit`
- **Defined in source**: `hru_module.f90:272`

### precip_eff

- **Type**: `real`
- **Defined in source**: `hru_module.f90:275`
- **Source note**: mm   |daily effective precip for runoff calculations = precipday + ls_overq + snomlt - canstor

### qday

- **Type**: `real`
- **Defined in source**: `hru_module.f90:277`
- **Source note**: mm   |surface runoff that reaches main channel during day in HRU

### satexq_chan

- **Type**: `real`
- **Defined in source**: `hru_module.f90:278`
- **Source note**: mm   |saturation excess runoff that reaches main channel during day in HRU

### ipl

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:282`

### isol

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:283`

### strsa_av

- **Type**: `real`
- **Defined in source**: `hru_module.f90:285`

### strsn_av

- **Type**: `real`
- **Defined in source**: `hru_module.f90:286`

### strsp_av

- **Type**: `real`
- **Defined in source**: `hru_module.f90:287`

### strstmp_av

- **Type**: `real`
- **Defined in source**: `hru_module.f90:288`

### rto_no3

- **Type**: `real`
- **Defined in source**: `hru_module.f90:289`

### rto_solp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:290`

### uno3d_tot

- **Type**: `real`
- **Defined in source**: `hru_module.f90:291`

### uapd_tot

- **Type**: `real`
- **Defined in source**: `hru_module.f90:292`

### sum_no3

- **Type**: `real`
- **Defined in source**: `hru_module.f90:293`

### sum_solp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:294`

### epmax

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:295`

### cvm_com

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:296`

### translt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:297`

### uno3d

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:298`

### uapd

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:299`

### par

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:300`

### htfac

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:301`

### un2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:302`

### up2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:303`

### iseptic

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:304`

### qp_cms

- **Type**: `real`
- **Defined in source**: `hru_module.f90:307`

### sw_excess

- **Type**: `real`
- **Defined in source**: `hru_module.f90:308`

### albday

- **Type**: `real`
- **Defined in source**: `hru_module.f90:309`

### wt_shall

- **Type**: `real`
- **Defined in source**: `hru_module.f90:310`

### sq_rto

- **Type**: `real`
- **Defined in source**: `hru_module.f90:311`

### snomlt

- **Type**: `real`
- **Defined in source**: `hru_module.f90:312`

### snofall

- **Type**: `real`
- **Defined in source**: `hru_module.f90:313`

### fixn

- **Type**: `real`
- **Defined in source**: `hru_module.f90:314`

### qtile

- **Type**: `real`
- **Defined in source**: `hru_module.f90:315`

### latlyr

- **Type**: `real`
- **Defined in source**: `hru_module.f90:316`
- **Source note**: mm            |lateral flow in soil layer for the day

### inflpcp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:317`
- **Source note**: mm            |amount of precipitation that infiltrates

### fertn

- **Type**: `real`
- **Defined in source**: `hru_module.f90:318`

### sepday

- **Type**: `real`
- **Defined in source**: `hru_module.f90:319`

### bioday

- **Type**: `real`
- **Defined in source**: `hru_module.f90:320`

### sepcrk

- **Type**: `real`
- **Defined in source**: `hru_module.f90:321`

### sepcrktot

- **Type**: `real`
- **Defined in source**: `hru_module.f90:322`

### fertno3

- **Type**: `real`
- **Defined in source**: `hru_module.f90:323`

### fertnh3

- **Type**: `real`
- **Defined in source**: `hru_module.f90:324`

### fertorgn

- **Type**: `real`
- **Defined in source**: `hru_module.f90:325`

### fertsolp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:326`

### fertorgp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:327`

### fertp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:328`

### grazn

- **Type**: `real`
- **Defined in source**: `hru_module.f90:329`

### grazp

- **Type**: `real`
- **Defined in source**: `hru_module.f90:330`

### sdti

- **Type**: `real`
- **Defined in source**: `hru_module.f90:331`

### voltot

- **Type**: `real`
- **Defined in source**: `hru_module.f90:332`
- **Source note**: mm            |total volume of cracks expressed as depth per area unit

### volcrmin

- **Type**: `real`
- **Defined in source**: `hru_module.f90:333`
- **Source note**: mm            |minimum crack volume allowed in any soil layer

### canev

- **Type**: `real`
- **Defined in source**: `hru_module.f90:334`

### usle

- **Type**: `real`
- **Defined in source**: `hru_module.f90:335`

### rcn

- **Type**: `real`
- **Defined in source**: `hru_module.f90:336`

### enratio

- **Type**: `real`
- **Defined in source**: `hru_module.f90:337`

### vpd

- **Type**: `real`
- **Defined in source**: `hru_module.f90:338`

### pet_day

- **Type**: `real`
- **Defined in source**: `hru_module.f90:339`

### ep_day

- **Type**: `real`
- **Defined in source**: `hru_module.f90:340`

### snoev

- **Type**: `real`
- **Defined in source**: `hru_module.f90:341`

### es_day

- **Type**: `real`
- **Defined in source**: `hru_module.f90:342`

### ls_overq

- **Type**: `real`
- **Defined in source**: `hru_module.f90:343`

### latqrunon

- **Type**: `real`
- **Defined in source**: `hru_module.f90:344`

### tilerunon

- **Type**: `real`
- **Defined in source**: `hru_module.f90:345`

### ep_max

- **Type**: `real`
- **Defined in source**: `hru_module.f90:346`

### bsprev

- **Type**: `real`
- **Defined in source**: `hru_module.f90:347`

### usle_ei

- **Type**: `real`
- **Defined in source**: `hru_module.f90:348`

### snocov1

- **Type**: `real`
- **Defined in source**: `hru_module.f90:349`

### snocov2

- **Type**: `real`
- **Defined in source**: `hru_module.f90:350`

### lyrtile

- **Type**: `real`
- **Defined in source**: `hru_module.f90:351`

### etday

- **Type**: `real`
- **Defined in source**: `hru_module.f90:353`

### mo

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:354`

### ihru

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:355`
- **Source note**: none          |HRU number

### nd_30

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:356`

### mpst

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:357`

### mlyr

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:358`

### date

- **Type**: `character(len=8)`
- **Defined in source**: `hru_module.f90:360`

### isep_ly

- **Type**: `integer`
- **Defined in source**: `hru_module.f90:363`

### qstemm

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:364`

### bio_bod

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:366`

### biom

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:367`

### rbiom

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:368`

### fcoli

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:369`

### bz_perc

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:370`

### plqm

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:371`

### i_sep

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:373`

### sep_tsincefail

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:374`

### sol_sumno3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:376`

### sol_sumsolp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:377`

### sanyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:381`

### silyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:382`

### clayld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:383`

### sagyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:384`

### lagyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:385`

### grayld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:386`

### itb

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:387`

### wnan

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:390`

### phusw

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:392`

### yr_skip

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:393`

### isweep

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:394`

### sweepeff

- **Type**: `real`
- **Defined in source**: `hru_module.f90:395`

### ranrns_hru

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:397`

### itill

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:398`

### tc_gwat

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:400`

### wfsh

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:401`

### sed_con

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:402`

### orgn_con

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:403`

### orgp_con

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:404`

### soln_con

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:405`

### solp_con

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:406`

### filterw

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:407`

### cn2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:408`

### smx

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:409`

### cnday

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:410`

### tconc

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:411`

### usle_cfac

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:412`

### usle_eifac

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:413`

### t_ov

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:414`

### canstor

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:415`

### ovrlnd

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:416`

### cumei

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:419`

### cumeira

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:420`

### cumrt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:421`

### cumrai

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:422`

### sstmaxd

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:423`

### stmaxd

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:424`

### surqsolp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:426`

### cklsp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:427`

### pplnt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:428`

### brt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:429`

### twash

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:431`

### doxq

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:432`

### percn

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:433`

### cbodu

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:434`

### chl_a

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:435`

### qdr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:436`

### latno3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:437`

### latq

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:438`

### nplnt

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:439`

### tileno3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:440`

### sedminpa

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:441`

### sedminps

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:442`

### sedorgn

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:443`

### sedorgp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:444`

### sedyld

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:445`

### sepbtm

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:446`

### surfq

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:447`

### surqno3

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:448`

### surqsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:449`

### latqsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:450`

### tilesalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:451`

### percsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:452`

### gwupsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:453`

### urbqsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:454`

### irswsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:455`

### irgwsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:456`

### wetqsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:457`

### wtspsalt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:458`

### surqcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:459`
- **Source note**: rtb cs

### latqcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:460`
- **Source note**: rtb cs

### tilecs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:461`
- **Source note**: rtb cs

### perccs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:462`
- **Source note**: rtb cs

### gwupcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:463`
- **Source note**: rtb cs

### urbqcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:464`
- **Source note**: rtb cs

### sedmcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:465`
- **Source note**: rtb cs

### irswcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:466`
- **Source note**: rtb cs

### irgwcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:467`
- **Source note**: rtb cs

### wetqcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:468`
- **Source note**: rtb cs

### wtspcs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:469`
- **Source note**: rtb cs

### phubase

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:470`

### dormhr

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:471`

### wrt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:472`

### bss

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:473`

### surf_bs

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:474`

### swtrg

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:475`

### rateinf_prev

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:476`

### urb_abstinit

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:477`

### grz_days

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:479`

### igrz

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:480`

### ndeat

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:481`

### gwsoilq

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:483`
- **Source note**: rtb gwflow

### satexq

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:484`
- **Source note**: rtb gwflow

### bss_ex

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:485`
- **Source note**: rtb gwflow

### gwsoiln

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:486`
- **Source note**: rtb gwflow

### gwsoilp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:487`
- **Source note**: rtb gwflow

### satexn

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:488`
- **Source note**: rtb gwflow

### irrn

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:489`
- **Source note**: rtb irrig (irrigation nutrient mass)

### irrp

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:490`
- **Source note**: rtb irrig (irrigation nutrient mass)

### mgt_ops

- **Type**: `integer, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:493`

### hhqday

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:495`

### ubnrunoff

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:500`

### ubntss

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hru_module.f90:501`

### ovrlnd_dt

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:502`

### hhsurfq

- **Type**: `real, dimension (:,:), allocatable`
- **Defined in source**: `hru_module.f90:503`

### hhsurf_bs

- **Type**: `real, dimension (:,:,:), allocatable`
- **Defined in source**: `hru_module.f90:504`

### hhsedy

- **Type**: `real, dimension(:,:), allocatable`
- **Defined in source**: `hru_module.f90:507`

### init_abstrc

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `hru_module.f90:508`

### tillage_switch

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `hru_module.f90:510`

### tillage_depth

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `hru_module.f90:511`

### tillage_days

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `hru_module.f90:512`

### tillage_factor

- **Type**: `real, dimension(:), allocatable`
- **Defined in source**: `hru_module.f90:513`

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

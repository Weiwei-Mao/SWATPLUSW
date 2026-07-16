---
type: module
tags:
  - swat/module
  - swat/to-read
file: hydrograph_module.f90
note_file: hydrograph_module.f90
module_name: hydrograph_module
defines_types:
  - hyd_output
  - hyd_sep
  - wallo_source_object
  - wallo_transfer_object
  - water_allocation_object
  - object_output
  - channel_floodplain_water_balance
  - timestep
  - sorted_duration_curve
  - duration_curve_points
  - flow_duration_curve
  - inflow_unit_hyds
  - flashiness_index
  - object_connectivity
  - irrigation_water_transfer
  - recall_hydrograph_inputs
  - spatial_objects
  - object_total_hydrographs
  - routing_unit_data
  - routing_unit_elements
  - channel_surface_elements
  - geomorphic_baseflow_channel_data
  - channel_aquifer_elements
  - hyd_header
  - hyd_stor_header
  - hyd_in_header
  - hyd_out_header
  - hyd_inout_header
  - wtmp_out_header
  - sed_hyd_header
  - sd_hyd_header_units
  - sol_header
  - plant_header
  - flood_plain_header
  - ch_watbod_header
  - ch_watbod_header_units
  - ch_watbod_inoutheader
  - ch_watbod_inoutheader_units
  - hyd_header_units1
  - hyd_header_units3
  - hydinout_header_units1
  - wtmp_header_units
  - hyd_header_units
  - hyd_header_units2
  - hyd_header_time
  - rec_header_time
  - hyd_header_obj
  - output_flow_duration_header
  - calibration_header
  - calibration2_header
  - calibration3_header
  - output_checker_header
  - output_checker_unit
  - hru_swift_header_base
  - hru_swift_header_baseunit
  - hru_swift_header_base2
  - hru_swift_header_baseunit2
  - hru_swift_header
  - shade_factor_data
defines_vars:
  - mhyd
  - mcmd
  - inum2
  - jrch
  - jrchq
  - mrte
  - ihout
  - iwst
  - isdch
  - icmd
  - ich
  - mobj_out
  - isd_chsur
  - rcv_sum
  - dfn_sum
  - elem_cnt
  - defunit_num
  - ru_seq
  - hyd_km2
  - ob_order
  - rchhr
  - wyld_rto
  - hd
  - rec_d
  - rec_m
  - rec_y
  - rec_a
  - srec_d
  - srec_m
  - srec_y
  - srec_a
  - ru_d
  - ru_m
  - ru_y
  - ru_a
  - brec_d
  - brec_m
  - brec_y
  - brec_a
  - bru_d
  - bru_m
  - bru_y
  - bru_a
  - binhyd_d
  - hz
  - dr1
  - hcnst
  - hhr
  - ht1
  - ht2
  - ht3
  - ht4
  - ht5
  - delrto
  - fp_dep
  - ch_dep
  - bank_ero
  - bed_ero
  - ch_trans
  - hdsep1
  - hdsep2
  - ch_stor_hdsep
  - hyd_sep_array
  - om_init_name
  - aqu
  - res
  - wet
  - res_om_init
  - wet_om_init
  - wet_seep_day
  - resz
  - wbody
  - om_init_water
  - ch_om_water_init
  - fp_om_water_init
  - ch_stor
  - fp_stor
  - tot_stor
  - wet_stor
  - ch_stor_m
  - ch_stor_y
  - ch_stor_a
  - chaz
  - res_in_d
  - res_in_m
  - res_in_y
  - res_in_a
  - res_trap
  - bres_in_d
  - bres_in_m
  - bres_in_y
  - bres_in_a
  - res_out_d
  - res_out_m
  - res_out_y
  - res_out_a
  - bres
  - bres_out_d
  - bres_out_m
  - bres_out_y
  - bres_out_a
  - resmz
  - wet_in_d
  - wet_in_m
  - wet_in_y
  - wet_in_a
  - bwet_in_d
  - bwet_in_m
  - bwet_in_y
  - bwet_in_a
  - wet_out_d
  - wet_out_m
  - wet_out_y
  - wet_out_a
  - bwet_out_d
  - bwet_out_m
  - bwet_out_y
  - bwet_out_a
  - ch_in_d
  - ch_in_m
  - ch_in_y
  - ch_in_a
  - bch_stor_d
  - bch_stor_m
  - bch_stor_y
  - bch_stor_a
  - bch_in_d
  - bch_in_m
  - bch_in_y
  - bch_in_a
  - ch_out_d
  - ch_out_m
  - ch_out_y
  - ch_out_a
  - bch_out_d
  - bch_out_m
  - bch_out_y
  - bch_out_a
  - chomz
  - wal_omd
  - wal_omm
  - wal_omy
  - wal_oma
  - wdraw_om
  - wdraw_om_tot
  - outflo_om
  - wtp_om_stor
  - wtp_om_out
  - wtp_om_treat
  - wal_tr_omd
  - wal_tr_omm
  - wal_tr_omy
  - wal_tr_oma
  - wal_use_omd
  - wal_use_omm
  - wal_use_omy
  - wal_use_oma
  - wuse_om_stor
  - wuse_om_out
  - wuse_om_efflu
  - osrc_om
  - orcv_om
  - canal_om_stor
  - canal_om_out
  - wtow_om_stor
  - wtow_om_out
  - ob_out
  - ch_fp_wb
  - ts
  - fdc_npts
  - fdc_p
  - fdc_days
  - fdc_n
  - fdc_norm_mean
  - ob
  - irrig
  - recall
  - sp_ob
  - sp_ob1
  - hd_tot
  - ru_def
  - ru_elem
  - ielem_ru
  - ch_sur
  - aqu_cha
  - aq_ch
  - dr
  - exco
  - hyd_hdr
  - hyd_stor_hdr
  - hyd_in_hdr
  - hyd_out_hdr
  - hyd_inout_hdr
  - wtmp_hdr
  - sd_hyd_hdr
  - sd_hyd_hdr_units
  - sol_hdr
  - plt_hdr
  - fp_hdr
  - ch_wbod_hdr
  - ch_wbod_hdr_units
  - ch_wbod_inouthdr
  - ch_wbod_inouthdr_units
  - hyd_hdr_units1
  - hyd_hdr_units3
  - hydinout_hdr_units1
  - wtmp_units
  - hyd_hdr_units
  - hyd_hdr_units2
  - hyd_hdr_time
  - rec_hdr_time
  - hyd_hdr_obj
  - fdc_hdr
  - calb_hdr
  - calb2_hdr
  - calb3_hdr
  - chk_hdr
  - chk_unit
  - hru_swift_hdr
  - shf_db
defines_subroutines:
  - hyd_convert_conc_to_mass
  - hyd_min
  - res_convert_mass
  - hyd_convert_mass_to_conc
defines_functions:
  - hydout_add
  - hydout_subtract
  - hydout_mult
  - hydout_add_const
  - hydout_mult_const
  - hydout_div_const
  - hydout_div_conv
defines_procedures:
  - hyd_convert_conc_to_mass
  - hyd_min
  - res_convert_mass
  - hyd_convert_mass_to_conc
  - hydout_add
  - hydout_subtract
  - hydout_mult
  - hydout_add_const
  - hydout_mult_const
  - hydout_div_const
  - hydout_div_conv
purpose: ""
---

# hydrograph_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### hyd_output

- **Defined in source**: `hydrograph_module.f90:31`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `real` | 32 | m^3 \|volume of water |
| `sed` | `real` | 33 | metric tons \|sediment |
| `orgn` | `real` | 34 | kg N \|organic N |
| `sedp` | `real` | 35 | kg P \|organic P |
| `no3` | `real` | 36 | kg N \|NO3-N |
| `solp` | `real` | 37 | kg P \|mineral (soluble P) |
| `chla` | `real` | 38 | kg \|chlorophyll-a |
| `nh3` | `real` | 39 | kg N \|NH3 |
| `no2` | `real` | 40 | kg N \|NO2 |
| `cbod` | `real` | 41 | kg \|carbonaceous biological oxygen demand |
| `dox` | `real` | 42 | kg \|dissolved oxygen |
| `san` | `real` | 43 | tons \|detached sand |
| `sil` | `real` | 44 | tons \|detached silt |
| `cla` | `real` | 45 | tons \|detached clay |
| `sag` | `real` | 46 | tons \|detached small ag |
| `lag` | `real` | 47 | tons \|detached large ag |
| `grv` | `real` | 48 | tons \|gravel |
| `temp` | `real` | 49 | deg c \|temperature |

### hyd_sep

- **Defined in source**: `hydrograph_module.f90:53`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_surq` | `real` | 54 | m3 \|volume of water from surface runoff |
| `flo_latq` | `real` | 55 | m3 \|volume of water from surface runoff |
| `flo_gwsw` | `real` | 56 | m3 \|volume of water from groundwater discharge |
| `flo_swgw` | `real` | 57 | m3 \|volume of water from stream seepage |
| `flo_satex` | `real` | 58 | m3 \|volume of water from saturation excess (high water table; from gwflow module) |
| `flo_satexsw` | `real` | 59 | m3 \|volume of water from saturation excess (saturated profile) |
| `flo_tile` | `real` | 60 | m3 \|volume of water from tile flow |

### wallo_source_object

- **Defined in source**: `hydrograph_module.f90:174`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hd` | `hyd_output` | 175 |  |

### wallo_transfer_object

- **Defined in source**: `hydrograph_module.f90:179`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `h_tot` | `hyd_output` | 181 |  |
| `src` | `wallo_source_object` | 182 |  |

### water_allocation_object

- **Defined in source**: `hydrograph_module.f90:186`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `trn` | `wallo_transfer_object` | 188 |  |

### object_output

- **Defined in source**: `hydrograph_module.f90:240`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=10)` | 241 |  |
| `obtyp` | `character (len=10)` | 242 | object type: hru,hlt,hs,rxc,dr,out,sdc |
| `obtypno` | `integer` | 243 | object type number: 1=hru, 2=hru_lte, 3=channel |
| `hydtyp` | `character (len=20)` | 244 | hydrograph type: tot,rhg,sur,lat,til |
| `objno` | `integer` | 245 | object number |
| `hydno` | `integer` | 246 | code computes from hydtyp |
| `filename` | `character (len=26)` | 247 | file with hydrograph output from the object |
| `unitno` | `integer` | 248 | filename unit number |

### channel_floodplain_water_balance

- **Defined in source**: `hydrograph_module.f90:252`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `inflo` | `real` | 253 | m3 \| inflow |
| `outflo` | `real` | 254 | m3 \| outflow |
| `tl` | `real` | 255 | m3 \| transmission losses |
| `ev` | `real` | 256 | m3 \| evaporation |
| `ch_stor_init` | `real` | 257 | m3 \| channel storage at start of time step |
| `ch_stor` | `real` | 258 | m3 \| channel storage at end of time step |
| `fp_stor_init` | `real` | 259 | m3 \| flood plain storage at start of time step (all flood plain storage above wetland emergency volume) |
| `fp_stor` | `real` | 260 | m3 \| flood plain storage at end of time step |
| `tot_stor_init` | `real` | 261 | m3 \| total channel + wetland storage at start of time step |
| `tot_stor` | `real` | 262 | m3 \| total channel + wetland storage at end of time step |
| `wet_stor_init` | `real` | 263 | m3 \| wetland flood plain storage at start of time step |
| `wet_stor` | `real` | 264 | m3 \| wetland flood plain storage at end of time step |

### timestep

- **Defined in source**: `hydrograph_module.f90:268`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hh` | `hyd_output` | 269 |  |

### sorted_duration_curve

- **Defined in source**: `hydrograph_module.f90:273`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `val` | `real` | 275 |  |
| `next` | `integer` | 276 |  |

### duration_curve_points

- **Defined in source**: `hydrograph_module.f90:279`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `min` | `real` | 280 |  |
| `max` | `real` | 281 |  |
| `mean` | `real` | 282 |  |
| `p` | `real, dimension (27)` | 283 | probabilities for all points on the fdc |

### flow_duration_curve

- **Defined in source**: `hydrograph_module.f90:294`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `mfe` | `integer` | 295 |  |
| `mle` | `integer` | 296 |  |
| `p_md` | `duration_curve_points` | 297 | median of all years |
| `yr` | `duration_curve_points` | 298 | flow on the fdc at given percents for each year |

### inflow_unit_hyds

- **Defined in source**: `hydrograph_module.f90:301`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `uh` | `real, dimension (:,:), allocatable` | 303 | unit hydrograph |
| `hyd_flo` | `real, dimension (:,:), allocatable` | 304 | flow hydrograph |

### flashiness_index

- **Defined in source**: `hydrograph_module.f90:307`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sum_q_q1` | `real` | 309 | sum of difference in current day flow minus previous day flow |
| `sum_q` | `real` | 310 | sum of daily flow over simulation period |
| `q_prev` | `real` | 311 | previous day flow |
| `index` | `real` | 312 | index |

### object_connectivity

- **Defined in source**: `hydrograph_module.f90:315`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 316 |  |
| `typ` | `character(len=8)` | 317 | object type - ie hru, hru_lte, sub, chan, res, recall |
| `nhyds` | `integer` | 318 | hru=5, chan=3 - see type hd_tot for each object |
| `lat` | `real` | 319 | latitude (degrees) |
| `long` | `real` | 320 | longitude (degrees) |
| `elev` | `real` | 321 | elevation (m) |
| `plaps` | `real` | 322 | precipitation lapse applied to object precip |
| `tlaps` | `real` | 323 | temperature lapse applied to object precip |
| `area_ha` | `real` | 324 | input drainag area - ha |
| `sp_ob_no` | `integer` | 325 | spatial object number - ie: hru number, channel number, etc |
| `area_ha_calc` | `real` | 326 | calculated drainage area-ha. only for checking - doesn't work if routing across landscape |
| `props` | `integer` | 327 | properties number from data base (ie hru.dat, sub.dat) - change props to data |
| `wst_c` | `character (len=50)` | 328 | weather station name |
| `wst` | `integer` | 329 | weather station number |
| `constit` | `integer` | 330 | constituent data pointer to pesticides, pathogens, metals, salts |
| `props2` | `integer` | 331 | overbank connectivity pointer to landscape units - change props2 to overbank |
| `ruleset` | `character(len=16)` | 332 | points to the name of the dtbl in flo_con.dtl for out flow control |
| `flo_dtbl` | `integer` | 333 | dtbl pointer for flow fraction of hydrograph |
| `num` | `integer` | 334 | spatial object number- ie hru number corresponding to sequential command number this is the first column in hru_dat (doesn"t have to be sequential) |
| `gis_id` | `integer*8` | 336 | gis number for database purposes |
| `fired` | `integer` | 337 | 0=not fired; 1=fired off as a command |
| `cmd_next` | `integer` | 338 | next command (object) number |
| `cmd_prev` | `integer` | 339 | previous command (object) number |
| `cmd_order` | `integer` | 340 | 1=headwater,2=2nd order,etc |
| `src_tot` | `integer` | 341 | total number of outgoing (source) objects |
| `rcv_tot` | `integer` | 342 | total number of incoming (receiving) hydrographs |
| `dfn_tot` | `integer` | 343 | total number of defining objects (ie hru"s within a subbasin) |
| `ru_tot` | `integer` | 344 | number of routing units that contain this object |
| `ru` | `integer, dimension (:), allocatable` | 345 | subbasin the element is in |
| `elem` | `integer` | 346 | subbasins element number for this object- used for routing over (can only have one) |
| `flood_ch_lnk` | `integer` | 347 | channel the landscape unit is linked to |
| `flood_ch_elem` | `integer` | 348 | landscape unit number - 1 is nearest to stream |
| `flood_frac` | `integer` | 349 | fraction of flood flow assigned to the object |
| `obtyp_out` | `character (len=3), dimension (:), allocatable` | 350 | outflow object type (ie 1=hru, 2=sd_hru, 3=sub, 4=chan, etc) |
| `obtypno_out` | `integer, dimension(:), allocatable` | 351 | outflow object type name |
| `obj_out` | `integer, dimension(:), allocatable` | 352 | outflow object |
| `htyp_out` | `character (len=3), dimension (:), allocatable` | 353 | outflow hyd type (ie 1=tot, 2= recharge, 3=surf, etc) |
| `ihtyp_out` | `integer, dimension (:), allocatable` | 354 | outflow hyd type (ie 1=tot, 2= recharge, 3=surf, etc) |
| `frac_out` | `real, dimension (:), allocatable` | 355 | fraction of hydrograph |
| `obtyp_in` | `character(len=8), dimension(:), allocatable` | 356 | inflow object type (ie 1=hru, 2=sd_hru, 3=sub, 4=chan, etc) |
| `obtypno_in` | `integer, dimension(:), allocatable` | 357 | inflow object type number |
| `obj_in` | `integer, dimension(:), allocatable` | 358 |  |
| `htyp_in` | `character (len=3), dimension(:), allocatable` | 359 | inflow hyd type (ie 1=tot, 2= recharge, 3=surf, etc) |
| `ihtyp_in` | `integer, dimension(:), allocatable` | 360 |  |
| `frac_in` | `real, dimension(:), allocatable` | 361 |  |
| `rcvob_inhyd` | `integer, dimension(:), allocatable` | 362 | inflow hydrograph number of receiving object - used for dtbl flow fractions |
| `fdc` | `flow_duration_curve` | 363 | use for daily flows and then use to get median of annual fdc"s |
| `fdc_ll` | `sorted_duration_curve` | 364 | linked list of daily flow for year - dimensioned to 366 |
| `fdc_lla` | `sorted_duration_curve` | 365 | linked list of annual flow for simulation - dimensioned to nbyr |
| `flash_idx` | `flashiness_index` | 366 | flashiness index object |
| `hin` | `hyd_output` | 367 | inflow hydrograph for surface runon - sum of all inflow hyds |
| `hin_sur` | `hyd_output` | 368 | inflow hydrograph for surface runoff - sum of all surface inflow hyds |
| `hin_lat` | `hyd_output` | 369 | inflow hydrograph for lateral soil flow - sum of all lateral inflow hyds |
| `hin_til` | `hyd_output` | 370 | inflow hydrograph for tile flow - sum of all tile inflow hyds |
| `hin_aqu` | `hyd_output` | 371 | inflow hydrograph for aquifer flow - sum of all aquifer inflow hyds |
| `hd` | `hyd_output` | 372 | daily hydrograph (ie 1=tot, 2= recharge, 3=surf, etc) |
| `hd_aa` | `hyd_output` | 373 | ave annual hydrograph for hru for swift (ie 1=tot, 2= recharge, 3=surf, etc) |
| `ts` | `hyd_output` | 374 | subdaily hydrographs |
| `hin_uh` | `inflow_unit_hyds` | 375 | inflow unit hydrographs |
| `uh` | `real, dimension(:,:), allocatable` | 376 | subdaily surface runoff unit hydrograph |
| `hyd_flo` | `real, dimension(:,:), allocatable` | 377 | subdaily surface runoff hydrograph |
| `tsin` | `real, dimension(:),allocatable` | 378 | inflow subdaily flow hydrograph |
| `trans` | `hyd_output` | 379 | water transfer in water allocation |
| `hin_tot` | `hyd_output` | 380 | total inflow hydrograph to the object |
| `hout_tot` | `hyd_output` | 381 | total outflow hydrograph to the object |
| `conc_prev` | `hyd_output` | 382 | concentration of previous timestep for watqual2e routine |
| `demand` | `real` | 383 | water irrigation demand (ha-m) |
| `day_cur` | `integer` | 384 | current hydrograph day in ts |
| `day_max` | `integer` | 385 | maximum number of days to store the hydrograph |
| `peakrate` | `real` | 386 | peak flow rate during time step - m3/s |
| `hin_d` | `hyd_output` | 388 |  |
| `hin_m` | `hyd_output` | 389 |  |
| `hin_y` | `hyd_output` | 390 |  |
| `hin_a` | `hyd_output` | 391 |  |
| `hout_m` | `hyd_output` | 392 |  |
| `hout_y` | `hyd_output` | 393 |  |
| `hout_a` | `hyd_output` | 394 |  |
| `hdep_m` | `hyd_output` | 395 |  |
| `hdep_y` | `hyd_output` | 396 |  |
| `hdep_a` | `hyd_output` | 397 | rtb gwflow |
| `hdsep` | `hyd_sep` | 400 |  |
| `hdsep_in` | `hyd_sep` | 400 |  |
| `obj_subs` | `integer, dimension(:), allocatable` | 402 | subbasins object number that contain this object |

### irrigation_water_transfer

- **Defined in source**: `hydrograph_module.f90:407`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `demand` | `real` | 408 | irrigation demand \|m3 |
| `applied` | `real` | 409 | irrigation applied \|mm |
| `runoff` | `real` | 410 | irrigation surface runoff \|mm |
| `eff` | `real` | 411 | irrigation efficiency as a fraction of irrigation. Jaehak 2022 |
| `frac_surq` | `real` | 412 | fraction of irrigation lost in runoff flow. Jaehak 2022 |
| `no3` | `real` | 413 | nitrate concentration in irrigation water \|kg Jaehak 2023 |
| `salt` | `real` | 414 | salt concentration in irrigation water \|ppm hyd_output units are in mm and mg/L |
| `water` | `hyd_output` | 416 | irrigation water |

### recall_hydrograph_inputs

- **Defined in source**: `hydrograph_module.f90:421`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hd` | `hyd_output` | 423 | m3/s for flow \|input total hyd for daily, monthly, annual and exco |
| `hyd_flo` | `real, dimension (:,:), allocatable` | 424 | m3/s \|input total flow hyd only for subdaily recall |
| `start_yr` | `integer` | 425 | start year of point source file |
| `end_yr` | `integer` | 426 | end year of point source file |

### spatial_objects

- **Defined in source**: `hydrograph_module.f90:430`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `objs` | `integer` | 431 | number of objects or 1st object command |
| `hru` | `integer` | 432 | 1-number of hru"s or 1st hru command |
| `hru_lte` | `integer` | 433 | 2-number of hru_lte"s or 1st hru_lte command |
| `ru` | `integer` | 435 | 3-number of ru"s or 1st ru command |
| `gwflow` | `integer` | 436 | 4-number of gwflow"s or 1st gwflow command !rtb gwflow |
| `aqu` | `integer` | 437 | 5-number of aquifer"s or 1st aquifer command |
| `chan` | `integer` | 438 | 6-number of chan"s or 1st chan command |
| `res` | `integer` | 439 | 7-number of res"s or 1st res command |
| `recall` | `integer` | 440 | 8-number of recdays"s or 1st recday command |
| `exco` | `integer` | 441 | 11-number of exco"s or 1st export coeff command |
| `dr` | `integer` | 442 | 12-number of dr"s or 1st del ratio command |
| `canal` | `integer` | 443 | 13-number of canal"s or 1st canal command |
| `pump` | `integer` | 444 | 14-number of pump"s or 1st pump command |
| `outlet` | `integer` | 445 | 15-number of outlet"s or 1st outlet command |
| `chandeg` | `integer` | 446 | 16-number of swat-deg channel"s or 1st swat-deg channel command |
| `aqu2d` | `integer` | 447 | 17-not currently used (number of 2D aquifer"s or 1st 2D aquifer command) |
| `herd` | `integer` | 448 | 18-not currently used (number of herds) |
| `wro` | `integer` | 449 | 19-not currently used (number of water rights) |

### object_total_hydrographs

- **Defined in source**: `hydrograph_module.f90:454`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru` | `integer` | 455 | 1=total 2=recharge 3=surface 4=lateral 5= tile |
| `hru_lte` | `integer` | 456 | 1=total 2=recharge 3=surface 4=lateral 5= tile |
| `ru` | `integer` | 457 | 1=total 2=recharge 3=surface 4=lateral 5= tile |
| `gwflow` | `integer` | 458 | 1=total |
| `aqu` | `integer` | 459 | 1=return flow 2=deep perc |
| `chan` | `integer` | 460 | 1=total 2=recharge 3=overbank |
| `res` | `integer` | 461 | 1=total 2=recharge |
| `recall` | `integer` | 462 | 1=total |
| `exco` | `integer` | 463 | 1=surface 2=groundwater |
| `dr` | `integer` | 464 | 1=surface 2=groundwater |
| `pump` | `integer` | 465 | 1=total |
| `outlet` | `integer` | 466 | 1=total |
| `chandeg` | `integer` | 467 | 1=total 2=recharge 3=overbank |
| `aqu2d` | `integer` | 468 | 1=return flow 3=deep perc |
| `herd` | `integer` | 469 |  |
| `wro` | `integer` | 470 |  |

### routing_unit_data

- **Defined in source**: `hydrograph_module.f90:474`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 475 |  |
| `num_tot` | `integer` | 476 |  |
| `num` | `integer, dimension (:), allocatable` | 477 | points to subbasin element (sub_elem) |

### routing_unit_elements

- **Defined in source**: `hydrograph_module.f90:481`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 482 |  |
| `obj` | `integer` | 483 | object number |
| `obtyp` | `character (len=3)` | 484 | object type- 1=hru, 2=hru_lte, 11=export coef, etc |
| `obtypno` | `integer` | 485 | 2-number of hru_lte"s or 1st hru_lte command |
| `frac` | `real` | 486 | fraction of element in ru (expansion factor) |
| `dr_name` | `character(len=16)` | 487 | name of dr in delratio.del |
| `dr` | `hyd_output` | 488 | calculated (or input in delratio.del) dr's for element |

### channel_surface_elements

- **Defined in source**: `hydrograph_module.f90:495`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 496 |  |
| `num` | `integer` | 497 | number of elements |
| `chnum` | `integer` | 498 | channel number |
| `resnum` | `integer` | 499 |  |
| `obtyp` | `character (len=3), dimension(:), allocatable` | 500 | object type- 1=hru, 2=hru_lte, 11=export coef, etc |
| `obtypno` | `integer, dimension(:), allocatable` | 501 | 2-number of hru_lte"s or 1st hru_lte command |
| `wid` | `real, dimension(:), allocatable` | 503 | maxflood plain width for each element |
| `dep` | `real, dimension(:), allocatable` | 504 | max flood depth for each element |
| `flood_volmx` | `real, dimension(:), allocatable` | 505 | max flood volume for each landscape unit |
| `hd` | `hyd_output` | 506 | flood water for each element |

### geomorphic_baseflow_channel_data

- **Defined in source**: `hydrograph_module.f90:511`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `area` | `real` | 513 | drainage area of the channel |
| `len` | `real` | 514 | length of the channel |
| `len_left` | `real` | 515 | fraction of chan length left when channel becomes non-contributing |
| `flo_fr` | `real` | 516 | fraction of aquifer baseflow for each channel |

### channel_aquifer_elements

- **Defined in source**: `hydrograph_module.f90:521`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 522 |  |
| `num_tot` | `integer` | 523 | number of elements |
| `num` | `integer, dimension(:), allocatable` | 524 | channel numbers |
| `len_tot` | `real` | 525 | total length of channels in aquifer (km) |
| `hd` | `hyd_output` | 526 | baseflow hydrograph for the aquifer |
| `ch` | `geomorphic_baseflow_channel_data` | 527 |  |

### hyd_header

- **Defined in source**: `hydrograph_module.f90:537`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=17)` | 538 | ha-m \|volume of water |
| `sed` | `character (len=15)` | 539 | metric tons \|sediment |
| `orgn` | `character (len=15)` | 540 | kg N \|organic N |
| `sedp` | `character (len=15)` | 541 | kg P \|organic P |
| `no3` | `character (len=15)` | 542 | kg N \|NO3-N |
| `solp` | `character (len=15)` | 543 | kg P \|mineral (soluble P) |
| `chla` | `character (len=15)` | 544 | kg \|chlorophyll-a |
| `nh3` | `character (len=15)` | 545 | kg N \|NH3 |
| `no2` | `character (len=15)` | 546 | kg N \|NO2 |
| `cbod` | `character (len=15)` | 547 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=15)` | 548 | kg \|dissolved oxygen |
| `san` | `character (len=15)` | 549 | tons \|detached sand |
| `sil` | `character (len=15)` | 550 | tons \|detached silt |
| `cla` | `character (len=15)` | 551 | tons \|detached clay |
| `sag` | `character (len=15)` | 552 | tons \|detached small ag |
| `lag` | `character (len=15)` | 553 | tons \|detached large ag |
| `grv` | `character (len=15)` | 554 | tons \|gravel |
| `temp` | `character (len=15)` | 555 | deg c \|temperature |

### hyd_stor_header

- **Defined in source**: `hydrograph_module.f90:559`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_stor` | `character (len=17)` | 560 | m^3/s \|water stored at the end of time period |
| `sed_stor` | `character (len=15)` | 561 | metric tons \|sediment stored at the end of time period |
| `orgn_stor` | `character (len=15)` | 562 | kg N \|organic N stored at the end of time period |
| `sedp_stor` | `character (len=15)` | 563 | kg P \|organic P stored at the end of time period |
| `no3_stor` | `character (len=15)` | 564 | kg N \|NO3-N stored at the end of time period |
| `solp_stor` | `character (len=15)` | 565 | kg P \|mineral (soluble P) stored at end of time period |
| `chla_stor` | `character (len=15)` | 566 | kg \|chlorophyll-a stored at end of time period |
| `nh3_stor` | `character (len=15)` | 567 | kg N \|NH3-N (ammonium) stored at end of time period |
| `no2_stor` | `character (len=15)` | 568 | kg N \|NO2-N (nitrite) stored at end of time period |
| `cbod_stor` | `character (len=15)` | 569 | kg \|carbonaceous biological oxygen demand at end of time period |
| `dox_stor` | `character (len=15)` | 570 | kg \|dissolved oxygen stored at end of time period |
| `san_stor` | `character (len=15)` | 571 | tons \|detached sand stored at end of time period |
| `sil_stor` | `character (len=15)` | 572 | tons \|detached silt stored at end of time period |
| `cla_stor` | `character (len=15)` | 573 | tons \|detached clay stored at end of time period |
| `sag_stor` | `character (len=15)` | 574 | tons \|detached small ag stored at end of time period |
| `lag_stor` | `character (len=15)` | 575 | tons \|detached large ag stored at end of time period |
| `grv_stor` | `character (len=15)` | 576 | tons \|gravel stored at end of time period |
| `temp_stor` | `character (len=15)` | 577 | deg c \|water temperature |

### hyd_in_header

- **Defined in source**: `hydrograph_module.f90:581`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `character (len=15)` | 582 | m^3/s \|water in |
| `sed_in` | `character (len=15)` | 583 | metric tons \|sediment in |
| `orgn_in` | `character (len=15)` | 584 | kg N \|organic N in |
| `sedp_in` | `character (len=15)` | 585 | kg P \|organic P in |
| `no3_in` | `character (len=15)` | 586 | kg N \|NO3-N (nitrate) in |
| `solp_in` | `character (len=15)` | 587 | kg P \|mineral (soluble P) in |
| `chla_in` | `character (len=15)` | 588 | kg \|chlorophyll-a in |
| `nh3_in` | `character (len=15)` | 589 | kg N \|NH3-N (ammonium) in |
| `no2_in` | `character (len=15)` | 590 | kg N \|NO2-N (nitrate) in |
| `cbod_in` | `character (len=15)` | 591 | kg \|carbonaceous biological oxygen demand in |
| `dox_in` | `character (len=15)` | 592 | kg \|dissolved oxygen in |
| `san_in` | `character (len=15)` | 593 | tons \|detached sand in |
| `sil_in` | `character (len=15)` | 594 | tons \|detached silt in |
| `cla_in` | `character (len=15)` | 595 | tons \|detached clay in |
| `sag_in` | `character (len=15)` | 596 | tons \|detached small ag in |
| `lag_in` | `character (len=15)` | 597 | tons \|detached large ag in |
| `grv_in` | `character (len=15)` | 598 | tons \|gravel in |
| `temp_in` | `character (len=15)` | 599 | deg c \|temperature in |

### hyd_out_header

- **Defined in source**: `hydrograph_module.f90:603`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_out` | `character (len=15)` | 604 | m^3/s \|water out |
| `sed_out` | `character (len=15)` | 605 | metric tons \|sediment out |
| `orgn_out` | `character (len=15)` | 606 | kg N \|organic N out |
| `sedp_out` | `character (len=15)` | 607 | kg P \|organic P out |
| `no3_out` | `character (len=15)` | 608 | kg N \|NO3-N out |
| `solp_out` | `character (len=15)` | 609 | kg P \|mineral (soluble P) out |
| `chla_out` | `character (len=15)` | 610 | kg \|chlorophyll-a out |
| `nh3_out` | `character (len=15)` | 611 | kg N \|NH3-N (ammonium) out |
| `no2_out` | `character (len=15)` | 612 | kg N \|NO2-N (nitrite) out |
| `cbod_out` | `character (len=15)` | 613 | kg \|carbonaceous biological oxygen demand out |
| `dox_out` | `character (len=15)` | 614 | kg \|dissolved oxygen out |
| `san_out` | `character (len=15)` | 615 | tons \|detached sand out |
| `sil_out` | `character (len=15)` | 616 | tons \|detached silt out |
| `cla_out` | `character (len=15)` | 617 | tons \|detached clay out |
| `sag_out` | `character (len=15)` | 618 | tons \|detached small ag out |
| `lag_out` | `character (len=15)` | 619 | tons \|detached large ag out |
| `grv_out` | `character (len=15)` | 620 | tons \|gravel out |
| `temp_out` | `character (len=15)` | 621 | deg c \|temperature out |

### hyd_inout_header

- **Defined in source**: `hydrograph_module.f90:625`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `character (len=15)` | 626 | m^3/s \|water in |
| `flo_out` | `character (len=15)` | 627 | m^3/s \|water out |
| `sed_in` | `character (len=15)` | 628 | metric tons \|sediment in |
| `sed_out` | `character (len=15)` | 629 | metric tons \|sediment out |
| `orgn_in` | `character (len=15)` | 630 | kg N \|organic N in |
| `orgn_out` | `character (len=15)` | 631 | kg N \|organic N out |
| `sedp_in` | `character (len=15)` | 632 | kg P \|organic P in |
| `sedp_out` | `character (len=15)` | 633 | kg P \|organic P out |
| `no3_in` | `character (len=15)` | 634 | kg N \|NO3-N (nitrate) in |
| `no3_out` | `character (len=15)` | 635 | kg N \|NO3-N out |
| `solp_in` | `character (len=15)` | 636 | kg P \|mineral (soluble P) in |
| `solp_out` | `character (len=15)` | 637 | kg P \|mineral (soluble P) out |
| `chla_in` | `character (len=15)` | 638 | kg \|chlorophyll-a in |
| `chla_out` | `character (len=15)` | 639 | kg \|chlorophyll-a out |
| `nh3_in` | `character (len=15)` | 640 | kg N \|NH3-N (ammonium) in |
| `nh3_out` | `character (len=15)` | 641 | kg N \|NH3-N (ammonium) out |
| `no2_in` | `character (len=15)` | 642 | kg N \|NO2-N (nitrate) in |
| `no2_out` | `character (len=15)` | 643 | kg N \|NO2-N (nitrite) out |
| `cbod_in` | `character (len=15)` | 644 | kg \|carbonaceous biological oxygen demand in |
| `cbod_out` | `character (len=15)` | 645 | kg \|carbonaceous biological oxygen demand out |
| `dox_in` | `character (len=15)` | 646 | kg \|dissolved oxygen in |
| `dox_out` | `character (len=15)` | 647 | kg \|dissolved oxygen out |

### wtmp_out_header

- **Defined in source**: `hydrograph_module.f90:651`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `water_temp` | `character (len=15)` | 652 | deg c \|temperature |

### sed_hyd_header

- **Defined in source**: `hydrograph_module.f90:656`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `character (len=15)` | 657 | m^3/s \|volume of water |
| `flo_out` | `character (len=15)` | 658 | m^3/s \|volume of water |
| `sed_in` | `character (len=15)` | 659 | metric tons \|sediment |
| `sed_out` | `character (len=15)` | 660 | metric tons \|sediment |
| `orgn_in` | `character (len=15)` | 661 | kg N \|organic N |
| `orgn_out` | `character (len=15)` | 662 | kg N \|organic N |
| `sedp_in` | `character (len=15)` | 663 | kg P \|organic P |
| `sedp_out` | `character (len=15)` | 664 | kg P \|organic P |
| `no3_in` | `character (len=15)` | 665 | kg N \|NO3-N |
| `no3_out` | `character (len=15)` | 666 | kg N \|NO3-N |
| `solp_in` | `character (len=15)` | 667 | kg P \|mineral (soluble P) |
| `solp_out` | `character (len=15)` | 668 | kg P \|mineral (soluble P) |
| `chla_in` | `character (len=15)` | 669 | kg \|chlorophyll-a |
| `chla_out` | `character (len=15)` | 670 | kg \|chlorophyll-a |
| `nh3_in` | `character (len=15)` | 671 | kg N \|NH3 |
| `nh3_out` | `character (len=15)` | 672 | kg N \|NH3 |
| `no2_in` | `character (len=15)` | 673 | kg N \|NO2 |
| `no2_out` | `character (len=15)` | 674 | kg N \|NO2 |
| `cbod_in` | `character (len=15)` | 675 | kg \|carbonaceous biological oxygen demand |
| `cbod_out` | `character (len=15)` | 676 | kg \|carbonaceous biological oxygen demand |
| `dox_in` | `character (len=15)` | 677 | kg \|dissolved oxygen |
| `dox_out` | `character (len=15)` | 678 | kg \|dissolved oxygen |
| `temp_in` | `character (len=15)` | 679 | deg c \|temperature |
| `temp_out` | `character (len=15)` | 680 | deg c \|temperature |

### sd_hyd_header_units

- **Defined in source**: `hydrograph_module.f90:684`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `character (len=15)` | 685 | avg daily m^3/s \|volume of water |
| `flo_out` | `character (len=15)` | 686 | avg daily m^3/s \|volume of water |
| `sed_in` | `character (len=15)` | 687 | metric tons \|sediment |
| `sed_out` | `character (len=15)` | 688 | metric tons \|sediment |
| `orgn_in` | `character (len=15)` | 689 | kg N \|organic N |
| `orgn_out` | `character (len=15)` | 690 | kg N \|organic N |
| `sedp_in` | `character (len=15)` | 691 | kg P \|organic P |
| `sedp_out` | `character (len=15)` | 692 | kg P \|organic P |
| `no3_in` | `character (len=15)` | 693 | kg N \|NO3-N |
| `no3_out` | `character (len=15)` | 694 | kg N \|NO3-N |
| `solp_in` | `character (len=15)` | 695 | kg P \|mineral (soluble P) |
| `solp_out` | `character (len=15)` | 696 | kg P \|mineral (soluble P) |
| `chla_in` | `character (len=15)` | 697 | kg \|chlorophyll-a |
| `chla_out` | `character (len=15)` | 698 | kg \|chlorophyll-a |
| `nh3_in` | `character (len=15)` | 699 | kg N \|NH3 |
| `nh3_out` | `character (len=15)` | 700 | kg N \|NH3 |
| `no2_in` | `character (len=15)` | 701 | kg N \|NO2 |
| `no2_out` | `character (len=15)` | 702 | kg N \|NO2 |
| `cbod_in` | `character (len=15)` | 703 | kg \|carbonaceous biological oxygen demand |
| `cbod_out` | `character (len=15)` | 704 | kg \|carbonaceous biological oxygen demand |
| `dox_in` | `character (len=15)` | 705 | kg \|dissolved oxygen |
| `dox_out` | `character (len=15)` | 706 | kg \|dissolved oxygen |
| `temp_in` | `character (len=15)` | 707 | deg c \|temperature |
| `temp_out` | `character (len=15)` | 708 | deg c \|temperature |

### sol_header

- **Defined in source**: `hydrograph_module.f90:712`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `layer1` | `character (len=15)` | 713 | mm H2O \|plant name |
| `layer2` | `character (len=15)` | 714 | mm H2O \|amt of water stored in layer 2 |
| `layer3` | `character (len=15)` | 715 | mm H2O \|amt of water stored in layer 3 |
| `layer4` | `character (len=15)` | 716 | mm H2O \|amt of water stored in layer 4 |
| `layer5` | `character (len=15)` | 717 | mm H2O \|amt of water stored in layer 5 |
| `layer6` | `character (len=15)` | 718 | mm H2O \|amt of water stored in layer 6 |
| `layer7` | `character (len=15)` | 719 | mm H2O \|amt of water stored in layer 7 |
| `layer8` | `character (len=15)` | 720 | mm H2O \|amt of water stored in layer 8 |
| `layer9` | `character (len=15)` | 721 | mm H2O \|amt of water stored in layer 9 |
| `layer10` | `character (len=15)` | 722 | mm H2O \|amt of water stored in layer 10 |

### plant_header

- **Defined in source**: `hydrograph_module.f90:726`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=17)` | 727 | none \|plant name |
| `growing` | `character (len=15)` | 728 | none \|plant growing |
| `dormant` | `character (len=15)` | 729 | none \|plant dormant |
| `lai` | `character (len=15)` | 730 | none \|leaf area index |
| `can_hgt` | `character (len=15)` | 731 | m \|canopy height |
| `root_dep` | `character (len=15)` | 732 | m \|root depth |
| `phuacc` | `character (len=15)` | 733 | 0-1 \|accumulated heat units |
| `tot_m` | `character (len=15)` | 734 | kg/ha \|total biomass |
| `ab_gr_m` | `character (len=15)` | 735 | kg/ha \|above ground biomass |
| `leaf_m` | `character (len=15)` | 736 | kg/ha \|leaf biomass |
| `root_m` | `character (len=15)` | 737 | kg/ha \|root biomass |
| `stem_m` | `character (len=15)` | 738 | kg/ha \|stem biomass |
| `seed_m` | `character (len=15)` | 739 | kg/ha \|seed biomass |

### flood_plain_header

- **Defined in source**: `hydrograph_module.f90:743`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `inflo` | `character (len=15)` | 744 | m3 \| inflow |
| `outflo` | `character (len=15)` | 745 | m3 \| outflow |
| `dormant` | `character (len=15)` | 746 | m3 \| evaporation |
| `tl` | `character (len=15)` | 747 | m3 \| transmission losses |
| `ev` | `character (len=15)` | 748 | m3 \| evaporation |
| `ch_stor_init` | `character (len=15)` | 749 | m3 \| channel storage at start of time step |
| `ch_stor` | `character (len=15)` | 750 | m3 \| channel storage at end of time step |
| `fp_stor_init` | `character (len=15)` | 751 | m3 \| flood plain storage at start of time step (all flood plain storage above wetland emergency volume) |
| `fp_stor` | `character (len=15)` | 752 | m3 \| flood plain storage at end of time step |
| `tot_stor_init` | `character (len=15)` | 753 | m3 \| total channel + wetland storage at start of time step |
| `tot_stor` | `character (len=15)` | 754 | m3 \| total channel + wetland storage at end of time step |
| `wet_stor_init` | `character (len=15)` | 755 | m3 \| wetland flood plain storage at start of time step |
| `wet_stor` | `character (len=15)` | 756 | m3 \| wetland flood plain storage at end of time step |

### ch_watbod_header

- **Defined in source**: `hydrograph_module.f90:760`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 761 |  |
| `mo` | `character (len=6)` | 762 |  |
| `day_mo` | `character (len=6)` | 763 |  |
| `yrc` | `character (len=6)` | 764 |  |
| `isd` | `character (len=9)` | 765 |  |
| `id` | `character (len=9)` | 766 |  |
| `name` | `character (len=15)` | 767 |  |
| `area_ha` | `character (len=15)` | 768 |  |
| `precip` | `character (len=15)` | 769 |  |
| `evap` | `character (len=15)` | 770 |  |
| `seep` | `character (len=15)` | 771 |  |

### ch_watbod_header_units

- **Defined in source**: `hydrograph_module.f90:775`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 776 |  |
| `mo` | `character (len=6)` | 777 |  |
| `day_mo` | `character (len=6)` | 778 |  |
| `yrc` | `character (len=6)` | 779 |  |
| `isd` | `character (len=9)` | 780 |  |
| `id` | `character (len=9)` | 781 |  |
| `name` | `character (len=15)` | 782 |  |
| `area_ha` | `character (len=15)` | 783 |  |
| `precip` | `character (len=15)` | 784 |  |
| `evap` | `character (len=15)` | 785 |  |
| `seep` | `character (len=15)` | 786 |  |

### ch_watbod_inoutheader

- **Defined in source**: `hydrograph_module.f90:790`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 791 |  |
| `mo` | `character (len=6)` | 792 |  |
| `day_mo` | `character (len=6)` | 793 |  |
| `yrc` | `character (len=6)` | 794 |  |
| `id` | `character (len=9)` | 795 |  |
| `gis_id` | `character (len=9)` | 796 |  |
| `name` | `character (len=15)` | 797 |  |

### ch_watbod_inoutheader_units

- **Defined in source**: `hydrograph_module.f90:801`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=6)` | 802 |  |
| `mo` | `character (len=6)` | 803 |  |
| `day_mo` | `character (len=6)` | 804 |  |
| `yrc` | `character (len=6)` | 805 |  |
| `id` | `character (len=9)` | 806 |  |
| `gis_id` | `character (len=9)` | 807 |  |
| `name` | `character (len=15)` | 808 |  |

### hyd_header_units1

- **Defined in source**: `hydrograph_module.f90:812`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=15)` | 813 | m^3/s \|volume of water |
| `sed` | `character (len=15)` | 814 | metric tons \|sediment |
| `orgn` | `character (len=15)` | 815 | kg N \|organic N |
| `sedp` | `character (len=15)` | 816 | kg P \|organic P |
| `no3` | `character (len=15)` | 817 | kg N \|NO3-N |
| `solp` | `character (len=15)` | 818 | kg P \|mineral (soluble P) |
| `chla` | `character (len=15)` | 819 | kg \|chlorophyll-a |
| `nh3` | `character (len=15)` | 820 | kg N \|NH3 |
| `no2` | `character (len=15)` | 821 | kg N \|NO2 |
| `cbod` | `character (len=15)` | 822 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=15)` | 823 | kg \|dissolved oxygen |
| `san` | `character (len=15)` | 824 | tons \|detached sand |
| `sil` | `character (len=15)` | 825 | tons \|detached silt |
| `cla` | `character (len=15)` | 826 | tons \|detached clay |
| `sag` | `character (len=15)` | 827 | tons \|detached small ag |
| `lag` | `character (len=15)` | 828 | tons \|detached large ag |
| `grv` | `character (len=15)` | 829 | tons \|gravel |
| `temp` | `character (len=15)` | 830 | deg c \|temperature Jaehak 2023 deg c \|temperature deg c \|temperature |

### hyd_header_units3

- **Defined in source**: `hydrograph_module.f90:837`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=15)` | 838 | m^3 \|volume of water |
| `sed` | `character (len=15)` | 839 | metric tons \|sediment |
| `orgn` | `character (len=15)` | 840 | kg N \|organic N |
| `sedp` | `character (len=15)` | 841 | kg P \|organic P |
| `no3` | `character (len=15)` | 842 | kg N \|NO3-N |
| `solp` | `character (len=15)` | 843 | kg P \|mineral (soluble P) |
| `chla` | `character (len=15)` | 844 | kg \|chlorophyll-a |
| `nh3` | `character (len=15)` | 845 | kg N \|NH3 |
| `no2` | `character (len=15)` | 846 | kg N \|NO2 |
| `cbod` | `character (len=15)` | 847 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=15)` | 848 | kg \|dissolved oxygen |
| `san` | `character (len=15)` | 849 | tons \|detached sand |
| `sil` | `character (len=15)` | 850 | tons \|detached silt |
| `cla` | `character (len=15)` | 851 | tons \|detached clay |
| `sag` | `character (len=15)` | 852 | tons \|detached small ag |
| `lag` | `character (len=15)` | 853 | tons \|detached large ag |
| `grv` | `character (len=15)` | 854 | tons \|gravel |
| `temp` | `character (len=15)` | 855 | deg c \|temperature Jaehak 2023 deg c \|temperature deg c \|temperature |

### hydinout_header_units1

- **Defined in source**: `hydrograph_module.f90:862`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo_in` | `character (len=15)` | 863 | avg daily m^3/s \|volume of water |
| `flo_out` | `character (len=15)` | 864 | avg daily m^3/s \|volume of water |
| `sed_in` | `character (len=15)` | 865 | metric tons \|sediment |
| `sed_out` | `character (len=15)` | 866 | metric tons \|sediment |
| `orgn_in` | `character (len=15)` | 867 | kg N \|organic N |
| `orgn_out` | `character (len=15)` | 868 | kg N \|organic N |
| `sedp_in` | `character (len=15)` | 869 | kg P \|organic P |
| `sedp_ouy` | `character (len=15)` | 870 | kg P \|organic P |
| `no3_in` | `character (len=15)` | 871 | kg N \|NO3-N |
| `no3_out` | `character (len=15)` | 872 | kg N \|NO3-N |
| `solp_in` | `character (len=15)` | 873 | kg P \|mineral (soluble P) |
| `solp_out` | `character (len=15)` | 874 | kg P \|mineral (soluble P) |
| `chla_in` | `character (len=15)` | 875 | kg \|chlorophyll-a |
| `chla_out` | `character (len=15)` | 876 | kg \|chlorophyll-a |
| `nh3_in` | `character (len=15)` | 877 | kg N \|NH3 |
| `nh3_out` | `character (len=15)` | 878 | kg N \|NH3 |
| `no2_in` | `character (len=15)` | 879 | kg N \|NO2 |
| `no2_out` | `character (len=15)` | 880 | kg N \|NO2 |
| `cbod_in` | `character (len=15)` | 881 | kg \|carbonaceous biological oxygen demand |
| `cbod_out` | `character (len=15)` | 882 | kg \|carbonaceous biological oxygen demand |
| `dox_in` | `character (len=15)` | 883 | kg \|dissolved oxygen |
| `dox_out` | `character (len=15)` | 884 | kg \|dissolved oxygen |

### wtmp_header_units

- **Defined in source**: `hydrograph_module.f90:888`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `wtmp` | `character (len=15)` | 889 | deg c \|temperature |

### hyd_header_units

- **Defined in source**: `hydrograph_module.f90:893`
- **Source note**: pts (point source)/deposition/ru (routing_unit) files output uses this units header

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 894 |  |
| `mo` | `character (len=12)` | 895 |  |
| `day_mo` | `character (len=12)` | 896 |  |
| `yrc` | `character (len=13)` | 897 |  |
| `name` | `character (len=12)` | 898 |  |
| `otype` | `character (len=6)` | 899 |  |
| `flo` | `character (len=17)` | 900 | m^3/s \|volume of water |
| `sed` | `character (len=15)` | 901 | metric tons \|sediment |
| `orgn` | `character (len=15)` | 902 | kg N \|organic N |
| `sedp` | `character (len=15)` | 903 | kg P \|organic P |
| `no3` | `character (len=15)` | 904 | kg N \|NO3-N |
| `solp` | `character (len=15)` | 905 | kg P \|mineral (soluble P) |
| `chla` | `character (len=15)` | 906 | kg \|chlorophyll-a |
| `nh3` | `character (len=15)` | 907 | kg N \|NH3 |
| `no2` | `character (len=15)` | 908 | kg N \|NO2 |
| `cbod` | `character (len=15)` | 909 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=15)` | 910 | kg \|dissolved oxygen |
| `san` | `character (len=15)` | 911 | tons \|detached sand |
| `sil` | `character (len=15)` | 912 | tons \|detached silt |
| `cla` | `character (len=15)` | 913 | tons \|detached clay |
| `sag` | `character (len=15)` | 914 | tons \|detached small ag |
| `lag` | `character (len=15)` | 915 | tons \|detached large ag |
| `grv` | `character (len=15)` | 916 | tons \|gravel |
| `temp` | `character (len=15)` | 917 | deg c \|temperature |

### hyd_header_units2

- **Defined in source**: `hydrograph_module.f90:921`
- **Source note**: hydin/hydout files uses this units header

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 922 |  |
| `mo` | `character (len=12)` | 923 |  |
| `day_mo` | `character (len=12)` | 924 |  |
| `yrc` | `character (len=13)` | 925 |  |
| `name` | `character (len=12)` | 926 |  |
| `otype` | `character (len=6)` | 927 |  |
| `iotyp` | `character (len=13)` | 928 |  |
| `iotypno` | `character (len=9)` | 929 |  |
| `hydio` | `character (len=8)` | 930 |  |
| `objno` | `character (len=8)` | 931 |  |
| `flo` | `character (len=17)` | 932 | m^3/s \|volume of water |
| `sed` | `character (len=15)` | 933 | metric tons \|sediment |
| `orgn` | `character (len=15)` | 934 | kg N \|organic N |
| `sedp` | `character (len=15)` | 935 | kg P \|organic P |
| `no3` | `character (len=15)` | 936 | kg N \|NO3-N |
| `solp` | `character (len=15)` | 937 | kg P \|mineral (soluble P) |
| `chla` | `character (len=15)` | 938 | kg \|chlorophyll-a |
| `nh3` | `character (len=15)` | 939 | kg N \|NH3 |
| `no2` | `character (len=15)` | 940 | kg N \|NO2 |
| `cbod` | `character (len=15)` | 941 | kg \|carbonaceous biological oxygen demand |
| `dox` | `character (len=15)` | 942 | kg \|dissolved oxygen |
| `san` | `character (len=15)` | 943 | tons \|detached sand |
| `sil` | `character (len=15)` | 944 | tons \|detached silt |
| `cla` | `character (len=15)` | 945 | tons \|detached clay |
| `sag` | `character (len=15)` | 946 | tons \|detached small ag |
| `lag` | `character (len=15)` | 947 | tons \|detached large ag |
| `grv` | `character (len=15)` | 948 | tons \|gravel |
| `temp` | `character (len=15)` | 949 | deg c \|temperature |

### hyd_header_time

- **Defined in source**: `hydrograph_module.f90:954`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 955 |  |
| `mo` | `character (len=12)` | 956 |  |
| `day_mo` | `character (len=12)` | 957 |  |
| `yrc` | `character (len=13)` | 958 |  |
| `name` | `character (len=12)` | 959 |  |
| `otype` | `character (len=6)` | 960 |  |

### rec_header_time

- **Defined in source**: `hydrograph_module.f90:964`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 965 |  |
| `mo` | `character (len=12)` | 966 |  |
| `day_mo` | `character (len=12)` | 967 |  |
| `yrc` | `character (len=13)` | 968 |  |
| `name` | `character (len=12)` | 969 |  |
| `blank` | `character (len=6)` | 970 |  |

### hyd_header_obj

- **Defined in source**: `hydrograph_module.f90:974`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `iotyp` | `character (len=13)` | 975 |  |
| `iotypno` | `character (len=9)` | 976 |  |
| `hydio` | `character (len=8)` | 977 |  |
| `objno` | `character (len=8)` | 978 |  |

### output_flow_duration_header

- **Defined in source**: `hydrograph_module.f90:982`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `obtyp` | `character (len=11)` | 983 |  |
| `props` | `character (len=12)` | 984 |  |
| `area` | `character (len=12)` | 985 |  |
| `f_idx` | `character (len=12)` | 986 |  |
| `mean` | `character (len=13)` | 987 |  |
| `max` | `character (len=11)` | 988 |  |
| `p01` | `character (len=18)` | 989 |  |
| `p05` | `character (len=13)` | 990 |  |
| `p1` | `character (len=19)` | 991 |  |
| `p2` | `character (len=15)` | 992 |  |
| `p3` | `character (len=15)` | 993 |  |
| `p5` | `character (len=15)` | 994 |  |
| `p10` | `character (len=15)` | 995 |  |
| `p15` | `character (len=15)` | 996 |  |
| `p20` | `character (len=15)` | 997 |  |
| `p25` | `character (len=15)` | 998 |  |
| `p30` | `character (len=15)` | 999 |  |
| `p35` | `character (len=15)` | 1000 |  |
| `p40` | `character (len=15)` | 1001 |  |
| `p45` | `character (len=15)` | 1002 |  |
| `p50` | `character (len=15)` | 1003 |  |
| `p55` | `character (len=15)` | 1004 |  |
| `p60` | `character (len=15)` | 1005 |  |
| `p65` | `character (len=15)` | 1006 |  |
| `p70` | `character (len=15)` | 1007 |  |
| `p75` | `character (len=15)` | 1008 |  |
| `p80` | `character (len=15)` | 1009 |  |
| `p85` | `character (len=15)` | 1010 |  |
| `p90` | `character (len=15)` | 1011 |  |
| `p95` | `character (len=15)` | 1012 |  |
| `p97` | `character (len=15)` | 1013 |  |
| `p98` | `character (len=15)` | 1014 |  |
| `p99` | `character (len=15)` | 1015 |  |
| `min` | `character (len=11)` | 1016 |  |

### calibration_header

- **Defined in source**: `hydrograph_module.f90:1020`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 1021 |  |
| `ha` | `character (len=12)` | 1022 |  |
| `nbyr` | `character (len=12)` | 1023 |  |
| `prec` | `character (len=12)` | 1024 |  |
| `meas` | `character (len=16)` | 1025 |  |
| `srr` | `character (len=12)` | 1026 |  |
| `lfr` | `character (len=12)` | 1027 |  |
| `pcr` | `character (len=12)` | 1028 |  |
| `etr` | `character (len=12)` | 1029 |  |
| `tfr` | `character (len=12)` | 1030 |  |
| `sed` | `character (len=12)` | 1031 |  |
| `orgn` | `character (len=12)` | 1032 |  |
| `orgp` | `character (len=12)` | 1033 |  |
| `no3` | `character (len=12)` | 1034 |  |
| `solp` | `character (len=12)` | 1035 |  |
| `aa` | `character (len=16)` | 1036 |  |
| `srr_aa` | `character (len=12)` | 1037 |  |
| `lfr_aa` | `character (len=12)` | 1038 |  |
| `pcr_aa` | `character (len=12)` | 1039 |  |
| `etr_aa` | `character (len=12)` | 1040 |  |
| `tfr_aa` | `character (len=12)` | 1041 |  |
| `sed_aa` | `character (len=12)` | 1042 |  |
| `orgn_aa` | `character (len=12)` | 1043 |  |
| `orgp_aa` | `character (len=12)` | 1044 |  |
| `no3_aa` | `character (len=12)` | 1045 |  |
| `solp_aa` | `character (len=12)` | 1046 |  |
| `cn_prm_aa` | `character (len=12)` | 1047 |  |
| `esco` | `character (len=12)` | 1048 |  |
| `lat_len` | `character (len=12)` | 1049 |  |
| `petco` | `character (len=12)` | 1050 |  |
| `slope` | `character (len=12)` | 1051 |  |
| `tconc` | `character (len=12)` | 1052 |  |
| `etco` | `character (len=12)` | 1053 |  |
| `perco` | `character (len=12)` | 1054 |  |
| `revapc` | `character (len=12)` | 1055 |  |
| `cn3_swf` | `character (len=12)` | 1056 |  |

### calibration2_header

- **Defined in source**: `hydrograph_module.f90:1060`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 1061 |  |
| `dakm2` | `character (len=12)` | 1062 |  |
| `cn2` | `character (len=12)` | 1063 |  |
| `tc` | `character (len=12)` | 1064 |  |
| `soildep` | `character (len=12)` | 1065 |  |
| `perco_co` | `character (len=12)` | 1066 |  |
| `slope` | `character (len=12)` | 1067 |  |
| `slopelen` | `character (len=12)` | 1068 |  |
| `etco` | `character (len=12)` | 1069 |  |
| `sy` | `character (len=12)` | 1070 |  |
| `abf` | `character (len=12)` | 1071 |  |
| `revapc` | `character (len=12)` | 1072 |  |
| `percc` | `character (len=12)` | 1073 |  |
| `sw` | `character (len=12)` | 1074 |  |
| `gw` | `character (len=12)` | 1075 |  |
| `gwflow` | `character (len=12)` | 1076 |  |
| `gwdeep` | `character (len=12)` | 1077 |  |
| `snow` | `character (len=12)` | 1078 |  |
| `xlat` | `character (len=12)` | 1079 |  |
| `itext` | `character (len=12)` | 1080 |  |
| `tropical` | `character (len=12)` | 1081 |  |
| `igrow1` | `character (len=12)` | 1082 |  |
| `igrow2` | `character (len=12)` | 1083 |  |
| `plant` | `character (len=12)` | 1084 |  |
| `ipet` | `character (len=12)` | 1085 |  |
| `irr` | `character (len=12)` | 1086 |  |
| `irrsrc` | `character (len=12)` | 1087 |  |
| `tdrain` | `character (len=12)` | 1088 |  |
| `uslek` | `character (len=12)` | 1089 |  |
| `uslec` | `character (len=12)` | 1090 |  |
| `uslep` | `character (len=12)` | 1091 |  |
| `uslels` | `character (len=12)` | 1092 |  |

### calibration3_header

- **Defined in source**: `hydrograph_module.f90:1096`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 1097 |  |
| `chgtyp` | `character (len=12)` | 1098 |  |
| `val` | `character (len=12)` | 1099 |  |
| `conds` | `character (len=12)` | 1100 |  |
| `lyr1` | `character (len=12)` | 1101 |  |
| `lyr2` | `character (len=12)` | 1102 |  |
| `year1` | `character (len=12)` | 1103 |  |
| `year2` | `character (len=12)` | 1104 |  |
| `day1` | `character (len=12)` | 1105 |  |
| `day2` | `character (len=12)` | 1106 |  |
| `objtot` | `character (len=12)` | 1107 |  |

### output_checker_header

- **Defined in source**: `hydrograph_module.f90:1111`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sname` | `character (len=16)` | 1112 |  |
| `hydgrp` | `character (len=16)` | 1113 |  |
| `zmx` | `character (len=12)` | 1114 |  |
| `usle_k` | `character (len=12)` | 1115 |  |
| `sumfc` | `character (len=12)` | 1116 |  |
| `sumul` | `character (len=12)` | 1117 |  |
| `usle_p` | `character (len=12)` | 1118 |  |
| `usle_ls` | `character (len=12)` | 1119 |  |
| `esco` | `character (len=12)` | 1120 |  |
| `epco` | `character (len=12)` | 1121 |  |
| `cn3_swf` | `character (len=12)` | 1122 |  |
| `perco` | `character (len=12)` | 1123 |  |
| `latq_co` | `character (len=12)` | 1124 |  |
| `tiledrain` | `character (len=12)` | 1125 |  |

### output_checker_unit

- **Defined in source**: `hydrograph_module.f90:1129`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sname` | `character (len=16)` | 1130 |  |
| `hydgrp` | `character (len=16)` | 1131 |  |
| `zmx` | `character (len=12)` | 1132 |  |
| `usle_k` | `character (len=12)` | 1133 |  |
| `sumfc` | `character (len=12)` | 1134 |  |
| `sumul` | `character (len=12)` | 1135 |  |
| `usle_p` | `character (len=12)` | 1136 |  |
| `usle_ls` | `character (len=12)` | 1137 |  |
| `esco` | `character (len=12)` | 1138 |  |
| `epco` | `character (len=12)` | 1139 |  |
| `cn3_swf` | `character (len=12)` | 1140 |  |
| `perco` | `character (len=12)` | 1141 |  |
| `latq_co` | `character (len=12)` | 1142 |  |
| `tiledrain` | `character (len=16)` | 1143 |  |

### hru_swift_header_base

- **Defined in source**: `hydrograph_module.f90:1147`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sed` | `character (len=16)` | 1148 | metric tons \|sediment |
| `orgn` | `character (len=16)` | 1149 | kg N \|organic N |
| `sedp` | `character (len=16)` | 1150 | kg P \|organic P |
| `no3` | `character (len=16)` | 1151 | kg N \|NO3-N |
| `solp` | `character (len=16)` | 1152 | kg P \|mineral (soluble P) kg \|chlorophyll-a |
| `nh3` | `character (len=16)` | 1154 | kg N \|NH3 |
| `no2` | `character (len=16)` | 1155 | kg N \|NO2 |

### hru_swift_header_baseunit

- **Defined in source**: `hydrograph_module.f90:1158`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `unitsed` | `character (len=16)` | 1160 | metric tons \|sediment |
| `unitorgn` | `character (len=16)` | 1161 | kg N \|organic N |
| `unitsedp` | `character (len=16)` | 1162 | kg P \|organic P |
| `unitno3` | `character (len=16)` | 1163 | kg N \|NO3-N |
| `unitsolp` | `character (len=16)` | 1164 | kg P \|mineral (soluble P) kg \|chlorophyll-a |
| `unitnh3` | `character (len=16)` | 1166 | kg N \|NH3 |
| `unitno2` | `character (len=16)` | 1167 | kg N \|NO2 |

### hru_swift_header_base2

- **Defined in source**: `hydrograph_module.f90:1170`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `character (len=17)` | 1171 | ha-m \|volume of water |
| `base` | `hru_swift_header_base` | 1172 |  |

### hru_swift_header_baseunit2

- **Defined in source**: `hydrograph_module.f90:1175`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `unitflo` | `character (len=16)` | 1176 | m^3 \|volume of water |
| `base` | `hru_swift_header_baseunit` | 1177 |  |

### hru_swift_header

- **Defined in source**: `hydrograph_module.f90:1180`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hd_type` | `character(len=17)` | 1181 |  |
| `exco` | `hru_swift_header_base` | 1182 |  |
| `exco_unit` | `hru_swift_header_baseunit` | 1183 |  |
| `dr` | `hru_swift_header_base2` | 1184 |  |
| `dr_unit` | `hru_swift_header_baseunit2` | 1185 |  |

### shade_factor_data

- **Defined in source**: `hydrograph_module.f90:1189`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `jday` | `integer` | 1190 | none \|day of the year |
| `lsu` | `integer` | 1191 | none \|landscape unit |
| `value` | `real` | 1192 | none \|shade factor value |

## Variables Defined
### mhyd

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:8`
- **Source note**: none          |max number of hydrographs

### mcmd

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:9`
- **Source note**: |

### inum2

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:10`
- **Source note**: none          |inflow hydrograph storage location number

### jrch

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:11`
- **Source note**: none          |reach number

### jrchq

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:12`
- **Source note**: |

### mrte

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:13`
- **Source note**: |

### ihout

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:14`
- **Source note**: none          |outflow hydrograph storage location number

### iwst

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:15`
- **Source note**: |

### isdch

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:16`
- **Source note**: |

### icmd

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:17`
- **Source note**: |

### ich

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:18`
- **Source note**: none          |object number

### mobj_out

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:19`
- **Source note**: none          |end of loop

### isd_chsur

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:20`
- **Source note**: |

### rcv_sum

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:21`
- **Source note**: |

### dfn_sum

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:22`
- **Source note**: |

### elem_cnt

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:23`
- **Source note**: |

### defunit_num

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:24`
- **Source note**: |

### ru_seq

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:25`
- **Source note**: |

### hyd_km2

- **Type**: `real, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:26`
- **Source note**: |

### ob_order

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `hydrograph_module.f90:27`
- **Source note**: |

### rchhr

- **Type**: `real, dimension(:,:,:), allocatable`
- **Defined in source**: `hydrograph_module.f90:28`
- **Source note**: |

### wyld_rto

- **Type**: `real, allocatable`
- **Defined in source**: `hydrograph_module.f90:29`
- **Source note**: mm=m3/(10*ha) |output runoff/precip ratio

### hd

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:63`

### rec_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:64`

### rec_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:65`

### rec_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:66`

### rec_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:67`

### srec_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:68`

### srec_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:69`

### srec_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:70`

### srec_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:71`

### ru_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:72`

### ru_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:73`

### ru_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:74`

### ru_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:75`

### brec_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:76`

### brec_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:76`

### brec_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:76`

### brec_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:76`

### bru_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:77`

### bru_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:77`

### bru_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:77`

### bru_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:77`

### binhyd_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:78`

### hz

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:79`

### dr1

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:80`

### hcnst

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:81`

### hhr

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:82`

### ht1

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### ht2

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### ht3

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### ht4

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### ht5

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### delrto

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:83`

### fp_dep

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:84`

### ch_dep

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:84`

### bank_ero

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:84`

### bed_ero

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:84`

### ch_trans

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:84`

### hdsep1

- **Type**: `hyd_sep`
- **Defined in source**: `hydrograph_module.f90:87`

### hdsep2

- **Type**: `hyd_sep`
- **Defined in source**: `hydrograph_module.f90:87`

### ch_stor_hdsep

- **Type**: `hyd_sep`
- **Defined in source**: `hydrograph_module.f90:88`

### hyd_sep_array

- **Type**: `real, dimension(:,:),allocatable`
- **Defined in source**: `hydrograph_module.f90:89`

### om_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `hydrograph_module.f90:91`

### aqu

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:93`

### res

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:94`

### wet

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:95`

### res_om_init

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:96`

### wet_om_init

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:97`

### wet_seep_day

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:98`
- **Source note**: Jaehak 2022 wetland seepage volume

### resz

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:99`

### wbody

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:100`
- **Source note**: used for reservoir and wetlands

### om_init_water

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:102`

### ch_om_water_init

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:103`

### fp_om_water_init

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:104`

### ch_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:105`
- **Source note**: channel storage - max bankfull

### fp_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:106`
- **Source note**: flood plain storage above wetland emergency

### tot_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:107`
- **Source note**: total - channel + flood plain storage

### wet_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:108`
- **Source note**: wetland storage in flood plain

### ch_stor_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:109`

### ch_stor_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:110`

### ch_stor_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:111`

### chaz

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:112`

### res_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:114`

### res_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:115`

### res_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:116`

### res_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:117`

### res_trap

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:118`

### bres_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:119`

### bres_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:120`

### bres_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:121`

### bres_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:122`

### res_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:123`

### res_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:124`

### res_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:125`

### res_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:126`

### bres

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:127`

### bres_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:128`

### bres_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:129`

### bres_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:130`

### bres_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:131`

### resmz

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:132`

### wet_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:134`

### wet_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:135`

### wet_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:136`

### wet_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:137`

### bwet_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:138`

### bwet_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:139`

### bwet_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:140`

### bwet_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:141`

### wet_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:142`

### wet_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:143`

### wet_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:144`

### wet_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:145`

### bwet_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:146`

### bwet_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:147`

### bwet_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:148`

### bwet_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:149`

### ch_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:151`

### ch_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:152`

### ch_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:153`

### ch_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:154`

### bch_stor_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:155`

### bch_stor_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:156`

### bch_stor_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:157`

### bch_stor_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:158`

### bch_in_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:159`

### bch_in_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:160`

### bch_in_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:161`

### bch_in_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:162`

### ch_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:163`

### ch_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:164`

### ch_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:165`

### ch_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:166`

### bch_out_d

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:167`

### bch_out_m

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:168`

### bch_out_y

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:169`

### bch_out_a

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:170`

### chomz

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:171`

### wal_omd

- **Type**: `water_allocation_object`
- **Defined in source**: `hydrograph_module.f90:190`

### wal_omm

- **Type**: `water_allocation_object`
- **Defined in source**: `hydrograph_module.f90:191`

### wal_omy

- **Type**: `water_allocation_object`
- **Defined in source**: `hydrograph_module.f90:192`

### wal_oma

- **Type**: `water_allocation_object`
- **Defined in source**: `hydrograph_module.f90:193`

### wdraw_om

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:196`

### wdraw_om_tot

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:198`

### outflo_om

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:200`

### wtp_om_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:203`

### wtp_om_out

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:204`

### wtp_om_treat

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:206`

### wal_tr_omd

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:209`

### wal_tr_omm

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:210`

### wal_tr_omy

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:211`

### wal_tr_oma

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:212`

### wal_use_omd

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:215`

### wal_use_omm

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:216`

### wal_use_omy

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:217`

### wal_use_oma

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:218`

### wuse_om_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:221`

### wuse_om_out

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:222`

### wuse_om_efflu

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:224`

### osrc_om

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:227`

### orcv_om

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:230`

### canal_om_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:233`

### canal_om_out

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:234`

### wtow_om_stor

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:237`

### wtow_om_out

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:238`

### ob_out

- **Type**: `object_output`
- **Defined in source**: `hydrograph_module.f90:250`

### ch_fp_wb

- **Type**: `channel_floodplain_water_balance`
- **Defined in source**: `hydrograph_module.f90:266`

### ts

- **Type**: `timestep`
- **Defined in source**: `hydrograph_module.f90:271`

### fdc_npts

- **Type**: `integer`
- **Defined in source**: `hydrograph_module.f90:288`

### fdc_p

- **Type**: `real, dimension (27)`
- **Defined in source**: `hydrograph_module.f90:289`
- **Source note**: percent        |output percent on the fdc (input)

### fdc_days

- **Type**: `integer, dimension (27)`
- **Defined in source**: `hydrograph_module.f90:290`

### fdc_n

- **Type**: `real, dimension (27)`
- **Defined in source**: `hydrograph_module.f90:291`
- **Source note**: |flow on the fdc at given percents

### fdc_norm_mean

- **Type**: `real, dimension (27)`
- **Defined in source**: `hydrograph_module.f90:292`
- **Source note**: |normalized flow on the fdc at given percents

### ob

- **Type**: `object_connectivity`
- **Defined in source**: `hydrograph_module.f90:404`

### irrig

- **Type**: `irrigation_water_transfer`
- **Defined in source**: `hydrograph_module.f90:418`
- **Source note**: dimension by hru

### recall

- **Type**: `recall_hydrograph_inputs`
- **Defined in source**: `hydrograph_module.f90:428`

### sp_ob

- **Type**: `spatial_objects`
- **Defined in source**: `hydrograph_module.f90:451`
- **Source note**: total number of the object

### sp_ob1

- **Type**: `spatial_objects`
- **Defined in source**: `hydrograph_module.f90:452`
- **Source note**: first sequential number of the object

### hd_tot

- **Type**: `object_total_hydrographs`
- **Defined in source**: `hydrograph_module.f90:472`

### ru_def

- **Type**: `routing_unit_data`
- **Defined in source**: `hydrograph_module.f90:479`

### ru_elem

- **Type**: `routing_unit_elements`
- **Defined in source**: `hydrograph_module.f90:490`

### ielem_ru

- **Type**: `integer, dimension(:), allocatable`
- **Defined in source**: `hydrograph_module.f90:492`
- **Source note**: sequential counter for ru the hru is in

### ch_sur

- **Type**: `channel_surface_elements`
- **Defined in source**: `hydrograph_module.f90:508`

### aqu_cha

- **Type**: `geomorphic_baseflow_channel_data`
- **Defined in source**: `hydrograph_module.f90:518`
- **Source note**: unsorted

### aq_ch

- **Type**: `channel_aquifer_elements`
- **Defined in source**: `hydrograph_module.f90:529`
- **Source note**: sorted by drainage area (smallest first)

### dr

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:532`
- **Source note**: delivery ratio for objects- chan, res, lu

### exco

- **Type**: `hyd_output`
- **Defined in source**: `hydrograph_module.f90:535`
- **Source note**: export coefficient

### hyd_hdr

- **Type**: `hyd_header`
- **Defined in source**: `hydrograph_module.f90:557`

### hyd_stor_hdr

- **Type**: `hyd_stor_header`
- **Defined in source**: `hydrograph_module.f90:579`

### hyd_in_hdr

- **Type**: `hyd_in_header`
- **Defined in source**: `hydrograph_module.f90:601`

### hyd_out_hdr

- **Type**: `hyd_out_header`
- **Defined in source**: `hydrograph_module.f90:623`

### hyd_inout_hdr

- **Type**: `hyd_inout_header`
- **Defined in source**: `hydrograph_module.f90:649`

### wtmp_hdr

- **Type**: `wtmp_out_header`
- **Defined in source**: `hydrograph_module.f90:654`

### sd_hyd_hdr

- **Type**: `sed_hyd_header`
- **Defined in source**: `hydrograph_module.f90:682`

### sd_hyd_hdr_units

- **Type**: `sd_hyd_header_units`
- **Defined in source**: `hydrograph_module.f90:710`

### sol_hdr

- **Type**: `sol_header`
- **Defined in source**: `hydrograph_module.f90:724`

### plt_hdr

- **Type**: `plant_header`
- **Defined in source**: `hydrograph_module.f90:741`

### fp_hdr

- **Type**: `flood_plain_header`
- **Defined in source**: `hydrograph_module.f90:758`

### ch_wbod_hdr

- **Type**: `ch_watbod_header`
- **Defined in source**: `hydrograph_module.f90:773`

### ch_wbod_hdr_units

- **Type**: `ch_watbod_header_units`
- **Defined in source**: `hydrograph_module.f90:788`

### ch_wbod_inouthdr

- **Type**: `ch_watbod_inoutheader`
- **Defined in source**: `hydrograph_module.f90:799`

### ch_wbod_inouthdr_units

- **Type**: `ch_watbod_inoutheader_units`
- **Defined in source**: `hydrograph_module.f90:810`

### hyd_hdr_units1

- **Type**: `hyd_header_units1`
- **Defined in source**: `hydrograph_module.f90:835`

### hyd_hdr_units3

- **Type**: `hyd_header_units3`
- **Defined in source**: `hydrograph_module.f90:860`

### hydinout_hdr_units1

- **Type**: `hydinout_header_units1`
- **Defined in source**: `hydrograph_module.f90:886`

### wtmp_units

- **Type**: `wtmp_header_units`
- **Defined in source**: `hydrograph_module.f90:891`

### hyd_hdr_units

- **Type**: `hyd_header_units`
- **Defined in source**: `hydrograph_module.f90:919`

### hyd_hdr_units2

- **Type**: `hyd_header_units2`
- **Defined in source**: `hydrograph_module.f90:951`

### hyd_hdr_time

- **Type**: `hyd_header_time`
- **Defined in source**: `hydrograph_module.f90:962`

### rec_hdr_time

- **Type**: `rec_header_time`
- **Defined in source**: `hydrograph_module.f90:972`

### hyd_hdr_obj

- **Type**: `hyd_header_obj`
- **Defined in source**: `hydrograph_module.f90:980`

### fdc_hdr

- **Type**: `output_flow_duration_header`
- **Defined in source**: `hydrograph_module.f90:1018`

### calb_hdr

- **Type**: `calibration_header`
- **Defined in source**: `hydrograph_module.f90:1058`

### calb2_hdr

- **Type**: `calibration2_header`
- **Defined in source**: `hydrograph_module.f90:1094`

### calb3_hdr

- **Type**: `calibration3_header`
- **Defined in source**: `hydrograph_module.f90:1109`

### chk_hdr

- **Type**: `output_checker_header`
- **Defined in source**: `hydrograph_module.f90:1127`

### chk_unit

- **Type**: `output_checker_unit`
- **Defined in source**: `hydrograph_module.f90:1145`

### hru_swift_hdr

- **Type**: `hru_swift_header`
- **Defined in source**: `hydrograph_module.f90:1187`

### shf_db

- **Type**: `shade_factor_data`
- **Defined in source**: `hydrograph_module.f90:1194`

## Subroutines Defined
### hyd_convert_conc_to_mass

### hyd_min

### res_convert_mass

### hyd_convert_mass_to_conc

## Functions Defined
### hydout_add

### hydout_subtract

### hydout_mult

### hydout_add_const

### hydout_mult_const

### hydout_div_const

### hydout_div_conv

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

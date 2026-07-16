---
type: module
tags:
  - swat/module
  - swat/to-read
file: constituent_mass_module.f90
note_file: constituent_mass_module.f90
module_name: constituent_mass_module
defines_types:
  - constituents
  - exco_pesticide
  - dr_pesticide
  - exco_pathogens
  - dr_pathogens
  - exco_heavy_metals
  - dr_heavy_metals
  - exco_salts
  - dr_salts
  - salt_solids_soil
  - constituent_mass
  - soil_constituent_mass
  - plant_constituent_mass
  - all_constituent_hydrograph
  - gw_load_hydrograph
  - recall_salt_inputs
  - recall_cs_inputs
  - recall_pesticide_inputs
  - cs_soil_init_concentrations
  - salt_aqu_init_concentrations
  - cs_aqu_init_concentrations
  - salt_cha_init_concentrations
  - cs_cha_init_concentrations
  - cs_water_init_concentrations
  - cs_irrigation_concentrations
  - output_rusaltb_header
  - output_rucsb_header
  - constituents_header_in
  - constituents_header_out
  - sol_sor
defines_vars:
  - pest_init_name
  - path_init_name
  - hmet_init_name
  - salt_init_name
  - cs_init_name
  - cs_db
  - exco_pest
  - dr_pest
  - exco_path
  - dr_path
  - exco_hmet
  - dr_hmet
  - exco_salt
  - dr_salt
  - sol_salt_solid
  - cs_irr
  - cs_soil
  - cs_pl
  - cs_aqu
  - cs_aqu_init
  - ch_water
  - ch_benthic
  - ch_water_init
  - ch_benthic_init
  - wtp_cs_stor
  - wtp_cs_treat
  - wuse_cs_stor
  - wuse_cs_efflu
  - osrc_cs
  - canal_cs_stor
  - wtow_cs_stor
  - wdraw_cs
  - wdraw_cs_tot
  - outflo_cs
  - res_water
  - res_benthic
  - wet_water
  - hcs1
  - hcs2
  - hcs3
  - hin_csz
  - obcs
  - obcs_alloc
  - aq_chcs
  - hcsz
  - rusaltb_d
  - rusaltb_m
  - rusaltb_y
  - rusaltb_a
  - rucsb_d
  - rucsb_m
  - rucsb_y
  - rucsb_a
  - rec_salt
  - rec_cs
  - recsaltb_d
  - recsaltb_m
  - recsaltb_y
  - recsaltb_a
  - recoutsaltb_d
  - recoutsaltb_m
  - recoutsaltb_y
  - recoutsaltb_a
  - reccsb_d
  - reccsb_m
  - reccsb_y
  - reccsb_a
  - recoutcsb_d
  - recoutcsb_m
  - recoutcsb_y
  - recoutcsb_a
  - rec_pest
  - pest_soil_ini
  - path_soil_ini
  - hmet_soil_ini
  - salt_soil_ini
  - cs_soil_ini
  - salt_aqu_ini
  - cs_aqu_ini
  - salt_cha_ini
  - cs_cha_ini
  - pest_water_ini
  - path_water_ini
  - hmet_water_ini
  - salt_water_irr
  - cs_water_irr
  - cs_obs_file
  - cs_str_nobs
  - cs_str_obs
  - rusaltb_hdr
  - rucsb_hdr
  - csin_hyd_hdr
  - csout_hyd_hdr
  - cs_pest_solsor
  - cs_path_solsor
  - cs_hmet_solsor
  - cs_salt_solsor
defines_subroutines:
  - hydcsout_conc_mass
defines_functions:
  - hydcsout_add
  - hydcsout_mult_const
defines_procedures:
  - hydcsout_conc_mass
  - hydcsout_add
  - hydcsout_mult_const
purpose: ""
---

# constituent_mass_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### constituents

- **Defined in source**: `constituent_mass_module.f90:12`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num_tot` | `integer` | 13 | number of total constituents simulated |
| `num_pests` | `integer` | 14 | number of pesticides simulated |
| `pests` | `character (len=16), dimension(:), allocatable` | 15 | name of the pesticides- points to pesticide database need to crosswalk pests to get pest_num for database - use sequential for object |
| `pest_num` | `integer, dimension(:), allocatable` | 17 | number of the pesticides- points to pesticide database |
| `num_paths` | `integer` | 18 | number of pathogens simulated |
| `paths` | `character (len=16), dimension(:), allocatable` | 19 | name of the pathogens- points to pathogens database |
| `path_num` | `integer, dimension(:), allocatable` | 20 | number of the pathogens- points to pathogens database |
| `num_metals` | `integer` | 21 | number of heavy metals simulated |
| `metals` | `character (len=16), dimension(:), allocatable` | 22 | name of the heavy metals- points to heavy metals database |
| `metals_num` | `integer, dimension(:), allocatable` | 23 | number of the heavy metals- points to heavy metals database |
| `num_salts` | `integer` | 24 | number of salt ions simulated |
| `salts` | `character (len=16), dimension(:), allocatable` | 25 | name of the salts - points to salts database |
| `salts_num` | `integer, dimension(:), allocatable` | 26 | number of the salts - points to salts database |
| `num_cs` | `integer` | 27 | number of other constituents simulated |
| `cs` | `character (len=16), dimension(:), allocatable` | 28 | name of the constituents - points to cs database |
| `cs_num` | `integer, dimension(:), allocatable` | 29 | number of the constituents - points to salts database |

### exco_pesticide

- **Defined in source**: `constituent_mass_module.f90:33`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `real, dimension (:), allocatable` | 34 | pesticide hydrographs |

### dr_pesticide

- **Defined in source**: `constituent_mass_module.f90:38`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `real, dimension (:), allocatable` | 39 | pesticide delivery |

### exco_pathogens

- **Defined in source**: `constituent_mass_module.f90:43`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `path` | `real, dimension (:), allocatable` | 44 | pesticide hydrographs |

### dr_pathogens

- **Defined in source**: `constituent_mass_module.f90:48`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `path` | `real, dimension (:), allocatable` | 49 | pathogen delivery |

### exco_heavy_metals

- **Defined in source**: `constituent_mass_module.f90:53`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hmet` | `real, dimension (:), allocatable` | 54 | heavy metals hydrographs |

### dr_heavy_metals

- **Defined in source**: `constituent_mass_module.f90:58`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hmet` | `real, dimension (:), allocatable` | 59 | heavy metals delivery |

### exco_salts

- **Defined in source**: `constituent_mass_module.f90:63`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `real, dimension (:), allocatable` | 64 | salts hydrographs |

### dr_salts

- **Defined in source**: `constituent_mass_module.f90:68`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `salt` | `real, dimension (:), allocatable` | 69 | salts delivery |

### salt_solids_soil

- **Defined in source**: `constituent_mass_module.f90:73`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `solid` | `real, dimension (:), allocatable` | 74 | salt solid by soil layer |

### constituent_mass

- **Defined in source**: `constituent_mass_module.f90:79`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pest` | `real, dimension (:), allocatable` | 80 | pesticide (kg/ha) |
| `path` | `real, dimension (:), allocatable` | 81 | pathogen (cfu) |
| `hmet` | `real, dimension (:), allocatable` | 82 | heavy metal (kg/ha) |
| `salt` | `real, dimension (:), allocatable` | 83 | salt ion mass (kg/ha) |
| `salt_min` | `real, dimension (:), allocatable` | 84 | salt mineral hydrographs |
| `saltc` | `real, dimension (:), allocatable` | 85 | salt ion concentrations (mg/L) |
| `cs` | `real, dimension (:), allocatable` | 86 | constituent mass (kg/ha) |
| `csc` | `real, dimension (:), allocatable` | 87 | constituent concentration (mg/L) |
| `cs_sorb` | `real, dimension (:), allocatable` | 88 | sorbed constituent mass (kg/ha) |
| `csc_sorb` | `real, dimension (:), allocatable` | 89 | sorbed constituent concentration (mg/kg) |

### soil_constituent_mass

- **Defined in source**: `constituent_mass_module.f90:96`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ly` | `constituent_mass` | 97 |  |

### plant_constituent_mass

- **Defined in source**: `constituent_mass_module.f90:102`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pl_in` | `constituent_mass` | 103 | constituent in plant |
| `pl_on` | `constituent_mass` | 104 | constituent on plant |
| `pl_up` | `constituent_mass` | 105 | constituent uptake by plant |

### all_constituent_hydrograph

- **Defined in source**: `constituent_mass_module.f90:159`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hd` | `constituent_mass` | 160 |  |
| `hin` | `constituent_mass` | 161 |  |
| `hin_sur` | `constituent_mass` | 162 |  |
| `hin_lat` | `constituent_mass` | 163 |  |
| `hin_til` | `constituent_mass` | 164 |  |
| `hin_aqu` | `constituent_mass` | 165 |  |
| `hcsin_d` | `constituent_mass` | 166 |  |
| `hcsin_m` | `constituent_mass` | 167 |  |
| `hcsin_y` | `constituent_mass` | 168 |  |
| `hcsin_a` | `constituent_mass` | 169 |  |
| `hcsout_m` | `constituent_mass` | 170 |  |
| `hcsout_y` | `constituent_mass` | 171 |  |
| `hcsout_a` | `constituent_mass` | 172 |  |

### gw_load_hydrograph

- **Defined in source**: `constituent_mass_module.f90:180`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hd` | `constituent_mass` | 181 |  |

### recall_salt_inputs

- **Defined in source**: `constituent_mass_module.f90:201`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 202 |  |
| `typ` | `integer` | 203 | recall type - 1=day, 2=mon, 3=year |
| `filename` | `character(len=30)` | 204 | filename |
| `start_yr` | `integer` | 205 | start year of point source file |
| `end_yr` | `integer` | 206 | end year of point source file |
| `pts_type` | `integer` | 207 | 1 = within watershed; 2 = from outside watershed |
| `hd_salt` | `constituent_mass` | 208 |  |

### recall_cs_inputs

- **Defined in source**: `constituent_mass_module.f90:213`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 214 |  |
| `typ` | `integer` | 215 | recall type - 1=day, 2=mon, 3=year |
| `filename` | `character(len=30)` | 216 | filename |
| `start_yr` | `integer` | 217 | start year of point source file |
| `end_yr` | `integer` | 218 | end year of point source file |
| `pts_type` | `integer` | 219 | 1 = within watershed; 2 = from outside watershed |
| `hd_cs` | `constituent_mass` | 220 |  |

### recall_pesticide_inputs

- **Defined in source**: `constituent_mass_module.f90:249`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 250 |  |
| `num` | `integer` | 251 | number of elements |
| `typ` | `integer` | 252 | recall type - 1=day, 2=mon, 3=year |
| `filename` | `character(len=13)` | 253 | filename hyd_output units are in cms and mg/L |
| `hd_pest` | `constituent_mass` | 255 |  |

### cs_soil_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:260`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 261 | name of the constituent - points to constituent database |
| `soil` | `real, dimension (:), allocatable` | 262 | ppm \|amount of constituent in soil at start of simulation |
| `plt` | `real, dimension (:), allocatable` | 263 | ppm or #cfu/m^2 \|amount of constituent on plant at start of simulation |

### salt_aqu_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:273`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 274 | name of the constituent - points to constituent database |
| `conc` | `real, dimension (:), allocatable` | 275 | g/m3 \|salt ion concentration at start of simulation |
| `frac` | `real, dimension (:), allocatable` | 276 | fractions \|salt mineral fractions at start of simulation |

### cs_aqu_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:281`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 282 | name of the constituent - points to constituent database |
| `aqu` | `real, dimension (:), allocatable` | 283 | ppm \|concentration, sorbed mass at start of simulation |

### salt_cha_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:288`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 289 | name of the constituent - points to salt ion database |
| `conc` | `real, dimension (:), allocatable` | 290 | g/m3 \|salt ion concentration at start of simulation |

### cs_cha_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:295`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 296 | name of the constituent - points to salt ion database |
| `conc` | `real, dimension (:), allocatable` | 297 | g/m3 \|constituent concentration at start of simulation |

### cs_water_init_concentrations

- **Defined in source**: `constituent_mass_module.f90:302`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 303 | name of the constituent - points to constituent database |
| `water` | `real, dimension (:), allocatable` | 304 | ppm,fracitons \|amount of constituents (dissolved, salt minerals) in aquifer at start of simulation |
| `benthic` | `real, dimension (:), allocatable` | 305 | ppm or #cfu/m^2 \|amount of constituent in benthic at start of simulation |
| `reservoir` | `real, dimension (:), allocatable` | 306 | ppm \|amount of constituent in reservoir water at start of simulation |

### cs_irrigation_concentrations

- **Defined in source**: `constituent_mass_module.f90:313`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 314 | name of the constituent - points to constituent database |
| `water` | `real, dimension (:), allocatable` | 315 | ppm \|amount of constituent in water at start of simulation |

### output_rusaltb_header

- **Defined in source**: `constituent_mass_module.f90:328`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character(len=6)` | 329 |  |
| `mo` | `character(len=6)` | 330 |  |
| `day_mo` | `character(len=6)` | 331 |  |
| `yrc` | `character(len=6)` | 332 |  |
| `isd` | `character(len=8)` | 333 |  |
| `id` | `character(len=12)` | 334 | total salt out (surq + latq + tile) --> see hru_hyds subroutine |
| `so4tot` | `character(len=15)` | 336 |  |
| `castot` | `character(len=15)` | 337 |  |
| `mgstot` | `character(len=15)` | 338 |  |
| `nastot` | `character(len=15)` | 339 |  |
| `kstot` | `character(len=15)` | 340 |  |
| `clstot` | `character(len=15)` | 341 |  |
| `co3stot` | `character(len=15)` | 342 |  |
| `hco3stot` | `character(len=15)` | 343 | percolation |
| `so4pc` | `character(len=15)` | 345 |  |
| `capc` | `character(len=15)` | 346 |  |
| `mgpc` | `character(len=15)` | 347 |  |
| `napc` | `character(len=15)` | 348 |  |
| `kpc` | `character(len=15)` | 349 |  |
| `clpc` | `character(len=15)` | 350 |  |
| `co3pc` | `character(len=15)` | 351 |  |
| `hco3pc` | `character(len=15)` | 352 | surface runoff |
| `so4sq` | `character(len=15)` | 354 |  |
| `casq` | `character(len=15)` | 355 |  |
| `mgsq` | `character(len=15)` | 356 |  |
| `nasq` | `character(len=15)` | 357 |  |
| `ksq` | `character(len=15)` | 358 |  |
| `clsq` | `character(len=15)` | 359 |  |
| `co3sq` | `character(len=15)` | 360 |  |
| `hco3sq` | `character(len=15)` | 361 | lateral flow |
| `so4lq` | `character(len=15)` | 363 |  |
| `calq` | `character(len=15)` | 364 |  |
| `mglq` | `character(len=15)` | 365 |  |
| `nalq` | `character(len=15)` | 366 |  |
| `klq` | `character(len=15)` | 367 |  |
| `cllq` | `character(len=15)` | 368 |  |
| `co3lq` | `character(len=15)` | 369 |  |
| `hco3lq` | `character(len=15)` | 370 | tile flow |
| `so4tq` | `character(len=15)` | 372 |  |
| `catq` | `character(len=15)` | 373 |  |
| `mgtq` | `character(len=15)` | 374 |  |
| `natq` | `character(len=15)` | 375 |  |
| `ktq` | `character(len=15)` | 376 |  |
| `cltq` | `character(len=15)` | 377 |  |
| `co3tq` | `character(len=15)` | 378 |  |
| `hco3tq` | `character(len=15)` | 379 | wetland seepage to soil profile |
| `so4ws` | `character(len=15)` | 381 |  |
| `caws` | `character(len=15)` | 382 |  |
| `mgws` | `character(len=15)` | 383 |  |
| `naws` | `character(len=15)` | 384 |  |
| `kws` | `character(len=15)` | 385 |  |
| `clws` | `character(len=15)` | 386 |  |
| `co3ws` | `character(len=15)` | 387 |  |
| `hco3ws` | `character(len=15)` | 388 | irrigation (surface water) |
| `so4is` | `character(len=15)` | 390 |  |
| `cais` | `character(len=15)` | 391 |  |
| `mgis` | `character(len=15)` | 392 |  |
| `nais` | `character(len=15)` | 393 |  |
| `kis` | `character(len=15)` | 394 |  |
| `clis` | `character(len=15)` | 395 |  |
| `co3is` | `character(len=15)` | 396 |  |
| `hco3is` | `character(len=15)` | 397 | irrigation (groundwater) |
| `so4ig` | `character(len=15)` | 399 |  |
| `caig` | `character(len=15)` | 400 |  |
| `mgig` | `character(len=15)` | 401 |  |
| `naig` | `character(len=15)` | 402 |  |
| `kig` | `character(len=15)` | 403 |  |
| `clig` | `character(len=15)` | 404 |  |
| `co3ig` | `character(len=15)` | 405 |  |
| `hco3ig` | `character(len=15)` | 406 | irrigation (outside watershed) |
| `so4io` | `character(len=15)` | 408 |  |
| `caio` | `character(len=15)` | 409 |  |
| `mgio` | `character(len=15)` | 410 |  |
| `naio` | `character(len=15)` | 411 |  |
| `kio` | `character(len=15)` | 412 |  |
| `clio` | `character(len=15)` | 413 |  |
| `co3io` | `character(len=15)` | 414 |  |
| `hco3io` | `character(len=15)` | 415 | rainfall (wet deposition) |
| `so4rn` | `character(len=15)` | 417 |  |
| `carn` | `character(len=15)` | 418 |  |
| `mgrn` | `character(len=15)` | 419 |  |
| `narn` | `character(len=15)` | 420 |  |
| `krn` | `character(len=15)` | 421 |  |
| `clrn` | `character(len=15)` | 422 |  |
| `co3rn` | `character(len=15)` | 423 |  |
| `hco3rn` | `character(len=15)` | 424 | dry deposition |
| `so4dd` | `character(len=15)` | 426 |  |
| `cadd` | `character(len=15)` | 427 |  |
| `mgdd` | `character(len=15)` | 428 |  |
| `nadd` | `character(len=15)` | 429 |  |
| `kdd` | `character(len=15)` | 430 |  |
| `cldd` | `character(len=15)` | 431 |  |
| `co3dd` | `character(len=15)` | 432 |  |
| `hco3dd` | `character(len=15)` | 433 | road salt application |
| `so4rd` | `character(len=15)` | 435 |  |
| `card` | `character(len=15)` | 436 |  |
| `mgrd` | `character(len=15)` | 437 |  |
| `nard` | `character(len=15)` | 438 |  |
| `krd` | `character(len=15)` | 439 |  |
| `clrd` | `character(len=15)` | 440 |  |
| `co3rd` | `character(len=15)` | 441 |  |
| `hco3rd` | `character(len=15)` | 442 | fertilizer application |
| `so4fz` | `character(len=15)` | 444 |  |
| `cafz` | `character(len=15)` | 445 |  |
| `mgfz` | `character(len=15)` | 446 |  |
| `nafz` | `character(len=15)` | 447 |  |
| `kfz` | `character(len=15)` | 448 |  |
| `clfz` | `character(len=15)` | 449 |  |
| `co3fz` | `character(len=15)` | 450 |  |
| `hco3fz` | `character(len=15)` | 451 | soil salt amendments |
| `so4am` | `character(len=15)` | 453 |  |
| `caam` | `character(len=15)` | 454 |  |
| `mgam` | `character(len=15)` | 455 |  |
| `naam` | `character(len=15)` | 456 |  |
| `kam` | `character(len=15)` | 457 |  |
| `clam` | `character(len=15)` | 458 |  |
| `co3am` | `character(len=15)` | 459 |  |
| `hco3am` | `character(len=15)` | 460 | plant salt uptake |
| `so4up` | `character(len=15)` | 462 |  |
| `caup` | `character(len=15)` | 463 |  |
| `mgup` | `character(len=15)` | 464 |  |
| `naup` | `character(len=15)` | 465 |  |
| `kup` | `character(len=15)` | 466 |  |
| `clup` | `character(len=15)` | 467 |  |
| `co3up` | `character(len=15)` | 468 |  |
| `hco3up` | `character(len=15)` | 469 | salt mineral dissolution and precipitation |
| `dssl` | `character(len=15)` | 471 |  |

### output_rucsb_header

- **Defined in source**: `constituent_mass_module.f90:476`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character(len=6)` | 477 |  |
| `mo` | `character(len=6)` | 478 |  |
| `day_mo` | `character(len=6)` | 479 |  |
| `yrc` | `character(len=6)` | 480 |  |
| `isd` | `character(len=8)` | 481 |  |
| `id` | `character(len=12)` | 482 | total cs out (surq + latq + tile) --> see hru_hyds subroutine |
| `seo4tot` | `character(len=15)` | 484 |  |
| `seo3tot` | `character(len=15)` | 485 |  |
| `borntot` | `character(len=15)` | 486 | percolation |
| `seo4pc` | `character(len=15)` | 488 |  |
| `seo3pc` | `character(len=15)` | 489 |  |
| `bornpc` | `character(len=15)` | 490 | surface runoff |
| `seo4sq` | `character(len=15)` | 492 |  |
| `seo3sq` | `character(len=15)` | 493 |  |
| `bornsq` | `character(len=15)` | 494 | lateral flow |
| `seo4lq` | `character(len=15)` | 496 |  |
| `seo3lq` | `character(len=15)` | 497 |  |
| `bornlq` | `character(len=15)` | 498 | tile flow |
| `seo4tq` | `character(len=15)` | 500 |  |
| `seo3tq` | `character(len=15)` | 501 |  |
| `borntq` | `character(len=15)` | 502 | sediment runoff |
| `seo4sd` | `character(len=15)` | 504 |  |
| `seo3sd` | `character(len=15)` | 505 |  |
| `bornsd` | `character(len=15)` | 506 | wetland seepage to soil profile |
| `seo4ws` | `character(len=15)` | 508 |  |
| `seo3ws` | `character(len=15)` | 509 |  |
| `bornws` | `character(len=15)` | 510 | irrigation (surface water) |
| `seo4is` | `character(len=15)` | 512 |  |
| `seo3is` | `character(len=15)` | 513 |  |
| `bornis` | `character(len=15)` | 514 | irrigation (groundwater) |
| `seo4ig` | `character(len=15)` | 516 |  |
| `seo3ig` | `character(len=15)` | 517 |  |
| `bornig` | `character(len=15)` | 518 | irrigation (outside watershed) |
| `seo4io` | `character(len=15)` | 520 |  |
| `seo3io` | `character(len=15)` | 521 |  |
| `bornio` | `character(len=15)` | 522 | rainfall (wet deposition) |
| `seo4rn` | `character(len=15)` | 524 |  |
| `seo3rn` | `character(len=15)` | 525 |  |
| `bornrn` | `character(len=15)` | 526 | dry deposition |
| `seo4dd` | `character(len=15)` | 528 |  |
| `seo3dd` | `character(len=15)` | 529 |  |
| `borndd` | `character(len=15)` | 530 | fertilizer |
| `seo4fz` | `character(len=15)` | 532 |  |
| `seo3fz` | `character(len=15)` | 533 |  |
| `bornfz` | `character(len=15)` | 534 | plant selenium uptake |
| `seo4up` | `character(len=15)` | 536 |  |
| `seo3up` | `character(len=15)` | 537 |  |
| `bornup` | `character(len=15)` | 538 | chemical reactions |
| `seo4rc` | `character(len=15)` | 540 |  |
| `seo3rc` | `character(len=15)` | 541 |  |
| `bornrc` | `character(len=15)` | 542 | mass transfer from sorption |
| `seo4sb` | `character(len=15)` | 544 |  |
| `seo3sb` | `character(len=15)` | 545 |  |
| `bornsb` | `character(len=15)` | 546 |  |

### constituents_header_in

- **Defined in source**: `constituent_mass_module.f90:550`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 551 |  |
| `mo` | `character (len=12)` | 552 |  |
| `day_mo` | `character (len=12)` | 553 |  |
| `yrc` | `character (len=12)` | 554 |  |
| `name` | `character (len=12)` | 555 |  |
| `otype` | `character (len=12)` | 556 |  |
| `type` | `character (len=12)` | 557 |  |
| `num` | `character (len=12)` | 558 |  |
| `obout` | `character (len=12)` | 559 |  |
| `obno_out` | `character (len=12)` | 560 |  |
| `htyp_out` | `character (len=12)` | 561 |  |
| `frac` | `character (len=12)` | 562 |  |
| `sol` | `character (len=12)` | 563 |  |
| `sor` | `character (len=12)` | 564 |  |

### constituents_header_out

- **Defined in source**: `constituent_mass_module.f90:568`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=11)` | 569 |  |
| `mo` | `character (len=12)` | 570 |  |
| `day_mo` | `character (len=12)` | 571 |  |
| `yrc` | `character (len=12)` | 572 |  |
| `name` | `character (len=12)` | 573 |  |
| `otype` | `character (len=12)` | 574 |  |
| `type` | `character (len=12)` | 575 |  |
| `num` | `character (len=12)` | 576 |  |
| `obout` | `character (len=12)` | 577 |  |
| `obno_out` | `character (len=12)` | 578 |  |
| `htyp_out` | `character (len=12)` | 579 |  |
| `frac` | `character (len=12)` | 580 |  |

### sol_sor

- **Defined in source**: `constituent_mass_module.f90:584`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `sol` | `character (len=12)` | 585 |  |
| `sor` | `character (len=12)` | 586 |  |

## Variables Defined
### pest_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:5`

### path_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:6`

### hmet_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:7`

### salt_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:8`

### cs_init_name

- **Type**: `character(len=16), dimension(:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:9`
- **Source note**: rtb cs

### cs_db

- **Type**: `constituents`
- **Defined in source**: `constituent_mass_module.f90:31`

### exco_pest

- **Type**: `exco_pesticide`
- **Defined in source**: `constituent_mass_module.f90:36`
- **Source note**: export coefficients

### dr_pest

- **Type**: `dr_pesticide`
- **Defined in source**: `constituent_mass_module.f90:41`
- **Source note**: delivery ratios

### exco_path

- **Type**: `exco_pathogens`
- **Defined in source**: `constituent_mass_module.f90:46`
- **Source note**: export coefficients

### dr_path

- **Type**: `dr_pathogens`
- **Defined in source**: `constituent_mass_module.f90:51`
- **Source note**: delivery ratios

### exco_hmet

- **Type**: `exco_heavy_metals`
- **Defined in source**: `constituent_mass_module.f90:56`
- **Source note**: export coefficients

### dr_hmet

- **Type**: `dr_heavy_metals`
- **Defined in source**: `constituent_mass_module.f90:61`
- **Source note**: delivery ratios

### exco_salt

- **Type**: `exco_salts`
- **Defined in source**: `constituent_mass_module.f90:66`
- **Source note**: export coefficients

### dr_salt

- **Type**: `dr_salts`
- **Defined in source**: `constituent_mass_module.f90:71`
- **Source note**: delivery ratios

### sol_salt_solid

- **Type**: `salt_solids_soil`
- **Defined in source**: `constituent_mass_module.f90:76`
- **Source note**: salt solid by hru

### cs_irr

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:93`

### cs_soil

- **Type**: `soil_constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:99`

### cs_pl

- **Type**: `plant_constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:108`

### cs_aqu

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:111`

### cs_aqu_init

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:112`

### ch_water

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:115`

### ch_benthic

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:116`

### ch_water_init

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:117`

### ch_benthic_init

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:118`

### wtp_cs_stor

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:121`

### wtp_cs_treat

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:123`

### wuse_cs_stor

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:126`

### wuse_cs_efflu

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:128`

### osrc_cs

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:131`

### canal_cs_stor

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:134`

### wtow_cs_stor

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:137`

### wdraw_cs

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:140`

### wdraw_cs_tot

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:142`

### outflo_cs

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:144`

### res_water

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:147`

### res_benthic

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:148`

### wet_water

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:151`

### hcs1

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:154`

### hcs2

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:154`

### hcs3

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:154`

### hin_csz

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:156`

### obcs

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:174`

### obcs_alloc

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:177`

### aq_chcs

- **Type**: `gw_load_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:183`

### hcsz

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:186`

### rusaltb_d

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:189`

### rusaltb_m

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:190`

### rusaltb_y

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:191`

### rusaltb_a

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:192`

### rucsb_d

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:195`

### rucsb_m

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:196`

### rucsb_y

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:197`

### rucsb_a

- **Type**: `all_constituent_hydrograph`
- **Defined in source**: `constituent_mass_module.f90:198`

### rec_salt

- **Type**: `recall_salt_inputs`
- **Defined in source**: `constituent_mass_module.f90:210`

### rec_cs

- **Type**: `recall_cs_inputs`
- **Defined in source**: `constituent_mass_module.f90:222`

### recsaltb_d

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:226`

### recsaltb_m

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:227`

### recsaltb_y

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:228`

### recsaltb_a

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:229`

### recoutsaltb_d

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:231`

### recoutsaltb_m

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:232`

### recoutsaltb_y

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:233`

### recoutsaltb_a

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:234`

### reccsb_d

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:238`

### reccsb_m

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:239`

### reccsb_y

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:240`

### reccsb_a

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:241`

### recoutcsb_d

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:243`

### recoutcsb_m

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:244`

### recoutcsb_y

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:245`

### recoutcsb_a

- **Type**: `constituent_mass`
- **Defined in source**: `constituent_mass_module.f90:246`

### rec_pest

- **Type**: `recall_pesticide_inputs`
- **Defined in source**: `constituent_mass_module.f90:257`

### pest_soil_ini

- **Type**: `cs_soil_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:265`

### path_soil_ini

- **Type**: `cs_soil_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:266`

### hmet_soil_ini

- **Type**: `cs_soil_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:267`

### salt_soil_ini

- **Type**: `cs_soil_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:269`

### cs_soil_ini

- **Type**: `cs_soil_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:270`
- **Source note**: rtb cs

### salt_aqu_ini

- **Type**: `salt_aqu_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:278`

### cs_aqu_ini

- **Type**: `cs_aqu_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:285`

### salt_cha_ini

- **Type**: `salt_cha_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:292`

### cs_cha_ini

- **Type**: `cs_cha_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:299`

### pest_water_ini

- **Type**: `cs_water_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:308`

### path_water_ini

- **Type**: `cs_water_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:309`

### hmet_water_ini

- **Type**: `cs_water_init_concentrations`
- **Defined in source**: `constituent_mass_module.f90:310`

### salt_water_irr

- **Type**: `cs_irrigation_concentrations`
- **Defined in source**: `constituent_mass_module.f90:317`

### cs_water_irr

- **Type**: `cs_irrigation_concentrations`
- **Defined in source**: `constituent_mass_module.f90:318`

### cs_obs_file

- **Type**: `integer`
- **Defined in source**: `constituent_mass_module.f90:322`
- **Source note**: |flag: file for channels with daily output

### cs_str_nobs

- **Type**: `integer`
- **Defined in source**: `constituent_mass_module.f90:323`
- **Source note**: |number of channels for daily output

### cs_str_obs

- **Type**: `integer, dimension (:), allocatable`
- **Defined in source**: `constituent_mass_module.f90:324`
- **Source note**: |list of channels for daily output

### rusaltb_hdr

- **Type**: `output_rusaltb_header`
- **Defined in source**: `constituent_mass_module.f90:473`

### rucsb_hdr

- **Type**: `output_rucsb_header`
- **Defined in source**: `constituent_mass_module.f90:548`

### csin_hyd_hdr

- **Type**: `constituents_header_in`
- **Defined in source**: `constituent_mass_module.f90:566`

### csout_hyd_hdr

- **Type**: `constituents_header_out`
- **Defined in source**: `constituent_mass_module.f90:582`

### cs_pest_solsor

- **Type**: `sol_sor`
- **Defined in source**: `constituent_mass_module.f90:588`

### cs_path_solsor

- **Type**: `sol_sor`
- **Defined in source**: `constituent_mass_module.f90:589`

### cs_hmet_solsor

- **Type**: `sol_sor`
- **Defined in source**: `constituent_mass_module.f90:590`

### cs_salt_solsor

- **Type**: `sol_sor`
- **Defined in source**: `constituent_mass_module.f90:591`

## Subroutines Defined
### hydcsout_conc_mass

## Functions Defined
### hydcsout_add

### hydcsout_mult_const

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/module
  - swat/to-read
file: organic_mineral_mass_module.f90
note_file: organic_mineral_mass_module.f90
module_name: organic_mineral_mass_module
defines_types:
  - organic_mass
  - organic_mixing_mass
  - clay_mass
  - sediment
  - mineral_nitrogen
  - mineral_phosphorus
  - plant_residue
  - soil_profile_mass
  - plant_community_mass
  - mineral_mass
  - organic_mineral_mass
  - animal_herds
  - fertilizer_mass
  - organic_mineral_hydrograph
  - spatial_object_hydrographs
  - recall_organic_mineral_inputs
  - routing_unit_elements_hydrographs
  - channel_surface_elements_hydrographs
defines_vars:
  - meta_frac
  - str_frac
  - lig_frac
  - orgz
  - mix_org
  - mnz
  - mix_mn
  - mpz
  - mix_mp
  - soil1
  - soil1_init
  - soil_prof_tot
  - soil_prof_root
  - soil_prof_root_frac
  - soil_prof_rsd
  - soil_prof_srsd
  - soil_prof_hact
  - soil_prof_hsta
  - soil_prof_hs
  - soil_prof_hp
  - soil_prof_microb
  - soil_prof_seq_hs
  - soil_prof_seq_hp
  - soil_prof_seq_microb
  - soil_prof_str
  - soil_prof_lig
  - soil_prof_nonlig
  - soil_prof_meta
  - soil_prof_sstr
  - soil_prof_slig
  - soil_prof_smeta
  - soil_prof_man
  - soil_prof_water
  - soil_org_z
  - soil_prof_somc
  - soil_prof_mn
  - soil_prof_mp
  - soil_mn_z
  - soil_mp_z
  - bsn_org_soil
  - bsn_org_pl
  - bsn_org_rsd
  - bsn_mn
  - bsn_mp
  - decomp
  - photo_decomp
  - transfer
  - pl_burn
  - rsd_meta
  - rsd_str
  - pl_mass
  - pl_mass_init
  - pl_yield
  - pl_mass_up
  - pl_residue
  - harv_seed
  - harv_leaf
  - harv_stem
  - harv_left
  - graz_plant
  - graz_seed
  - graz_leaf
  - graz_stem
  - leaf_drop
  - abgr_drop
  - stem_drop
  - seed_drop
  - plt_mass_z
  - fert
  - org_frt
  - manure
  - obom
  - rec_om
  - exco_om
  - dr_om
  - sub_e_hd
  - ch_sur_hd
  - o_m1
  - o_m2
  - o_m3
  - pmin_m1
  - pmin_m2
  - pmin_m3
  - nmin_m1
  - nmin_m2
  - nmin_m3
defines_subroutines: []
defines_functions:
  - nmin_add
  - nmin_mult_const
  - pmin_add
  - pmin_mult_const
  - om_add1
  - om_subtract
  - om_mult_const
  - om_divide
  - org_flux_add1
defines_procedures:
  - nmin_add
  - nmin_mult_const
  - pmin_add
  - pmin_mult_const
  - om_add1
  - om_subtract
  - om_mult_const
  - om_divide
  - org_flux_add1
purpose: ""
---

# organic_mineral_mass_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### organic_mass

- **Defined in source**: `organic_mineral_mass_module.f90:11`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `m` | `real` | 12 | kg/ha \|total object mass |
| `c` | `real` | 13 | kg/ha \|carbon mass |
| `n` | `real` | 14 | kg/ha \|organic nitrogen mass |
| `p` | `real` | 15 | kg/ha \|organic phosphorus mass |

### organic_mixing_mass

- **Defined in source**: `organic_mineral_mass_module.f90:19`
- **Source note**: |used for each layer in mgt_newtillmix

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tot` | `organic_mass` | 20 | \|total organic pool |
| `surf_rsd` | `organic_mass` | 21 | \|fresh surface residue mixed into layers |
| `rsd` | `organic_mass` | 22 | \|fresh soil residue (max 12 plants) humus pools for old mineralization model (static carbon) |
| `hact` | `organic_mass` | 24 | \|active humus for old mineralization model |
| `hsta` | `organic_mass` | 25 | \|stable humus for old mineralization model organic pools used in CENTURY model |
| `hs` | `organic_mass` | 27 | \|slow humus |
| `hp` | `organic_mass` | 28 | \|passive humus |
| `microb` | `organic_mass` | 29 | \|microbial biomass |
| `str` | `organic_mass` | 30 | \|structural litter pool |
| `lig` | `organic_mass` | 31 | \|lignin pool |
| `nonlig` | `organic_mass` | 32 | \|non lignin pool |
| `meta` | `organic_mass` | 33 | \|metabolic litter pool |
| `man` | `organic_mass` | 34 | \|manure pool |
| `water` | `organic_mass` | 35 | \|water soluble |

### clay_mass

- **Defined in source**: `organic_mineral_mass_module.f90:39`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `m` | `real` | 40 | kg or kg/ha \|total object mass |
| `nh4` | `real` | 41 | kg or kg/ha \|ammonium mass |

### sediment

- **Defined in source**: `organic_mineral_mass_module.f90:44`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `m` | `real` | 45 | kg or kg/ha \|total object mass |
| `sand` | `real` | 46 | kg or kg/ha \|sand mass |
| `silt` | `real` | 47 | kg or kg/ha \|silt mass |
| `clay` | `clay_mass` | 48 | kg or kg/ha \|clay mass |
| `gravel` | `real` | 49 | kg or kg/ha \|gravel mass |

### mineral_nitrogen

- **Defined in source**: `organic_mineral_mass_module.f90:52`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `no3` | `real` | 53 | kg/ha \|nitrate dimensioned by layer |
| `nh4` | `real` | 54 | kg/ha \|ammonium dimensioned by layer |

### mineral_phosphorus

- **Defined in source**: `organic_mineral_mass_module.f90:59`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `wsol` | `real` | 60 | kg/ha \|water soluble p dimensioned by layer |
| `lab` | `real` | 61 | kg/ha \|labile p dimensioned by layer |
| `act` | `real` | 62 | kg/ha \|active mineral p dimensioned by layer |
| `sta` | `real` | 63 | kg/ha \|stable mineral p dimensioned by layer |

### plant_residue

- **Defined in source**: `organic_mineral_mass_module.f90:68`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `rsd` | `organic_mass` | 69 | \|fresh surface residue dimensioned by layer |

### soil_profile_mass

- **Defined in source**: `organic_mineral_mass_module.f90:72`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 73 |  |
| `tot_mn` | `real` | 74 | \|total mineral n pool (no3+nh4) in soil profile |
| `tot_mp` | `real` | 75 | \|mineral p pool (wsol+lab+act+sta) in soil profile |
| `salt` | `real` | 76 | \|total salt amount (kg/ha) in soil profile |
| `tot_org` | `organic_mass` | 77 | \|total organics in soil profile |
| `seq_org` | `organic_mass` | 78 | \|sequestered organics in soil profile wich does not include the surface layer |
| `surf_org` | `organic_mass` | 79 | \|soil surface layer soil soil profile |
| `sw` | `real, dimension(:), allocatable` | 80 | mm \|soil water dimensioned by layer |
| `cbn` | `real, dimension(:), allocatable` | 81 | % \|percent carbon |
| `sed` | `sediment` | 82 | \|sediment dimensioned by layer |
| `mn` | `mineral_nitrogen` | 83 | \|mineral n pool dimensioned by layer |
| `mp` | `mineral_phosphorus` | 84 | \|mineral p humus pool dimensioned by layer tot and rsd used for both carbon methods |
| `tot` | `organic_mass` | 86 | \|total organic pool dimensioned by layer |
| `seq` | `organic_mass` | 87 | \|total sequestered organic pool dimensioned by layer, surface layer = 0.0 |
| `seq_tot_300_c` | `real` | 88 | \|total sequestered equal to or above 300mm soil depth |
| `tot_300_c` | `real` | 89 | \|total carbon equal to or above 300mm soil depth |
| `emix` | `real, dimension(:), allocatable` | 90 | \|the fraction of mixing that occurs from tillage or biomixing in each soil layer |
| `pl` | `plant_residue` | 91 | \|fresh surface residue dimensioned by plant and by layer |
| `rsd_tot` | `organic_mass` | 92 | \|total fresh surface residue dimensioned by layer |
| `root_tot` | `organic_mass` | 93 | \|total live roots dimensioned by layer humus pools for old mineralization model (static carbon) |
| `org_con_lr` | `organic_controls` | 95 | \|organic contral variables by layer |
| `org_allo_lr` | `organic_allocations` | 96 | \|organic allocation variables by layer |
| `org_ratio_lr` | `organic_ratio` | 97 | \|organic nitrogen carbon ratios layer |
| `org_tran_lr` | `organic_transformations` | 98 | \|portential organic transformations layer |
| `org_flx_tot` | `organic_flux` | 99 | \|total organic flux for soil profile |
| `org_flx_lr` | `organic_flux` | 100 | \|organic flux by layer |
| `org_flx_cum_lr` | `organic_flux` | 101 | \|cumulative organic flux by layer |
| `hact` | `organic_mass` | 102 | \|active humus for old mineralization model dimensioned by layer |
| `hsta` | `organic_mass` | 103 | \|stable humus for old mineralization model dimensioned by layer organic pools used in CENTURY model |
| `hs` | `organic_mass` | 105 | \|slow humus dimensioned by layer |
| `hp` | `organic_mass` | 106 | \|passive humus dimensioned by layer rest are used in CENTURY model |
| `microb` | `organic_mass` | 109 | \|microbial biomass |
| `str` | `organic_mass` | 110 | \|structural litter pool dimensioned by layer |
| `lig` | `organic_mass` | 111 | \|lignin pool dimensioned by layer |
| `nonlig` | `organic_mass` | 112 | \|non lignin pool dimensioned by layer |
| `meta` | `organic_mass` | 113 | \|metabolic litter pool dimensioned by layer |
| `man` | `organic_mass` | 114 | \|manure pool dimensioned by layer |
| `water` | `organic_mass` | 115 | \|water soluble |

### plant_community_mass

- **Defined in source**: `organic_mineral_mass_module.f90:161`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=4)` | 162 |  |
| `tot` | `organic_mass` | 163 | kg/ha \|total biomass for individual plant in community |
| `ab_gr` | `organic_mass` | 164 | kg/ha \|above ground biomass for individual plant in community |
| `leaf` | `organic_mass` | 165 | kg/ha \|leaf mass for individual plant in community |
| `stem` | `organic_mass` | 166 | kg/ha \|wood/stalk mass for individual plant in community |
| `root` | `organic_mass` | 167 | kg/ha \|root mass for individual plant in community (by soil layer) |
| `seed` | `organic_mass` | 168 | kg/ha \|seed (grain) mass for individual plant in community |
| `yield_tot` | `organic_mass` | 169 | kg/ha \|running total sum of yield at harvest - ave annual print |
| `yield_yr` | `organic_mass` | 170 | kg/ha \|running yearly sum of yield at harvest - yearly print |
| `rsd` | `organic_mass` | 171 | kg/ha \|fresh surface residue dimensioned by plant |
| `rsd_tot` | `organic_mass` | 172 | kg/ha \|total fresh surface residue |
| `tot_com` | `organic_mass` | 173 | kg/ha \|total biomass for entire community |
| `ab_gr_com` | `organic_mass` | 174 | kg/ha \|above ground mass for entire community |
| `leaf_com` | `organic_mass` | 175 | kg/ha \|leaf mass for entire community |
| `stem_com` | `organic_mass` | 176 | kg/ha \|wood/stalk mass for entire community |
| `root_com` | `organic_mass` | 177 | kg/ha \|root mass for entire community |
| `seed_com` | `organic_mass` | 178 | kg/ha \|seed (grain) mass for entire community |

### mineral_mass

- **Defined in source**: `organic_mineral_mass_module.f90:194`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `m` | `real` | 195 | kg or kg/ha \|total object mass |
| `no3` | `real` | 196 | kg or kg/ha \|nitrate mass |
| `no2` | `real` | 197 | kg or kg/ha \|nitrite mass |
| `nh4` | `real` | 198 | kg or kg/ha \|ammonium mass |
| `po4` | `real` | 199 | kg or kg/ha \|phosphate mass |

### organic_mineral_mass

- **Defined in source**: `organic_mineral_mass_module.f90:202`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `vol` | `real` | 203 |  |
| `hum` | `organic_mass` | 204 |  |
| `hum_act` | `organic_mass` | 205 |  |
| `min` | `mineral_mass` | 206 |  |

### animal_herds

- **Defined in source**: `organic_mineral_mass_module.f90:211`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=16)` | 212 | \|herd name (small_dairy, ) |
| `num_tot` | `integer` | 213 | \|total number of animals in the herd |
| `herd_mass` | `organic_mass` | 214 | kg \|total mass of herd |
| `typ` | `character(len=16), dimension(:), allocatable` | 215 | \|animal type (points to animal.hrd) |
| `num` | `integer, dimension(:), allocatable` | 216 | \|number of each type of animal |
| `mass` | `organic_mass` | 217 | \|mass of each type of animal |
| `eat` | `organic_mass` | 218 | \|biomass eaten by each type of animal |
| `manure` | `organic_mineral_mass` | 219 | \|manure from each type of animal |

### fertilizer_mass

- **Defined in source**: `organic_mineral_mass_module.f90:223`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 224 |  |
| `org` | `mineral_mass` | 225 | soil matrix dimensioned by layer |
| `min` | `organic_mass` | 226 | soil water dimensioned by layer |

### organic_mineral_hydrograph

- **Defined in source**: `organic_mineral_mass_module.f90:236`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `flo` | `real` | 237 | m^3 \|volume of water |
| `sed` | `real` | 238 | metric tons \|sediment |
| `org` | `organic_mass` | 239 |  |
| `min` | `mineral_mass` | 240 |  |
| `chla` | `real` | 241 | kg \|chlorophyll-a |
| `cbod` | `real` | 242 | kg \|carbonaceous biological oxygen demand |
| `dox` | `real` | 243 | kg \|dissolved oxygen |
| `temp` | `real` | 244 | deg c \|temperature |
| `san` | `real` | 245 | tons \|detached sand |
| `sil` | `real` | 246 | tons \|detached silt |
| `cla` | `real` | 247 | tons \|detached clay |
| `sag` | `real` | 248 | tons \|detached small ag |
| `lag` | `real` | 249 | tons \|detached large ag |
| `grv` | `real` | 250 | tons \|gravel |

### spatial_object_hydrographs

- **Defined in source**: `organic_mineral_mass_module.f90:253`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 254 | should match the object_connectivity object water and soluble components |
| `hin` | `organic_mineral_hydrograph` | 256 | inflow hydrograph for surface runon - sum of all inflow hyds |
| `hin_sur` | `organic_mineral_hydrograph` | 257 | inflow hydrograph for surface flow - sum of all surface inflow hyds |
| `hin_lat` | `organic_mineral_hydrograph` | 258 | inflow hydrograph for lateral soil flow - sum of all lateral inflow hyds |
| `hin_til` | `organic_mineral_hydrograph` | 259 | inflow hydrograph for tile flow - sum of all tile inflow hyds |
| `hin_aqu` | `organic_mineral_hydrograph` | 260 | inflow hydrograph for aquifer flow - sum of all aquifer inflow hyds |
| `hd` | `organic_mineral_hydrograph` | 261 | generated hydrograph (ie 1=tot, 2= recharge, 3=surf, etc) |
| `ts` | `organic_mineral_hydrograph` | 262 | subdaily hydrographs |
| `tsin` | `organic_mineral_hydrograph` | 263 | inflow subdaily hydrograph sediment (sorbed) in the water components |
| `hins` | `organic_mineral_hydrograph` | 265 | inflow hydrograph for surface runon - sum of all inflow hyds |
| `hin_ssur` | `organic_mineral_hydrograph` | 266 | inflow hydrograph for surface flow - sum of all surface inflow hyds |
| `hin_slat` | `organic_mineral_hydrograph` | 267 | inflow hydrograph for lateral soil flow - sum of all lateral inflow hyds |
| `hin_stil` | `organic_mineral_hydrograph` | 268 | inflow hydrograph for tile flow - sum of all tile inflow hyds |
| `hds` | `organic_mineral_hydrograph` | 269 | generated hydrograph (ie 1=tot, 2= recharge, 3=surf, etc) |
| `tss` | `organic_mineral_hydrograph` | 270 | subdaily hydrographs |
| `tsins` | `organic_mineral_hydrograph` | 271 | inflow subdaily hydrograph hydrograph output variables |
| `hin_d` | `organic_mineral_hydrograph` | 273 |  |
| `hin_m` | `organic_mineral_hydrograph` | 274 |  |
| `hin_y` | `organic_mineral_hydrograph` | 275 |  |
| `hin_a` | `organic_mineral_hydrograph` | 276 |  |
| `hout_m` | `organic_mineral_hydrograph` | 277 |  |
| `hout_y` | `organic_mineral_hydrograph` | 278 |  |
| `hout_a` | `organic_mineral_hydrograph` | 279 |  |
| `hdep_m` | `organic_mineral_hydrograph` | 280 |  |
| `hdep_y` | `organic_mineral_hydrograph` | 281 |  |
| `hdep_a` | `organic_mineral_hydrograph` | 282 |  |

### recall_organic_mineral_inputs

- **Defined in source**: `organic_mineral_mass_module.f90:288`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 289 |  |
| `num` | `integer` | 290 | number of elements |
| `typ` | `integer` | 291 | recall type - 1=day, 2=mon, 3=year |
| `filename` | `character(len=13)` | 292 | filename hyd_output units are in cms and mg/L |
| `hd_om` | `organic_mineral_hydrograph` | 294 | export coefficients |

### routing_unit_elements_hydrographs

- **Defined in source**: `organic_mineral_mass_module.f90:304`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 305 | should match the object_connectivity object |
| `hd` | `organic_mineral_mass` | 306 |  |

### channel_surface_elements_hydrographs

- **Defined in source**: `organic_mineral_mass_module.f90:311`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=16)` | 312 | should match the channel_surface_elements object |
| `hd` | `organic_mineral_mass` | 313 |  |

## Variables Defined
### meta_frac

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:7`
- **Source note**: none       |fraction of that is metabolic

### str_frac

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:8`
- **Source note**: none       |fraction of that is structural

### lig_frac

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:9`
- **Source note**: none       |fraction of that is lignin

### orgz

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:17`

### mix_org

- **Type**: `organic_mixing_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:37`

### mnz

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:56`

### mix_mn

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:57`
- **Source note**: |mineral n pool used in tillage mixing

### mpz

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:65`

### mix_mp

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:66`
- **Source note**: |mineral p pool used in tillage mixing

### soil1

- **Type**: `soil_profile_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:119`

### soil1_init

- **Type**: `soil_profile_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:120`

### soil_prof_tot

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:121`
- **Source note**: |total organic pool for profile (summed by layer)

### soil_prof_root

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:122`
- **Source note**: |total live roots for profile (summed by lower layers)

### soil_prof_root_frac

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:123`
- **Source note**: |total live root fraction for profile (summed by lower layers)

### soil_prof_rsd

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:124`
- **Source note**: |total fresh organic residue pool for profile (summed by lower layers)

### soil_prof_srsd

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:125`
- **Source note**: |total fresh organic residue pool for surface

### soil_prof_hact

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:126`
- **Source note**: |total active humus pool for profile (summed by layer)

### soil_prof_hsta

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:127`
- **Source note**: |total stable huumus pool for profile (summed by layer)

### soil_prof_hs

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:128`
- **Source note**: |total slow humus pool for profile (summed by layer)

### soil_prof_hp

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:129`
- **Source note**: |total passive humus pool for profile (summed by layer)

### soil_prof_microb

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:130`
- **Source note**: |total microbial pool for profile (summed by layer)

### soil_prof_seq_hs

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:131`
- **Source note**: |sequestered slow humus pool for profile summed up by layer excluding layer 1

### soil_prof_seq_hp

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:132`
- **Source note**: |sequestered passive humus pool for profile summed up by layer excluding layer 1

### soil_prof_seq_microb

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:133`
- **Source note**: |sequestered microbial pool for profile summed up by layer excluding layer 1

### soil_prof_str

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:134`
- **Source note**: |total structural pool for profile (summed by layer)

### soil_prof_lig

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:135`
- **Source note**: |total lignin pool for profile (summed by layer)

### soil_prof_nonlig

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:136`
- **Source note**: |total nonlignin pool for profile (summed by layer)

### soil_prof_meta

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:137`
- **Source note**: |total metabolic pool for profile (summed by layer)

### soil_prof_sstr

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:138`
- **Source note**: |total structural pool for surface (summed by lower layers)

### soil_prof_slig

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:139`
- **Source note**: |total lignin pool for surface (summed by lower layers)

### soil_prof_smeta

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:140`
- **Source note**: |total metabolic pool for profile (summed by layer)

### soil_prof_man

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:141`
- **Source note**: |total manure pool for profile (summed by layer)

### soil_prof_water

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:142`
- **Source note**: |total dissolved pool for profile (summed by layer)

### soil_org_z

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:143`
- **Source note**: |used to zero organic objects

### soil_prof_somc

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:144`

### soil_prof_mn

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:145`
- **Source note**: |mineral n pool (summed by layer)

### soil_prof_mp

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:146`
- **Source note**: |mineral p  pool (summed by layer)

### soil_mn_z

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:147`

### soil_mp_z

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:148`

### bsn_org_soil

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:149`
- **Source note**: |total soil organics in basin

### bsn_org_pl

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:150`
- **Source note**: |total plant organics in basin

### bsn_org_rsd

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:151`
- **Source note**: |total residue organics in basin

### bsn_mn

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:152`
- **Source note**: |total mineral n pool (no3+nh4) in basin

### bsn_mp

- **Type**: `real`
- **Defined in source**: `organic_mineral_mass_module.f90:153`
- **Source note**: |mineral p pool (wsol+lab+act+sta) in basin

### decomp

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:154`
- **Source note**: |temporary storage for residue decomp

### photo_decomp

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:155`
- **Source note**: |temporary storage for photo_residue decomp

### transfer

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:156`
- **Source note**: |temporary storage for residue decomp

### pl_burn

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:157`
- **Source note**: |residue and plant mass burned in fire

### rsd_meta

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:158`
- **Source note**: |temporary storage for initial metabolic litter

### rsd_str

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:159`
- **Source note**: |temporary storage for initial structural litter

### pl_mass

- **Type**: `plant_community_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:181`

### pl_mass_init

- **Type**: `plant_community_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:182`

### pl_yield

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:183`
- **Source note**: kg/ha      |crop yield

### pl_mass_up

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:184`
- **Source note**: kg/ha      |daily biomass and c increase; n and p uptake

### pl_residue

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:185`

### harv_seed

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:186`

### harv_leaf

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:186`

### harv_stem

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:186`

### harv_left

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:186`

### graz_plant

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:187`

### graz_seed

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:187`

### graz_leaf

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:187`

### graz_stem

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:187`

### leaf_drop

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:188`
- **Source note**: kg/ha      |organic mass of falling leaves

### abgr_drop

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:189`
- **Source note**: kg/ha      |above ground that dies at dormancy

### stem_drop

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:190`
- **Source note**: kg/ha      |stem that dies at dormancy

### seed_drop

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:191`
- **Source note**: kg/ha      |seed that dies at dormancy

### plt_mass_z

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:192`

### fert

- **Type**: `fertilizer_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:229`
- **Source note**: dimension to number of fertilzers in database

### org_frt

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:231`
- **Source note**: dimension to number of manures in database

### manure

- **Type**: `organic_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:234`
- **Source note**: dimension to number of manures in database

### obom

- **Type**: `spatial_object_hydrographs`
- **Defined in source**: `organic_mineral_mass_module.f90:285`

### rec_om

- **Type**: `recall_organic_mineral_inputs`
- **Defined in source**: `organic_mineral_mass_module.f90:296`

### exco_om

- **Type**: `organic_mineral_hydrograph`
- **Defined in source**: `organic_mineral_mass_module.f90:299`

### dr_om

- **Type**: `organic_mineral_hydrograph`
- **Defined in source**: `organic_mineral_mass_module.f90:302`

### sub_e_hd

- **Type**: `routing_unit_elements_hydrographs`
- **Defined in source**: `organic_mineral_mass_module.f90:309`

### ch_sur_hd

- **Type**: `channel_surface_elements_hydrographs`
- **Defined in source**: `organic_mineral_mass_module.f90:316`

### o_m1

- **Type**: `organic_mineral_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:319`

### o_m2

- **Type**: `organic_mineral_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:319`

### o_m3

- **Type**: `organic_mineral_mass`
- **Defined in source**: `organic_mineral_mass_module.f90:319`

### pmin_m1

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:320`

### pmin_m2

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:320`

### pmin_m3

- **Type**: `mineral_phosphorus`
- **Defined in source**: `organic_mineral_mass_module.f90:320`

### nmin_m1

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:321`

### nmin_m2

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:321`

### nmin_m3

- **Type**: `mineral_nitrogen`
- **Defined in source**: `organic_mineral_mass_module.f90:321`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### nmin_add

### nmin_mult_const

### pmin_add

### pmin_mult_const

### om_add1

### om_subtract

### om_mult_const

### om_divide

### org_flux_add1

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->

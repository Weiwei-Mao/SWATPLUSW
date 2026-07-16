---
type: module
tags:
  - swat/module
  - swat/to-read
file: input_file_module.f90
note_file: input_file_module.f90
module_name: input_file_module
defines_types:
  - input_sim
  - input_basin
  - input_cli
  - input_con
  - input_cha
  - input_res
  - input_ru
  - input_hru
  - input_exco
  - input_rec
  - input_delr
  - input_aqu
  - input_herd
  - input_water_rights
  - input_link
  - input_hydrology
  - input_structural
  - input_parameter_databases
  - input_ops
  - input_lum
  - input_chg
  - input_init
  - input_soils
  - input_condition
  - input_regions
  - shade_factor
  - input_path_pcp
  - input_path_tmp
  - input_path_slr
  - input_path_hmd
  - input_path_wnd
  - input_path_pet
defines_vars:
  - in_sim
  - in_basin
  - in_cli
  - in_con
  - in_cha
  - in_res
  - in_ru
  - in_hru
  - in_exco
  - in_rec
  - in_delr
  - in_aqu
  - in_herd
  - in_watrts
  - in_link
  - in_hyd
  - in_str
  - in_parmdb
  - in_ops
  - in_lum
  - in_chg
  - in_init
  - in_sol
  - in_cond
  - in_regs
  - in_shf
  - in_path_pcp
  - in_path_tmp
  - in_path_slr
  - in_path_hmd
  - in_path_wnd
  - in_path_pet
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# input_file_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### input_sim

- **Defined in source**: `input_file_module.f90:8`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `time` | `character(len=25)` | 9 |  |
| `prt` | `character(len=25)` | 10 |  |
| `object_prt` | `character(len=25)` | 11 |  |
| `object_cnt` | `character(len=25)` | 12 |  |
| `cs_db` | `character(len=25)` | 13 |  |

### input_basin

- **Defined in source**: `input_file_module.f90:18`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `codes_bas` | `character(len=25)` | 19 |  |
| `parms_bas` | `character(len=25)` | 20 |  |
| `carbon_bsn` | `character(len=25)` | 21 |  |

### input_cli

- **Defined in source**: `input_file_module.f90:26`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `weat_sta` | `character(len=25)` | 27 |  |
| `weat_wgn` | `character(len=25)` | 28 |  |
| `pet_cli` | `character(len=25)` | 29 |  |
| `pcp_cli` | `character(len=25)` | 31 |  |
| `tmp_cli` | `character(len=25)` | 32 |  |
| `slr_cli` | `character(len=25)` | 33 |  |
| `hmd_cli` | `character(len=25)` | 34 |  |
| `wnd_cli` | `character(len=25)` | 35 |  |
| `atmo_cli` | `character(len=25)` | 36 |  |

### input_con

- **Defined in source**: `input_file_module.f90:41`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru_con` | `character(len=25)` | 42 |  |
| `hruez_con` | `character(len=25)` | 43 |  |
| `ru_con` | `character(len=25)` | 44 |  |
| `gwflow_con` | `character(len=25)` | 45 |  |
| `aqu_con` | `character(len=25)` | 46 |  |
| `aqu2d_con` | `character(len=25)` | 47 |  |
| `chan_con` | `character(len=25)` | 48 |  |
| `res_con` | `character(len=25)` | 49 |  |
| `rec_con` | `character(len=25)` | 50 |  |
| `exco_con` | `character(len=25)` | 51 |  |
| `delr_con` | `character(len=25)` | 52 |  |
| `out_con` | `character(len=25)` | 53 |  |
| `chandeg_con` | `character(len=25)` | 54 |  |

### input_cha

- **Defined in source**: `input_file_module.f90:59`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init` | `character(len=25)` | 60 |  |
| `dat` | `character(len=25)` | 61 |  |
| `hyd` | `character(len=25)` | 62 |  |
| `sed` | `character(len=25)` | 63 |  |
| `nut` | `character(len=25)` | 64 |  |
| `chan_ez` | `character(len=25)` | 65 |  |
| `hyd_sed` | `character(len=25)` | 66 |  |
| `temp` | `character(len=25)` | 67 |  |

### input_res

- **Defined in source**: `input_file_module.f90:72`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init_res` | `character(len=25)` | 73 |  |
| `res` | `character(len=25)` | 74 |  |
| `hyd_res` | `character(len=25)` | 75 |  |
| `sed_res` | `character(len=25)` | 76 |  |
| `nut_res` | `character(len=25)` | 77 |  |
| `weir_res` | `character(len=25)` | 78 |  |
| `wet` | `character(len=25)` | 79 |  |
| `hyd_wet` | `character(len=25)` | 80 |  |

### input_ru

- **Defined in source**: `input_file_module.f90:85`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ru_def` | `character(len=25)` | 86 |  |
| `ru_ele` | `character(len=25)` | 87 |  |
| `ru` | `character(len=25)` | 88 |  |
| `ru_dr` | `character(len=25)` | 89 |  |

### input_hru

- **Defined in source**: `input_file_module.f90:94`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hru_data` | `character(len=25)` | 95 |  |
| `hru_ez` | `character(len=25)` | 96 |  |

### input_exco

- **Defined in source**: `input_file_module.f90:101`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `exco` | `character(len=25)` | 102 |  |
| `om` | `character(len=25)` | 103 |  |
| `pest` | `character(len=25)` | 104 |  |
| `path` | `character(len=25)` | 105 |  |
| `hmet` | `character(len=25)` | 106 |  |
| `salt` | `character(len=25)` | 107 |  |

### input_rec

- **Defined in source**: `input_file_module.f90:112`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `recall_rec` | `character(len=25)` | 113 |  |

### input_delr

- **Defined in source**: `input_file_module.f90:118`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `del_ratio` | `character(len=25)` | 119 |  |
| `om` | `character(len=25)` | 120 |  |
| `pest` | `character(len=25)` | 121 |  |
| `path` | `character(len=25)` | 122 |  |
| `hmet` | `character(len=25)` | 123 |  |
| `salt` | `character(len=25)` | 124 |  |

### input_aqu

- **Defined in source**: `input_file_module.f90:129`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `init` | `character(len=25)` | 130 |  |
| `aqu` | `character(len=25)` | 131 |  |

### input_herd

- **Defined in source**: `input_file_module.f90:136`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `animal` | `character(len=25)` | 137 |  |
| `herd` | `character(len=25)` | 138 |  |
| `ranch` | `character(len=25)` | 139 |  |

### input_water_rights

- **Defined in source**: `input_file_module.f90:144`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `transfer_wro` | `character(len=25)` | 145 | transferring water using water rights objects (using decision tables) |
| `element` | `character(len=25)` | 146 |  |
| `water_rights` | `character(len=25)` | 147 | 2 sources and compensation (used for NAM) |

### input_link

- **Defined in source**: `input_file_module.f90:152`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `chan_surf` | `character(len=25)` | 153 |  |
| `aqu_cha` | `character(len=25)` | 154 |  |

### input_hydrology

- **Defined in source**: `input_file_module.f90:159`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hydrol_hyd` | `character(len=25)` | 160 |  |
| `topogr_hyd` | `character(len=25)` | 161 |  |
| `field_fld` | `character(len=25)` | 162 |  |

### input_structural

- **Defined in source**: `input_file_module.f90:167`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tiledrain_str` | `character(len=25)` | 168 |  |
| `septic_str` | `character(len=25)` | 169 |  |
| `fstrip_str` | `character(len=25)` | 170 |  |
| `grassww_str` | `character(len=25)` | 171 |  |
| `bmpuser_str` | `character(len=25)` | 172 |  |

### input_parameter_databases

- **Defined in source**: `input_file_module.f90:177`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plants_plt` | `character(len=25)` | 178 |  |
| `fert_frt` | `character(len=25)` | 179 |  |
| `till_til` | `character(len=25)` | 180 |  |
| `pest` | `character(len=25)` | 181 |  |
| `pathcom_db` | `character(len=25)` | 182 |  |
| `hmetcom_db` | `character(len=25)` | 183 |  |
| `saltcom_db` | `character(len=25)` | 184 |  |
| `urban_urb` | `character(len=25)` | 185 |  |
| `septic_sep` | `character(len=25)` | 186 |  |
| `snow` | `character(len=25)` | 187 |  |

### input_ops

- **Defined in source**: `input_file_module.f90:192`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `harv_ops` | `character(len=25)` | 193 |  |
| `graze_ops` | `character(len=25)` | 194 |  |
| `irr_ops` | `character(len=25)` | 195 |  |
| `chem_ops` | `character(len=25)` | 196 |  |
| `fire_ops` | `character(len=25)` | 197 |  |
| `sweep_ops` | `character(len=25)` | 198 |  |

### input_lum

- **Defined in source**: `input_file_module.f90:203`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `landuse_lum` | `character(len=25)` | 204 |  |
| `management_sch` | `character(len=25)` | 205 |  |
| `cntable_lum` | `character(len=25)` | 206 |  |
| `cons_prac_lum` | `character(len=25)` | 207 |  |
| `ovn_lum` | `character(len=25)` | 208 |  |

### input_chg

- **Defined in source**: `input_file_module.f90:213`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `cal_parms` | `character(len=25)` | 214 |  |
| `cal_upd` | `character(len=25)` | 215 |  |
| `codes_sft` | `character(len=25)` | 216 | renamed from codes.cal |
| `wb_parms_sft` | `character(len=25)` | 217 | renamed from ls_parms.cal |
| `water_balance_sft` | `character(len=25)` | 218 | renamed from ls_regions.cal |
| `ch_sed_budget_sft` | `character(len=25)` | 219 | renamed from ch_orders.cal |
| `ch_sed_parms_sft` | `character(len=25)` | 220 | renamed from ch_parms.cal |
| `plant_parms_sft` | `character(len=25)` | 221 | renamed from pl_parms.cal |
| `plant_gro_sft` | `character(len=25)` | 222 | renamed from pl_regions.cal |

### input_init

- **Defined in source**: `input_file_module.f90:227`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `plant` | `character(len=25)` | 228 |  |
| `soil_plant_ini` | `character(len=25)` | 229 |  |
| `om_water` | `character(len=25)` | 230 |  |
| `pest_soil` | `character(len=25)` | 231 |  |
| `pest_water` | `character(len=25)` | 232 |  |
| `path_soil` | `character(len=25)` | 233 |  |
| `path_water` | `character(len=25)` | 234 |  |
| `hmet_soil` | `character(len=25)` | 235 |  |
| `hmet_water` | `character(len=25)` | 236 |  |
| `salt_soil` | `character(len=25)` | 237 |  |
| `salt_water` | `character(len=25)` | 238 |  |

### input_soils

- **Defined in source**: `input_file_module.f90:243`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `soils_sol` | `character(len=25)` | 244 |  |
| `nut_sol` | `character(len=25)` | 245 |  |
| `lte_sol` | `character(len=25)` | 246 |  |

### input_condition

- **Defined in source**: `input_file_module.f90:251`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `dtbl_lum` | `character(len=25)` | 252 |  |
| `dtbl_res` | `character(len=25)` | 253 |  |
| `dtbl_scen` | `character(len=25)` | 254 |  |
| `dtbl_flo` | `character(len=25)` | 255 |  |

### input_regions

- **Defined in source**: `input_file_module.f90:260`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ele_lsu` | `character(len=25)` | 261 |  |
| `def_lsu` | `character(len=25)` | 262 |  |
| `ele_reg` | `character(len=25)` | 263 |  |
| `def_reg` | `character(len=25)` | 264 |  |
| `cal_lcu` | `character(len=25)` | 265 |  |
| `ele_cha` | `character(len=25)` | 266 |  |
| `def_cha` | `character(len=25)` | 267 |  |
| `def_cha_reg` | `character(len=25)` | 268 |  |
| `ele_aqu` | `character(len=25)` | 269 |  |
| `def_aqu` | `character(len=25)` | 270 |  |
| `def_aqu_reg` | `character(len=25)` | 271 |  |
| `ele_res` | `character(len=25)` | 272 |  |
| `def_res` | `character(len=25)` | 273 |  |
| `def_res_reg` | `character(len=25)` | 274 |  |
| `ele_psc` | `character(len=25)` | 275 |  |
| `def_psc` | `character(len=25)` | 276 |  |
| `def_psc_reg` | `character(len=25)` | 277 |  |

### shade_factor

- **Defined in source**: `input_file_module.f90:282`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `ssff_shf` | `character(len=25)` | 283 |  |

### input_path_pcp

- **Defined in source**: `input_file_module.f90:287`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `pcp` | `character(len=80)` | 288 |  |

### input_path_tmp

- **Defined in source**: `input_file_module.f90:292`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `tmp` | `character(len=80)` | 293 |  |

### input_path_slr

- **Defined in source**: `input_file_module.f90:297`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `slr` | `character(len=80)` | 298 |  |

### input_path_hmd

- **Defined in source**: `input_file_module.f90:302`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `hmd` | `character(len=80)` | 303 |  |

### input_path_wnd

- **Defined in source**: `input_file_module.f90:307`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `wnd` | `character(len=80)` | 308 |  |

### input_path_pet

- **Defined in source**: `input_file_module.f90:312`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `peti` | `character(len=80)` | 313 |  |

## Variables Defined
### in_sim

- **Type**: `input_sim`
- **Defined in source**: `input_file_module.f90:15`

### in_basin

- **Type**: `input_basin`
- **Defined in source**: `input_file_module.f90:23`

### in_cli

- **Type**: `input_cli`
- **Defined in source**: `input_file_module.f90:38`

### in_con

- **Type**: `input_con`
- **Defined in source**: `input_file_module.f90:56`

### in_cha

- **Type**: `input_cha`
- **Defined in source**: `input_file_module.f90:69`

### in_res

- **Type**: `input_res`
- **Defined in source**: `input_file_module.f90:82`

### in_ru

- **Type**: `input_ru`
- **Defined in source**: `input_file_module.f90:91`

### in_hru

- **Type**: `input_hru`
- **Defined in source**: `input_file_module.f90:98`

### in_exco

- **Type**: `input_exco`
- **Defined in source**: `input_file_module.f90:109`

### in_rec

- **Type**: `input_rec`
- **Defined in source**: `input_file_module.f90:115`

### in_delr

- **Type**: `input_delr`
- **Defined in source**: `input_file_module.f90:126`

### in_aqu

- **Type**: `input_aqu`
- **Defined in source**: `input_file_module.f90:133`

### in_herd

- **Type**: `input_herd`
- **Defined in source**: `input_file_module.f90:141`

### in_watrts

- **Type**: `input_water_rights`
- **Defined in source**: `input_file_module.f90:149`

### in_link

- **Type**: `input_link`
- **Defined in source**: `input_file_module.f90:156`

### in_hyd

- **Type**: `input_hydrology`
- **Defined in source**: `input_file_module.f90:164`

### in_str

- **Type**: `input_structural`
- **Defined in source**: `input_file_module.f90:174`

### in_parmdb

- **Type**: `input_parameter_databases`
- **Defined in source**: `input_file_module.f90:189`

### in_ops

- **Type**: `input_ops`
- **Defined in source**: `input_file_module.f90:200`

### in_lum

- **Type**: `input_lum`
- **Defined in source**: `input_file_module.f90:210`

### in_chg

- **Type**: `input_chg`
- **Defined in source**: `input_file_module.f90:224`

### in_init

- **Type**: `input_init`
- **Defined in source**: `input_file_module.f90:240`

### in_sol

- **Type**: `input_soils`
- **Defined in source**: `input_file_module.f90:248`

### in_cond

- **Type**: `input_condition`
- **Defined in source**: `input_file_module.f90:257`

### in_regs

- **Type**: `input_regions`
- **Defined in source**: `input_file_module.f90:279`

### in_shf

- **Type**: `shade_factor`
- **Defined in source**: `input_file_module.f90:285`

### in_path_pcp

- **Type**: `input_path_pcp`
- **Defined in source**: `input_file_module.f90:290`

### in_path_tmp

- **Type**: `input_path_tmp`
- **Defined in source**: `input_file_module.f90:295`

### in_path_slr

- **Type**: `input_path_slr`
- **Defined in source**: `input_file_module.f90:300`

### in_path_hmd

- **Type**: `input_path_hmd`
- **Defined in source**: `input_file_module.f90:305`

### in_path_wnd

- **Type**: `input_path_wnd`
- **Defined in source**: `input_file_module.f90:310`

### in_path_pet

- **Type**: `input_path_pet`
- **Defined in source**: `input_file_module.f90:315`

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

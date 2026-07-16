---
type: module
tags:
  - swat/模块
  - swat/待读
file: input_file_module.f90
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
  - time
  - prt
  - object_prt
  - object_cnt
  - cs_db
  - codes_bas
  - parms_bas
  - carbon_bsn
  - weat_sta
  - weat_wgn
  - pet_cli
  - pcp_cli
  - tmp_cli
  - slr_cli
  - hmd_cli
  - wnd_cli
  - atmo_cli
  - hru_con
  - hruez_con
  - ru_con
  - gwflow_con
  - aqu_con
  - aqu2d_con
  - chan_con
  - res_con
  - rec_con
  - exco_con
  - delr_con
  - out_con
  - chandeg_con
  - init
  - dat
  - hyd
  - sed
  - nut
  - chan_ez
  - hyd_sed
  - temp
  - init_res
  - res
  - hyd_res
  - sed_res
  - nut_res
  - weir_res
  - wet
  - hyd_wet
  - ru_def
  - ru_ele
  - ru
  - ru_dr
  - hru_data
  - hru_ez
  - exco
  - om
  - pest
  - path
  - hmet
  - salt
  - recall_rec
  - del_ratio
  - aqu
  - animal
  - herd
  - ranch
  - transfer_wro
  - element
  - water_rights
  - chan_surf
  - aqu_cha
  - hydrol_hyd
  - topogr_hyd
  - field_fld
  - tiledrain_str
  - septic_str
  - fstrip_str
  - grassww_str
  - bmpuser_str
  - plants_plt
  - fert_frt
  - till_til
  - pathcom_db
  - hmetcom_db
  - saltcom_db
  - urban_urb
  - septic_sep
  - snow
  - harv_ops
  - graze_ops
  - irr_ops
  - chem_ops
  - fire_ops
  - sweep_ops
  - landuse_lum
  - management_sch
  - cntable_lum
  - cons_prac_lum
  - ovn_lum
  - cal_parms
  - cal_upd
  - codes_sft
  - wb_parms_sft
  - water_balance_sft
  - ch_sed_budget_sft
  - ch_sed_parms_sft
  - plant_parms_sft
  - plant_gro_sft
  - plant
  - soil_plant_ini
  - om_water
  - pest_soil
  - pest_water
  - path_soil
  - path_water
  - hmet_soil
  - hmet_water
  - salt_soil
  - salt_water
  - soils_sol
  - nut_sol
  - lte_sol
  - dtbl_lum
  - dtbl_res
  - dtbl_scen
  - dtbl_flo
  - ele_lsu
  - def_lsu
  - ele_reg
  - def_reg
  - cal_lcu
  - ele_cha
  - def_cha
  - def_cha_reg
  - ele_aqu
  - def_aqu
  - def_aqu_reg
  - ele_res
  - def_res
  - def_res_reg
  - ele_psc
  - def_psc
  - def_psc_reg
  - ssff_shf
  - pcp
  - tmp
  - slr
  - hmd
  - wnd
  - peti
purpose: ""
---

# input_file_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `input_sim` |  |
| `input_basin` |  |
| `input_cli` |  |
| `input_con` |  |
| `input_cha` |  |
| `input_res` |  |
| `input_ru` |  |
| `input_hru` |  |
| `input_exco` |  |
| `input_rec` |  |
| `input_delr` |  |
| `input_aqu` |  |
| `input_herd` |  |
| `input_water_rights` |  |
| `input_link` |  |
| `input_hydrology` |  |
| `input_structural` |  |
| `input_parameter_databases` |  |
| `input_ops` |  |
| `input_lum` |  |
| `input_chg` |  |
| `input_init` |  |
| `input_soils` |  |
| `input_condition` |  |
| `input_regions` |  |
| `shade_factor` |  |
| `input_path_pcp` |  |
| `input_path_tmp` |  |
| `input_path_slr` |  |
| `input_path_hmd` |  |
| `input_path_wnd` |  |
| `input_path_pet` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `in_sim` |  |  |
| `in_basin` |  |  |
| `in_cli` |  |  |
| `in_con` |  |  |
| `in_cha` |  |  |
| `in_res` |  |  |
| `in_ru` |  |  |
| `in_hru` |  |  |
| `in_exco` |  |  |
| `in_rec` |  |  |
| `in_delr` |  |  |
| `in_aqu` |  |  |
| `in_herd` |  |  |
| `in_watrts` |  |  |
| `in_link` |  |  |
| `in_hyd` |  |  |
| `in_str` |  |  |
| `in_parmdb` |  |  |
| `in_ops` |  |  |
| `in_lum` |  |  |
| `in_chg` |  |  |
| `in_init` |  |  |
| `in_sol` |  |  |
| `in_cond` |  |  |
| `in_regs` |  |  |
| `in_shf` |  |  |
| `in_path_pcp` |  |  |
| `in_path_tmp` |  |  |
| `in_path_slr` |  |  |
| `in_path_hmd` |  |  |
| `in_path_wnd` |  |  |
| `in_path_pet` |  |  |
| `time` |  |  |
| `prt` |  |  |
| `object_prt` |  |  |
| `object_cnt` |  |  |
| `cs_db` |  |  |
| `codes_bas` |  |  |
| `parms_bas` |  |  |
| `carbon_bsn` |  |  |

*（仅显示前 40 个，共 180 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

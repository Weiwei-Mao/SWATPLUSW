---
type: module
tags:
  - swat/模块
  - swat/待读
file: carbon_legacy_module.f90
module_name: carbon_legacy_module
defines_types:
  - output_plc_header
  - output_plc_header_units
  - output_soil_org_flux_header
  - output_soil_org_flux_header_units
  - output_cpool_header
  - output_cpool_header_units
  - output_n_p_pool_header
  - output_n_p_pool_header_units
  - output_carb_vars_header
  - output_org_allo_header
  - output_org_ratio_header
  - output_org_trans_header
  - output_org_trans_header_units
  - output_endsim_soil_prop_header
  - output_bsn_carb_header
  - output_bsn_carb_header_units
defines_vars:
  - plc_hdr
  - plc_hdr_units
  - soil_org_flux_hdr
  - soil_org_flux_hdr_units
  - cpool_hdr
  - cpool_units
  - n_p_pool_hdr
  - n_p_pool_units
  - carbvars_hdr
  - org_allow_hdr
  - org_ratio_hdr
  - org_trans_hdr
  - org_trans_units
  - endsim_soil_prop_hdr
  - bsn_carb_hdr
  - bsn_carb_hdr_units
  - freq
  - day
  - day_mo
  - mo
  - yrc
  - isd
  - id
  - name
  - tot_c
  - ab_gr_c
  - leaf_c
  - stem_c
  - seed_c
  - root_c
  - rsd_c
  - soil_lyr
  - soil_depth
  - cfmets1
  - cfstrs1
  - cfstrs2
  - efmets1
  - efstrs1
  - efstrs2
  - immmets1
  - immstrs1
  - immstrs2
  - mnrmets1
  - mnrstrs1
  - mnrstrs2
  - co2fmet
  - co2fstr
  - cfs1s2
  - cfs1s3
  - cfs2s1
  - cfs2s3
  - cfs3s1
  - efs1s2
  - efs1s3
  - efs2s1
  - efs2s3
  - efs3s1
  - imms1s2
  - imms1s3
  - imms2s1
  - imms2s3
  - imms3s1
  - mnrs1s2
  - mnrs1s3
  - mnrs2s1
  - mnrs2s3
  - mnrs3s1
  - co2fs1
  - co2fs2
  - co2fs3
  - residue_c
  - str_c
  - meta_c
  - hs_c
  - hp_c
  - microb_c
  - lig_c
  - nonlig_c
  - water_c
  - manure_c
  - root_mass
  - soil_water
  - total_pool_n
  - residue_n
  - str_n
  - meta_n
  - hs_n
  - hp_n
  - microb_n
  - lig_n
  - nonlig_n
  - water_n
  - manure_n
  - total_pool_p
  - residue_p
  - str_p
  - meta_p
  - hs_p
  - hp_p
  - microb_p
  - lig_p
  - nonlig_p
  - water_p
  - manure_p
  - sut
  - tillagef
  - bmix
  - tillagef_biomix
  - tillagef_tillmix
  - till_eff
  - cdg
  - ox
  - cs
  - no3
  - nh4
  - resp
  - soil_tmp
  - emix
  - asp
  - abpt
  - abco2
  - a1co2
  - asco2
  - apco2
  - ncbm
  - nchp
  - nchs
  - bmctp
  - bmntp
  - hsctp
  - hsntp
  - hpctp
  - hpntp
  - lmctp
  - lmntp
  - lsctp
  - lslctp
  - lslnctp
  - lsntp
  - soil_name
  - bd
  - awc
  - soil_k
  - carbon
  - clay
  - silt
  - sand
  - rock
  - alb
  - usle_k
  - ec
  - caco3
  - ph
  - blnk
  - org_soilc
  - org_plc
  - org_resc
purpose: ""
---

# carbon_legacy_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `output_plc_header` |  |
| `output_plc_header_units` |  |
| `output_soil_org_flux_header` |  |
| `output_soil_org_flux_header_units` |  |
| `output_cpool_header` |  |
| `output_cpool_header_units` |  |
| `output_n_p_pool_header` |  |
| `output_n_p_pool_header_units` |  |
| `output_carb_vars_header` |  |
| `output_org_allo_header` |  |
| `output_org_ratio_header` |  |
| `output_org_trans_header` |  |
| `output_org_trans_header_units` |  |
| `output_endsim_soil_prop_header` |  |
| `output_bsn_carb_header` |  |
| `output_bsn_carb_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `plc_hdr` |  |  |
| `plc_hdr_units` |  |  |
| `soil_org_flux_hdr` |  |  |
| `soil_org_flux_hdr_units` |  |  |
| `cpool_hdr` |  |  |
| `cpool_units` |  |  |
| `n_p_pool_hdr` |  |  |
| `n_p_pool_units` |  |  |
| `carbvars_hdr` |  |  |
| `org_allow_hdr` |  |  |
| `org_ratio_hdr` |  |  |
| `org_trans_hdr` |  |  |
| `org_trans_units` |  |  |
| `endsim_soil_prop_hdr` |  |  |
| `bsn_carb_hdr` |  |  |
| `bsn_carb_hdr_units` |  |  |
| `freq` |  |  |
| `day` |  |  |
| `day_mo` |  |  |
| `mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `tot_c` |  |  |
| `ab_gr_c` |  |  |
| `leaf_c` |  |  |
| `stem_c` |  |  |
| `seed_c` |  |  |
| `root_c` |  |  |
| `rsd_c` |  |  |
| `soil_lyr` |  |  |
| `soil_depth` |  |  |
| `cfmets1` |  |  |
| `cfstrs1` |  |  |
| `cfstrs2` |  |  |
| `efmets1` |  |  |
| `efstrs1` |  |  |
| `efstrs2` |  |  |
| `immmets1` |  |  |

*（仅显示前 40 个，共 157 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

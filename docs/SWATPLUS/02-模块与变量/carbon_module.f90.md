---
type: module
tags:
  - swat/模块
  - swat/待读
file: carbon_module.f90
module_name: carbon_module
defines_types:
  - carbon_inputs
  - manure_coef
  - organic_allocations
  - organic_controls
  - organic_fractions
  - organic_ratio
  - carbon_water_coef
  - organic_transformations
  - organic_flux
  - carbon_soil_transformations
  - carbon_soil_gain_losses
  - carbon_residue_gain_losses
  - carbon_plant_gain_losses
defines_vars:
  - carbz
  - man_coef
  - org_alloz
  - org_con
  - org_frac
  - org_ratio
  - org_ratio_zero
  - cb_wtr_coef
  - org_tran
  - org_tran_zero
  - org_flux
  - org_flux_zero
  - hscfz
  - bscf_d
  - bscf_m
  - bscf_y
  - bscf_a
  - hscz
  - bsc_d
  - bsc_m
  - bsc_y
  - bsc_a
  - hrcz
  - brc_d
  - brc_m
  - brc_y
  - brc_a
  - hpcz
  - bpc_d
  - bpc_m
  - bpc_y
  - bpc_a
  - cpool_vars
  - n_p_pool_vars
  - cflux_vars
  - carb_drv_vars
  - carb_dyn_vars
  - soil_snap_vars
purpose: ""
---

# carbon_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `carbon_inputs` |  |
| `manure_coef` |  |
| `organic_allocations` |  |
| `organic_controls` |  |
| `organic_fractions` |  |
| `organic_ratio` |  |
| `carbon_water_coef` |  |
| `organic_transformations` |  |
| `organic_flux` |  |
| `carbon_soil_transformations` |  |
| `carbon_soil_gain_losses` |  |
| `carbon_residue_gain_losses` |  |
| `carbon_plant_gain_losses` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `carbz` |  |  |
| `man_coef` |  |  |
| `org_alloz` |  |  |
| `org_con` |  |  |
| `org_frac` |  |  |
| `org_ratio` |  |  |
| `org_ratio_zero` |  |  |
| `cb_wtr_coef` |  |  |
| `org_tran` |  |  |
| `org_tran_zero` |  |  |
| `org_flux` |  |  |
| `org_flux_zero` |  |  |
| `hscfz` |  |  |
| `bscf_d` |  |  |
| `bscf_m` |  |  |
| `bscf_y` |  |  |
| `bscf_a` |  |  |
| `hscz` |  |  |
| `bsc_d` |  |  |
| `bsc_m` |  |  |
| `bsc_y` |  |  |
| `bsc_a` |  |  |
| `hrcz` |  |  |
| `brc_d` |  |  |
| `brc_m` |  |  |
| `brc_y` |  |  |
| `brc_a` |  |  |
| `hpcz` |  |  |
| `bpc_d` |  |  |
| `bpc_m` |  |  |
| `bpc_y` |  |  |
| `bpc_a` |  |  |
| `cpool_vars` |  |  |
| `n_p_pool_vars` |  |  |
| `cflux_vars` |  |  |
| `carb_drv_vars` |  |  |
| `carb_dyn_vars` |  |  |
| `soil_snap_vars` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

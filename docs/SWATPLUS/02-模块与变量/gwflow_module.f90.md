---
type: module
tags:
  - swat/模块
  - swat/待读
file: gwflow_module.f90
module_name: gwflow_module
defines_types:
  - groundwater_state
  - groundwater_transit
  - groundwater_ss
  - cell_channel_info
  - satx_channel_info
  - cell_connections
  - tile_channel_info
  - cell_reservoir_info
  - cell_floodplain_info
  - canal_chan_info
  - cell_canal_info
  - cell_canal_out_info
  - cell_canal_div_info
  - canal_info
  - cell_pond_info
  - groundwater_heat_state
  - solute_state
  - object_solute_state
  - minl_state
  - solute_chem
  - solute_ss
  - object_solute_ss
  - solute_ss_sum
  - object_solute_ss_sum
defines_vars:
  - gw_hyd_grid_mo
  - gw_hyd_grid_yr
  - gw_hyd_grid_aa
  - gw_heat_grid_mo
  - gw_heat_grid_yr
  - gw_heat_grid_aa
  - grid_type
  - gwsol_nm
purpose: ""
---

# gwflow_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `groundwater_state` |  |
| `groundwater_transit` |  |
| `groundwater_ss` |  |
| `cell_channel_info` |  |
| `satx_channel_info` |  |
| `cell_connections` |  |
| `tile_channel_info` |  |
| `cell_reservoir_info` |  |
| `cell_floodplain_info` |  |
| `canal_chan_info` |  |
| `cell_canal_info` |  |
| `cell_canal_out_info` |  |
| `cell_canal_div_info` |  |
| `canal_info` |  |
| `cell_pond_info` |  |
| `groundwater_heat_state` |  |
| `solute_state` |  |
| `object_solute_state` |  |
| `minl_state` |  |
| `solute_chem` |  |
| `solute_ss` |  |
| `object_solute_ss` |  |
| `solute_ss_sum` |  |
| `object_solute_ss_sum` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `gw_hyd_grid_mo` |  |  |
| `gw_hyd_grid_yr` |  |  |
| `gw_hyd_grid_aa` |  |  |
| `gw_heat_grid_mo` |  |  |
| `gw_heat_grid_yr` |  |  |
| `gw_heat_grid_aa` |  |  |
| `grid_type` |  |  |
| `gwsol_nm` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

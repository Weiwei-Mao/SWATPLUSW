---
type: module
tags:
  - swat/模块
  - swat/待读
file: hru_module.f90
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
  - uptake
  - sb_db
  - dbs
  - dbsc
  - topo
  - field
  - hyd
  - hydcal
  - luse
  - lumv
  - sdr
  - sno
  - nut
  - sb
  - timest
  - name
  - flocon_dtbl
  - urb_ro
  - nutc
  - pestc
  - pathc
  - saltc
  - hmetc
  - csc
  - topo
  - hyd
  - soil
  - land_use_mgt
  - soil_plant_init
  - surf_stor
  - snow
  - field
  - land_use_mgt_c
  - lum_group_c
  - cal_group
  - wet_fp
  - irr_src
  - date
purpose: ""
---

# hru_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `uptake_parameters` |  |
| `irrigation_sources` |  |
| `topography` |  |
| `field` |  |
| `hydrology` |  |
| `snow_parameters` |  |
| `subsurface_drainage_parameters` |  |
| `saturated_buffer_parameters` |  |
| `saturated_buffer` |  |
| `landuse` |  |
| `soil_plant_initialize` |  |
| `hru_databases` |  |
| `hru_databases_char` |  |
| `hydrologic_response_unit_db` |  |
| `land_use_mgt_variables` |  |
| `nutrient_parameters` |  |
| `hydrologic_response_unit` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `uptake` |  |  |
| `sb_db` |  |  |
| `dbs` |  |  |
| `dbsc` |  |  |
| `topo` |  |  |
| `field` |  |  |
| `hyd` |  |  |
| `hydcal` |  |  |
| `luse` |  |  |
| `lumv` |  |  |
| `sdr` |  |  |
| `sno` |  |  |
| `nut` |  |  |
| `sb` |  |  |
| `timest` |  |  |
| `name` |  |  |
| `flocon_dtbl` |  |  |
| `urb_ro` |  |  |
| `nutc` |  |  |
| `pestc` |  |  |
| `pathc` |  |  |
| `saltc` |  |  |
| `hmetc` |  |  |
| `csc` |  |  |
| `topo` |  |  |
| `hyd` |  |  |
| `soil` |  |  |
| `land_use_mgt` |  |  |
| `soil_plant_init` |  |  |
| `surf_stor` |  |  |
| `snow` |  |  |
| `field` |  |  |
| `land_use_mgt_c` |  |  |
| `lum_group_c` |  |  |
| `cal_group` |  |  |
| `wet_fp` |  |  |
| `irr_src` |  |  |
| `date` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

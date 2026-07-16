---
type: module
tags:
  - swat/模块
  - swat/待读
file: climate_module.f90
module_name: climate_module
defines_types:
  - weather_generator_db
  - wgn_parms
  - wind_direction_db
  - weather_daily
  - weather_codes_station
  - weather_codes_station_char
  - weather_station
  - climate_change_variables
  - climate_measured_data
  - atmospheric_deposition
  - atmospheric_deposition_control
  - atmospheric_deposition_cs
  - object_deposition_cs
  - road_salt
  - object_road_salt
defines_vars:
  - w
  - wco_c
  - wco
  - weat
  - name
  - precip_prior_day
  - wgn
  - pgage
  - tgage
  - sgage
  - hgage
  - wgage
  - petgage
  - atmodep
  - filename
  - timestep
  - salt_atmo
  - cs_atmo
purpose: ""
---

# climate_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `weather_generator_db` |  |
| `wgn_parms` |  |
| `wind_direction_db` |  |
| `weather_daily` |  |
| `weather_codes_station` |  |
| `weather_codes_station_char` |  |
| `weather_station` |  |
| `climate_change_variables` |  |
| `climate_measured_data` |  |
| `atmospheric_deposition` |  |
| `atmospheric_deposition_control` |  |
| `atmospheric_deposition_cs` |  |
| `object_deposition_cs` |  |
| `road_salt` |  |
| `object_road_salt` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `w` |  |  |
| `wco_c` |  |  |
| `wco` |  |  |
| `weat` |  |  |
| `name` |  |  |
| `precip_prior_day` |  |  |
| `wgn` |  |  |
| `pgage` |  |  |
| `tgage` |  |  |
| `sgage` |  |  |
| `hgage` |  |  |
| `wgage` |  |  |
| `petgage` |  |  |
| `atmodep` |  |  |
| `filename` |  |  |
| `timestep` |  |  |
| `salt_atmo` |  |  |
| `cs_atmo` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

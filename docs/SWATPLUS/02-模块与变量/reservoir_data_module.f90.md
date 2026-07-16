---
type: module
tags:
  - swat/模块
  - swat/待读
file: reservoir_data_module.f90
module_name: reservoir_data_module
defines_types:
  - reservoir_data_char_input
  - reservoir_data_char_input_cs
  - reservoir_data
  - reservoir_init_data_char
  - reservoir_init_data
  - reservoir_hyd_data
  - wetland_hyd_data
  - reservoir_sed_data
  - reservoir_nut_data
  - water_body_data_parameters
  - reservoir_weir_outflow
defines_vars:
  - res_datz
  - sed
  - nut
  - name
  - init
  - hyd
  - release
  - sed
  - nut
  - pst
  - weir
  - salt
  - cs
  - org_min
  - pest
  - path
  - hmet
purpose: ""
---

# reservoir_data_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `reservoir_data_char_input` |  |
| `reservoir_data_char_input_cs` |  |
| `reservoir_data` |  |
| `reservoir_init_data_char` |  |
| `reservoir_init_data` |  |
| `reservoir_hyd_data` |  |
| `wetland_hyd_data` |  |
| `reservoir_sed_data` |  |
| `reservoir_nut_data` |  |
| `water_body_data_parameters` |  |
| `reservoir_weir_outflow` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `res_datz` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `name` |  |  |
| `init` |  |  |
| `hyd` |  |  |
| `release` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `pst` |  |  |
| `weir` |  |  |
| `salt` |  |  |
| `cs` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

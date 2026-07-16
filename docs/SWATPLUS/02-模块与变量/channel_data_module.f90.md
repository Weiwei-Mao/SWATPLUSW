---
type: module
tags:
  - swat/模块
  - swat/待读
file: channel_data_module.f90
module_name: channel_data_module
defines_types:
  - routing_nut_data
  - channel_data_char_input
  - channel_init_datafiles
  - channel_init_datafiles_cs
  - channel_data
  - channel_hyd_data
  - channel_sed_data
  - channel_nut_data
  - channel_temperature_data
  - water_temperature_data
defines_vars:
  - name
  - init
  - hyd
  - sed
  - nut
  - org_min
  - pest
  - path
  - hmet
  - salt
  - cs
purpose: ""
---

# channel_data_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `routing_nut_data` |  |
| `channel_data_char_input` |  |
| `channel_init_datafiles` |  |
| `channel_init_datafiles_cs` |  |
| `channel_data` |  |
| `channel_hyd_data` |  |
| `channel_sed_data` |  |
| `channel_nut_data` |  |
| `channel_temperature_data` |  |
| `water_temperature_data` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `name` |  |  |
| `init` |  |  |
| `hyd` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |
| `salt` |  |  |
| `cs` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

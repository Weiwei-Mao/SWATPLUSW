---
type: module
tags:
  - swat/模块
  - swat/待读
file: soil_nutcarb_module.f90
module_name: soil_nutcarb_module
defines_types:
  - organic_carbon_header
  - total_carbon_header
  - organic_carbon_units
  - total_carbon_units
defines_vars:
  - orgc_hdr
  - totc_hdr
  - orgc_units
  - totc_units
  - day_mo
  - yrc
  - hru
  - str_c
  - lig_c
  - meta_c
  - man_c
  - hum_c
  - phum_c
  - mb_c
  - day
  - isd
  - soil_org_c
  - plm_com_c
  - rsd_com_c
purpose: ""
---

# soil_nutcarb_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `organic_carbon_header` |  |
| `total_carbon_header` |  |
| `organic_carbon_units` |  |
| `total_carbon_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `orgc_hdr` |  |  |
| `totc_hdr` |  |  |
| `orgc_units` |  |  |
| `totc_units` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `hru` |  |  |
| `str_c` |  |  |
| `lig_c` |  |  |
| `meta_c` |  |  |
| `man_c` |  |  |
| `hum_c` |  |  |
| `phum_c` |  |  |
| `mb_c` |  |  |
| `day` |  |  |
| `isd` |  |  |
| `soil_org_c` |  |  |
| `plm_com_c` |  |  |
| `rsd_com_c` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

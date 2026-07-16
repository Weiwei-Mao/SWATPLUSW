---
type: module
tags:
  - swat/模块
  - swat/待读
file: landuse_data_module.f90
module_name: landuse_data_module
defines_types:
  - land_use_management
  - land_use_structures
  - curvenumber_table
  - land_use_mgt_groups
  - conservation_practice_table
  - overlandflow_n_table
defines_vars:
  - lum_grp
  - name
  - cal_group
  - plant_cov
  - mgt_ops
  - cn_lu
  - cons_prac
  - urb_lu
  - urb_ro
  - ovn
  - tiledrain
  - septic
  - fstrip
  - grassww
  - bmpuser
purpose: ""
---

# landuse_data_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `land_use_management` |  |
| `land_use_structures` |  |
| `curvenumber_table` |  |
| `land_use_mgt_groups` |  |
| `conservation_practice_table` |  |
| `overlandflow_n_table` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `lum_grp` |  |  |
| `name` |  |  |
| `cal_group` |  |  |
| `plant_cov` |  |  |
| `mgt_ops` |  |  |
| `cn_lu` |  |  |
| `cons_prac` |  |  |
| `urb_lu` |  |  |
| `urb_ro` |  |  |
| `ovn` |  |  |
| `tiledrain` |  |  |
| `septic` |  |  |
| `fstrip` |  |  |
| `grassww` |  |  |
| `bmpuser` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

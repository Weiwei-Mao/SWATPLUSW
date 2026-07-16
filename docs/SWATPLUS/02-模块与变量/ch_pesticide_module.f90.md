---
type: module
tags:
  - swat/模块
  - swat/待读
file: ch_pesticide_module.f90
module_name: ch_pesticide_module
defines_types:
  - ch_pesticide_processes
  - ch_pesticide_output
  - ch_pesticide_header
defines_vars:
  - ch_pestbz
  - bchpst_d
  - bchpst_m
  - bchpst_y
  - bchpst_a
  - chpst
  - chpstz
  - chpest_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - pest
  - tot_in
  - sol_out
  - sor_out
  - react
  - metab
  - volat
  - settle
  - resus
  - difus
  - react_bot
  - metab_bot
  - bury
  - water
  - benthic
purpose: ""
---

# ch_pesticide_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `ch_pesticide_processes` |  |
| `ch_pesticide_output` |  |
| `ch_pesticide_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `ch_pestbz` |  |  |
| `bchpst_d` |  |  |
| `bchpst_m` |  |  |
| `bchpst_y` |  |  |
| `bchpst_a` |  |  |
| `chpst` |  |  |
| `chpstz` |  |  |
| `chpest_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `pest` |  |  |
| `tot_in` |  |  |
| `sol_out` |  |  |
| `sor_out` |  |  |
| `react` |  |  |
| `metab` |  |  |
| `volat` |  |  |
| `settle` |  |  |
| `resus` |  |  |
| `difus` |  |  |
| `react_bot` |  |  |
| `metab_bot` |  |  |
| `bury` |  |  |
| `water` |  |  |
| `benthic` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

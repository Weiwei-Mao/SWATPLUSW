---
type: module
tags:
  - swat/模块
  - swat/待读
file: aqu_pesticide_module.f90
module_name: aqu_pesticide_module
defines_types:
  - aqu_pesticide_processes
  - aqu_pesticide_output
  - aqu_pesticide_header
defines_vars:
  - aqu_pestbz
  - baqupst_d
  - baqupst_m
  - baqupst_y
  - baqupst_a
  - aqupst
  - aqupstz
  - aqupest_hdr
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
  - sol_perc
  - react
  - metab
  - stor_ave
  - stor_init
  - stor_final
purpose: ""
---

# aqu_pesticide_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `aqu_pesticide_processes` |  |
| `aqu_pesticide_output` |  |
| `aqu_pesticide_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `aqu_pestbz` |  |  |
| `baqupst_d` |  |  |
| `baqupst_m` |  |  |
| `baqupst_y` |  |  |
| `baqupst_a` |  |  |
| `aqupst` |  |  |
| `aqupstz` |  |  |
| `aqupest_hdr` |  |  |
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
| `sol_perc` |  |  |
| `react` |  |  |
| `metab` |  |  |
| `stor_ave` |  |  |
| `stor_init` |  |  |
| `stor_final` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

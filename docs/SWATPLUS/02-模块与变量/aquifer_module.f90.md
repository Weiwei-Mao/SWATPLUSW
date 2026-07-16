---
type: module
tags:
  - swat/模块
  - swat/待读
file: aquifer_module.f90
module_name: aquifer_module
defines_types:
  - aquifer_database
  - aquifer_data_parameters
  - aquifer_dynamic
  - aquifer_init_data_char
  - aquifer_init_data_char_cs
  - aquifer_init_data
  - aqu_header
  - aqu_header_units
defines_vars:
  - baqu_d
  - baqu_m
  - baqu_y
  - baqu_a
  - aquz
  - aqu_hdr
  - aqu_hdr_units
  - aqunm
  - aqu_ini
  - name
  - org_min
  - pest
  - path
  - hmet
  - salt
  - cs
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - flo
  - dep_wt
  - stor
  - rchrg
  - seep
  - revap
  - no3_st
  - minp
  - orgn
  - orgp
  - no3_rchg
  - no3_loss
  - no3_lat
  - no3_seep
  - flo_cha
  - flo_res
  - flo_ls
  - depwt
purpose: ""
---

# aquifer_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `aquifer_database` |  |
| `aquifer_data_parameters` |  |
| `aquifer_dynamic` |  |
| `aquifer_init_data_char` |  |
| `aquifer_init_data_char_cs` |  |
| `aquifer_init_data` |  |
| `aqu_header` |  |
| `aqu_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `baqu_d` |  |  |
| `baqu_m` |  |  |
| `baqu_y` |  |  |
| `baqu_a` |  |  |
| `aquz` |  |  |
| `aqu_hdr` |  |  |
| `aqu_hdr_units` |  |  |
| `aqunm` |  |  |
| `aqu_ini` |  |  |
| `name` |  |  |
| `org_min` |  |  |
| `pest` |  |  |
| `path` |  |  |
| `hmet` |  |  |
| `salt` |  |  |
| `cs` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `flo` |  |  |
| `dep_wt` |  |  |
| `stor` |  |  |
| `rchrg` |  |  |
| `seep` |  |  |
| `revap` |  |  |
| `no3_st` |  |  |
| `minp` |  |  |
| `orgn` |  |  |
| `orgp` |  |  |
| `no3_rchg` |  |  |
| `no3_loss` |  |  |
| `no3_lat` |  |  |
| `no3_seep` |  |  |
| `flo_cha` |  |  |
| `flo_res` |  |  |
| `flo_ls` |  |  |
| `depwt` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

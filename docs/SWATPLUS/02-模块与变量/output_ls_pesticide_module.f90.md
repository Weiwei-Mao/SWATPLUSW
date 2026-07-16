---
type: module
tags:
  - swat/模块
  - swat/待读
file: output_ls_pesticide_module.f90
module_name: output_ls_pesticide_module
defines_types:
  - pesticide_balance
  - object_pesticide_balance
  - output_pestbal_header
defines_vars:
  - pestbz
  - bpestb_d
  - bpestb_m
  - bpestb_y
  - bpestb_a
  - pestb_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - pest
  - on_plant
  - soil
  - sed
  - surq
  - latq
  - tileq
  - perc
  - apply_s
  - apply_f
  - decay_s
  - decay_f
  - wash
  - metab_s
  - metab_f
  - uptake
  - in_plant
purpose: ""
---

# output_ls_pesticide_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `pesticide_balance` |  |
| `object_pesticide_balance` |  |
| `output_pestbal_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `pestbz` |  |  |
| `bpestb_d` |  |  |
| `bpestb_m` |  |  |
| `bpestb_y` |  |  |
| `bpestb_a` |  |  |
| `pestb_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `pest` |  |  |
| `on_plant` |  |  |
| `soil` |  |  |
| `sed` |  |  |
| `surq` |  |  |
| `latq` |  |  |
| `tileq` |  |  |
| `perc` |  |  |
| `apply_s` |  |  |
| `apply_f` |  |  |
| `decay_s` |  |  |
| `decay_f` |  |  |
| `wash` |  |  |
| `metab_s` |  |  |
| `metab_f` |  |  |
| `uptake` |  |  |
| `in_plant` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

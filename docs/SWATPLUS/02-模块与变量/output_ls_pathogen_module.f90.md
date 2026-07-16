---
type: module
tags:
  - swat/模块
  - swat/待读
file: output_ls_pathogen_module.f90
module_name: output_ls_pathogen_module
defines_types:
  - pathogen_balance
  - object_pathogen_balance
  - output_pathbal_header
defines_vars:
  - pathbz
  - bpathb_d
  - bpathb_m
  - bpathb_y
  - bpathb_a
  - pathb_hdr
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - plant
  - soil
  - sed
  - surq
  - latq
  - perc
  - apply
  - decay
purpose: ""
---

# output_ls_pathogen_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `pathogen_balance` |  |
| `object_pathogen_balance` |  |
| `output_pathbal_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `pathbz` |  |  |
| `bpathb_d` |  |  |
| `bpathb_m` |  |  |
| `bpathb_y` |  |  |
| `bpathb_a` |  |  |
| `pathb_hdr` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `plant` |  |  |
| `soil` |  |  |
| `sed` |  |  |
| `surq` |  |  |
| `latq` |  |  |
| `perc` |  |  |
| `apply` |  |  |
| `decay` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

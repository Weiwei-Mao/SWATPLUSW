---
type: module
tags:
  - swat/模块
  - swat/待读
file: erosion_module.f90
module_name: erosion_module
defines_types:
  - erosion_output_variables
  - erosion_output
  - erosion_output_header
  - erosion_header_units
defines_vars:
  - ero_d
  - ero_ave
  - ero_hdr
  - ero_hdr_units
  - ero_1
  - ero_2
  - ero_3
  - hru
  - neve
  - sedyld
  - precip
  - peak
  - k
  - s
  - l
  - ls
  - p
  - c
  - rsd_m
  - grcov_frac
  - rsd_covfact
  - bio_covfact
purpose: ""
---

# erosion_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `erosion_output_variables` |  |
| `erosion_output` |  |
| `erosion_output_header` |  |
| `erosion_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `ero_d` |  |  |
| `ero_ave` |  |  |
| `ero_hdr` |  |  |
| `ero_hdr_units` |  |  |
| `ero_1` |  |  |
| `ero_2` |  |  |
| `ero_3` |  |  |
| `hru` |  |  |
| `neve` |  |  |
| `sedyld` |  |  |
| `precip` |  |  |
| `peak` |  |  |
| `k` |  |  |
| `s` |  |  |
| `l` |  |  |
| `ls` |  |  |
| `p` |  |  |
| `c` |  |  |
| `rsd_m` |  |  |
| `grcov_frac` |  |  |
| `rsd_covfact` |  |  |
| `bio_covfact` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/模块
  - swat/待读
file: reservoir_module.f90
module_name: reservoir_module
defines_types:
  - reservoir
  - wetland
  - reservoir_pest_processes
  - res_header
  - res_header1
  - reservoir_hdr
  - res_headerbsn
  - res_header_unit
  - res_header_unit1
  - res_header_unit2
  - res_header_unitbsn
defines_vars:
  - res_hdr
  - res_hdr1
  - res_hdr2
  - res_hdrbsn
  - res_hdr_unt
  - res_hdr_unt1
  - res_hdr_untbsn
  - name
  - rel_tbl
  - day
  - mo
  - day_mo
  - yrc
  - j
  - id
  - flo
  - sed
  - orgn
  - sedp
  - no3
  - solp
  - chla
  - nh3
  - no2
  - cbod
  - dox
  - san
  - sil
  - cla
  - sag
  - lag
  - grv
  - temp
  - area_ha
  - evap
  - seep
  - sed_setl
  - seci
  - solp_loss
  - sedp_loss
  - orgn_loss
  - no3_loss
  - nh3_loss
  - no2_loss
purpose: ""
---

# reservoir_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `reservoir` |  |
| `wetland` |  |
| `reservoir_pest_processes` |  |
| `res_header` |  |
| `res_header1` |  |
| `reservoir_hdr` |  |
| `res_headerbsn` |  |
| `res_header_unit` |  |
| `res_header_unit1` |  |
| `res_header_unit2` |  |
| `res_header_unitbsn` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `res_hdr` |  |  |
| `res_hdr1` |  |  |
| `res_hdr2` |  |  |
| `res_hdrbsn` |  |  |
| `res_hdr_unt` |  |  |
| `res_hdr_unt1` |  |  |
| `res_hdr_untbsn` |  |  |
| `name` |  |  |
| `rel_tbl` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `j` |  |  |
| `id` |  |  |
| `flo` |  |  |
| `sed` |  |  |
| `orgn` |  |  |
| `sedp` |  |  |
| `no3` |  |  |
| `solp` |  |  |
| `chla` |  |  |
| `nh3` |  |  |
| `no2` |  |  |
| `cbod` |  |  |
| `dox` |  |  |
| `san` |  |  |
| `sil` |  |  |
| `cla` |  |  |
| `sag` |  |  |
| `lag` |  |  |
| `grv` |  |  |
| `temp` |  |  |
| `area_ha` |  |  |
| `evap` |  |  |
| `seep` |  |  |
| `sed_setl` |  |  |
| `seci` |  |  |
| `solp_loss` |  |  |
| `sedp_loss` |  |  |

*（仅显示前 40 个，共 44 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

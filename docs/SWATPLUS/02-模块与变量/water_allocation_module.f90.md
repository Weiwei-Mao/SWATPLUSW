---
type: module
tags:
  - swat/模块
  - swat/待读
file: water_allocation_module.f90
module_name: water_allocation_module
defines_types:
  - transfer_source_objects
  - transfer_receiving_objects
  - outside_basin_objects
  - water_transfer_objects
  - source_output
  - water_allocation
  - water_treatment_use_data
  - outside_basin_source
  - outside_basin_receive
  - aquifer_loss
  - water_transfer_data
  - water_canal_data
  - transfer_object_output
  - water_allocation_output
  - wallo_header
  - wallo_header_units
defines_vars:
  - rcv
  - walloz
  - tot
  - wallo_hdr
  - wallo_hdr_units
  - typ
  - conv_typ
  - dtbl_lim
  - comp
  - trn_typ
  - trn_typ_name
  - right
  - dtbl_src
  - name
  - rule_typ
  - org_min
  - pests
  - paths
  - hmets
  - salts
  - constit
  - descrip
  - filename
  - init
  - w_sta
  - dtbl
  - day
  - mo
  - day_mo
  - yrc
  - itrn
  - trn_num
  - rcv_typ
  - rcv_num
  - src1_obj
  - src1_typ
  - src1_num
  - trn1
  - s1out
  - s1un
  - src2_typ
  - src2_num
  - trn2
  - s2out
  - s2un
  - src3_typ
  - src3_num
  - trn3
  - s3out
  - s3un
purpose: ""
---

# water_allocation_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `transfer_source_objects` |  |
| `transfer_receiving_objects` |  |
| `outside_basin_objects` |  |
| `water_transfer_objects` |  |
| `source_output` |  |
| `water_allocation` |  |
| `water_treatment_use_data` |  |
| `outside_basin_source` |  |
| `outside_basin_receive` |  |
| `aquifer_loss` |  |
| `water_transfer_data` |  |
| `water_canal_data` |  |
| `transfer_object_output` |  |
| `water_allocation_output` |  |
| `wallo_header` |  |
| `wallo_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `rcv` |  |  |
| `walloz` |  |  |
| `tot` |  |  |
| `wallo_hdr` |  |  |
| `wallo_hdr_units` |  |  |
| `typ` |  |  |
| `conv_typ` |  |  |
| `dtbl_lim` |  |  |
| `comp` |  |  |
| `trn_typ` |  |  |
| `trn_typ_name` |  |  |
| `right` |  |  |
| `dtbl_src` |  |  |
| `name` |  |  |
| `rule_typ` |  |  |
| `org_min` |  |  |
| `pests` |  |  |
| `paths` |  |  |
| `hmets` |  |  |
| `salts` |  |  |
| `constit` |  |  |
| `descrip` |  |  |
| `filename` |  |  |
| `init` |  |  |
| `w_sta` |  |  |
| `dtbl` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `itrn` |  |  |
| `trn_num` |  |  |
| `rcv_typ` |  |  |
| `rcv_num` |  |  |
| `src1_obj` |  |  |
| `src1_typ` |  |  |
| `src1_num` |  |  |
| `trn1` |  |  |
| `s1out` |  |  |
| `s1un` |  |  |

*（仅显示前 40 个，共 50 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

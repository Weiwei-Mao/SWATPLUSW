---
type: module
tags:
  - swat/模块
  - swat/待读
file: manure_allocation_module.f90
module_name: manure_allocation_module
defines_types:
  - manure_demand_amount
  - source_manure_output
  - manure_source_objects
  - manure_demand_objects
  - manure_allocation
  - mallo_header
  - mallo_header_units
defines_vars:
  - manure_amtz
  - malloz
  - bal_d
  - bal_m
  - bal_y
  - bal_a
  - manure_amt
  - tot
  - mallo_hdr
  - mallo_hdr_units
  - mois_typ
  - manure_typ
  - ob_typ
  - dtbl
  - right
  - name
  - rule_typ
  - day
  - mo
  - day_mo
  - yrc
  - itrn
  - trn_typ
  - trn_num
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

# manure_allocation_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `manure_demand_amount` |  |
| `source_manure_output` |  |
| `manure_source_objects` |  |
| `manure_demand_objects` |  |
| `manure_allocation` |  |
| `mallo_header` |  |
| `mallo_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `manure_amtz` |  |  |
| `malloz` |  |  |
| `bal_d` |  |  |
| `bal_m` |  |  |
| `bal_y` |  |  |
| `bal_a` |  |  |
| `manure_amt` |  |  |
| `tot` |  |  |
| `mallo_hdr` |  |  |
| `mallo_hdr_units` |  |  |
| `mois_typ` |  |  |
| `manure_typ` |  |  |
| `ob_typ` |  |  |
| `dtbl` |  |  |
| `right` |  |  |
| `name` |  |  |
| `rule_typ` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `itrn` |  |  |
| `trn_typ` |  |  |
| `trn_num` |  |  |
| `src1_obj` |  |  |
| `src1_typ` |  |  |
| `src1_num` |  |  |
| `trn1` |  |  |
| `s1out` |  |  |
| `s1un` |  |  |
| `src2_typ` |  |  |
| `src2_num` |  |  |
| `trn2` |  |  |
| `s2out` |  |  |
| `s2un` |  |  |
| `src3_typ` |  |  |
| `src3_num` |  |  |
| `trn3` |  |  |
| `s3out` |  |  |
| `s3un` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/模块
  - swat/待读
file: channel_module.f90
module_name: channel_module
defines_types:
  - channel
  - ch_output
  - regional_output_channel
  - ch_header
  - ch_header_units
defines_vars:
  - bch_d
  - bch_m
  - bch_y
  - bch_a
  - chz
  - ch_hdr
  - ch_hdr_units
  - sed_ch
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - flo_in
  - flo_out
  - evap
  - tloss
  - sed_in
  - sed_out
  - sed_conc
  - orgn_in
  - orgn_out
  - orgp_in
  - orgp_out
  - no3_in
  - no3_out
  - nh4_in
  - nh4_out
  - no2_in
  - no2_out
  - solp_in
  - solp_out
  - chla_in
  - chla_out
  - cbod_in
  - cbod_out
  - dis_in
  - dis_out
  - solpst_in
  - solpst_out
  - sorbpst_in
  - sorbpst_out
  - react
  - volat
  - setlpst
  - resuspst
  - difus
  - reactb
  - bury
  - sedpest
  - bacp
  - baclp
  - met1
  - met2
  - met3
  - sand_in
  - sand_out
  - silt_in
  - silt_out
  - clay_in
  - clay_out
  - smag_in
  - smag_out
  - lag_in
  - lag_out
  - grvl_in
  - grvl_out
  - bnk_ero
  - ch_deg
  - ch_dep
  - fp_dep
  - tot_ssed
purpose: ""
---

# channel_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `channel` |  |
| `ch_output` |  |
| `regional_output_channel` |  |
| `ch_header` |  |
| `ch_header_units` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `bch_d` |  |  |
| `bch_m` |  |  |
| `bch_y` |  |  |
| `bch_a` |  |  |
| `chz` |  |  |
| `ch_hdr` |  |  |
| `ch_hdr_units` |  |  |
| `sed_ch` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `flo_in` |  |  |
| `flo_out` |  |  |
| `evap` |  |  |
| `tloss` |  |  |
| `sed_in` |  |  |
| `sed_out` |  |  |
| `sed_conc` |  |  |
| `orgn_in` |  |  |
| `orgn_out` |  |  |
| `orgp_in` |  |  |
| `orgp_out` |  |  |
| `no3_in` |  |  |
| `no3_out` |  |  |
| `nh4_in` |  |  |
| `nh4_out` |  |  |
| `no2_in` |  |  |
| `no2_out` |  |  |
| `solp_in` |  |  |
| `solp_out` |  |  |
| `chla_in` |  |  |
| `chla_out` |  |  |
| `cbod_in` |  |  |
| `cbod_out` |  |  |
| `dis_in` |  |  |
| `dis_out` |  |  |

*（仅显示前 40 个，共 74 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

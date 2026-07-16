---
type: module
tags:
  - swat/模块
  - swat/待读
file: sd_channel_module.f90
module_name: sd_channel_module
defines_types:
  - swatdeg_hydsed_data
  - swatdeg_sednut_data
  - channel_sediment_budget_output
  - channel_morphology_output
  - gully_data
  - swatdeg_init_datafiles
  - swatdeg_datafiles
  - floodplain_parameters
  - muskingum_parameters
  - swatdeg_channel_dynamic
  - channel_rating_curve_parameters
  - channel_rating_curve
  - sd_ch_output
  - sdch_header
  - sdch_header_units
  - sdch_bud
  - sdch_bud_units
  - sdch_header_sub
  - sdch_header_units_sub
  - sd_chd_header
defines_vars:
  - ch_sed_budz
  - bch_sed_bud_d
  - bch_sed_bud_m
  - bch_sed_bud_y
  - bch_sed_bud_a
  - msk
  - fp
  - rcurv
  - rcz
  - in1
  - in2
  - out1
  - out2
  - bchsd_d
  - bchsd_m
  - bchsd_y
  - bchsd_a
  - chsdz
  - sdch_hdr
  - sdch_hdr_units
  - sdch_bud_hdr
  - sdch_bud_hdr_units
  - sdch_hdr_subday
  - sdch_hdr_units_sub
  - sd_chd_hdr
  - name
  - order
  - initc
  - hydc
  - sedc
  - nutc
  - region
  - overbank
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - flo_in
  - aqu_in
  - flo
  - peakr
  - sed_in
  - sed_out
  - washld
  - bedld
  - dep
  - deg_btm
  - deg_bank
  - hc_sed
  - width
  - depth
  - slope
  - deg_btm_m
  - deg_bank_m
  - hc_len
  - flo_in_mm
  - aqu_in_mm
  - flo_mm
  - sed_stor
  - n_tot
  - p_tot
  - dep_bf
  - velav_bf
  - in_sed
  - out_sed
  - fp_dep
  - ch_dep
  - bank_ero
  - bed_ero
  - in_no3
  - in_orgn
  - out_no3
  - out_orgn
  - fp_no3
  - bank_no3
  - bed_no3
  - fp_orgn
  - ch_orgn
  - bank_orgn
  - bed_orgn
  - in_solp
  - in_orgp
  - out_solp
  - out_orgp
  - fp_solp
  - bank_solp
  - bed_solp
  - fp_orgp
  - ch_orgp
  - bank_orgp
  - bed_orgp
  - no3_orgn
  - solp_orgp
  - no3_orgp
  - ii
  - hyd_flo
  - chw
  - chd
  - chs
  - chl
  - chn
  - chk
  - cherod
  - cov
  - sinu
  - chseq
  - d50
  - ch_clay
  - carbon
  - ch_bd
  - chss
  - bankfull_flo
  - fps
  - fpn
  - n_conc
  - p_conc
  - p_bio
purpose: ""
---

# sd_channel_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `swatdeg_hydsed_data` |  |
| `swatdeg_sednut_data` |  |
| `channel_sediment_budget_output` |  |
| `channel_morphology_output` |  |
| `gully_data` |  |
| `swatdeg_init_datafiles` |  |
| `swatdeg_datafiles` |  |
| `floodplain_parameters` |  |
| `muskingum_parameters` |  |
| `swatdeg_channel_dynamic` |  |
| `channel_rating_curve_parameters` |  |
| `channel_rating_curve` |  |
| `sd_ch_output` |  |
| `sdch_header` |  |
| `sdch_header_units` |  |
| `sdch_bud` |  |
| `sdch_bud_units` |  |
| `sdch_header_sub` |  |
| `sdch_header_units_sub` |  |
| `sd_chd_header` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `ch_sed_budz` |  |  |
| `bch_sed_bud_d` |  |  |
| `bch_sed_bud_m` |  |  |
| `bch_sed_bud_y` |  |  |
| `bch_sed_bud_a` |  |  |
| `msk` |  |  |
| `fp` |  |  |
| `rcurv` |  |  |
| `rcz` |  |  |
| `in1` |  |  |
| `in2` |  |  |
| `out1` |  |  |
| `out2` |  |  |
| `bchsd_d` |  |  |
| `bchsd_m` |  |  |
| `bchsd_y` |  |  |
| `bchsd_a` |  |  |
| `chsdz` |  |  |
| `sdch_hdr` |  |  |
| `sdch_hdr_units` |  |  |
| `sdch_bud_hdr` |  |  |
| `sdch_bud_hdr_units` |  |  |
| `sdch_hdr_subday` |  |  |
| `sdch_hdr_units_sub` |  |  |
| `sd_chd_hdr` |  |  |
| `name` |  |  |
| `order` |  |  |
| `initc` |  |  |
| `hydc` |  |  |
| `sedc` |  |  |
| `nutc` |  |  |
| `region` |  |  |
| `overbank` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `flo_in` |  |  |

*（仅显示前 40 个，共 119 个）*

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: module
tags:
  - swat/模块
  - swat/待读
file: calibration_data_module.f90
module_name: calibration_data_module
defines_types:
  - calibration_parameters
  - calibration_conditions
  - update_parameters
  - update_conditional
  - soft_calibration_codes
  - soft_calib_parms
  - soft_calib_ls_adjust
  - soft_calib_ls_processes
  - ls_calib_regions
  - soft_data_calib_landscape
  - pl_parms_cal
  - pl_parm_region
  - cataloging_units
  - landscape_units
  - landscape_region_elements
  - landscape_elements
  - soft_calib_pl_adjust
  - soft_calib_pl_processes
  - pl_calib_regions
  - soft_data_calib_plant
  - soft_calib_chan_adjust
  - soft_calib_chan_processes
  - chan_calib_regions
  - soft_data_calib_channel
defines_vars:
  - chg
  - cal_codes
  - lscal_z
  - meas
  - sim
  - aa
  - prev
  - prm
  - prm_prev
  - prm_lim
  - pcur
  - phi
  - plo
  - scur
  - shi
  - slo
  - plcal_z
  - prm_uplim
  - prm_lowlim
  - chcal_z
  - name
  - ob_typ
  - units
  - var
  - alt
  - targc
  - chg_typ
  - typ
  - dtbl
  - hyd_hru
  - hyd_hrul
  - plt
  - sed
  - nut
  - chsed
  - chnut
  - res
  - cal_soft
  - cal_hard
  - obtyp
purpose: ""
---

# calibration_data_module

> [!info] 模块
> 定义派生类型与模块级变量（关键变量的归宿）。

## 定义的类型
| 类型 | 说明 |
|---|---|
| `calibration_parameters` |  |
| `calibration_conditions` |  |
| `update_parameters` |  |
| `update_conditional` |  |
| `soft_calibration_codes` |  |
| `soft_calib_parms` |  |
| `soft_calib_ls_adjust` |  |
| `soft_calib_ls_processes` |  |
| `ls_calib_regions` |  |
| `soft_data_calib_landscape` |  |
| `pl_parms_cal` |  |
| `pl_parm_region` |  |
| `cataloging_units` |  |
| `landscape_units` |  |
| `landscape_region_elements` |  |
| `landscape_elements` |  |
| `soft_calib_pl_adjust` |  |
| `soft_calib_pl_processes` |  |
| `pl_calib_regions` |  |
| `soft_data_calib_plant` |  |
| `soft_calib_chan_adjust` |  |
| `soft_calib_chan_processes` |  |
| `chan_calib_regions` |  |
| `soft_data_calib_channel` |  |

## 模块级变量（关键变量）
| 变量 | 类型 | 含义 |
|---|---|---|
| `chg` |  |  |
| `cal_codes` |  |  |
| `lscal_z` |  |  |
| `meas` |  |  |
| `sim` |  |  |
| `aa` |  |  |
| `prev` |  |  |
| `prm` |  |  |
| `prm_prev` |  |  |
| `prm_lim` |  |  |
| `pcur` |  |  |
| `phi` |  |  |
| `plo` |  |  |
| `scur` |  |  |
| `shi` |  |  |
| `slo` |  |  |
| `plcal_z` |  |  |
| `prm_uplim` |  |  |
| `prm_lowlim` |  |  |
| `chcal_z` |  |  |
| `name` |  |  |
| `ob_typ` |  |  |
| `units` |  |  |
| `var` |  |  |
| `alt` |  |  |
| `targc` |  |  |
| `chg_typ` |  |  |
| `typ` |  |  |
| `dtbl` |  |  |
| `hyd_hru` |  |  |
| `hyd_hrul` |  |  |
| `plt` |  |  |
| `sed` |  |  |
| `nut` |  |  |
| `chsed` |  |  |
| `chnut` |  |  |
| `res` |  |  |
| `cal_soft` |  |  |
| `cal_hard` |  |  |
| `obtyp` |  |  |

## 被以下源码使用（dataview 实时反查）

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此记录类型/变量的含义、单位、取值。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

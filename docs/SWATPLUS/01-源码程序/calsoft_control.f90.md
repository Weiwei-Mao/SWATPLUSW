---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: calsoft_control.f90
subroutine: calsoft_control
module:
  - sd_channel_module
  - hru_lte_module
  - maximum_data_module
  - calibration_data_module
  - time_module
  - basin_module
  - hru_module
  - hydrograph_module
  - soil_module
calls:
  - calsoft_hyd
  - calsoft_hyd_bfr
  - caltsoft_hyd
  - calsoft_plant
  - calsoft_sed
  - pl_write_parms_cal
reads: []
writes: []
purpose: ""
---

# calsoft_control

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`calsoft_control.f90`
- **使用模块**：[[sd_channel_module.f90]]、[[hru_lte_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]、[[hru_module.f90]]、[[hydrograph_module.f90]]、[[soil_module.f90]]
- **调用子程序**：6 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[calsoft_hyd.f90]]
- [[calsoft_hyd_bfr.f90]]
- [[caltsoft_hyd.f90]]
- [[calsoft_plant.f90]]
- [[calsoft_sed.f90]]
- [[pl_write_parms_cal.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

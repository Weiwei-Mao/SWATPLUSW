---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: calsoft_sed.f90
subroutine: calsoft_sed
module:
  - hru_module
  - soil_module
  - plant_module
  - hydrograph_module
  - ru_module
  - aquifer_module
  - hru_lte_module
  - sd_channel_module
  - basin_module
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - reservoir_module
  - organic_mineral_mass_module
calls:
  - re_initialize
  - time_control
reads: []
writes: []
purpose: ""
---

# calsoft_sed

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`calsoft_sed.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[hydrograph_module.f90]]、[[ru_module.f90]]、[[aquifer_module.f90]]、[[hru_lte_module.f90]]、[[sd_channel_module.f90]]、[[basin_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[conditional_module.f90]]、[[reservoir_module.f90]]、[[organic_mineral_mass_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[re_initialize.f90]]
- [[time_control.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

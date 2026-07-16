---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: calsoft_plant.f90
subroutine: calsoft_plant
module:
  - hru_module
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
  - soil_module
  - plant_module
  - output_landscape_module
calls:
  - calsoft_plant_zero
  - time_control
  - re_initialize
reads: []
writes: []
purpose: ""
---

# calsoft_plant

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`calsoft_plant.f90`
- **使用模块**：[[hru_module.f90]]、[[hydrograph_module.f90]]、[[ru_module.f90]]、[[aquifer_module.f90]]、[[hru_lte_module.f90]]、[[sd_channel_module.f90]]、[[basin_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[conditional_module.f90]]、[[reservoir_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[output_landscape_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[calsoft_plant_zero.f90]]
- [[time_control.f90]]
- [[re_initialize.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

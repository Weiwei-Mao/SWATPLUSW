---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cal_parm_select.f90
subroutine: cal_parm_select
module:
  - basin_module
  - channel_data_module
  - reservoir_data_module
  - hru_module
  - soil_module
  - channel_module
  - conditional_module
  - sd_channel_module
  - reservoir_module
  - aquifer_module
  - hru_lte_module
  - organic_mineral_mass_module
  - hydrograph_module
  - pesticide_data_module
  - plant_module
  - plant_data_module
  - gwflow_module
  - carbon_module
  - tillage_data_module
calls:
  - curno
  - soil_awc_init
  - soil_text_init
reads: []
writes: []
purpose: "this subroutine finds the current parameter value based on；user defined change"
---

# cal_parm_select

> [!info] 概要
> this subroutine finds the current parameter value based on；user defined change

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cal_parm_select.f90`
- **使用模块**：[[basin_module.f90]]、[[channel_data_module.f90]]、[[reservoir_data_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[channel_module.f90]]、[[conditional_module.f90]]、[[sd_channel_module.f90]]、[[reservoir_module.f90]]、[[aquifer_module.f90]]、[[hru_lte_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hydrograph_module.f90]]、[[pesticide_data_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[gwflow_module.f90]]、[[carbon_module.f90]]、[[tillage_data_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[curno.f90]]
- [[soil_awc_init.f90]]
- [[soil_text_init.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

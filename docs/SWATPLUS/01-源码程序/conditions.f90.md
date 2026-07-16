---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: conditions.f90
subroutine: conditions
module:
  - conditional_module
  - climate_module
  - time_module
  - hru_module
  - soil_module
  - plant_module
  - reservoir_module
  - reservoir_data_module
  - sd_channel_module
  - hydrograph_module
  - output_landscape_module
  - aquifer_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - water_allocation_module
calls:
  - cond_real
  - cond_integer
reads: []
writes: []
purpose: ""
---

# conditions

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`conditions.f90`
- **使用模块**：[[conditional_module.f90]]、[[climate_module.f90]]、[[time_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[reservoir_module.f90]]、[[reservoir_data_module.f90]]、[[sd_channel_module.f90]]、[[hydrograph_module.f90]]、[[output_landscape_module.f90]]、[[aquifer_module.f90]]、[[organic_mineral_mass_module.f90]]、[[mgt_operations_module.f90]]、[[water_allocation_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cond_real.f90]]
- [[cond_integer.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wallo_control.f90
subroutine: wallo_control
module:
  - water_allocation_module
  - hydrograph_module
  - hru_module
  - basin_module
  - time_module
  - plant_module
  - soil_module
  - reservoir_module
  - sd_channel_module
  - organic_mineral_mass_module
  - constituent_mass_module
calls:
  - wallo_demand
  - wallo_withdraw
  - wallo_transfer
  - salt_irrig
  - cs_irrig
  - res_control
  - wallo_treatment
  - wallo_use
  - wallo_canal
reads: []
writes: []
purpose: ""
---

# wallo_control

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wallo_control.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[basin_module.f90]]、[[time_module.f90]]、[[plant_module.f90]]、[[soil_module.f90]]、[[reservoir_module.f90]]、[[sd_channel_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：9 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[wallo_demand.f90]]
- [[wallo_withdraw.f90]]
- [[wallo_transfer.f90]]
- [[salt_irrig.f90]]
- [[cs_irrig.f90]]
- [[res_control.f90]]
- [[wallo_treatment.f90]]
- [[wallo_use.f90]]
- [[wallo_canal.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

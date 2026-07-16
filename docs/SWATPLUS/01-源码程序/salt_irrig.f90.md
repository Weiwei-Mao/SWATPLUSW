---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: salt_irrig.f90
subroutine: salt_irrig
module:
  - water_allocation_module
  - water_body_module
  - aquifer_module
  - reservoir_data_module
  - hydrograph_module
  - hru_module
  - salt_module
  - salt_aquifer
  - ch_salt_module
  - res_salt_module
  - basin_module
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine adds salt mass from irrigation water into the soil profile, and removes salt mass；from the source object"
---

# salt_irrig

> [!info] 概要
> this subroutine adds salt mass from irrigation water into the soil profile, and removes salt mass；from the source object

## 基本信息
- **类型**：`subroutine`
- **源文件**：`salt_irrig.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[water_body_module.f90]]、[[aquifer_module.f90]]、[[reservoir_data_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[salt_module.f90]]、[[salt_aquifer.f90]]、[[ch_salt_module.f90]]、[[res_salt_module.f90]]、[[basin_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

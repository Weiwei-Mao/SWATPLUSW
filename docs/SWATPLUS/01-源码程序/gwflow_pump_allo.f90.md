---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_pump_allo.f90
subroutine: gwflow_pump_allo
module:
  - gwflow_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
  - soil_module
  - constituent_mass_module
  - res_salt_module
  - res_cs_module
  - salt_module
  - cs_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is extracted；from gwflow grid cells；(pumping volume are used in gwflow_simulate, in groundwater balance equations)"
---

# gwflow_pump_allo

> [!info] 概要
> this subroutine determines the volume of groundwater that is extracted；from gwflow grid cells；(pumping volume are used in gwflow_simulate, in groundwater balance equations)

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_pump_allo.f90`
- **使用模块**：[[gwflow_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hru_module.f90]]、[[hydrograph_module.f90]]、[[soil_module.f90]]、[[constituent_mass_module.f90]]、[[res_salt_module.f90]]、[[res_cs_module.f90]]、[[salt_module.f90]]、[[cs_module.f90]]
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

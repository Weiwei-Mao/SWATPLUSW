---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: nut_solp.f90
subroutine: nut_solp
module:
  - basin_module
  - organic_mineral_mass_module
  - gwflow_module
  - hru_module
  - soil_module
  - output_landscape_module
  - hydrograph_module
  - utils
calls: []
reads: []
writes: []
purpose: "this subroutine calculates the amount of phosphorus lost from the soil；profile in runoff and the movement of soluble phosphorus from the first；to the second layer via percolation"
---

# nut_solp

> [!info] 概要
> this subroutine calculates the amount of phosphorus lost from the soil；profile in runoff and the movement of soluble phosphorus from the first；to the second layer via percolation

## 基本信息
- **类型**：`subroutine`
- **源文件**：`nut_solp.f90`
- **使用模块**：[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[gwflow_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[output_landscape_module.f90]]、[[hydrograph_module.f90]]、[[utils.f90]]
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

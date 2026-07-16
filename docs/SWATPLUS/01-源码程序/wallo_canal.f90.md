---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wallo_canal.f90
subroutine: wallo_canal
module:
  - water_allocation_module
  - hydrograph_module
  - constituent_mass_module
  - basin_module
  - aquifer_module
  - gwflow_module
calls: []
reads: []
writes: []
purpose: "Routes water through a wallo canal: computes outflow, applies loss,；and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer)."
---

# wallo_canal

> [!info] 概要
> Routes water through a wallo canal: computes outflow, applies loss,；and distributes canal seepage to aquifer (gwflow grid cells or 1-D aquifer).

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wallo_canal.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[basin_module.f90]]、[[aquifer_module.f90]]、[[gwflow_module.f90]]
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

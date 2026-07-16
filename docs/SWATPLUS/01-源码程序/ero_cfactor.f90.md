---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ero_cfactor.f90
subroutine: ero_cfactor
module:
  - basin_module
  - hru_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - time_module
  - erosion_module
  - utils
calls: []
reads: []
writes: []
purpose: "this subroutine predicts daily soil loss caused by water erosion；using the modified universal soil loss equation"
---

# ero_cfactor

> [!info] 概要
> this subroutine predicts daily soil loss caused by water erosion；using the modified universal soil loss equation

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ero_cfactor.f90`
- **使用模块**：[[basin_module.f90]]、[[hru_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[organic_mineral_mass_module.f90]]、[[time_module.f90]]、[[erosion_module.f90]]、[[utils.f90]]
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

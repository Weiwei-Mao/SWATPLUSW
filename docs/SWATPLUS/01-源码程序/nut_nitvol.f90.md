---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: nut_nitvol.f90
subroutine: nut_nitvol
module:
  - septic_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this subroutine estimates daily mineralization (NH3 to NO3)；and volatilization of NH3"
---

# nut_nitvol

> [!info] 概要
> this subroutine estimates daily mineralization (NH3 to NO3)；and volatilization of NH3

## 基本信息
- **类型**：`subroutine`
- **源文件**：`nut_nitvol.f90`
- **使用模块**：[[septic_data_module.f90]]、[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]
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

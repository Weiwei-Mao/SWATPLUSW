---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: mallo_control.f90
subroutine: mallo_control
module:
  - manure_allocation_module
  - hru_module
  - basin_module
  - time_module
  - plant_module
  - soil_module
  - organic_mineral_mass_module
  - conditional_module
calls:
  - conditions
  - actions
  - pl_fert
reads: []
writes: []
purpose: ""
---

# mallo_control

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`mallo_control.f90`
- **使用模块**：[[manure_allocation_module.f90]]、[[hru_module.f90]]、[[basin_module.f90]]、[[time_module.f90]]、[[plant_module.f90]]、[[soil_module.f90]]、[[organic_mineral_mass_module.f90]]、[[conditional_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[conditions.f90]]
- [[actions.f90]]
- [[pl_fert.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

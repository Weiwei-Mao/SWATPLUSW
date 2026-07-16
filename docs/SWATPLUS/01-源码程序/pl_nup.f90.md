---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_nup.f90
subroutine: pl_nup
module:
  - plant_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - output_landscape_module
calls:
  - pl_nfix
  - nuts
reads: []
writes: []
purpose: "This subroutine calculates plant nitrogen uptake"
---

# pl_nup

> [!info] 概要
> This subroutine calculates plant nitrogen uptake

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_nup.f90`
- **使用模块**：[[plant_data_module.f90]]、[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[output_landscape_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[pl_nfix.f90]]
- [[nuts.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

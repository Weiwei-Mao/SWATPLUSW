---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cbn_zhang2.f90
subroutine: cbn_zhang2
module:
  - hru_module
  - soil_module
  - basin_module
  - organic_mineral_mass_module
  - carbon_module
  - output_landscape_module
  - tillage_data_module
calls:
  - nut_np_flow
reads: []
writes: []
purpose: ""
---

# cbn_zhang2

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cbn_zhang2.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[carbon_module.f90]]、[[output_landscape_module.f90]]、[[tillage_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[nut_np_flow.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

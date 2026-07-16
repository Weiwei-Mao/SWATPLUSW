---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_waterup.f90
subroutine: pl_waterup
module:
  - plant_data_module
  - basin_module
  - hru_module
  - soil_module
  - plant_module
  - urban_data_module
  - constituent_mass_module
  - salt_data_module
calls:
  - salt_chem_soil_single
reads: []
writes: []
purpose: "this subroutine distributes potential plant evaporation through；the root zone and calculates actual plant water use based on soil；water availability. Also estimates water stress factor."
---

# pl_waterup

> [!info] 概要
> this subroutine distributes potential plant evaporation through；the root zone and calculates actual plant water use based on soil；water availability. Also estimates water stress factor.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_waterup.f90`
- **使用模块**：[[plant_data_module.f90]]、[[basin_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[urban_data_module.f90]]、[[constituent_mass_module.f90]]、[[salt_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[salt_chem_soil_single.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

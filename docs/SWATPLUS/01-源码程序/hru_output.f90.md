---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: hru_output.f90
subroutine: hru_output
module:
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - hydrograph_module
  - organic_mineral_mass_module
  - soil_module
  - carbon_module
  - hru_module
  - landuse_data_module
calls:
  - soil_nutcarb_write
  - soil_nutcarb_write_legacy
reads: []
writes: []
purpose: "this subroutine outputs HRU variables on daily, monthly and annual time steps"
---

# hru_output

> [!info] 概要
> this subroutine outputs HRU variables on daily, monthly and annual time steps

## 基本信息
- **类型**：`subroutine`
- **源文件**：`hru_output.f90`
- **使用模块**：[[plant_module.f90]]、[[plant_data_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]、[[output_landscape_module.f90]]、[[hydrograph_module.f90]]、[[organic_mineral_mass_module.f90]]、[[soil_module.f90]]、[[carbon_module.f90]]、[[hru_module.f90]]、[[landuse_data_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[soil_nutcarb_write.f90]]
- [[soil_nutcarb_write_legacy.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

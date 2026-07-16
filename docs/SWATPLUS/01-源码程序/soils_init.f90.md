---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: soils_init.f90
subroutine: soils_init
module:
  - hru_module
  - soil_module
  - plant_module
  - maximum_data_module
  - soil_data_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - hydrograph_module
  - time_module
  - basin_module
  - septic_data_module
calls:
  - soils_test_adjust
  - soil_phys_init
  - layersplit
reads:
  - soil_lyr_depths.sol
writes: []
purpose: ""
---

# soils_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`soils_init.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[maximum_data_module.f90]]、[[soil_data_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]、[[septic_data_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[soils_test_adjust.f90]]
- [[soil_phys_init.f90]]
- [[layersplit.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`soil_lyr_depths.sol`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_biomass_gro.f90
subroutine: pl_biomass_gro
module:
  - plant_data_module
  - basin_module
  - hru_module
  - plant_module
  - carbon_module
  - organic_mineral_mass_module
  - climate_module
  - hydrograph_module
  - constituent_mass_module
  - salt_module
  - salt_data_module
  - output_landscape_module
calls:
  - pl_tstr
  - pl_nup
  - pl_pup
  - salt_uptake
  - cs_uptake
reads: []
writes: []
purpose: ""
---

# pl_biomass_gro

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_biomass_gro.f90`
- **使用模块**：[[plant_data_module.f90]]、[[basin_module.f90]]、[[hru_module.f90]]、[[plant_module.f90]]、[[carbon_module.f90]]、[[organic_mineral_mass_module.f90]]、[[climate_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[salt_module.f90]]、[[salt_data_module.f90]]、[[output_landscape_module.f90]]
- **调用子程序**：5 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[pl_tstr.f90]]
- [[pl_nup.f90]]
- [[pl_pup.f90]]
- [[salt_uptake.f90]]
- [[cs_uptake.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

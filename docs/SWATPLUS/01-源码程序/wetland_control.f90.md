---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: wetland_control.f90
subroutine: wetland_control
module:
  - reservoir_data_module
  - reservoir_module
  - hru_module
  - conditional_module
  - climate_module
  - hydrograph_module
  - time_module
  - basin_module
  - channel_module
  - water_body_module
  - soil_module
  - organic_mineral_mass_module
  - mgt_operations_module
  - constituent_mass_module
  - aquifer_module
  - gwflow_module
calls:
  - gwflow_wetland
  - res_weir_release
  - conditions
  - res_hydro
  - res_sediment
  - res_nutrient
  - wet_salt
  - wet_cs
  - ero_cfactor
reads: []
writes: []
purpose: ""
---

# wetland_control

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`wetland_control.f90`
- **使用模块**：[[reservoir_data_module.f90]]、[[reservoir_module.f90]]、[[hru_module.f90]]、[[conditional_module.f90]]、[[climate_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]、[[channel_module.f90]]、[[water_body_module.f90]]、[[soil_module.f90]]、[[organic_mineral_mass_module.f90]]、[[mgt_operations_module.f90]]、[[constituent_mass_module.f90]]、[[aquifer_module.f90]]、[[gwflow_module.f90]]
- **调用子程序**：9 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gwflow_wetland.f90]]
- [[res_weir_release.f90]]
- [[conditions.f90]]
- [[res_hydro.f90]]
- [[res_sediment.f90]]
- [[res_nutrient.f90]]
- [[wet_salt.f90]]
- [[wet_cs.f90]]
- [[ero_cfactor.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

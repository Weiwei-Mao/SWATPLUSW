---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_nut_demand.f90
subroutine: pl_nut_demand
module:
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - organic_mineral_mass_module
  - climate_module
calls:
  - pl_nupd
  - pl_pupd
reads: []
writes: []
purpose: "this subroutine predicts daily potential growth of total plant；biomass and roots and calculates leaf area index. Incorporates；residue for tillage functions and decays residue on ground"
---

# pl_nut_demand

> [!info] 概要
> this subroutine predicts daily potential growth of total plant；biomass and roots and calculates leaf area index. Incorporates；residue for tillage functions and decays residue on ground

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_nut_demand.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[organic_mineral_mass_module.f90]]、[[climate_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[pl_nupd.f90]]
- [[pl_pupd.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

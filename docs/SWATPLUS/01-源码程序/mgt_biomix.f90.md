---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: mgt_biomix.f90
subroutine: mgt_biomix
module:
  - tillage_data_module
  - basin_module
  - organic_mineral_mass_module
  - soil_module
  - constituent_mass_module
  - plant_module
  - plant_data_module
  - hru_module
calls:
  - mgt_tillfactor
reads: []
writes: []
purpose: "this subroutine mixes residue and nutrients from biological mixing；New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi；A subroutine to simulate stimulation of organic matter decomposition was added"
---

# mgt_biomix

> [!info] 概要
> this subroutine mixes residue and nutrients from biological mixing；New version developed by Armen R. Kemanian in collaboration with Stefan Julich and Cole Rossi；A subroutine to simulate stimulation of organic matter decomposition was added

## 基本信息
- **类型**：`subroutine`
- **源文件**：`mgt_biomix.f90`
- **使用模块**：[[tillage_data_module.f90]]、[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[soil_module.f90]]、[[constituent_mass_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[hru_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[mgt_tillfactor.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

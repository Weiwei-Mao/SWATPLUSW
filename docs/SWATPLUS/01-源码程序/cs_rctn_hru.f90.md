---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cs_rctn_hru.f90
subroutine: cs_rctn_hru
module:
  - hru_module
  - constituent_mass_module
  - cs_data_module
  - soil_module
  - organic_mineral_mass_module
  - cs_module
calls:
  - se_reactions_soil
reads: []
writes: []
purpose: "this subroutine updates constituent concentrations based on chemical reactions and sorption in the soil profile"
---

# cs_rctn_hru

> [!info] 概要
> this subroutine updates constituent concentrations based on chemical reactions and sorption in the soil profile

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cs_rctn_hru.f90`
- **使用模块**：[[hru_module.f90]]、[[constituent_mass_module.f90]]、[[cs_data_module.f90]]、[[soil_module.f90]]、[[organic_mineral_mass_module.f90]]、[[cs_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[se_reactions_soil.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

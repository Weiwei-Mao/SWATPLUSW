---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pathogen_init.f90
subroutine: pathogen_init
module:
  - hru_module
  - soil_module
  - plant_module
  - pathogen_data_module
  - channel_module
  - basin_module
  - conditional_module
  - organic_mineral_mass_module
  - hydrograph_module
  - constituent_mass_module
  - output_ls_pathogen_module
calls: []
reads: []
writes: []
purpose: "this subroutine calls subroutines which read input data for the；databases and the HRUs"
---

# pathogen_init

> [!info] 概要
> this subroutine calls subroutines which read input data for the；databases and the HRUs

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pathogen_init.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[pathogen_data_module.f90]]、[[channel_module.f90]]、[[basin_module.f90]]、[[conditional_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[output_ls_pathogen_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: res_control.f90
subroutine: res_control
module:
  - basin_module
  - reservoir_data_module
  - time_module
  - reservoir_module
  - climate_module
  - hydrograph_module
  - conditional_module
  - water_body_module
  - constituent_mass_module
calls:
  - cli_lapse
  - move_alloc
  - conditions
  - res_hydro
  - res_sediment
  - res_rel_conds
  - gwflow_reservoir
  - res_nutrient
  - res_pest
  - res_salt
  - res_cs
reads: []
writes: []
purpose: ""
---

# res_control

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`res_control.f90`
- **使用模块**：[[basin_module.f90]]、[[reservoir_data_module.f90]]、[[time_module.f90]]、[[reservoir_module.f90]]、[[climate_module.f90]]、[[hydrograph_module.f90]]、[[conditional_module.f90]]、[[water_body_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：11 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cli_lapse.f90]]
- `move_alloc`
- [[conditions.f90]]
- [[res_hydro.f90]]
- [[res_sediment.f90]]
- [[res_rel_conds.f90]]
- [[gwflow_reservoir.f90]]
- [[res_nutrient.f90]]
- [[res_pest.f90]]
- [[res_salt.f90]]
- [[res_cs.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

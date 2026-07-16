---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cal_conditions.f90
subroutine: cal_conditions
module:
  - maximum_data_module
  - calibration_data_module
  - conditional_module
  - hru_lte_module
  - hru_module
  - soil_module
  - plant_module
  - plant_data_module
  - time_module
  - reservoir_module
  - climate_module
  - landuse_data_module
calls:
  - cal_parm_select
reads: []
writes: []
purpose: ""
---

# cal_conditions

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cal_conditions.f90`
- **使用模块**：[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[conditional_module.f90]]、[[hru_lte_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[time_module.f90]]、[[reservoir_module.f90]]、[[climate_module.f90]]、[[landuse_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cal_parm_select.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

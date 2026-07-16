---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_simulate.f90
subroutine: gwflow_simulate
module:
  - gwflow_module
  - hydrograph_module
  - hru_module
  - sd_channel_module
  - time_module
  - soil_module
calls:
  - gwflow_rech
  - gwflow_gwet
  - gwflow_phreatophyte
  - gwflow_pump_ext
  - gwflow_canal_ext
  - gwflow_pond
  - gwflow_canal_div
  - gwflow_lateral
  - gwflow_output_day
  - gwflow_output_mon
  - gwflow_output_yr
  - gwflow_output_aa
reads: []
writes: []
purpose: "this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;；also, computes and write out daily/annual/average annual fluxes and mass balance error"
---

# gwflow_simulate

> [!info] 概要
> this subroutine calculates new groundwater storage and solute mass for each gwflow grid cell;；also, computes and write out daily/annual/average annual fluxes and mass balance error

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_simulate.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[sd_channel_module.f90]]、[[time_module.f90]]、[[soil_module.f90]]
- **调用子程序**：12 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gwflow_rech.f90]]
- [[gwflow_gwet.f90]]
- [[gwflow_phreatophyte.f90]]
- [[gwflow_pump_ext.f90]]
- [[gwflow_canal_ext.f90]]
- [[gwflow_pond.f90]]
- [[gwflow_canal_div.f90]]
- [[gwflow_lateral.f90]]
- `gwflow_output_day`
- `gwflow_output_mon`
- `gwflow_output_yr`
- `gwflow_output_aa`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: climate_control.f90
subroutine: climate_control
module:
  - climate_module
  - basin_module
  - time_module
  - hydrograph_module
  - maximum_data_module
calls:
  - cli_precip_control
  - cli_weatgn
  - cli_tgen
  - cli_bounds_check
  - cli_clgen
  - cli_slrgen
  - cli_rhgen
  - cli_wndgen
reads: []
writes: []
purpose: "this subroutine controls weather inputs to SWAT. Precipitation and；temperature data is read in and the weather generator is called to；fill in radiation, wind speed and relative humidity as well as"
---

# climate_control

> [!info] 概要
> this subroutine controls weather inputs to SWAT. Precipitation and；temperature data is read in and the weather generator is called to；fill in radiation, wind speed and relative humidity as well as

## 基本信息
- **类型**：`subroutine`
- **源文件**：`climate_control.f90`
- **使用模块**：[[climate_module.f90]]、[[basin_module.f90]]、[[time_module.f90]]、[[hydrograph_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：8 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cli_precip_control.f90]]
- [[cli_weatgn.f90]]
- [[cli_tgen.f90]]
- [[cli_bounds_check.f90]]
- [[cli_clgen.f90]]
- [[cli_slrgen.f90]]
- [[cli_rhgen.f90]]
- [[cli_wndgen.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

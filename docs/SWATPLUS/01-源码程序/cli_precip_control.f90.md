---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: cli_precip_control.f90
subroutine: cli_precip_control
module:
  - climate_module
  - basin_module
  - time_module
  - hydrograph_module
  - maximum_data_module
calls:
  - cli_pgen
  - cli_pgenhr
  - cli_bounds_check
reads: []
writes: []
purpose: "this subroutine controls weather inputs to SWAT. Precipitation and；temperature data is read in and the weather generator is called to；fill in radiation, wind speed and relative humidity as well as"
---

# cli_precip_control

> [!info] 概要
> this subroutine controls weather inputs to SWAT. Precipitation and；temperature data is read in and the weather generator is called to；fill in radiation, wind speed and relative humidity as well as

## 基本信息
- **类型**：`subroutine`
- **源文件**：`cli_precip_control.f90`
- **使用模块**：[[climate_module.f90]]、[[basin_module.f90]]、[[time_module.f90]]、[[hydrograph_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：3 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cli_pgen.f90]]
- [[cli_pgenhr.f90]]
- [[cli_bounds_check.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

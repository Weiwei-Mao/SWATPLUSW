---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: sd_channel_sediment3.f90
subroutine: sd_channel_sediment3
module:
  - climate_module
  - sd_channel_module
  - channel_module
  - hydrograph_module
  - time_module
  - hru_module
  - water_body_module
  - reservoir_module
  - utils
  - basin_module
  - gwflow_module
  - channel_velocity_module
calls:
  - rcurv_interp_flo
  - gwflow_floodplain
reads: []
writes: []
purpose: ""
---

# sd_channel_sediment3

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`sd_channel_sediment3.f90`
- **使用模块**：[[climate_module.f90]]、[[sd_channel_module.f90]]、[[channel_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]、[[hru_module.f90]]、[[water_body_module.f90]]、[[reservoir_module.f90]]、[[utils.f90]]、[[basin_module.f90]]、[[gwflow_module.f90]]、[[channel_velocity_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[rcurv_interp_flo.f90]]
- [[gwflow_floodplain.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

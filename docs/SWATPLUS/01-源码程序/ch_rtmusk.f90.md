---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_rtmusk.f90
subroutine: ch_rtmusk
module:
  - basin_module
  - channel_data_module
  - channel_module
  - hydrograph_module
  - time_module
  - channel_velocity_module
  - sd_channel_module
  - climate_module
  - reservoir_module
  - reservoir_data_module
  - water_body_module
  - conditional_module
calls:
  - rcurv_interp_flo
reads: []
writes: []
purpose: "this subroutine routes a daily flow through a reach using the；Muskingum method；code provided by Dr. Valentina Krysanova, Pottsdam Institute for"
---

# ch_rtmusk

> [!info] 概要
> this subroutine routes a daily flow through a reach using the；Muskingum method；code provided by Dr. Valentina Krysanova, Pottsdam Institute for

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_rtmusk.f90`
- **使用模块**：[[basin_module.f90]]、[[channel_data_module.f90]]、[[channel_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]、[[channel_velocity_module.f90]]、[[sd_channel_module.f90]]、[[climate_module.f90]]、[[reservoir_module.f90]]、[[reservoir_data_module.f90]]、[[water_body_module.f90]]、[[conditional_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[rcurv_interp_flo.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

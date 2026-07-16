---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: sd_channel_control3.f90
subroutine: sd_channel_control3
module:
  - sd_channel_module
  - channel_velocity_module
  - basin_module
  - hydrograph_module
  - constituent_mass_module
  - conditional_module
  - channel_data_module
  - channel_module
  - ch_pesticide_module
  - climate_module
  - water_body_module
  - time_module
  - ch_salt_module
  - ch_cs_module
  - gwflow_module
  - water_allocation_module
  - maximum_data_module
calls:
  - cli_lapse
  - gwflow_channel_exch
  - gwflow_canal
  - gwflow_tile
  - gwflow_satexcess
  - sd_channel_sediment3
  - ch_rtmusk
  - ch_rtpest
  - ch_rtpath
  - rcurv_interp_flo
  - ch_watqual4
  - wallo_control
  - ch_temp
reads: []
writes: []
purpose: ""
---

# sd_channel_control3

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`sd_channel_control3.f90`
- **使用模块**：[[sd_channel_module.f90]]、[[channel_velocity_module.f90]]、[[basin_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[conditional_module.f90]]、[[channel_data_module.f90]]、[[channel_module.f90]]、[[ch_pesticide_module.f90]]、[[climate_module.f90]]、[[water_body_module.f90]]、[[time_module.f90]]、[[ch_salt_module.f90]]、[[ch_cs_module.f90]]、[[gwflow_module.f90]]、[[water_allocation_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：13 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[cli_lapse.f90]]
- [[gwflow_channel_exch.f90]]
- [[gwflow_canal.f90]]
- [[gwflow_tile.f90]]
- [[gwflow_satexcess.f90]]
- [[sd_channel_sediment3.f90]]
- [[ch_rtmusk.f90]]
- [[ch_rtpest.f90]]
- [[ch_rtpath.f90]]
- [[rcurv_interp_flo.f90]]
- [[ch_watqual4.f90]]
- [[wallo_control.f90]]
- [[ch_temp.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

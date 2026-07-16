---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_rthr.f90
subroutine: ch_rthr
module:
  - basin_module
  - climate_module
  - channel_data_module
  - time_module
  - channel_module
  - hydrograph_module
  - sd_channel_module
calls:
  - chrc_interp
reads: []
writes: []
purpose: "This subroutine routes flow at any required time step through the reach；using a constant storage coefficient；Routing method: Variable Storage routing"
---

# ch_rthr

> [!info] 概要
> This subroutine routes flow at any required time step through the reach；using a constant storage coefficient；Routing method: Variable Storage routing

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_rthr.f90`
- **使用模块**：[[basin_module.f90]]、[[climate_module.f90]]、[[channel_data_module.f90]]、[[time_module.f90]]、[[channel_module.f90]]、[[hydrograph_module.f90]]、[[sd_channel_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `chrc_interp`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_watqual4.f90
subroutine: ch_watqual4
module:
  - channel_module
  - hydrograph_module
  - climate_module
  - channel_data_module
  - sd_channel_module
  - water_body_module
calls:
  - rcurv_interp_flo
reads: []
writes: []
purpose: "this subroutine performs in-stream nutrient transformations and water；quality calculations"
---

# ch_watqual4

> [!info] 概要
> this subroutine performs in-stream nutrient transformations and water；quality calculations

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_watqual4.f90`
- **使用模块**：[[channel_module.f90]]、[[hydrograph_module.f90]]、[[climate_module.f90]]、[[channel_data_module.f90]]、[[sd_channel_module.f90]]、[[water_body_module.f90]]
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

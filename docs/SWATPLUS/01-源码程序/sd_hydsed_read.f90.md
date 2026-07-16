---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: sd_hydsed_read.f90
subroutine: sd_hydsed_read
module:
  - input_file_module
  - sd_channel_module
  - channel_velocity_module
  - maximum_data_module
  - hydrograph_module
  - time_module
calls: []
reads:
  - in_cha%hyd_sed
  - sed_nut.cha
writes: []
purpose: ""
---

# sd_hydsed_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`sd_hydsed_read.f90`
- **使用模块**：[[input_file_module.f90]]、[[sd_channel_module.f90]]、[[channel_velocity_module.f90]]、[[maximum_data_module.f90]]、[[hydrograph_module.f90]]、[[time_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：2 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_cha%hyd_sed` _（变量，见 file.cio）_、`sed_nut.cha`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_rtpest.f90
subroutine: ch_rtpest
module:
  - channel_data_module
  - channel_module
  - sd_channel_module
  - ch_pesticide_module
  - hydrograph_module
  - constituent_mass_module
  - pesticide_data_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes the daily stream pesticide balance；(soluble and sorbed)"
---

# ch_rtpest

> [!info] 概要
> this subroutine computes the daily stream pesticide balance；(soluble and sorbed)

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_rtpest.f90`
- **使用模块**：[[channel_data_module.f90]]、[[channel_module.f90]]、[[sd_channel_module.f90]]、[[ch_pesticide_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[pesticide_data_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

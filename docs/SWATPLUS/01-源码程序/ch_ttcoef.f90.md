---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_ttcoef.f90
subroutine: ch_ttcoef
module:
  - channel_data_module
  - channel_module
  - channel_velocity_module
calls: []
reads: []
writes: []
purpose: "this subroutine computes travel time coefficients for routing；along the main channel"
---

# ch_ttcoef

> [!info] 概要
> this subroutine computes travel time coefficients for routing；along the main channel

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_ttcoef.f90`
- **使用模块**：[[channel_data_module.f90]]、[[channel_module.f90]]、[[channel_velocity_module.f90]]
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

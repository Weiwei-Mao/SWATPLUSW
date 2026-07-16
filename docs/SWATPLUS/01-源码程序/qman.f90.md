---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: qman.f90
subroutine: qman
module: []
calls: []
reads: []
writes: []
purpose: "this subroutine calculates flow rate or flow velocity using Manning\"s；equation. If x1 is set to 1, the velocity is calculated. If x1 is set to；cross-sectional area of flow, the flow rate is calculated."
---

# qman

> [!info] 概要
> this subroutine calculates flow rate or flow velocity using Manning"s；equation. If x1 is set to 1, the velocity is calculated. If x1 is set to；cross-sectional area of flow, the flow rate is calculated.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`qman.f90`
- **使用模块**：—
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

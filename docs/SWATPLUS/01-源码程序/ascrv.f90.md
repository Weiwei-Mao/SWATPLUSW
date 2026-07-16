---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ascrv.f90
subroutine: ascrv
module: []
calls: []
reads: []
writes: []
purpose: "this subroutine computes shape parameters x5 and x6 for the S curve；equation x = y/(y + exp(x5 + x6*y)) given 2 (x,y) points along the curve.；x5 is determined by solving the equation with x and y values measured"
---

# ascrv

> [!info] 概要
> this subroutine computes shape parameters x5 and x6 for the S curve；equation x = y/(y + exp(x5 + x6*y)) given 2 (x,y) points along the curve.；x5 is determined by solving the equation with x and y values measured

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ascrv.f90`
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

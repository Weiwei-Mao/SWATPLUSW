---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: sq_volq.f90
subroutine: sq_volq
module:
  - basin_module
calls:
  - sq_daycn
  - sq_greenampt
reads: []
writes: []
purpose: "Call subroutines to calculate the current day\"s CN for the HRU and；to calculate surface runoff"
---

# sq_volq

> [!info] 概要
> Call subroutines to calculate the current day"s CN for the HRU and；to calculate surface runoff

## 基本信息
- **类型**：`subroutine`
- **源文件**：`sq_volq.f90`
- **使用模块**：[[basin_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[sq_daycn.f90]]
- [[sq_greenampt.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

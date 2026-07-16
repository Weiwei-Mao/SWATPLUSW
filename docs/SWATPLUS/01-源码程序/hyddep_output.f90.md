---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: hyddep_output.f90
subroutine: hyddep_output
module:
  - hydrograph_module
  - time_module
  - basin_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs hyd variables on daily, monthly and annual time steps；0 = average annual (always print)；1 = yearly"
---

# hyddep_output

> [!info] 概要
> this subroutine outputs hyd variables on daily, monthly and annual time steps；0 = average annual (always print)；1 = yearly

## 基本信息
- **类型**：`subroutine`
- **源文件**：`hyddep_output.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]
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

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_lateral.f90
subroutine: gwflow_lateral
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_heat
  - gwflow_solute
reads: []
writes: []
purpose: "this subroutine calculates lateral groundwater flow between adjacent cells；using Darcy's Law, then updates head and storage；(extracted from gwflow_simulate)"
---

# gwflow_lateral

> [!info] 概要
> this subroutine calculates lateral groundwater flow between adjacent cells；using Darcy's Law, then updates head and storage；(extracted from gwflow_simulate)

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_lateral.f90`
- **使用模块**：[[gwflow_module.f90]]、[[time_module.f90]]
- **调用子程序**：2 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gwflow_heat.f90]]
- [[gwflow_solute.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

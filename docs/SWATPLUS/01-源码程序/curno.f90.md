---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: curno.f90
subroutine: curno
module:
  - time_module
  - hru_module
  - soil_module
calls:
  - ascrv
reads: []
writes: []
purpose: "this subroutine determines the curve numbers for moisture conditions；I and III and calculates coefficients and shape parameters for the；water retention curve"
---

# curno

> [!info] 概要
> this subroutine determines the curve numbers for moisture conditions；I and III and calculates coefficients and shape parameters for the；water retention curve

## 基本信息
- **类型**：`subroutine`
- **源文件**：`curno.f90`
- **使用模块**：[[time_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[ascrv.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

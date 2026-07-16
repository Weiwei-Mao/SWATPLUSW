---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: swr_percmain.f90
subroutine: swr_percmain
module:
  - hru_module
  - soil_module
  - septic_data_module
  - hydrograph_module
  - basin_module
calls:
  - gwflow_soil
  - swr_percmacro
  - swr_percmicro
  - swr_satexcess
  - swr_drains
  - swr_origtile
reads: []
writes: []
purpose: "this subroutine is the master soil percolation component."
---

# swr_percmain

> [!info] 概要
> this subroutine is the master soil percolation component.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`swr_percmain.f90`
- **使用模块**：[[hru_module.f90]]、[[soil_module.f90]]、[[septic_data_module.f90]]、[[hydrograph_module.f90]]、[[basin_module.f90]]
- **调用子程序**：6 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gwflow_soil.f90]]
- [[swr_percmacro.f90]]
- [[swr_percmicro.f90]]
- [[swr_satexcess.f90]]
- [[swr_drains.f90]]
- [[swr_origtile.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

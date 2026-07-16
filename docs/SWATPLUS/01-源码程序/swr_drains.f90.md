---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: swr_drains.f90
subroutine: swr_drains
module:
  - basin_module
  - hydrograph_module
  - hru_module
  - soil_module
  - time_module
  - reservoir_module
calls:
  - swr_depstor
reads: []
writes: []
purpose: "this subroutine finds the effective lateral hydraulic conductivity；and computes drainage or subirrigation flux"
---

# swr_drains

> [!info] 概要
> this subroutine finds the effective lateral hydraulic conductivity；and computes drainage or subirrigation flux

## 基本信息
- **类型**：`subroutine`
- **源文件**：`swr_drains.f90`
- **使用模块**：[[basin_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[time_module.f90]]、[[reservoir_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[swr_depstor.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

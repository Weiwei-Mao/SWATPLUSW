---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: surface.f90
subroutine: surface
module:
  - basin_module
  - time_module
  - hydrograph_module
  - hru_module
  - soil_module
  - urban_data_module
  - output_landscape_module
calls:
  - sq_dailycn
  - sq_volq
  - sq_crackflow
  - ero_pkq
  - ero_eiusle
  - ero_ovrsed
  - ero_cfactor
  - ero_ysed
reads: []
writes: []
purpose: "this subroutine models surface hydrology at any desired time step"
---

# surface

> [!info] 概要
> this subroutine models surface hydrology at any desired time step

## 基本信息
- **类型**：`subroutine`
- **源文件**：`surface.f90`
- **使用模块**：[[basin_module.f90]]、[[time_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[urban_data_module.f90]]、[[output_landscape_module.f90]]
- **调用子程序**：8 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[sq_dailycn.f90]]
- [[sq_volq.f90]]
- [[sq_crackflow.f90]]
- [[ero_pkq.f90]]
- [[ero_eiusle.f90]]
- [[ero_ovrsed.f90]]
- [[ero_cfactor.f90]]
- [[ero_ysed.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

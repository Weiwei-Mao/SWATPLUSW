---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: basin_sw_init.f90
subroutine: basin_sw_init
module:
  - time_module
  - hydrograph_module
  - calibration_data_module
  - output_landscape_module
  - basin_module
  - maximum_data_module
  - soil_module
  - hru_module
calls: []
reads: []
writes: []
purpose: ""
---

# basin_sw_init

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`basin_sw_init.f90`
- **使用模块**：[[time_module.f90]]、[[hydrograph_module.f90]]、[[calibration_data_module.f90]]、[[output_landscape_module.f90]]、[[basin_module.f90]]、[[maximum_data_module.f90]]、[[soil_module.f90]]、[[hru_module.f90]]
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

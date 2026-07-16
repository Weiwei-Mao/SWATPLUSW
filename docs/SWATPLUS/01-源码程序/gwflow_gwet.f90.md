---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_gwet.f90
subroutine: gwflow_gwet
module:
  - gwflow_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine determines the volume of groundwater that is removed from the；aquifer via ET"
---

# gwflow_gwet

> [!info] 概要
> this subroutine determines the volume of groundwater that is removed from the；aquifer via ET

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_gwet.f90`
- **使用模块**：[[gwflow_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[hydrograph_module.f90]]
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

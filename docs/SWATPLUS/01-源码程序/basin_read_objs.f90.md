---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: basin_read_objs.f90
subroutine: basin_read_objs
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - basin_module
  - gwflow_module
calls: []
reads:
  - in_sim%object_cnt
  - chancell.gw
  - gwflow_record
writes: []
purpose: "reads in the routing information from the watershed configuration；input file (.fig) and calculates the number of subbasins, reaches,；and reservoirs"
---

# basin_read_objs

> [!info] 概要
> reads in the routing information from the watershed configuration；input file (.fig) and calculates the number of subbasins, reaches,；and reservoirs

## 基本信息
- **类型**：`subroutine`
- **源文件**：`basin_read_objs.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[input_file_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]、[[basin_module.f90]]、[[gwflow_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：3 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_sim%object_cnt` _（变量，见 file.cio）_、`chancell.gw`、`gwflow_record` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

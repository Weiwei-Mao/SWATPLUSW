---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: ch_cs_output.f90
subroutine: ch_cs_output
module:
  - output_ls_pesticide_module
  - ch_cs_module
  - plant_module
  - plant_data_module
  - time_module
  - basin_module
  - output_landscape_module
  - constituent_mass_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass in channels"
---

# ch_cs_output

> [!info] 概要
> this subroutine outputs constituent mass in channels

## 基本信息
- **类型**：`subroutine`
- **源文件**：`ch_cs_output.f90`
- **使用模块**：[[output_ls_pesticide_module.f90]]、[[ch_cs_module.f90]]、[[plant_module.f90]]、[[plant_data_module.f90]]、[[time_module.f90]]、[[basin_module.f90]]、[[output_landscape_module.f90]]、[[constituent_mass_module.f90]]、[[hydrograph_module.f90]]
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

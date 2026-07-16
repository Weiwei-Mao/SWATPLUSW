---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_fert_wet.f90
subroutine: pl_fert_wet
module:
  - mgt_operations_module
  - fertilizer_data_module
  - basin_module
  - organic_mineral_mass_module
  - hru_module
  - hydrograph_module
calls: []
reads: []
writes: []
purpose: "this subroutine applies N and P specified by date and；amount in the management file (.mgt) for rice fields during ponding periods；Jaehak 2022"
---

# pl_fert_wet

> [!info] 概要
> this subroutine applies N and P specified by date and；amount in the management file (.mgt) for rice fields during ponding periods；Jaehak 2022

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_fert_wet.f90`
- **使用模块**：[[mgt_operations_module.f90]]、[[fertilizer_data_module.f90]]、[[basin_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hru_module.f90]]、[[hydrograph_module.f90]]
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

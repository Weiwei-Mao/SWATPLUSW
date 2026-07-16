---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: aqu_cs_output.f90
subroutine: aqu_cs_output
module:
  - time_module
  - basin_module
  - aquifer_module
  - hydrograph_module
  - cs_aquifer
  - constituent_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine outputs constituent mass loadings and concentrations in aquifers"
---

# aqu_cs_output

> [!info] 概要
> this subroutine outputs constituent mass loadings and concentrations in aquifers

## 基本信息
- **类型**：`subroutine`
- **源文件**：`aqu_cs_output.f90`
- **使用模块**：[[time_module.f90]]、[[basin_module.f90]]、[[aquifer_module.f90]]、[[hydrograph_module.f90]]、[[cs_aquifer.f90]]、[[constituent_mass_module.f90]]
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

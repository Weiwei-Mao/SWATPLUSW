---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_chem.f90
subroutine: gwflow_chem
module:
  - gwflow_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - gwflow_minl
reads: []
writes: []
purpose: "this subroutine calculates chemical reactions in gwflow cells.；Fills module arrays mass_rct and mass_min. Called from gwflow_solute."
---

# gwflow_chem

> [!info] 概要
> this subroutine calculates chemical reactions in gwflow cells.；Fills module arrays mass_rct and mass_min. Called from gwflow_solute.

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_chem.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `gwflow_minl`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

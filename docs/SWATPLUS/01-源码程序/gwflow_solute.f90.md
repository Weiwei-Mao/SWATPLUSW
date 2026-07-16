---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_solute.f90
subroutine: gwflow_solute
module:
  - gwflow_module
  - time_module
calls:
  - gwflow_chem
reads: []
writes: []
purpose: "this subroutine calculates solute advection, dispersion, chemical；reactions, and sorption for groundwater solute transport. Called from；gwflow_lateral once per flow time step. Contains its own sub-timestep"
---

# gwflow_solute

> [!info] 概要
> this subroutine calculates solute advection, dispersion, chemical；reactions, and sorption for groundwater solute transport. Called from；gwflow_lateral once per flow time step. Contains its own sub-timestep

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_solute.f90`
- **使用模块**：[[gwflow_module.f90]]、[[time_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[gwflow_chem.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

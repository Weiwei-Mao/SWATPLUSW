---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: pl_burnop.f90
subroutine: pl_burnop
module:
  - basin_module
  - mgt_operations_module
  - organic_mineral_mass_module
  - hru_module
  - soil_module
  - plant_module
  - carbon_module
calls:
  - curno
reads: []
writes: []
purpose: "this subroutine performs all management operations"
---

# pl_burnop

> [!info] 概要
> this subroutine performs all management operations

## 基本信息
- **类型**：`subroutine`
- **源文件**：`pl_burnop.f90`
- **使用模块**：[[basin_module.f90]]、[[mgt_operations_module.f90]]、[[organic_mineral_mass_module.f90]]、[[hru_module.f90]]、[[soil_module.f90]]、[[plant_module.f90]]、[[carbon_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[curno.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

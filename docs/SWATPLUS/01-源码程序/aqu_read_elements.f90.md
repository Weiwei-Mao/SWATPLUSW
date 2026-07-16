---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: aqu_read_elements.f90
subroutine: aqu_read_elements
module:
  - input_file_module
  - calibration_data_module
  - hydrograph_module
  - aquifer_module
  - maximum_data_module
calls:
  - define_unit_elements
reads:
  - in_regs%def_aqu
  - in_regs%def_aqu
  - in_regs%ele_aqu
writes: []
purpose: ""
---

# aqu_read_elements

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`aqu_read_elements.f90`
- **使用模块**：[[input_file_module.f90]]、[[calibration_data_module.f90]]、[[hydrograph_module.f90]]、[[aquifer_module.f90]]、[[maximum_data_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：3 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[define_unit_elements.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_regs%def_aqu` _（变量，见 file.cio）_、`in_regs%def_aqu` _（变量，见 file.cio）_、`in_regs%ele_aqu` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

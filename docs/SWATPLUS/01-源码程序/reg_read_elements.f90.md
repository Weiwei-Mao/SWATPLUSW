---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: reg_read_elements.f90
subroutine: reg_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - landuse_data_module
  - hydrograph_module
  - hru_module
  - output_landscape_module
calls:
  - define_unit_elements
reads:
  - in_regs%def_reg
  - in_regs%ele_reg
writes: []
purpose: ""
---

# reg_read_elements

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`reg_read_elements.f90`
- **使用模块**：[[input_file_module.f90]]、[[maximum_data_module.f90]]、[[calibration_data_module.f90]]、[[landuse_data_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]、[[output_landscape_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：2 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[define_unit_elements.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_regs%def_reg` _（变量，见 file.cio）_、`in_regs%ele_reg` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

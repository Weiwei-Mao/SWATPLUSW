---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: hru_read.f90
subroutine: hru_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - hydrology_data_module
  - topography_data_module
  - soil_data_module
  - input_file_module
  - hru_module
  - constituent_mass_module
calls:
  - allocate_parms
reads:
  - in_hru%hru_data
writes: []
purpose: ""
---

# hru_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`hru_read.f90`
- **使用模块**：[[maximum_data_module.f90]]、[[reservoir_data_module.f90]]、[[landuse_data_module.f90]]、[[hydrology_data_module.f90]]、[[topography_data_module.f90]]、[[soil_data_module.f90]]、[[input_file_module.f90]]、[[hru_module.f90]]、[[constituent_mass_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[allocate_parms.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_hru%hru_data` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

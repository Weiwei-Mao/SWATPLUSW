---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: dtbl_lum_read.f90
subroutine: dtbl_lum_read
module:
  - maximum_data_module
  - reservoir_data_module
  - landuse_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - input_file_module
  - conditional_module
  - pesticide_data_module
  - plant_data_module
  - constituent_mass_module
  - hydrograph_module
  - hru_module
calls: []
reads:
  - in_cond%dtbl_lum
writes: []
purpose: ""
---

# dtbl_lum_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`dtbl_lum_read.f90`
- **使用模块**：[[maximum_data_module.f90]]、[[reservoir_data_module.f90]]、[[landuse_data_module.f90]]、[[mgt_operations_module.f90]]、[[tillage_data_module.f90]]、[[fertilizer_data_module.f90]]、[[input_file_module.f90]]、[[conditional_module.f90]]、[[pesticide_data_module.f90]]、[[plant_data_module.f90]]、[[constituent_mass_module.f90]]、[[hydrograph_module.f90]]、[[hru_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_cond%dtbl_lum` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

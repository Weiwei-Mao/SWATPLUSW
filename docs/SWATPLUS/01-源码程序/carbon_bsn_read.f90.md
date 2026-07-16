---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: carbon_bsn_read.f90
subroutine: carbon_bsn_read
module:
  - carbon_module
  - basin_module
  - tillage_data_module
  - plant_data_module
  - input_file_module
calls: []
reads:
  - in_basin%carbon_bsn
  - carbon_lyr
writes: []
purpose: ""
---

# carbon_bsn_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`carbon_bsn_read.f90`
- **使用模块**：[[carbon_module.f90]]、[[basin_module.f90]]、[[tillage_data_module.f90]]、[[plant_data_module.f90]]、[[input_file_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：2 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`in_basin%carbon_bsn` _（变量，见 file.cio）_、`carbon_lyr` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

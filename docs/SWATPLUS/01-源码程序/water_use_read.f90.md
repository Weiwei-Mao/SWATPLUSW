---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: water_use_read.f90
subroutine: water_use_read
module:
  - input_file_module
  - water_allocation_module
  - mgt_operations_module
  - maximum_data_module
  - hydrograph_module
  - constituent_mass_module
  - sd_channel_module
calls: []
reads:
  - water_use.wal
writes: []
purpose: ""
---

# water_use_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`water_use_read.f90`
- **使用模块**：[[input_file_module.f90]]、[[water_allocation_module.f90]]、[[mgt_operations_module.f90]]、[[maximum_data_module.f90]]、[[hydrograph_module.f90]]、[[constituent_mass_module.f90]]、[[sd_channel_module.f90]]
- **调用子程序**：0 个 ｜ **读取文件**：1 ｜ **写入文件**：0

## 调用关系
（无 call 语句，叶子节点）

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`water_use.wal`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: recall_read.f90
subroutine: recalldb_read
module:
  - water_allocation_module
  - maximum_data_module
  - recall_module
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - time_module
  - exco_module
calls:
  - recall_read
reads:
  - recall_db.rec
  - recall_db(irec
  - pest.com
  - rec_pest(i
writes: []
purpose: ""
---

# recalldb_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`recall_read.f90`
- **使用模块**：[[water_allocation_module.f90]]、[[maximum_data_module.f90]]、[[recall_module.f90]]、[[hydrograph_module.f90]]、[[input_file_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]、[[time_module.f90]]、[[exco_module.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：4 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[recall_read.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`recall_db.rec`、`recall_db(irec` _（变量，见 file.cio）_、`pest.com`、`rec_pest(i` _（变量，见 file.cio）_

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

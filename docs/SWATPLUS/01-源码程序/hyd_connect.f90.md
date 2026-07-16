---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: hyd_connect.f90
subroutine: hyd_connect
module:
  - hydrograph_module
  - input_file_module
  - recall_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - ru_module
  - basin_module
calls:
  - hyd_read_connect
  - ru_read
  - ru_read_elements
  - aqu2d_read
  - overbank_read
  - dr_db_read
  - gwflow_chan_read
  - gwflow_read
  - exit
reads: []
writes:
  - looping.con
purpose: "reads in the routing information from the watershed configuration；input file (.fig) and calculates the number of subbasins, reaches,；and reservoirs"
---

# hyd_connect

> [!info] 概要
> reads in the routing information from the watershed configuration；input file (.fig) and calculates the number of subbasins, reaches,；and reservoirs

## 基本信息
- **类型**：`subroutine`
- **源文件**：`hyd_connect.f90`
- **使用模块**：[[hydrograph_module.f90]]、[[input_file_module.f90]]、[[recall_module.f90]]、[[organic_mineral_mass_module.f90]]、[[constituent_mass_module.f90]]、[[ru_module.f90]]、[[basin_module.f90]]
- **调用子程序**：9 个 ｜ **读取文件**：0 ｜ **写入文件**：1

## 调用关系
**本程序调用：**

- [[hyd_read_connect.f90]]
- [[ru_read.f90]]
- [[ru_read_elements.f90]]
- [[aqu2d_read.f90]]
- [[overbank_read.f90]]
- [[dr_db_read.f90]]
- [[gwflow_chan_read.f90]]
- [[gwflow_read.f90]]
- `exit`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **写入**：`looping.con`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

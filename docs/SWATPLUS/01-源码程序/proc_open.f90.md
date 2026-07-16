---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_open.f90
subroutine: proc_open
module: []
calls:
  - output_landscape_init
  - header_channel
  - header_aquifer
  - header_sd_channel
  - header_mgt
  - header_lu_change
  - header_yield
  - header_hyd
  - header_reservoir
  - header_wetland
  - header_water_allocation
  - header_pest
  - header_path
  - header_salt
  - header_const
  - header_write
reads: []
writes: []
purpose: ""
---

# proc_open

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_open.f90`
- **使用模块**：—
- **调用子程序**：16 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[output_landscape_init.f90]]
- [[header_channel.f90]]
- [[header_aquifer.f90]]
- [[header_sd_channel.f90]]
- [[header_mgt.f90]]
- [[header_lu_change.f90]]
- [[header_yield.f90]]
- [[header_hyd.f90]]
- [[header_reservoir.f90]]
- [[header_wetland.f90]]
- [[header_water_allocation.f90]]
- [[header_pest.f90]]
- [[header_path.f90]]
- [[header_salt.f90]]
- [[header_const.f90]]
- [[header_write.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

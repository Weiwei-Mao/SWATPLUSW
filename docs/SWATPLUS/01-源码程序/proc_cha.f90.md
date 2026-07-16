---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: proc_cha.f90
subroutine: proc_cha
module:
  - hydrograph_module
calls:
  - ch_read_init
  - ch_read_init_cs
  - sd_hydsed_read
  - ch_read_hyd
  - ch_read_sed
  - ch_read_nut
  - ch_read
  - sd_channel_read
  - sd_hydsed_init
  - aqu2d_init
  - ch_ttcoef
  - ch_initial
  - overbank_read
  - sd_channel_surf_link
  - time_conc_init
reads: []
writes: []
purpose: ""
---

# proc_cha

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`proc_cha.f90`
- **使用模块**：[[hydrograph_module.f90]]
- **调用子程序**：15 个 ｜ **读取文件**：0 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- [[ch_read_init.f90]]
- [[ch_read_init_cs.f90]]
- [[sd_hydsed_read.f90]]
- [[ch_read_hyd.f90]]
- [[ch_read_sed.f90]]
- [[ch_read_nut.f90]]
- [[ch_read.f90]]
- [[sd_channel_read.f90]]
- [[sd_hydsed_init.f90]]
- [[aqu2d_init.f90]]
- [[ch_ttcoef.f90]]
- [[ch_initial.f90]]
- [[overbank_read.f90]]
- [[sd_channel_surf_link.f90]]
- [[time_conc_init.f90]]

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->

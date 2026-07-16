---
type: source
subtype: subroutine
tags:
  - swat/源码
  - swat/待读
file: gwflow_chan_read.f90
subroutine: gwflow_chan_read
module:
  - gwflow_module
  - hydrograph_module
  - utils
calls:
  - split_line
reads:
  - chancell.gw
  - chan_depth.gw
writes: []
purpose: ""
---

# gwflow_chan_read

> [!info] 概要
> 待补充

## 基本信息
- **类型**：`subroutine`
- **源文件**：`gwflow_chan_read.f90`
- **使用模块**：[[gwflow_module.f90]]、[[hydrograph_module.f90]]、[[utils.f90]]
- **调用子程序**：1 个 ｜ **读取文件**：2 ｜ **写入文件**：0

## 调用关系
**本程序调用：**

- `split_line`

**被以下程序调用**（dataview 实时反查）：

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## 文件读写
- **读取**：`chancell.gw`、`chan_depth.gw`

<!-- USER-NOTES-START -->
## 我的笔记
（在此自由记录：逐行注解、关键变量、个人理解。重跑生成脚本时本段会被保留。）
<!-- USER-NOTES-END -->
